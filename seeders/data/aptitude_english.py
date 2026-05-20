from datetime import datetime, timezone

# English aptitude questions
# 4 topics × 3 difficulties × 6 questions = 72 total
# Selected at runtime: 1 easy + 1 medium + 1 hard per topic = 12 per subject

APTITUDE_ENGLISH_QUESTIONS = [

    # ════════════════════════════════════════
    # TOPIC: GRAMMAR & SENTENCE STRUCTURE
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "easy",
     "text": "Which sentence is grammatically correct?",
     "options": [{"label": "A", "value": "She don't like apples."}, {"label": "B", "value": "She doesn't likes apples."}, {"label": "C", "value": "She doesn't like apples."}, {"label": "D", "value": "She not like apples."}],
     "correct_answer": "C", "explanation": "Third-person singular requires 'doesn't' + base verb.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "easy",
     "text": "Choose the correct verb: 'The dogs ___ barking loudly.'",
     "options": [{"label": "A", "value": "is"}, {"label": "B", "value": "are"}, {"label": "C", "value": "was"}, {"label": "D", "value": "am"}],
     "correct_answer": "B", "explanation": "'Dogs' is plural, so the verb must be 'are'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "easy",
     "text": "Which word is a conjunction in this sentence: 'I wanted to go, but it rained.'",
     "options": [{"label": "A", "value": "wanted"}, {"label": "B", "value": "go"}, {"label": "C", "value": "but"}, {"label": "D", "value": "rained"}],
     "correct_answer": "C", "explanation": "'But' is a coordinating conjunction connecting two independent clauses.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "easy",
     "text": "Identify the correct punctuation: 'What time is it___'",
     "options": [{"label": "A", "value": "."}, {"label": "B", "value": "!"}, {"label": "C", "value": "?"}, {"label": "D", "value": ","}],
     "correct_answer": "C", "explanation": "A direct question ends with a question mark.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "easy",
     "text": "Which is the correct plural of 'child'?",
     "options": [{"label": "A", "value": "childs"}, {"label": "B", "value": "childes"}, {"label": "C", "value": "children"}, {"label": "D", "value": "childrens"}],
     "correct_answer": "C", "explanation": "'Children' is the irregular plural of 'child'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "easy",
     "text": "Which sentence uses the past tense correctly?",
     "options": [{"label": "A", "value": "She go to school yesterday."}, {"label": "B", "value": "She goes to school yesterday."}, {"label": "C", "value": "She went to school yesterday."}, {"label": "D", "value": "She gone to school yesterday."}],
     "correct_answer": "C", "explanation": "'Went' is the correct simple past tense of 'go'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "medium",
     "text": "Choose the sentence that is NOT a run-on sentence.",
     "options": [{"label": "A", "value": "I went to the store I bought milk."}, {"label": "B", "value": "She ran fast she won the race."}, {"label": "C", "value": "He studied hard, and he passed the exam."}, {"label": "D", "value": "They played outside it was sunny."}],
     "correct_answer": "C", "explanation": "Option C correctly uses a comma and coordinating conjunction to join two clauses.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "medium",
     "text": "Which sentence uses the correct form of the pronoun?",
     "options": [{"label": "A", "value": "Between you and I, this is wrong."}, {"label": "B", "value": "Between you and me, this is wrong."}, {"label": "C", "value": "Between you and myself, this is wrong."}, {"label": "D", "value": "Between I and you, this is wrong."}],
     "correct_answer": "B", "explanation": "After prepositions (like 'between'), use objective case: 'me', not 'I'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "medium",
     "text": "Identify the type of sentence: 'Although it was raining, we still went outside.'",
     "options": [{"label": "A", "value": "Simple"}, {"label": "B", "value": "Compound"}, {"label": "C", "value": "Complex"}, {"label": "D", "value": "Compound-complex"}],
     "correct_answer": "C", "explanation": "A complex sentence has one independent clause and at least one dependent clause ('Although it was raining').", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "medium",
     "text": "Which sentence uses the subjunctive mood correctly?",
     "options": [{"label": "A", "value": "If I was you, I would leave."}, {"label": "B", "value": "If I were you, I would leave."}, {"label": "C", "value": "If I am you, I would leave."}, {"label": "D", "value": "If I be you, I would leave."}],
     "correct_answer": "B", "explanation": "The subjunctive mood uses 'were' for hypothetical or contrary-to-fact conditions.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "medium",
     "text": "Which sentence contains a dangling modifier?",
     "options": [{"label": "A", "value": "Running quickly, Marco caught the bus."}, {"label": "B", "value": "Running quickly, the bus was caught."}, {"label": "C", "value": "Marco, running quickly, caught the bus."}, {"label": "D", "value": "The bus was caught by Marco, who was running quickly."}],
     "correct_answer": "B", "explanation": "In B, 'Running quickly' modifies 'the bus', but the bus can't run — that's a dangling modifier.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "medium",
     "text": "Which option correctly uses a semicolon?",
     "options": [{"label": "A", "value": "I love coffee; but I also love tea."}, {"label": "B", "value": "She studied hard; she passed the exam."}, {"label": "C", "value": "He bought apples; and oranges."}, {"label": "D", "value": "They arrived; late."}],
     "correct_answer": "B", "explanation": "A semicolon correctly joins two related independent clauses without a conjunction.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "hard",
     "text": "Which sentence correctly uses the past perfect tense?",
     "options": [{"label": "A", "value": "She has left before he arrived."}, {"label": "B", "value": "She had left before he arrived."}, {"label": "C", "value": "She was leaving before he arrived."}, {"label": "D", "value": "She left before he has arrived."}],
     "correct_answer": "B", "explanation": "Past perfect ('had left') is used for an action completed before another past action.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "hard",
     "text": "Identify the error: 'Neither the manager nor the employees was informed.'",
     "options": [{"label": "A", "value": "Neither"}, {"label": "B", "value": "nor"}, {"label": "C", "value": "was"}, {"label": "D", "value": "informed"}],
     "correct_answer": "C", "explanation": "With 'neither/nor', the verb agrees with the closer subject ('employees' = plural), so 'were' is correct.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "hard",
     "text": "Which sentence demonstrates correct parallel structure?",
     "options": [{"label": "A", "value": "She likes swimming, to run, and cycling."}, {"label": "B", "value": "She likes to swim, run, and cycle."}, {"label": "C", "value": "She likes swimming, running, and to cycle."}, {"label": "D", "value": "She likes to swim, running, and cycling."}],
     "correct_answer": "B", "explanation": "Parallel structure requires consistent grammatical form: 'to swim, run, and cycle' are all infinitives.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "hard",
     "text": "Choose the sentence that correctly uses the active voice for emphasis.",
     "options": [{"label": "A", "value": "The report was written by the team."}, {"label": "B", "value": "The team had been writing the report."}, {"label": "C", "value": "The team wrote the report."}, {"label": "D", "value": "It was the team that had the report written."}],
     "correct_answer": "C", "explanation": "Active voice: subject (team) performs the action (wrote). Direct and clear.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "hard",
     "text": "What grammatical error appears in: 'The data shows that results is significant.'",
     "options": [{"label": "A", "value": "Subject-verb disagreement on 'data shows'"}, {"label": "B", "value": "Subject-verb disagreement on 'results is'"}, {"label": "C", "value": "Misuse of 'that'"}, {"label": "D", "value": "Incorrect tense of 'shows'"}],
     "correct_answer": "B", "explanation": "'Results' is plural → should be 'results are significant'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "grammar_and_sentence_structure", "difficulty": "hard",
     "text": "Which correctly converts this sentence to reported speech: 'She said, \"I am tired.\"'",
     "options": [{"label": "A", "value": "She said that she is tired."}, {"label": "B", "value": "She said that she was tired."}, {"label": "C", "value": "She said that I am tired."}, {"label": "D", "value": "She told that she was tired."}],
     "correct_answer": "B", "explanation": "Reported speech shifts tense back: 'am' → 'was'. 'Said' takes 'that', not 'told'.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: READING COMPREHENSION
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'Maria woke up late, skipped breakfast, and rushed to school. She arrived just as the bell rang.' Why did Maria rush to school?",
     "options": [{"label": "A", "value": "She was hungry."}, {"label": "B", "value": "She woke up late."}, {"label": "C", "value": "She forgot her bag."}, {"label": "D", "value": "She wanted to be early."}],
     "correct_answer": "B", "explanation": "The passage directly states she woke up late, which caused her to rush.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'The sun sets in the west. Every evening, the sky turns orange, pink, and purple.' What is the main idea?",
     "options": [{"label": "A", "value": "The sun is very hot."}, {"label": "B", "value": "Sunsets are colorful."}, {"label": "C", "value": "Sunrise happens in the morning."}, {"label": "D", "value": "The sky changes color during storms."}],
     "correct_answer": "B", "explanation": "The passage describes the colorful appearance of sunsets.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'Dogs are loyal animals. They protect their owners and offer companionship.' What does 'loyal' most likely mean here?",
     "options": [{"label": "A", "value": "Dangerous"}, {"label": "B", "value": "Faithful and dependable"}, {"label": "C", "value": "Loud and aggressive"}, {"label": "D", "value": "Wild and unpredictable"}],
     "correct_answer": "B", "explanation": "The context (protect, companionship) supports 'faithful and dependable'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'Juan studied every night for a week. On exam day, he felt confident and answered all questions.' What can you infer about Juan?",
     "options": [{"label": "A", "value": "He was lucky."}, {"label": "B", "value": "He cheated on the exam."}, {"label": "C", "value": "His preparation helped him feel ready."}, {"label": "D", "value": "He found the exam very difficult."}],
     "correct_answer": "C", "explanation": "His consistent studying directly explains his confidence on exam day.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'The library was quiet. Students sat with their books open, heads bowed in concentration.' What is the mood of this passage?",
     "options": [{"label": "A", "value": "Chaotic"}, {"label": "B", "value": "Peaceful and focused"}, {"label": "C", "value": "Tense and fearful"}, {"label": "D", "value": "Joyful and lively"}],
     "correct_answer": "B", "explanation": "Words like 'quiet', 'heads bowed', and 'concentration' create a calm, focused mood.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "easy",
     "text": "Read: 'Trees absorb carbon dioxide and release oxygen. They also provide shade and habitat for animals.' What is one benefit of trees mentioned?",
     "options": [{"label": "A", "value": "They produce food for humans."}, {"label": "B", "value": "They cause rain."}, {"label": "C", "value": "They release oxygen."}, {"label": "D", "value": "They produce electricity."}],
     "correct_answer": "C", "explanation": "The passage explicitly states that trees release oxygen.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'Despite the heavy rainfall, the farmers celebrated. The drought had lasted three years, and the crops desperately needed water.' Why did the farmers celebrate the rain?",
     "options": [{"label": "A", "value": "They wanted a day off."}, {"label": "B", "value": "Rain meant the harvest season was over."}, {"label": "C", "value": "The rain ended a long drought that threatened their crops."}, {"label": "D", "value": "They had never seen rain before."}],
     "correct_answer": "C", "explanation": "The passage explains the three-year drought — rain was a relief for their struggling crops.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'Social media connects people across the world. However, it has also been linked to increased anxiety, shorter attention spans, and the spread of misinformation.' What is the author's tone?",
     "options": [{"label": "A", "value": "Purely positive"}, {"label": "B", "value": "Balanced and cautionary"}, {"label": "C", "value": "Angry and accusatory"}, {"label": "D", "value": "Confused and uncertain"}],
     "correct_answer": "B", "explanation": "The author acknowledges both a benefit and multiple concerns — a balanced, cautionary tone.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'The principal announced new rules. Some students cheered, while others groaned. Teachers stood silently by the door.' What does this suggest about the students' reaction?",
     "options": [{"label": "A", "value": "All students agreed with the rules."}, {"label": "B", "value": "The rules were confusing."}, {"label": "C", "value": "Students had mixed feelings about the rules."}, {"label": "D", "value": "Teachers were against the rules."}],
     "correct_answer": "C", "explanation": "The contrast between cheering and groaning shows divided opinion.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'Technology has made communication faster. Yet, many argue that face-to-face interaction is becoming rare, weakening deep personal connections.' What is the implied argument?",
     "options": [{"label": "A", "value": "Technology should be banned."}, {"label": "B", "value": "Speed of communication is unimportant."}, {"label": "C", "value": "Faster communication may come at the cost of meaningful relationships."}, {"label": "D", "value": "Face-to-face meetings are obsolete."}],
     "correct_answer": "C", "explanation": "The passage implies that while technology speeds things up, it may reduce deep personal bonds.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'He had everything — wealth, fame, and admiration. Yet, sitting alone in his mansion at night, he felt an emptiness he could not name.' What theme does this best illustrate?",
     "options": [{"label": "A", "value": "Wealth leads to happiness."}, {"label": "B", "value": "Fame is the most important goal."}, {"label": "C", "value": "Material success does not guarantee fulfillment."}, {"label": "D", "value": "Large houses cause loneliness."}],
     "correct_answer": "C", "explanation": "The contrast between external success and inner emptiness illustrates the limits of material wealth.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "medium",
     "text": "Read: 'The committee reviewed three proposals. Proposal A was cost-effective but slow. Proposal B was fast but expensive. Proposal C balanced both.' Which proposal would most likely be chosen?",
     "options": [{"label": "A", "value": "Proposal A"}, {"label": "B", "value": "Proposal B"}, {"label": "C", "value": "Proposal C"}, {"label": "D", "value": "None of them"}],
     "correct_answer": "C", "explanation": "Proposal C offers the best balance of cost and speed — a logical choice.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'Critics praised the novel for its complex characters but noted its slow pacing. Readers, however, found it deeply moving.' What can be inferred about the author's style?",
     "options": [{"label": "A", "value": "The author prioritizes plot speed over character depth."}, {"label": "B", "value": "The author sacrifices fast pacing for emotional and character depth."}, {"label": "C", "value": "The author writes exclusively for critics."}, {"label": "D", "value": "The author's readers disliked the novel."}],
     "correct_answer": "B", "explanation": "Critics noted slow pacing alongside complex characters — suggesting the author values depth over speed.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'Governments worldwide fund the arts less every year, calling it a luxury. Yet studies show that arts education improves critical thinking, empathy, and academic performance.' What is the author's implicit argument?",
     "options": [{"label": "A", "value": "Arts funding should be eliminated."}, {"label": "B", "value": "Arts education is a luxury with no measurable value."}, {"label": "C", "value": "Arts education has practical academic and social benefits that justify funding."}, {"label": "D", "value": "Governments are always wrong about education policy."}],
     "correct_answer": "C", "explanation": "The author counters the 'luxury' label by citing specific measurable benefits, implying arts funding is justified.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'The new policy was introduced quietly. No announcements were made. When employees asked, managers gave vague answers.' What does this passage suggest about the organization?",
     "options": [{"label": "A", "value": "The organization values transparency."}, {"label": "B", "value": "The organization is disorganized and forgetful."}, {"label": "C", "value": "The organization deliberately withheld information from employees."}, {"label": "D", "value": "The policy was unimportant."}],
     "correct_answer": "C", "explanation": "The absence of announcements and vague responses suggest intentional withholding of information.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read two perspectives — A: 'Online learning offers flexibility and access.' B: 'Online learning lacks social interaction and mentorship.' A student who thrives under self-direction would most likely agree with:",
     "options": [{"label": "A", "value": "Perspective A only"}, {"label": "B", "value": "Perspective B only"}, {"label": "C", "value": "Both perspectives equally"}, {"label": "D", "value": "Neither perspective"}],
     "correct_answer": "A", "explanation": "A self-directed student benefits most from flexibility — the strength highlighted in Perspective A.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'Every generation calls the next one lazy. The Romans wrote about lazy youth. So did the Victorians. So do we today.' What logical point is the author making?",
     "options": [{"label": "A", "value": "Young people have always been lazy."}, {"label": "B", "value": "Older generations are always right about youth."}, {"label": "C", "value": "Criticism of younger generations is a recurring pattern, not necessarily a fact."}, {"label": "D", "value": "The Romans were the best judges of character."}],
     "correct_answer": "C", "explanation": "The historical pattern suggests this criticism is a generational bias, not an objective truth.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "reading_comprehension", "difficulty": "hard",
     "text": "Read: 'The scientist published findings that challenged the accepted model. Colleagues dismissed the work initially. Decades later, it became the foundation of modern theory.' What does this passage most powerfully illustrate?",
     "options": [{"label": "A", "value": "Scientists are always wrong at first."}, {"label": "B", "value": "Peer review is unnecessary."}, {"label": "C", "value": "Groundbreaking ideas are often rejected before being accepted."}, {"label": "D", "value": "Scientific consensus is always correct."}],
     "correct_answer": "C", "explanation": "The arc from dismissal to foundational theory illustrates how revolutionary ideas face initial rejection.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: VOCABULARY & CONTEXT CLUES
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "easy",
     "text": "What does 'enormous' mean? 'The enormous elephant barely fit through the gate.'",
     "options": [{"label": "A", "value": "Tiny"}, {"label": "B", "value": "Very large"}, {"label": "C", "value": "Angry"}, {"label": "D", "value": "Fast"}],
     "correct_answer": "B", "explanation": "Context: barely fitting through a gate implies the elephant is very large.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "easy",
     "text": "Choose the antonym of 'ancient'.",
     "options": [{"label": "A", "value": "Old"}, {"label": "B", "value": "Historical"}, {"label": "C", "value": "Modern"}, {"label": "D", "value": "Ruined"}],
     "correct_answer": "C", "explanation": "The antonym (opposite) of 'ancient' is 'modern'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "easy",
     "text": "What does 'curious' mean? 'The curious cat kept sniffing around every corner of the room.'",
     "options": [{"label": "A", "value": "Sleepy"}, {"label": "B", "value": "Angry"}, {"label": "C", "value": "Eager to explore and learn"}, {"label": "D", "value": "Frightened"}],
     "correct_answer": "C", "explanation": "Sniffing around every corner shows the cat is exploring — curious means eager to learn.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "easy",
     "text": "Which word is a synonym of 'happy'?",
     "options": [{"label": "A", "value": "Sad"}, {"label": "B", "value": "Joyful"}, {"label": "C", "value": "Angry"}, {"label": "D", "value": "Tired"}],
     "correct_answer": "B", "explanation": "'Joyful' has the same meaning as 'happy'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "easy",
     "text": "What does 'swift' mean? 'The swift runner crossed the finish line first.'",
     "options": [{"label": "A", "value": "Clumsy"}, {"label": "B", "value": "Fast"}, {"label": "C", "value": "Tall"}, {"label": "D", "value": "Nervous"}],
     "correct_answer": "B", "explanation": "Finishing first suggests the runner was fast — 'swift' means fast.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "easy",
     "text": "Choose the word closest in meaning to 'construct'.",
     "options": [{"label": "A", "value": "Destroy"}, {"label": "B", "value": "Build"}, {"label": "C", "value": "Paint"}, {"label": "D", "value": "Design"}],
     "correct_answer": "B", "explanation": "'Construct' means to build or create something.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "medium",
     "text": "What does 'ambiguous' mean? 'The instructions were so ambiguous that no one knew what to do.'",
     "options": [{"label": "A", "value": "Very clear and detailed"}, {"label": "B", "value": "Unclear and open to multiple interpretations"}, {"label": "C", "value": "Written in another language"}, {"label": "D", "value": "Too long to read"}],
     "correct_answer": "B", "explanation": "No one knew what to do → the instructions lacked clarity — ambiguous means unclear.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "medium",
     "text": "What does 'reluctant' mean? 'She was reluctant to speak in front of the class, despite knowing the answer.'",
     "options": [{"label": "A", "value": "Eager"}, {"label": "B", "value": "Unable"}, {"label": "C", "value": "Unwilling or hesitant"}, {"label": "D", "value": "Confident"}],
     "correct_answer": "C", "explanation": "Knowing the answer but not speaking suggests hesitancy — 'reluctant' means unwilling.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "medium",
     "text": "What does the prefix 'mis-' indicate in the word 'misinform'?",
     "options": [{"label": "A", "value": "Before"}, {"label": "B", "value": "Again"}, {"label": "C", "value": "Wrongly or incorrectly"}, {"label": "D", "value": "Without"}],
     "correct_answer": "C", "explanation": "'Mis-' means wrongly — 'misinform' means to give incorrect information.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "medium",
     "text": "What does 'meticulous' mean? 'She was meticulous in her work, checking every detail twice.'",
     "options": [{"label": "A", "value": "Careless"}, {"label": "B", "value": "Very careful and precise"}, {"label": "C", "value": "Speedy"}, {"label": "D", "value": "Creative"}],
     "correct_answer": "B", "explanation": "Checking every detail twice shows great care — meticulous means very careful.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "medium",
     "text": "Choose the word that best completes the analogy: 'Doctor : Hospital :: Teacher : ___'",
     "options": [{"label": "A", "value": "Library"}, {"label": "B", "value": "School"}, {"label": "C", "value": "Office"}, {"label": "D", "value": "Clinic"}],
     "correct_answer": "B", "explanation": "A doctor works at a hospital; a teacher works at a school.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "medium",
     "text": "What does 'prevalent' mean? 'Colds are prevalent during the rainy season.'",
     "options": [{"label": "A", "value": "Rare and unusual"}, {"label": "B", "value": "Dangerous"}, {"label": "C", "value": "Widespread and common"}, {"label": "D", "value": "Mild"}],
     "correct_answer": "C", "explanation": "Being common during a season implies widespread occurrence — prevalent means common.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "hard",
     "text": "What does 'equivocate' mean? 'The politician equivocated when asked about the scandal, never giving a direct answer.'",
     "options": [{"label": "A", "value": "To speak clearly and directly"}, {"label": "B", "value": "To use vague or ambiguous language to avoid commitment"}, {"label": "C", "value": "To lie openly"}, {"label": "D", "value": "To refuse to answer"}],
     "correct_answer": "B", "explanation": "Not giving direct answers suggests deliberate vagueness — equivocate means to be intentionally ambiguous.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "hard",
     "text": "What does 'ephemeral' mean? 'The ephemeral beauty of cherry blossoms makes them all the more precious.'",
     "options": [{"label": "A", "value": "Eternal and lasting"}, {"label": "B", "value": "Very colorful"}, {"label": "C", "value": "Short-lived and fleeting"}, {"label": "D", "value": "Fragrant and sweet"}],
     "correct_answer": "C", "explanation": "Their preciousness comes from being temporary — ephemeral means short-lived.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "hard",
     "text": "What does the root word 'bene' indicate in 'benevolent'?",
     "options": [{"label": "A", "value": "Against"}, {"label": "B", "value": "Good or well"}, {"label": "C", "value": "Below"}, {"label": "D", "value": "Many"}],
     "correct_answer": "B", "explanation": "'Bene' is Latin for 'good/well' — benevolent means well-meaning or kind.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "hard",
     "text": "What does 'sycophant' mean? 'He was known as a sycophant who constantly flattered his boss, regardless of merit.'",
     "options": [{"label": "A", "value": "A harsh critic"}, {"label": "B", "value": "An obedient employee"}, {"label": "C", "value": "A person who uses flattery to gain favor"}, {"label": "D", "value": "A logical thinker"}],
     "correct_answer": "C", "explanation": "Constantly flattering for personal gain describes a sycophant.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "hard",
     "text": "Choose the correct meaning of 'juxtapose': 'The photographer juxtaposed images of wealth and poverty to make a social statement.'",
     "options": [{"label": "A", "value": "To separate two things entirely"}, {"label": "B", "value": "To place two contrasting things side by side for effect"}, {"label": "C", "value": "To combine two things into one"}, {"label": "D", "value": "To hide one thing behind another"}],
     "correct_answer": "B", "explanation": "Placing wealth and poverty images together for contrast is the definition of juxtapose.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "vocabulary_and_context_clues", "difficulty": "hard",
     "text": "What does 'recalcitrant' mean? 'The recalcitrant student refused to follow any instructions from the teacher.'",
     "options": [{"label": "A", "value": "Enthusiastic and eager"}, {"label": "B", "value": "Stubbornly resistant to authority"}, {"label": "C", "value": "Confused and lost"}, {"label": "D", "value": "Shy and quiet"}],
     "correct_answer": "B", "explanation": "Refusing all instructions shows stubborn resistance — recalcitrant means uncooperative.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: LOGICAL/VERBAL REASONING
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "easy",
     "text": "Complete the analogy: 'Hot is to Cold as Day is to ___'",
     "options": [{"label": "A", "value": "Sun"}, {"label": "B", "value": "Night"}, {"label": "C", "value": "Morning"}, {"label": "D", "value": "Light"}],
     "correct_answer": "B", "explanation": "Hot and Cold are opposites; Day and Night are opposites.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "easy",
     "text": "Which word does NOT belong? Apples, Bananas, Carrots, Grapes",
     "options": [{"label": "A", "value": "Apples"}, {"label": "B", "value": "Bananas"}, {"label": "C", "value": "Carrots"}, {"label": "D", "value": "Grapes"}],
     "correct_answer": "C", "explanation": "Apples, bananas, and grapes are fruits. Carrots is a vegetable.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "easy",
     "text": "All birds have wings. A penguin is a bird. Therefore:",
     "options": [{"label": "A", "value": "A penguin can fly."}, {"label": "B", "value": "A penguin has wings."}, {"label": "C", "value": "All birds are penguins."}, {"label": "D", "value": "A penguin is not a bird."}],
     "correct_answer": "B", "explanation": "All birds have wings, and a penguin is a bird — therefore a penguin has wings.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "easy",
     "text": "Which is the most logical order? (1) Eat breakfast (2) Wake up (3) Brush teeth (4) Get dressed",
     "options": [{"label": "A", "value": "2, 1, 3, 4"}, {"label": "B", "value": "2, 3, 1, 4"}, {"label": "C", "value": "2, 4, 1, 3"}, {"label": "D", "value": "1, 2, 3, 4"}],
     "correct_answer": "A", "explanation": "Logically: wake up → eat → brush teeth → get dressed.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "easy",
     "text": "Which word is most similar in meaning to 'begin'?",
     "options": [{"label": "A", "value": "End"}, {"label": "B", "value": "Start"}, {"label": "C", "value": "Pause"}, {"label": "D", "value": "Continue"}],
     "correct_answer": "B", "explanation": "'Start' and 'begin' are synonyms.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "easy",
     "text": "If all squares are rectangles, which statement must be true?",
     "options": [{"label": "A", "value": "All rectangles are squares."}, {"label": "B", "value": "Some squares are not rectangles."}, {"label": "C", "value": "A square is a type of rectangle."}, {"label": "D", "value": "Rectangles have four unequal sides."}],
     "correct_answer": "C", "explanation": "If all squares are rectangles, then a square is a type (subset) of rectangle.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "medium",
     "text": "Pen is to Writer as Brush is to ___",
     "options": [{"label": "A", "value": "Canvas"}, {"label": "B", "value": "Paint"}, {"label": "C", "value": "Painter"}, {"label": "D", "value": "Gallery"}],
     "correct_answer": "C", "explanation": "A pen is the tool of a writer; a brush is the tool of a painter.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "medium",
     "text": "Some teachers are principals. All principals are administrators. Which is definitely true?",
     "options": [{"label": "A", "value": "All teachers are administrators."}, {"label": "B", "value": "Some teachers are administrators."}, {"label": "C", "value": "No teachers are administrators."}, {"label": "D", "value": "All administrators are teachers."}],
     "correct_answer": "B", "explanation": "Some teachers = principals, and all principals = administrators → some teachers are administrators.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "medium",
     "text": "Which conclusion logically follows? 'No fish can walk. Nemo is a fish.'",
     "options": [{"label": "A", "value": "Nemo can walk."}, {"label": "B", "value": "Nemo cannot walk."}, {"label": "C", "value": "Nemo is not a fish."}, {"label": "D", "value": "Some fish can walk."}],
     "correct_answer": "B", "explanation": "No fish walks, and Nemo is a fish → Nemo cannot walk.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "medium",
     "text": "Choose the word that best completes the sentence logically: 'Despite the storm warning, the captain decided to ___ the voyage.'",
     "options": [{"label": "A", "value": "cancel"}, {"label": "B", "value": "delay"}, {"label": "C", "value": "continue"}, {"label": "D", "value": "plan"}],
     "correct_answer": "C", "explanation": "'Despite' signals contrast — the captain went ahead despite the warning, so 'continue' fits.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "medium",
     "text": "Which word does NOT belong? Hammer, Screwdriver, Wrench, Microscope",
     "options": [{"label": "A", "value": "Hammer"}, {"label": "B", "value": "Screwdriver"}, {"label": "C", "value": "Wrench"}, {"label": "D", "value": "Microscope"}],
     "correct_answer": "D", "explanation": "Hammer, screwdriver, and wrench are hand tools. A microscope is a scientific instrument.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "medium",
     "text": "If 'FRIEND' is coded as 'GSJFOE', how is 'HAPPY' coded?",
     "options": [{"label": "A", "value": "IBQQZ"}, {"label": "B", "value": "GZOON"}, {"label": "C", "value": "IBPQZ"}, {"label": "D", "value": "HBQQZ"}],
     "correct_answer": "A", "explanation": "Each letter shifts +1: H→I, A→B, P→Q, P→Q, Y→Z = IBQQZ.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "hard",
     "text": "Statement: 'Only experienced candidates will be interviewed. Marco is not experienced.' Conclusion:",
     "options": [{"label": "A", "value": "Marco will be interviewed."}, {"label": "B", "value": "Marco will not be interviewed."}, {"label": "C", "value": "Marco might be interviewed."}, {"label": "D", "value": "Experienced candidates will not be interviewed."}],
     "correct_answer": "B", "explanation": "Only experienced candidates qualify → Marco, being inexperienced, will not be interviewed.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "hard",
     "text": "Identify the logical fallacy: 'You can't trust his opinion on climate change — he failed high school science.'",
     "options": [{"label": "A", "value": "Slippery slope"}, {"label": "B", "value": "Ad hominem"}, {"label": "C", "value": "Straw man"}, {"label": "D", "value": "False dichotomy"}],
     "correct_answer": "B", "explanation": "Attacking the person's past failure rather than the argument itself is ad hominem.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "hard",
     "text": "Which best completes the analogy? 'Anachronism : Time :: Oxymoron : ___'",
     "options": [{"label": "A", "value": "Logic"}, {"label": "B", "value": "Contradiction"}, {"label": "C", "value": "History"}, {"label": "D", "value": "Language"}],
     "correct_answer": "B", "explanation": "An anachronism is a contradiction in time; an oxymoron is a contradiction in terms.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "hard",
     "text": "All optimists are happy. Some students are optimists. No pessimists are happy. Which must be true?",
     "options": [{"label": "A", "value": "All students are happy."}, {"label": "B", "value": "No students are pessimists."}, {"label": "C", "value": "Some students are happy."}, {"label": "D", "value": "All happy people are students."}],
     "correct_answer": "C", "explanation": "Some students = optimists, and all optimists = happy → some students are happy.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "hard",
     "text": "Identify the flaw: 'We should invest in renewable energy because everyone who cares about the future supports it.'",
     "options": [{"label": "A", "value": "False cause"}, {"label": "B", "value": "Bandwagon fallacy"}, {"label": "C", "value": "Circular reasoning"}, {"label": "D", "value": "Red herring"}],
     "correct_answer": "B", "explanation": "Appealing to what 'everyone' does instead of providing evidence is the bandwagon fallacy.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "english", "topic": "logical_verbal_reasoning", "difficulty": "hard",
     "text": "Choose the word that best fits: 'The director's decision was ___ — it satisfied no one and resolved nothing.'",
     "options": [{"label": "A", "value": "decisive"}, {"label": "B", "value": "contentious"}, {"label": "C", "value": "ineffectual"}, {"label": "D", "value": "exemplary"}],
     "correct_answer": "C", "explanation": "Satisfying no one and resolving nothing means the decision had no effect — 'ineffectual' fits.", "active": True, "createdAt": datetime.now(timezone.utc)},
]