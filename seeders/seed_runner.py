    """
    Seed Runner — FastAPI + Motor (async MongoDB)
    =============================================
    Usage:
        python seed_runner.py --collection riasec
        python seed_runner.py --collection bigfive
        python seed_runner.py --collection aptitude_math
        python seed_runner.py --collection aptitude_english
        python seed_runner.py --collection aptitude_science
        python seed_runner.py --collection aptitude_abstract
        python seed_runner.py --collection all

    Options:
        --dry-run     Print what would be inserted without writing to DB
        --clear       Drop existing documents in the collection before seeding
    """

    import asyncio
    import argparse
    from motor.motor_asyncio import AsyncIOMotorClient
    from dotenv import load_dotenv
    import os

    from data.riasec import RIASEC_QUESTIONS
    from data.bigfive import BIGFIVE_QUESTIONS
    from data.aptitude_math import APTITUDE_MATH_QUESTIONS
    from data.aptitude_english import APTITUDE_ENGLISH_QUESTIONS   
    from data.aptitude_science import APTITUDE_SCIENCE_QUESTIONS   
    from data.aptitude_abstract import APTITUDE_ABSTRACT_QUESTIONS 
    load_dotenv()

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "coursify")  

    # ─── Collection mapping ──────────────────────────────────────────────────────
    COLLECTIONS = {
        "riasec": {
            "name": "questions_riasec",
            "data": RIASEC_QUESTIONS,
            "unique_field": "text",
        },
        "bigfive": {
            "name": "questions_bigfive",
            "data": BIGFIVE_QUESTIONS,
            "unique_field": "text",
        },
        "aptitude_math": {
            "name": "questions_aptitude",
            "data": APTITUDE_MATH_QUESTIONS,
            "unique_field": "text",
        },
        "aptitude_english": {
            "name": "questions_aptitude",
            "data": APTITUDE_ENGLISH_QUESTIONS,
            "unique_field": "text",
        },
        "aptitude_science": {
            "name": "questions_aptitude",
            "data": APTITUDE_SCIENCE_QUESTIONS,
            "unique_field": "text",
        },
        "aptitude_abstract": {
            "name": "questions_aptitude",
            "data": APTITUDE_ABSTRACT_QUESTIONS,
            "unique_field": "text",
        },
    }


    # ─── Core seeder ─────────────────────────────────────────────────────────────

    async def seed_collection(db, key: str, clear: bool = False, dry_run: bool = False):
        config = COLLECTIONS[key]
        col_name = config["name"]
        data = config["data"]
        unique_field = config["unique_field"]

        print(f"\n{'='*55}")
        print(f"  Seeding: {key.upper()} → collection: '{col_name}'")
        print(f"  Total records to seed: {len(data)}")
        print(f"{'='*55}")

        if dry_run:
            print("  [DRY RUN] Sample (first 2 records):")
            for item in data[:2]:
                print(f"    {item}")
            print(f"  [DRY RUN] Would insert {len(data)} records. No DB write.")
            return

        collection = db[col_name]

        if clear:
            if key == "riasec":
                result = await collection.delete_many({"type": "riasec"})
            elif key == "bigfive":
                result = await collection.delete_many({"type": "bigfive"})
            elif key.startswith("aptitude_"):
                subject = key.replace("aptitude_", "")
                result = await collection.delete_many({"type": "aptitude", "subject": subject})
            print(f"  Cleared {result.deleted_count} existing records.")

        # Deduplicate: skip records that already exist by unique_field
        inserted = 0
        skipped = 0

        for record in data:
            exists = await collection.find_one({unique_field: record[unique_field]})
            if exists:
                skipped += 1
                continue
            await collection.insert_one(record)
            inserted += 1

        print(f"   Inserted: {inserted} |   Skipped (already exist): {skipped}")


    async def create_indexes(db):
        """Create recommended indexes for fast random sampling."""
        print("\n  Creating indexes...")

        await db["questions_riasec"].create_index([("subcategory", 1), ("active", 1)])
        await db["questions_bigfive"].create_index([("subcategory", 1), ("active", 1)])
        await db["questions_aptitude"].create_index([
            ("subject", 1), ("topic", 1), ("difficulty", 1), ("active", 1)
        ])

        print("  Indexes created.")


    async def main(target: str, clear: bool, dry_run: bool):
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[DB_NAME]

        print(f"\n  Connected to: {MONGO_URI} / {DB_NAME}")

        if target == "all":
            keys = list(COLLECTIONS.keys())
        else:
            if target not in COLLECTIONS:
                print(f"\n  Unknown collection key: '{target}'")
                print(f"  Available keys: {list(COLLECTIONS.keys())}")
                client.close()
                return
            keys = [target]

        for key in keys:
            await seed_collection(db, key, clear=clear, dry_run=dry_run)

        if not dry_run:
            await create_indexes(db)

        print("\n  Done.\n")
        client.close()


    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Assessment DB Seeder")
        parser.add_argument(
            "--collection",
            type=str,
            default="riasec",
            help=f"Which collection to seed. Choices: {list(COLLECTIONS.keys()) + ['all']}"
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing records for this collection before seeding"
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Preview without writing to DB"
        )
        args = parser.parse_args()

        asyncio.run(main(args.collection, args.clear, args.dry_run))