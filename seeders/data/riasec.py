from datetime import datetime, timezone

# 10 questions per RIASEC code = 60 total
# type: riasec | difficulty: null (not applicable)
# Response scale: 1 (Strongly Disagree) to 5 (Strongly Agree)

RIASEC_QUESTIONS = [

    # ─────────────────────────────────────────
    # REALISTIC (R) — practical, hands-on, mechanical
    # ─────────────────────────────────────────
    {"type": "riasec", "subcategory": "realistic", "text": "I enjoy repairing or building mechanical things.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I like working with tools, machines, or equipment.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I prefer doing physical or outdoor activities over sitting at a desk.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I enjoy hands-on projects where I can see a tangible result.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I am good at fixing broken items around the house.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I find satisfaction in assembling or constructing things.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I enjoy working with plants, animals, or the natural environment.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I like doing tasks that require physical coordination and skill.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I would enjoy a career that involves operating machinery or equipment.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "realistic", "text": "I prefer practical solutions over theoretical discussions.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # INVESTIGATIVE (I) — analytical, curious, scientific
    # ─────────────────────────────────────────
    {"type": "riasec", "subcategory": "investigative", "text": "I enjoy researching topics in depth to find answers.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I like solving complex problems that require logical thinking.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I am curious about how things work scientifically.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I enjoy reading scientific articles or academic materials.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I like performing experiments or testing hypotheses.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I prefer analyzing data to draw conclusions.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I enjoy exploring new ideas and theories even if they have no immediate use.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I find math or science problems more engaging than creative tasks.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I enjoy thinking critically about why things happen the way they do.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "investigative", "text": "I would enjoy a career that involves research, analysis, or discovery.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # ARTISTIC (A) — creative, expressive, imaginative
    # ─────────────────────────────────────────
    {"type": "riasec", "subcategory": "artistic", "text": "I enjoy expressing myself through art, music, or writing.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I like activities that allow me to use my imagination.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I prefer open-ended tasks over structured step-by-step processes.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I enjoy designing, decorating, or creating visual presentations.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I am drawn to careers in the arts, media, or entertainment.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I enjoy performing in front of others (singing, acting, dancing).", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I find beauty in everyday objects and surroundings.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I like writing stories, poems, or creative essays.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I prefer working in environments that value originality and self-expression.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "artistic", "text": "I think creatively when solving problems rather than following rules.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # SOCIAL (S) — helpful, cooperative, empathetic
    # ─────────────────────────────────────────
    {"type": "riasec", "subcategory": "social", "text": "I enjoy helping others solve their personal problems.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I feel fulfilled when I make a positive difference in someone's life.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I enjoy working in teams and collaborating with others.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I like teaching or explaining things to other people.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I am drawn to careers in education, healthcare, or counseling.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I enjoy listening to others and offering support or advice.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I find it easy to understand how other people feel.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I like organizing group activities or community events.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I enjoy volunteering or doing community service.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "social", "text": "I prefer people-centered work over working alone with data or machines.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # ENTERPRISING (E) — persuasive, leadership, ambitious
    # ─────────────────────────────────────────
    {"type": "riasec", "subcategory": "enterprising", "text": "I enjoy taking charge and leading a group toward a goal.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I like persuading or motivating others to take action.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I am confident when speaking in front of a group.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I enjoy making decisions and taking calculated risks.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I am drawn to careers in business, sales, or management.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I like starting new projects or initiatives.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I enjoy competing and am motivated by achieving goals.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I feel comfortable negotiating or debating with others.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I like influencing people's opinions or decisions.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "enterprising", "text": "I see myself as someone who can inspire others to follow a vision.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},

    # ─────────────────────────────────────────
    # CONVENTIONAL (C) — organized, detail-oriented, structured
    # ─────────────────────────────────────────
    {"type": "riasec", "subcategory": "conventional", "text": "I enjoy organizing files, data, or records in a systematic way.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I prefer following established procedures over improvising.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I like working with numbers, spreadsheets, or financial records.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I pay close attention to detail in everything I do.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I am drawn to careers in accounting, administration, or data management.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I feel comfortable working in structured environments with clear rules.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I enjoy tasks that require precision and accuracy.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I like keeping records and making sure everything is in order.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I prefer predictable routines over constantly changing tasks.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
    {"type": "riasec", "subcategory": "conventional", "text": "I find satisfaction in completing tasks thoroughly and correctly.", "difficulty": None, "active": True, "createdAt": datetime.now(timezone.utc)},
]