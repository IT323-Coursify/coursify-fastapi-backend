from datetime import datetime, timezone

# Science aptitude questions
# 4 topics × 3 difficulties × 6 questions = 72 total
# Selected at runtime: 1 easy + 1 medium + 1 hard per topic = 12 per subject

APTITUDE_SCIENCE_QUESTIONS = [

    # ════════════════════════════════════════
    # TOPIC: BIOLOGY
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "easy",
     "text": "What is the basic unit of life?",
     "options": [{"label": "A", "value": "Tissue"}, {"label": "B", "value": "Organ"}, {"label": "C", "value": "Cell"}, {"label": "D", "value": "Atom"}],
     "correct_answer": "C", "explanation": "The cell is the basic structural and functional unit of all living things.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "easy",
     "text": "Which organ pumps blood throughout the body?",
     "options": [{"label": "A", "value": "Lungs"}, {"label": "B", "value": "Liver"}, {"label": "C", "value": "Kidney"}, {"label": "D", "value": "Heart"}],
     "correct_answer": "D", "explanation": "The heart is the muscular organ responsible for pumping blood.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "easy",
     "text": "What gas do plants absorb during photosynthesis?",
     "options": [{"label": "A", "value": "Oxygen"}, {"label": "B", "value": "Nitrogen"}, {"label": "C", "value": "Carbon Dioxide"}, {"label": "D", "value": "Hydrogen"}],
     "correct_answer": "C", "explanation": "Plants absorb CO₂ and use sunlight to produce glucose and oxygen.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "easy",
     "text": "What is the process by which cells divide to produce two identical daughter cells?",
     "options": [{"label": "A", "value": "Meiosis"}, {"label": "B", "value": "Mitosis"}, {"label": "C", "value": "Fertilization"}, {"label": "D", "value": "Mutation"}],
     "correct_answer": "B", "explanation": "Mitosis produces two genetically identical daughter cells for growth and repair.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "easy",
     "text": "Which part of the plant conducts photosynthesis most actively?",
     "options": [{"label": "A", "value": "Root"}, {"label": "B", "value": "Stem"}, {"label": "C", "value": "Flower"}, {"label": "D", "value": "Leaf"}],
     "correct_answer": "D", "explanation": "Leaves contain chlorophyll and are the primary site of photosynthesis.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "easy",
     "text": "What is the function of red blood cells?",
     "options": [{"label": "A", "value": "Fight infections"}, {"label": "B", "value": "Carry oxygen"}, {"label": "C", "value": "Digest food"}, {"label": "D", "value": "Produce hormones"}],
     "correct_answer": "B", "explanation": "Red blood cells contain hemoglobin which carries oxygen throughout the body.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "medium",
     "text": "What is the role of mitochondria in a cell?",
     "options": [{"label": "A", "value": "Protein synthesis"}, {"label": "B", "value": "Genetic storage"}, {"label": "C", "value": "Energy production (ATP)"}, {"label": "D", "value": "Cell division"}],
     "correct_answer": "C", "explanation": "Mitochondria are the 'powerhouses of the cell', producing ATP through cellular respiration.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "medium",
     "text": "Which type of reproduction involves only one parent?",
     "options": [{"label": "A", "value": "Sexual reproduction"}, {"label": "B", "value": "Asexual reproduction"}, {"label": "C", "value": "Cross-pollination"}, {"label": "D", "value": "Fertilization"}],
     "correct_answer": "B", "explanation": "Asexual reproduction requires only one parent and produces genetically identical offspring.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "medium",
     "text": "What happens during meiosis that does NOT happen during mitosis?",
     "options": [{"label": "A", "value": "Cell division"}, {"label": "B", "value": "DNA replication"}, {"label": "C", "value": "Genetic recombination"}, {"label": "D", "value": "Cytokinesis"}],
     "correct_answer": "C", "explanation": "Meiosis includes genetic recombination (crossing over), creating genetic diversity not seen in mitosis.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "medium",
     "text": "What is an ecosystem?",
     "options": [{"label": "A", "value": "A group of the same species"}, {"label": "B", "value": "All living things on Earth"}, {"label": "C", "value": "A community of organisms interacting with their environment"}, {"label": "D", "value": "The layer of gases around the Earth"}],
     "correct_answer": "C", "explanation": "An ecosystem includes both the living (biotic) and non-living (abiotic) components of an environment.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "medium",
     "text": "Which macromolecule stores and transmits genetic information?",
     "options": [{"label": "A", "value": "Protein"}, {"label": "B", "value": "Lipid"}, {"label": "C", "value": "Carbohydrate"}, {"label": "D", "value": "Nucleic acid (DNA/RNA)"}],
     "correct_answer": "D", "explanation": "DNA stores genetic information; RNA transmits and helps express it.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "medium",
     "text": "In a food chain: Grass → Rabbit → Fox. What is the rabbit's role?",
     "options": [{"label": "A", "value": "Producer"}, {"label": "B", "value": "Primary consumer"}, {"label": "C", "value": "Secondary consumer"}, {"label": "D", "value": "Decomposer"}],
     "correct_answer": "B", "explanation": "The rabbit eats the producer (grass), making it a primary consumer.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "hard",
     "text": "A plant is placed in a dark room for 48 hours. What would most likely happen to its starch content?",
     "options": [{"label": "A", "value": "It increases."}, {"label": "B", "value": "It stays the same."}, {"label": "C", "value": "It decreases."}, {"label": "D", "value": "It converts to protein."}],
     "correct_answer": "C", "explanation": "Without light, photosynthesis stops. The plant uses stored starch for respiration, decreasing its content.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "hard",
     "text": "If a parent has genotype Bb (B=dominant, b=recessive), what is the probability of an offspring being homozygous recessive (bb)?",
     "options": [{"label": "A", "value": "0%"}, {"label": "B", "value": "25%"}, {"label": "C", "value": "50%"}, {"label": "D", "value": "75%"}],
     "correct_answer": "B", "explanation": "Bb × Bb cross yields: BB, Bb, Bb, bb — 1 in 4 = 25% chance of bb.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "hard",
     "text": "What distinguishes viruses from living cells?",
     "options": [{"label": "A", "value": "Viruses have DNA."}, {"label": "B", "value": "Viruses lack cellular structure and cannot reproduce independently."}, {"label": "C", "value": "Viruses perform photosynthesis."}, {"label": "D", "value": "Viruses have a nucleus."}],
     "correct_answer": "B", "explanation": "Viruses are non-cellular and must hijack a host cell's machinery to replicate.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "hard",
     "text": "Which process removes nitrogenous waste from the blood?",
     "options": [{"label": "A", "value": "Respiration"}, {"label": "B", "value": "Digestion"}, {"label": "C", "value": "Excretion via the kidneys"}, {"label": "D", "value": "Circulation"}],
     "correct_answer": "C", "explanation": "The kidneys filter blood and excrete nitrogenous waste (urea) as urine.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "hard",
     "text": "Natural selection acts on phenotype, not genotype. What does this imply?",
     "options": [{"label": "A", "value": "Genes are irrelevant to evolution."}, {"label": "B", "value": "Only observable traits affect survival and reproduction."}, {"label": "C", "value": "All mutations are beneficial."}, {"label": "D", "value": "Genotype and phenotype are the same thing."}],
     "correct_answer": "B", "explanation": "Natural selection favors traits that are expressed and observed — the phenotype — affecting reproductive success.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "biology", "difficulty": "hard",
     "text": "The enzyme amylase breaks down starch. At very high temperatures, its activity drops to zero. Why?",
     "options": [{"label": "A", "value": "The starch is destroyed."}, {"label": "B", "value": "The enzyme becomes denatured."}, {"label": "C", "value": "The pH becomes too acidic."}, {"label": "D", "value": "The reaction needs cold temperatures."}],
     "correct_answer": "B", "explanation": "High temperatures disrupt the enzyme's 3D shape (denaturation), destroying its active site.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: PHYSICS
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "easy",
     "text": "What is the unit of force?",
     "options": [{"label": "A", "value": "Joule"}, {"label": "B", "value": "Watt"}, {"label": "C", "value": "Newton"}, {"label": "D", "value": "Pascal"}],
     "correct_answer": "C", "explanation": "Force is measured in Newtons (N).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "easy",
     "text": "What type of energy does a moving object have?",
     "options": [{"label": "A", "value": "Potential energy"}, {"label": "B", "value": "Chemical energy"}, {"label": "C", "value": "Kinetic energy"}, {"label": "D", "value": "Nuclear energy"}],
     "correct_answer": "C", "explanation": "Kinetic energy is the energy of motion.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "easy",
     "text": "What happens to the speed of light when it passes from air into water?",
     "options": [{"label": "A", "value": "It increases."}, {"label": "B", "value": "It stays the same."}, {"label": "C", "value": "It decreases."}, {"label": "D", "value": "It disappears."}],
     "correct_answer": "C", "explanation": "Light slows down when entering a denser medium (water), causing refraction.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "easy",
     "text": "Which of the following is NOT a form of energy?",
     "options": [{"label": "A", "value": "Sound"}, {"label": "B", "value": "Light"}, {"label": "C", "value": "Mass"}, {"label": "D", "value": "Heat"}],
     "correct_answer": "C", "explanation": "Mass is not a form of energy by itself (though it can be converted via E=mc²). Sound, light, and heat are all energy forms.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "easy",
     "text": "What is the formula for speed?",
     "options": [{"label": "A", "value": "Speed = Force × Time"}, {"label": "B", "value": "Speed = Distance / Time"}, {"label": "C", "value": "Speed = Mass × Acceleration"}, {"label": "D", "value": "Speed = Work / Power"}],
     "correct_answer": "B", "explanation": "Speed = Distance ÷ Time.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "easy",
     "text": "Which law states that for every action there is an equal and opposite reaction?",
     "options": [{"label": "A", "value": "Newton's First Law"}, {"label": "B", "value": "Newton's Second Law"}, {"label": "C", "value": "Newton's Third Law"}, {"label": "D", "value": "Law of Conservation of Energy"}],
     "correct_answer": "C", "explanation": "Newton's Third Law: every action has an equal and opposite reaction.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "medium",
     "text": "A 5 kg object accelerates at 3 m/s². What is the net force acting on it?",
     "options": [{"label": "A", "value": "8 N"}, {"label": "B", "value": "15 N"}, {"label": "C", "value": "2 N"}, {"label": "D", "value": "1.67 N"}],
     "correct_answer": "B", "explanation": "F = ma = 5 × 3 = 15 N.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "medium",
     "text": "A ball is dropped from a height. Just before hitting the ground, what type of energy is greatest?",
     "options": [{"label": "A", "value": "Potential energy"}, {"label": "B", "value": "Kinetic energy"}, {"label": "C", "value": "Chemical energy"}, {"label": "D", "value": "Thermal energy"}],
     "correct_answer": "B", "explanation": "As the ball falls, potential energy converts to kinetic energy — maximized just before impact.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "medium",
     "text": "What is the resistance of a circuit where voltage = 12V and current = 3A?",
     "options": [{"label": "A", "value": "36 Ω"}, {"label": "B", "value": "4 Ω"}, {"label": "C", "value": "9 Ω"}, {"label": "D", "value": "15 Ω"}],
     "correct_answer": "B", "explanation": "Ohm's Law: R = V/I = 12/3 = 4 Ω.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "medium",
     "text": "What property of a wave determines its pitch?",
     "options": [{"label": "A", "value": "Amplitude"}, {"label": "B", "value": "Wavelength"}, {"label": "C", "value": "Frequency"}, {"label": "D", "value": "Speed"}],
     "correct_answer": "C", "explanation": "Pitch is determined by frequency — higher frequency = higher pitch.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "medium",
     "text": "An object is in equilibrium. What does this tell you about the forces acting on it?",
     "options": [{"label": "A", "value": "No forces are acting."}, {"label": "B", "value": "One large force acts on it."}, {"label": "C", "value": "The net force is zero."}, {"label": "D", "value": "The object is moving fast."}],
     "correct_answer": "C", "explanation": "Equilibrium means balanced forces — net force = 0.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "medium",
     "text": "Which type of wave requires a medium to travel through?",
     "options": [{"label": "A", "value": "Electromagnetic wave"}, {"label": "B", "value": "Mechanical wave"}, {"label": "C", "value": "Gamma ray"}, {"label": "D", "value": "X-ray"}],
     "correct_answer": "B", "explanation": "Mechanical waves (like sound) require a medium; electromagnetic waves do not.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "hard",
     "text": "A 10 kg block is lifted 5 meters. What is its gravitational potential energy? (g = 10 m/s²)",
     "options": [{"label": "A", "value": "50 J"}, {"label": "B", "value": "500 J"}, {"label": "C", "value": "100 J"}, {"label": "D", "value": "250 J"}],
     "correct_answer": "B", "explanation": "PE = mgh = 10 × 10 × 5 = 500 J.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "hard",
     "text": "Two resistors (4Ω and 6Ω) are connected in parallel. What is the equivalent resistance?",
     "options": [{"label": "A", "value": "10 Ω"}, {"label": "B", "value": "2.4 Ω"}, {"label": "C", "value": "5 Ω"}, {"label": "D", "value": "24 Ω"}],
     "correct_answer": "B", "explanation": "1/R = 1/4 + 1/6 = 3/12 + 2/12 = 5/12 → R = 12/5 = 2.4 Ω.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "hard",
     "text": "A car travels 100 km at 50 km/h then 100 km at 100 km/h. What is its average speed?",
     "options": [{"label": "A", "value": "75 km/h"}, {"label": "B", "value": "66.7 km/h"}, {"label": "C", "value": "80 km/h"}, {"label": "D", "value": "60 km/h"}],
     "correct_answer": "B", "explanation": "Total distance = 200 km. Total time = 2h + 1h = 3h. Avg speed = 200/3 ≈ 66.7 km/h.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "hard",
     "text": "According to the law of conservation of momentum, what happens to total momentum in a closed system?",
     "options": [{"label": "A", "value": "It increases over time."}, {"label": "B", "value": "It decreases due to friction."}, {"label": "C", "value": "It remains constant."}, {"label": "D", "value": "It converts to energy."}],
     "correct_answer": "C", "explanation": "In a closed system with no external forces, total momentum is conserved.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "hard",
     "text": "Why does a ship made of steel float even though steel is denser than water?",
     "options": [{"label": "A", "value": "Steel repels water."}, {"label": "B", "value": "The ship's hollow shape displaces more water than its weight."}, {"label": "C", "value": "Salt water is denser than steel."}, {"label": "D", "value": "The ship's engine generates lift."}],
     "correct_answer": "B", "explanation": "Archimedes' principle: the ship floats because its hollow shape displaces enough water to equal its weight.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "physics", "difficulty": "hard",
     "text": "What happens to the half-life of a radioactive element as it decays?",
     "options": [{"label": "A", "value": "It shortens."}, {"label": "B", "value": "It lengthens."}, {"label": "C", "value": "It remains constant."}, {"label": "D", "value": "It doubles each decay."}],
     "correct_answer": "C", "explanation": "Half-life is a constant property of a radioactive isotope — it does not change over time.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: CHEMISTRY
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "easy",
     "text": "What is the chemical symbol for water?",
     "options": [{"label": "A", "value": "WA"}, {"label": "B", "value": "H₂O"}, {"label": "C", "value": "HO₂"}, {"label": "D", "value": "O₂H"}],
     "correct_answer": "B", "explanation": "Water is composed of 2 hydrogen atoms and 1 oxygen atom: H₂O.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "easy",
     "text": "What is the pH of a neutral solution?",
     "options": [{"label": "A", "value": "0"}, {"label": "B", "value": "7"}, {"label": "C", "value": "14"}, {"label": "D", "value": "1"}],
     "correct_answer": "B", "explanation": "A pH of 7 is neutral. Below 7 = acidic, above 7 = basic.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "easy",
     "text": "What is the smallest particle of an element that retains its chemical properties?",
     "options": [{"label": "A", "value": "Molecule"}, {"label": "B", "value": "Electron"}, {"label": "C", "value": "Atom"}, {"label": "D", "value": "Proton"}],
     "correct_answer": "C", "explanation": "An atom is the smallest unit of an element that retains its chemical identity.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "easy",
     "text": "Which state of matter has no fixed shape or volume?",
     "options": [{"label": "A", "value": "Solid"}, {"label": "B", "value": "Liquid"}, {"label": "C", "value": "Gas"}, {"label": "D", "value": "Plasma"}],
     "correct_answer": "C", "explanation": "Gases have neither a fixed shape nor a fixed volume — they expand to fill their container.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "easy",
     "text": "What type of bond involves the sharing of electrons?",
     "options": [{"label": "A", "value": "Ionic bond"}, {"label": "B", "value": "Covalent bond"}, {"label": "C", "value": "Metallic bond"}, {"label": "D", "value": "Hydrogen bond"}],
     "correct_answer": "B", "explanation": "Covalent bonds form when atoms share electrons.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "easy",
     "text": "What is produced when an acid reacts with a base?",
     "options": [{"label": "A", "value": "An acid"}, {"label": "B", "value": "A gas"}, {"label": "C", "value": "Salt and water"}, {"label": "D", "value": "A metal"}],
     "correct_answer": "C", "explanation": "Acid + Base → Salt + Water. This is called a neutralization reaction.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "medium",
     "text": "What does the atomic number of an element represent?",
     "options": [{"label": "A", "value": "Number of neutrons"}, {"label": "B", "value": "Number of protons"}, {"label": "C", "value": "Atomic mass"}, {"label": "D", "value": "Number of electron shells"}],
     "correct_answer": "B", "explanation": "The atomic number equals the number of protons in the nucleus.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "medium",
     "text": "In the reaction: 2H₂ + O₂ → 2H₂O, what type of reaction is this?",
     "options": [{"label": "A", "value": "Decomposition"}, {"label": "B", "value": "Synthesis (combination)"}, {"label": "C", "value": "Single displacement"}, {"label": "D", "value": "Double displacement"}],
     "correct_answer": "B", "explanation": "Two or more substances combine to form a single product — this is a synthesis reaction.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "medium",
     "text": "What indicates that a chemical change has occurred?",
     "options": [{"label": "A", "value": "Change in shape"}, {"label": "B", "value": "Change in size"}, {"label": "C", "value": "Change in state"}, {"label": "D", "value": "Formation of a new substance with different properties"}],
     "correct_answer": "D", "explanation": "Chemical changes produce new substances with different properties (e.g., color change, gas production, precipitate).", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "medium",
     "text": "Which element is the most abundant in Earth's atmosphere?",
     "options": [{"label": "A", "value": "Oxygen"}, {"label": "B", "value": "Carbon dioxide"}, {"label": "C", "value": "Hydrogen"}, {"label": "D", "value": "Nitrogen"}],
     "correct_answer": "D", "explanation": "Nitrogen makes up about 78% of Earth's atmosphere.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "medium",
     "text": "What is an isotope?",
     "options": [{"label": "A", "value": "Atoms of different elements with the same mass"}, {"label": "B", "value": "Atoms of the same element with different numbers of neutrons"}, {"label": "C", "value": "Ions with the same charge"}, {"label": "D", "value": "Molecules with the same formula but different structures"}],
     "correct_answer": "B", "explanation": "Isotopes are atoms of the same element that differ in neutron count.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "medium",
     "text": "Which of these is an example of a physical change?",
     "options": [{"label": "A", "value": "Burning wood"}, {"label": "B", "value": "Rusting iron"}, {"label": "C", "value": "Dissolving sugar in water"}, {"label": "D", "value": "Baking a cake"}],
     "correct_answer": "C", "explanation": "Dissolving is a physical change — no new substance is formed; the sugar can be recovered.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "hard",
     "text": "Balance the equation: _Fe + _O₂ → _Fe₂O₃",
     "options": [{"label": "A", "value": "2Fe + O₂ → Fe₂O₃"}, {"label": "B", "value": "4Fe + 3O₂ → 2Fe₂O₃"}, {"label": "C", "value": "Fe + O₂ → Fe₂O₃"}, {"label": "D", "value": "3Fe + 2O₂ → Fe₂O₃"}],
     "correct_answer": "B", "explanation": "4Fe + 3O₂ → 2Fe₂O₃ balances with 4 Fe and 6 O on each side.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "hard",
     "text": "What is the molarity of a solution containing 2 moles of NaCl in 500 mL of water?",
     "options": [{"label": "A", "value": "1 M"}, {"label": "B", "value": "2 M"}, {"label": "C", "value": "4 M"}, {"label": "D", "value": "0.5 M"}],
     "correct_answer": "C", "explanation": "M = moles/liters = 2/0.5 = 4 M.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "hard",
     "text": "In an electrochemical cell, what happens at the anode?",
     "options": [{"label": "A", "value": "Reduction occurs."}, {"label": "B", "value": "Electrons are gained."}, {"label": "C", "value": "Oxidation occurs."}, {"label": "D", "value": "Cations are produced."}],
     "correct_answer": "C", "explanation": "At the anode, oxidation (loss of electrons) occurs. At the cathode, reduction occurs.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "hard",
     "text": "What does Le Chatelier's Principle state?",
     "options": [{"label": "A", "value": "Energy is conserved in all reactions."}, {"label": "B", "value": "A system at equilibrium shifts to counteract any imposed change."}, {"label": "C", "value": "Reactions always move forward."}, {"label": "D", "value": "Temperature does not affect equilibrium."}],
     "correct_answer": "B", "explanation": "Le Chatelier's Principle: a system at equilibrium will shift to oppose any stress applied to it.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "hard",
     "text": "Which quantum number describes the shape of an electron orbital?",
     "options": [{"label": "A", "value": "Principal quantum number (n)"}, {"label": "B", "value": "Azimuthal quantum number (l)"}, {"label": "C", "value": "Magnetic quantum number (m)"}, {"label": "D", "value": "Spin quantum number (s)"}],
     "correct_answer": "B", "explanation": "The azimuthal (angular momentum) quantum number (l) defines the shape (s, p, d, f) of the orbital.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "chemistry", "difficulty": "hard",
     "text": "What is the hybridization of carbon in methane (CH₄)?",
     "options": [{"label": "A", "value": "sp"}, {"label": "B", "value": "sp²"}, {"label": "C", "value": "sp³"}, {"label": "D", "value": "sp³d"}],
     "correct_answer": "C", "explanation": "Carbon in CH₄ forms 4 bonds using sp³ hybridization — tetrahedral geometry.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: EARTH & ENVIRONMENTAL SCIENCE
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "easy",
     "text": "What is the outermost layer of the Earth called?",
     "options": [{"label": "A", "value": "Mantle"}, {"label": "B", "value": "Core"}, {"label": "C", "value": "Crust"}, {"label": "D", "value": "Asthenosphere"}],
     "correct_answer": "C", "explanation": "The crust is the thin outermost layer of the Earth.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "easy",
     "text": "What causes the seasons on Earth?",
     "options": [{"label": "A", "value": "Distance from the Sun"}, {"label": "B", "value": "Earth's tilt on its axis"}, {"label": "C", "value": "The Moon's position"}, {"label": "D", "value": "Solar flares"}],
     "correct_answer": "B", "explanation": "Earth's axial tilt (23.5°) causes different parts of Earth to receive varying amounts of sunlight throughout the year.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "easy",
     "text": "Which gas is primarily responsible for the greenhouse effect?",
     "options": [{"label": "A", "value": "Oxygen"}, {"label": "B", "value": "Nitrogen"}, {"label": "C", "value": "Carbon dioxide"}, {"label": "D", "value": "Hydrogen"}],
     "correct_answer": "C", "explanation": "CO₂ traps heat in the atmosphere, contributing to the greenhouse effect.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "easy",
     "text": "What type of rock is formed from cooled magma?",
     "options": [{"label": "A", "value": "Sedimentary"}, {"label": "B", "value": "Metamorphic"}, {"label": "C", "value": "Igneous"}, {"label": "D", "value": "Limestone"}],
     "correct_answer": "C", "explanation": "Igneous rocks form when magma or lava cools and solidifies.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "easy",
     "text": "What is the water cycle process where water vapor turns into liquid?",
     "options": [{"label": "A", "value": "Evaporation"}, {"label": "B", "value": "Condensation"}, {"label": "C", "value": "Precipitation"}, {"label": "D", "value": "Transpiration"}],
     "correct_answer": "B", "explanation": "Condensation is when water vapor cools and transforms into liquid water, forming clouds.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "easy",
     "text": "What is biodiversity?",
     "options": [{"label": "A", "value": "The number of plants in a forest"}, {"label": "B", "value": "The variety of living organisms in an environment"}, {"label": "C", "value": "The study of fossils"}, {"label": "D", "value": "The chemical composition of soil"}],
     "correct_answer": "B", "explanation": "Biodiversity refers to the variety of life forms within a given area.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "medium",
     "text": "What drives the movement of tectonic plates?",
     "options": [{"label": "A", "value": "Ocean tides"}, {"label": "B", "value": "Convection currents in the mantle"}, {"label": "C", "value": "Earth's rotation"}, {"label": "D", "value": "Gravitational pull of the Moon"}],
     "correct_answer": "B", "explanation": "Heat-driven convection currents in the mantle are the primary mechanism for tectonic plate movement.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "medium",
     "text": "What is the difference between weather and climate?",
     "options": [{"label": "A", "value": "Weather is long-term; climate is short-term."}, {"label": "B", "value": "Weather is short-term atmospheric conditions; climate is long-term patterns."}, {"label": "C", "value": "They are the same thing."}, {"label": "D", "value": "Weather involves temperature only."}],
     "correct_answer": "B", "explanation": "Weather = day-to-day atmospheric conditions. Climate = long-term average patterns in a region.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "medium",
     "text": "What is the role of decomposers in an ecosystem?",
     "options": [{"label": "A", "value": "They produce energy from sunlight."}, {"label": "B", "value": "They hunt and eat other animals."}, {"label": "C", "value": "They break down dead organic matter and return nutrients to the soil."}, {"label": "D", "value": "They store carbon dioxide."}],
     "correct_answer": "C", "explanation": "Decomposers (bacteria, fungi) recycle nutrients by breaking down dead organisms.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "medium",
     "text": "How are metamorphic rocks formed?",
     "options": [{"label": "A", "value": "By cooling of magma"}, {"label": "B", "value": "By layers of sediment compressing over time"}, {"label": "C", "value": "By existing rocks being transformed by heat and pressure"}, {"label": "D", "value": "By chemical reactions in the ocean"}],
     "correct_answer": "C", "explanation": "Metamorphic rocks form when pre-existing rocks are subjected to intense heat and/or pressure.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "medium",
     "text": "What is the primary cause of ocean tides?",
     "options": [{"label": "A", "value": "Wind patterns"}, {"label": "B", "value": "Earth's rotation"}, {"label": "C", "value": "Gravitational pull of the Moon"}, {"label": "D", "value": "Underwater volcanoes"}],
     "correct_answer": "C", "explanation": "The Moon's gravitational pull is the primary driver of ocean tides.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "medium",
     "text": "Which human activity contributes most to global warming?",
     "options": [{"label": "A", "value": "Farming"}, {"label": "B", "value": "Burning fossil fuels"}, {"label": "C", "value": "Using electricity"}, {"label": "D", "value": "Deforestation alone"}],
     "correct_answer": "B", "explanation": "Burning fossil fuels releases the largest amounts of CO₂, the main greenhouse gas driver of global warming.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "hard",
     "text": "What is the Coriolis effect?",
     "options": [{"label": "A", "value": "The cooling of air as it rises"}, {"label": "B", "value": "The deflection of moving objects due to Earth's rotation"}, {"label": "C", "value": "The reflection of sunlight by ice"}, {"label": "D", "value": "The warming of ocean water near the equator"}],
     "correct_answer": "B", "explanation": "The Coriolis effect deflects wind and ocean currents to the right in the Northern Hemisphere and left in the Southern.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "hard",
     "text": "What is the albedo effect, and why does melting Arctic ice accelerate global warming?",
     "options": [{"label": "A", "value": "Ice absorbs sunlight; water reflects it."}, {"label": "B", "value": "Ice reflects sunlight; dark water absorbs more heat."}, {"label": "C", "value": "Ice releases CO₂; water does not."}, {"label": "D", "value": "Melting ice has no effect on temperature."}],
     "correct_answer": "B", "explanation": "Ice has high albedo (reflects sunlight). When it melts, darker ocean absorbs more heat, accelerating warming — a positive feedback loop.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "hard",
     "text": "At a convergent plate boundary where oceanic meets continental crust, what typically occurs?",
     "options": [{"label": "A", "value": "Rifting and seafloor spreading"}, {"label": "B", "value": "Transform faulting"}, {"label": "C", "value": "Subduction of the oceanic plate beneath the continental plate"}, {"label": "D", "value": "Both plates rise to form mountains equally"}],
     "correct_answer": "C", "explanation": "Oceanic crust is denser and subducts beneath the lighter continental crust, forming trenches and volcanic arcs.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "hard",
     "text": "What is the significance of the ozone layer?",
     "options": [{"label": "A", "value": "It retains heat near Earth's surface."}, {"label": "B", "value": "It absorbs harmful ultraviolet radiation from the Sun."}, {"label": "C", "value": "It reflects solar energy back to space."}, {"label": "D", "value": "It generates oxygen for breathing."}],
     "correct_answer": "B", "explanation": "The ozone layer (stratosphere) absorbs ~97-99% of the Sun's medium-frequency UV radiation, protecting life on Earth.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "hard",
     "text": "A scientist finds fossils of marine animals at the top of a mountain. What does this suggest?",
     "options": [{"label": "A", "value": "Animals once lived on mountains."}, {"label": "B", "value": "The mountain was once underwater and was uplifted over time."}, {"label": "C", "value": "Floods once covered the mountain temporarily."}, {"label": "D", "value": "Marine animals can survive on land."}],
     "correct_answer": "B", "explanation": "Marine fossils at high altitude indicate tectonic uplift — the seafloor was raised over geological time.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "science", "topic": "earth_and_environmental_science", "difficulty": "hard",
     "text": "What is eutrophication and what causes it?",
     "options": [{"label": "A", "value": "Soil erosion caused by wind"}, {"label": "B", "value": "Excessive nutrient runoff causing algae blooms that deplete oxygen in water"}, {"label": "C", "value": "The process of rock formation under pressure"}, {"label": "D", "value": "Saltwater intrusion into freshwater sources"}],
     "correct_answer": "B", "explanation": "Eutrophication occurs when excess nutrients (often from fertilizers) cause algae overgrowth, blocking light and depleting oxygen.", "active": True, "createdAt": datetime.now(timezone.utc)},
]