from datetime import datetime, timezone

# 8 questions per OCEAN trait = 40 total
# type: bigfive | difficulty: null (not applicable)
# reverse_scored: True means the answer should be inverted before scoring
# Response scale: 1 (Strongly Disagree) to 5 (Strongly Agree)

BIGFIVE_QUESTIONS = [

    # ─────────────────────────────────────────
    # OPENNESS (O) — curiosity, imagination, creativity
    # ─────────────────────────────────────────
    {"type": "bigfive", "subcategory": "openness", "text": "I enjoy exploring new ideas and concepts.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "openness", "text": "I have a vivid imagination.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "openness", "text": "I enjoy art, music, or literature.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "openness", "text": "I like trying new and different things.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "openness", "text": "I prefer routine tasks over unfamiliar ones.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "openness", "text": "I am curious about many different things.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "openness", "text": "I find philosophical or abstract discussions interesting.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "openness", "text": "I tend to stick to what I know rather than experimenting.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # CONSCIENTIOUSNESS (C) — discipline, organization, goal-driven
    # ─────────────────────────────────────────
    {"type": "bigfive", "subcategory": "conscientiousness", "text": "I always complete tasks on time.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "conscientiousness", "text": "I keep my belongings and workspace organized.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "conscientiousness", "text": "I often procrastinate on important tasks.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "conscientiousness", "text": "I follow a schedule or plan to manage my responsibilities.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "conscientiousness", "text": "I am careful and thorough in everything I do.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "conscientiousness", "text": "I make impulsive decisions without thinking them through.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "conscientiousness", "text": "I set clear goals and work persistently toward them.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "conscientiousness", "text": "I often leave things unfinished.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # EXTRAVERSION (E) — sociability, energy, assertiveness
    # ─────────────────────────────────────────
    {"type": "bigfive", "subcategory": "extraversion", "text": "I feel energized when I am around other people.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "extraversion", "text": "I enjoy being the center of attention in social situations.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "extraversion", "text": "I prefer spending time alone over going to parties or gatherings.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "extraversion", "text": "I find it easy to start conversations with new people.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "extraversion", "text": "I am talkative and outgoing in group settings.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "extraversion", "text": "I tend to keep to myself rather than seeking social interaction.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "extraversion", "text": "I take charge in group activities and social events.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "extraversion", "text": "I feel drained after spending a lot of time with other people.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # AGREEABLENESS (A) — cooperation, empathy, trust
    # ─────────────────────────────────────────
    {"type": "bigfive", "subcategory": "agreeableness", "text": "I care about the feelings and well-being of others.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "agreeableness", "text": "I am willing to compromise to avoid conflict.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "agreeableness", "text": "I tend to be critical or skeptical of other people's motives.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "agreeableness", "text": "I try to be kind and considerate to everyone I meet.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "agreeableness", "text": "I easily forgive others when they make mistakes.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "agreeableness", "text": "I enjoy arguing or debating with others.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "agreeableness", "text": "I find it easy to trust and cooperate with others.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "agreeableness", "text": "I can be cold or distant toward people I disagree with.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # NEUROTICISM (N) — emotional instability, anxiety, moodiness
    # ─────────────────────────────────────────
    {"type": "bigfive", "subcategory": "neuroticism", "text": "I often feel anxious or worried about things.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "neuroticism", "text": "I remain calm under pressure and stressful situations.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "neuroticism", "text": "My mood changes frequently throughout the day.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "neuroticism", "text": "I easily get upset or frustrated by small problems.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "neuroticism", "text": "I feel confident and secure in most situations.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "neuroticism", "text": "I tend to dwell on negative events for a long time.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "neuroticism", "text": "I experience frequent shifts between feeling happy and feeling low.", "reverse_scored": False, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "bigfive", "subcategory": "neuroticism", "text": "I handle setbacks and failures without losing emotional balance.", "reverse_scored": True, "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
]