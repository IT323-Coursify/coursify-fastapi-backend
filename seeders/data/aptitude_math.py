from datetime import datetime, timezone

# Math aptitude questions
# 4 topics × 3 difficulties × 6 questions = 72 total
# Selected at runtime: 1 easy + 1 medium + 1 hard per topic = 12 per subject
# question_format: multiple_choice
# correct_answer: the label (A/B/C/D)

APTITUDE_MATH_QUESTIONS = [

    # ════════════════════════════════════════
    # TOPIC: ALGEBRA
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "easy",
     "text": "Solve for x: 2x + 5 = 15",
     "options": [{"label": "A", "value": "x = 3"}, {"label": "B", "value": "x = 5"}, {"label": "C", "value": "x = 7"}, {"label": "D", "value": "x = 10"}],
     "correct_answer": "B", "explanation": "2x = 10, so x = 5.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "easy",
     "text": "What is the value of y if y - 4 = 9?",
     "options": [{"label": "A", "value": "5"}, {"label": "B", "value": "13"}, {"label": "C", "value": "14"}, {"label": "D", "value": "4"}],
     "correct_answer": "B", "explanation": "y = 9 + 4 = 13.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "easy",
     "text": "If 3a = 18, what is a?",
     "options": [{"label": "A", "value": "3"}, {"label": "B", "value": "5"}, {"label": "C", "value": "6"}, {"label": "D", "value": "9"}],
     "correct_answer": "C", "explanation": "a = 18 ÷ 3 = 6.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "easy",
     "text": "What is 5x when x = 4?",
     "options": [{"label": "A", "value": "9"}, {"label": "B", "value": "16"}, {"label": "C", "value": "20"}, {"label": "D", "value": "25"}],
     "correct_answer": "C", "explanation": "5 × 4 = 20.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "easy",
     "text": "Solve: x/3 = 7",
     "options": [{"label": "A", "value": "21"}, {"label": "B", "value": "10"}, {"label": "C", "value": "3"}, {"label": "D", "value": "14"}],
     "correct_answer": "A", "explanation": "x = 7 × 3 = 21.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "easy",
     "text": "Which expression represents 'four more than a number n'?",
     "options": [{"label": "A", "value": "4n"}, {"label": "B", "value": "n - 4"}, {"label": "C", "value": "n + 4"}, {"label": "D", "value": "4/n"}],
     "correct_answer": "C", "explanation": "'More than' means addition: n + 4.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "medium",
     "text": "Solve for x: 3x - 7 = 2x + 5",
     "options": [{"label": "A", "value": "x = 10"}, {"label": "B", "value": "x = 12"}, {"label": "C", "value": "x = 7"}, {"label": "D", "value": "x = 2"}],
     "correct_answer": "B", "explanation": "3x - 2x = 5 + 7 → x = 12.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "medium",
     "text": "If 2(x + 3) = 14, what is x?",
     "options": [{"label": "A", "value": "4"}, {"label": "B", "value": "5"}, {"label": "C", "value": "7"}, {"label": "D", "value": "11"}],
     "correct_answer": "A", "explanation": "2x + 6 = 14 → 2x = 8 → x = 4.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "medium",
     "text": "What is the slope of the line y = 3x - 5?",
     "options": [{"label": "A", "value": "-5"}, {"label": "B", "value": "3"}, {"label": "C", "value": "5"}, {"label": "D", "value": "-3"}],
     "correct_answer": "B", "explanation": "In y = mx + b, m is the slope. m = 3.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "medium",
     "text": "Simplify: 4(2x - 3) - 2x",
     "options": [{"label": "A", "value": "6x - 12"}, {"label": "B", "value": "8x - 12"}, {"label": "C", "value": "6x - 3"}, {"label": "D", "value": "10x - 12"}],
     "correct_answer": "A", "explanation": "8x - 12 - 2x = 6x - 12.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "medium",
     "text": "If f(x) = 2x² - 1, what is f(3)?",
     "options": [{"label": "A", "value": "17"}, {"label": "B", "value": "16"}, {"label": "C", "value": "11"}, {"label": "D", "value": "35"}],
     "correct_answer": "A", "explanation": "f(3) = 2(9) - 1 = 18 - 1 = 17.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "medium",
     "text": "Which of the following is a solution to x² - 5x + 6 = 0?",
     "options": [{"label": "A", "value": "x = 1"}, {"label": "B", "value": "x = 2"}, {"label": "C", "value": "x = 4"}, {"label": "D", "value": "x = 6"}],
     "correct_answer": "B", "explanation": "(x-2)(x-3) = 0, so x = 2 or x = 3.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "hard",
     "text": "If log₂(x) = 5, what is x?",
     "options": [{"label": "A", "value": "10"}, {"label": "B", "value": "25"}, {"label": "C", "value": "32"}, {"label": "D", "value": "64"}],
     "correct_answer": "C", "explanation": "log₂(x) = 5 means 2⁵ = x = 32.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "hard",
     "text": "Solve: |2x - 4| = 10",
     "options": [{"label": "A", "value": "x = 7 or x = -3"}, {"label": "B", "value": "x = 3 or x = -7"}, {"label": "C", "value": "x = 5 or x = -5"}, {"label": "D", "value": "x = 7 only"}],
     "correct_answer": "A", "explanation": "2x - 4 = 10 → x = 7; 2x - 4 = -10 → x = -3.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "hard",
     "text": "If the roots of x² + bx + c = 0 are 3 and -5, what are b and c?",
     "options": [{"label": "A", "value": "b=2, c=-15"}, {"label": "B", "value": "b=-2, c=-15"}, {"label": "C", "value": "b=2, c=15"}, {"label": "D", "value": "b=-2, c=15"}],
     "correct_answer": "A", "explanation": "Sum of roots = -b → -b = 3 + (-5) = -2 → b = 2. Product = c → c = 3×(-5) = -15.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "hard",
     "text": "What is the inverse function of f(x) = 3x + 6?",
     "options": [{"label": "A", "value": "f⁻¹(x) = (x - 6)/3"}, {"label": "B", "value": "f⁻¹(x) = 3x - 6"}, {"label": "C", "value": "f⁻¹(x) = x/3 + 6"}, {"label": "D", "value": "f⁻¹(x) = (x + 6)/3"}],
     "correct_answer": "A", "explanation": "Swap x and y: x = 3y + 6 → y = (x-6)/3.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "hard",
     "text": "Solve the system: 2x + y = 7 and x - y = 2",
     "options": [{"label": "A", "value": "x=3, y=1"}, {"label": "B", "value": "x=2, y=3"}, {"label": "C", "value": "x=4, y=-1"}, {"label": "D", "value": "x=1, y=5"}],
     "correct_answer": "A", "explanation": "Adding equations: 3x = 9 → x = 3; y = 7 - 2(3) = 1.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "algebra", "difficulty": "hard",
     "text": "Expand and simplify: (x + 3)² - (x - 2)²",
     "options": [{"label": "A", "value": "10x + 5"}, {"label": "B", "value": "2x + 5"}, {"label": "C", "value": "10x - 5"}, {"label": "D", "value": "2x - 5"}],
     "correct_answer": "A", "explanation": "(x²+6x+9) - (x²-4x+4) = 10x + 5.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: GEOMETRY
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "easy",
     "text": "What is the perimeter of a square with side length 5 cm?",
     "options": [{"label": "A", "value": "10 cm"}, {"label": "B", "value": "20 cm"}, {"label": "C", "value": "25 cm"}, {"label": "D", "value": "15 cm"}],
     "correct_answer": "B", "explanation": "Perimeter = 4 × 5 = 20 cm.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "easy",
     "text": "How many degrees are in a straight angle?",
     "options": [{"label": "A", "value": "90°"}, {"label": "B", "value": "45°"}, {"label": "C", "value": "360°"}, {"label": "D", "value": "180°"}],
     "correct_answer": "D", "explanation": "A straight angle is 180°.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "easy",
     "text": "What is the area of a rectangle with length 8 and width 3?",
     "options": [{"label": "A", "value": "22"}, {"label": "B", "value": "24"}, {"label": "C", "value": "11"}, {"label": "D", "value": "18"}],
     "correct_answer": "B", "explanation": "Area = 8 × 3 = 24.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "easy",
     "text": "What type of triangle has all three sides equal?",
     "options": [{"label": "A", "value": "Scalene"}, {"label": "B", "value": "Isosceles"}, {"label": "C", "value": "Equilateral"}, {"label": "D", "value": "Right"}],
     "correct_answer": "C", "explanation": "An equilateral triangle has all sides equal.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "easy",
     "text": "What is the sum of angles in a triangle?",
     "options": [{"label": "A", "value": "90°"}, {"label": "B", "value": "180°"}, {"label": "C", "value": "270°"}, {"label": "D", "value": "360°"}],
     "correct_answer": "B", "explanation": "The angles of a triangle always sum to 180°.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "easy",
     "text": "How many faces does a cube have?",
     "options": [{"label": "A", "value": "4"}, {"label": "B", "value": "6"}, {"label": "C", "value": "8"}, {"label": "D", "value": "12"}],
     "correct_answer": "B", "explanation": "A cube has 6 faces.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "medium",
     "text": "What is the area of a circle with radius 7? (Use π ≈ 3.14)",
     "options": [{"label": "A", "value": "43.96"}, {"label": "B", "value": "153.86"}, {"label": "C", "value": "49"}, {"label": "D", "value": "21.98"}],
     "correct_answer": "B", "explanation": "A = πr² = 3.14 × 49 = 153.86.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "medium",
     "text": "Find the hypotenuse of a right triangle with legs 6 and 8.",
     "options": [{"label": "A", "value": "10"}, {"label": "B", "value": "12"}, {"label": "C", "value": "14"}, {"label": "D", "value": "100"}],
     "correct_answer": "A", "explanation": "c = √(6² + 8²) = √(36+64) = √100 = 10.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "medium",
     "text": "What is the volume of a rectangular prism with l=4, w=3, h=5?",
     "options": [{"label": "A", "value": "47"}, {"label": "B", "value": "60"}, {"label": "C", "value": "35"}, {"label": "D", "value": "12"}],
     "correct_answer": "B", "explanation": "V = l × w × h = 4 × 3 × 5 = 60.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "medium",
     "text": "Two parallel lines are cut by a transversal. If one angle is 65°, what is its co-interior angle?",
     "options": [{"label": "A", "value": "65°"}, {"label": "B", "value": "115°"}, {"label": "C", "value": "25°"}, {"label": "D", "value": "130°"}],
     "correct_answer": "B", "explanation": "Co-interior angles are supplementary: 180° - 65° = 115°.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "medium",
     "text": "What is the area of a triangle with base 10 and height 6?",
     "options": [{"label": "A", "value": "60"}, {"label": "B", "value": "16"}, {"label": "C", "value": "30"}, {"label": "D", "value": "15"}],
     "correct_answer": "C", "explanation": "A = ½ × base × height = ½ × 10 × 6 = 30.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "medium",
     "text": "The exterior angle of a regular polygon is 45°. How many sides does it have?",
     "options": [{"label": "A", "value": "6"}, {"label": "B", "value": "8"}, {"label": "C", "value": "10"}, {"label": "D", "value": "12"}],
     "correct_answer": "B", "explanation": "Number of sides = 360 ÷ exterior angle = 360 ÷ 45 = 8.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "hard",
     "text": "A cone has radius 3 and height 4. What is its volume? (Use π ≈ 3.14)",
     "options": [{"label": "A", "value": "37.68"}, {"label": "B", "value": "75.36"}, {"label": "C", "value": "113.04"}, {"label": "D", "value": "25.12"}],
     "correct_answer": "A", "explanation": "V = (1/3)πr²h = (1/3)(3.14)(9)(4) = 37.68.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "hard",
     "text": "In a circle, a chord is 8 cm and is 3 cm from the center. What is the radius?",
     "options": [{"label": "A", "value": "4"}, {"label": "B", "value": "5"}, {"label": "C", "value": "6"}, {"label": "D", "value": "7"}],
     "correct_answer": "B", "explanation": "r = √(4² + 3²) = √(16 + 9) = √25 = 5.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "hard",
     "text": "What is the surface area of a sphere with radius 5? (Use π ≈ 3.14)",
     "options": [{"label": "A", "value": "78.5"}, {"label": "B", "value": "314"}, {"label": "C", "value": "523.3"}, {"label": "D", "value": "157"}],
     "correct_answer": "B", "explanation": "SA = 4πr² = 4 × 3.14 × 25 = 314.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "hard",
     "text": "The coordinates of A are (1,2) and B are (4,6). What is the length of AB?",
     "options": [{"label": "A", "value": "5"}, {"label": "B", "value": "7"}, {"label": "C", "value": "√7"}, {"label": "D", "value": "√34"}],
     "correct_answer": "A", "explanation": "d = √((4-1)² + (6-2)²) = √(9+16) = √25 = 5.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "hard",
     "text": "A regular hexagon has side length 6. What is its area?",
     "options": [{"label": "A", "value": "36√3"}, {"label": "B", "value": "54√3"}, {"label": "C", "value": "72"}, {"label": "D", "value": "108"}],
     "correct_answer": "B", "explanation": "Area = (3√3/2)s² = (3√3/2)(36) = 54√3.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "geometry", "difficulty": "hard",
     "text": "What is the diagonal of a square with side 7?",
     "options": [{"label": "A", "value": "7√2"}, {"label": "B", "value": "14"}, {"label": "C", "value": "49"}, {"label": "D", "value": "7√3"}],
     "correct_answer": "A", "explanation": "d = s√2 = 7√2.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: STATISTICS
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "easy",
     "text": "What is the mean of: 4, 8, 6, 10, 2?",
     "options": [{"label": "A", "value": "5"}, {"label": "B", "value": "6"}, {"label": "C", "value": "7"}, {"label": "D", "value": "8"}],
     "correct_answer": "B", "explanation": "Mean = (4+8+6+10+2)/5 = 30/5 = 6.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "easy",
     "text": "What is the median of: 3, 7, 1, 9, 5?",
     "options": [{"label": "A", "value": "3"}, {"label": "B", "value": "7"}, {"label": "C", "value": "5"}, {"label": "D", "value": "1"}],
     "correct_answer": "C", "explanation": "Ordered: 1,3,5,7,9 → median = 5.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "easy",
     "text": "What is the mode of: 2, 4, 4, 5, 7, 4, 9?",
     "options": [{"label": "A", "value": "2"}, {"label": "B", "value": "5"}, {"label": "C", "value": "7"}, {"label": "D", "value": "4"}],
     "correct_answer": "D", "explanation": "4 appears 3 times — most frequent.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "easy",
     "text": "What is the range of: 10, 3, 7, 15, 6?",
     "options": [{"label": "A", "value": "9"}, {"label": "B", "value": "12"}, {"label": "C", "value": "15"}, {"label": "D", "value": "5"}],
     "correct_answer": "B", "explanation": "Range = max - min = 15 - 3 = 12.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "easy",
     "text": "A bag has 3 red, 2 blue, and 5 green balls. What is the probability of picking a red ball?",
     "options": [{"label": "A", "value": "1/3"}, {"label": "B", "value": "3/10"}, {"label": "C", "value": "3/5"}, {"label": "D", "value": "1/5"}],
     "correct_answer": "B", "explanation": "P(red) = 3/10.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "easy",
     "text": "Which measure of central tendency is most affected by extreme values?",
     "options": [{"label": "A", "value": "Median"}, {"label": "B", "value": "Mode"}, {"label": "C", "value": "Mean"}, {"label": "D", "value": "Range"}],
     "correct_answer": "C", "explanation": "The mean is affected by outliers/extreme values.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "medium",
     "text": "The average of 5 numbers is 12. If four of them are 10, 14, 8, and 16, what is the fifth?",
     "options": [{"label": "A", "value": "10"}, {"label": "B", "value": "12"}, {"label": "C", "value": "11"}, {"label": "D", "value": "14"}],
     "correct_answer": "B", "explanation": "Total = 60. Sum of four = 48. Fifth = 60 - 48 = 12.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "medium",
     "text": "In a class of 30, 18 passed. What is the probability that a randomly selected student failed?",
     "options": [{"label": "A", "value": "2/5"}, {"label": "B", "value": "3/5"}, {"label": "C", "value": "1/5"}, {"label": "D", "value": "18/30"}],
     "correct_answer": "A", "explanation": "Failed = 12. P(failed) = 12/30 = 2/5.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "medium",
     "text": "What is the standard deviation concept measuring?",
     "options": [{"label": "A", "value": "The middle value"}, {"label": "B", "value": "The most frequent value"}, {"label": "C", "value": "Spread of data around the mean"}, {"label": "D", "value": "The sum of all values"}],
     "correct_answer": "C", "explanation": "Standard deviation measures how spread out values are from the mean.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "medium",
     "text": "A die is rolled. What is the probability of rolling a number greater than 4?",
     "options": [{"label": "A", "value": "1/6"}, {"label": "B", "value": "1/3"}, {"label": "C", "value": "1/2"}, {"label": "D", "value": "2/3"}],
     "correct_answer": "B", "explanation": "Numbers > 4: {5, 6} = 2 outcomes. P = 2/6 = 1/3.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "medium",
     "text": "The median of an even-numbered data set is found by:",
     "options": [{"label": "A", "value": "Taking the middle value"}, {"label": "B", "value": "Averaging the two middle values"}, {"label": "C", "value": "Taking the highest value"}, {"label": "D", "value": "Summing all values and dividing"}],
     "correct_answer": "B", "explanation": "For even data sets, median = average of the two middle values.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "medium",
     "text": "Two events A and B are mutually exclusive. If P(A) = 0.3, P(B) = 0.4, what is P(A or B)?",
     "options": [{"label": "A", "value": "0.12"}, {"label": "B", "value": "0.1"}, {"label": "C", "value": "0.7"}, {"label": "D", "value": "1.0"}],
     "correct_answer": "C", "explanation": "Mutually exclusive: P(A or B) = P(A) + P(B) = 0.7.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "hard",
     "text": "The scores are: 5, 7, 7, 8, 10, 12. What is the variance?",
     "options": [{"label": "A", "value": "4.5"}, {"label": "B", "value": "5.25"}, {"label": "C", "value": "3.67"}, {"label": "D", "value": "4.92"}],
     "correct_answer": "B", "explanation": "Mean=8.17 (approx). Variance = Σ(x-mean)²/n ≈ 5.25. (Population variance)", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "hard",
     "text": "In a normal distribution, what percentage of data falls within 1 standard deviation of the mean?",
     "options": [{"label": "A", "value": "50%"}, {"label": "B", "value": "68%"}, {"label": "C", "value": "95%"}, {"label": "D", "value": "99.7%"}],
     "correct_answer": "B", "explanation": "Empirical rule: ~68% within ±1σ, 95% within ±2σ, 99.7% within ±3σ.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "hard",
     "text": "How many ways can 4 students be arranged in a row from a group of 6?",
     "options": [{"label": "A", "value": "24"}, {"label": "B", "value": "120"}, {"label": "C", "value": "360"}, {"label": "D", "value": "720"}],
     "correct_answer": "C", "explanation": "P(6,4) = 6!/(6-4)! = 6×5×4×3 = 360.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "hard",
     "text": "If P(A) = 0.5, P(B) = 0.4, and P(A∩B) = 0.2, what is P(A|B)?",
     "options": [{"label": "A", "value": "0.2"}, {"label": "B", "value": "0.4"}, {"label": "C", "value": "0.5"}, {"label": "D", "value": "0.7"}],
     "correct_answer": "C", "explanation": "P(A|B) = P(A∩B)/P(B) = 0.2/0.4 = 0.5.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "hard",
     "text": "A data set has mean 50 and standard deviation 10. What is the z-score for a value of 70?",
     "options": [{"label": "A", "value": "1.0"}, {"label": "B", "value": "1.5"}, {"label": "C", "value": "2.0"}, {"label": "D", "value": "2.5"}],
     "correct_answer": "C", "explanation": "z = (x - μ)/σ = (70-50)/10 = 2.0.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "statistics", "difficulty": "hard",
     "text": "How many ways can a committee of 3 be chosen from 8 people?",
     "options": [{"label": "A", "value": "24"}, {"label": "B", "value": "56"}, {"label": "C", "value": "336"}, {"label": "D", "value": "512"}],
     "correct_answer": "B", "explanation": "C(8,3) = 8!/(3!×5!) = 56.", "active": True, "createdAt": datetime.now(timezone.utc)},


    # ════════════════════════════════════════
    # TOPIC: LOGIC
    # ════════════════════════════════════════

    # --- EASY ---
    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "easy",
     "text": "If all cats are animals, and Whiskers is a cat, what can we conclude?",
     "options": [{"label": "A", "value": "Whiskers is not an animal"}, {"label": "B", "value": "Whiskers is an animal"}, {"label": "C", "value": "All animals are cats"}, {"label": "D", "value": "Cannot be determined"}],
     "correct_answer": "B", "explanation": "Deductive reasoning: Whiskers is a cat → Whiskers is an animal.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "easy",
     "text": "What comes next in the sequence: 2, 4, 6, 8, ___?",
     "options": [{"label": "A", "value": "9"}, {"label": "B", "value": "10"}, {"label": "C", "value": "12"}, {"label": "D", "value": "16"}],
     "correct_answer": "B", "explanation": "Even numbers: each increases by 2. Next = 10.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "easy",
     "text": "If it is NOT true that 'it is raining', what does that mean?",
     "options": [{"label": "A", "value": "It is raining"}, {"label": "B", "value": "It is not raining"}, {"label": "C", "value": "It might be raining"}, {"label": "D", "value": "We cannot determine the weather"}],
     "correct_answer": "B", "explanation": "Negation of 'it is raining' = 'it is not raining'.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "easy",
     "text": "Which of the following is a valid logical conclusion? 'If A then B. A is true. Therefore...'",
     "options": [{"label": "A", "value": "B is false"}, {"label": "B", "value": "B is true"}, {"label": "C", "value": "A is false"}, {"label": "D", "value": "Nothing can be concluded"}],
     "correct_answer": "B", "explanation": "Modus ponens: If A→B and A is true, then B must be true.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "easy",
     "text": "What comes next: 1, 3, 9, 27, ___?",
     "options": [{"label": "A", "value": "54"}, {"label": "B", "value": "81"}, {"label": "C", "value": "72"}, {"label": "D", "value": "36"}],
     "correct_answer": "B", "explanation": "Each term is multiplied by 3. 27 × 3 = 81.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "easy",
     "text": "Ana is taller than Ben. Ben is taller than Carlo. Who is the shortest?",
     "options": [{"label": "A", "value": "Ana"}, {"label": "B", "value": "Ben"}, {"label": "C", "value": "Carlo"}, {"label": "D", "value": "Cannot determine"}],
     "correct_answer": "C", "explanation": "Ana > Ben > Carlo, so Carlo is the shortest.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- MEDIUM ---
    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "medium",
     "text": "What is the contrapositive of 'If it rains, then the ground is wet'?",
     "options": [{"label": "A", "value": "If the ground is wet, then it rains"}, {"label": "B", "value": "If the ground is not wet, then it does not rain"}, {"label": "C", "value": "If it does not rain, then the ground is not wet"}, {"label": "D", "value": "The ground is wet only when it rains"}],
     "correct_answer": "B", "explanation": "Contrapositive of P→Q is ¬Q→¬P.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "medium",
     "text": "Find the missing number: 5, 11, 23, 47, ___",
     "options": [{"label": "A", "value": "94"}, {"label": "B", "value": "95"}, {"label": "C", "value": "96"}, {"label": "D", "value": "97"}],
     "correct_answer": "B", "explanation": "Pattern: ×2 + 1. 47×2+1 = 95.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "medium",
     "text": "All managers are employees. Some employees are part-time. Which must be true?",
     "options": [{"label": "A", "value": "All managers are part-time"}, {"label": "B", "value": "Some managers may be part-time"}, {"label": "C", "value": "No managers are part-time"}, {"label": "D", "value": "All part-time workers are managers"}],
     "correct_answer": "B", "explanation": "We can only conclude that some managers might be part-time — not definitely.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "medium",
     "text": "If P is true and Q is false, what is the truth value of P AND Q?",
     "options": [{"label": "A", "value": "True"}, {"label": "B", "value": "False"}, {"label": "C", "value": "Depends on context"}, {"label": "D", "value": "Undefined"}],
     "correct_answer": "B", "explanation": "AND requires both to be true. Since Q is false, P AND Q = false.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "medium",
     "text": "A is the brother of B. B is the daughter of C. C is the son of D. What is D to A?",
     "options": [{"label": "A", "value": "Grandfather"}, {"label": "B", "value": "Father"}, {"label": "C", "value": "Grandmother"}, {"label": "D", "value": "Uncle"}],
     "correct_answer": "A", "explanation": "A and B are siblings → C is their parent → D is C's parent = A's grandfather.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "medium",
     "text": "Which of the following is logically equivalent to 'NOT (P OR Q)'?",
     "options": [{"label": "A", "value": "NOT P OR NOT Q"}, {"label": "B", "value": "NOT P AND NOT Q"}, {"label": "C", "value": "P AND Q"}, {"label": "D", "value": "P OR NOT Q"}],
     "correct_answer": "B", "explanation": "De Morgan's law: NOT(P OR Q) = NOT P AND NOT Q.", "active": True, "createdAt": datetime.now(timezone.utc)},

    # --- HARD ---
    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "hard",
     "text": "All A are B. No B are C. Therefore:",
     "options": [{"label": "A", "value": "All A are C"}, {"label": "B", "value": "Some A are C"}, {"label": "C", "value": "No A are C"}, {"label": "D", "value": "Some C are A"}],
     "correct_answer": "C", "explanation": "All A ⊆ B and B ∩ C = ∅, therefore A ∩ C = ∅ → No A are C.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "hard",
     "text": "Three friends Alex, Ben, Carlo each own a different pet: cat, dog, fish. Alex doesn't own the dog. Ben doesn't own the cat. Carlo doesn't own the fish. Who owns the dog?",
     "options": [{"label": "A", "value": "Alex"}, {"label": "B", "value": "Ben"}, {"label": "C", "value": "Carlo"}, {"label": "D", "value": "Cannot determine"}],
     "correct_answer": "B", "explanation": "Carlo→not fish, so Carlo has cat or dog. Ben→not cat. Alex→not dog. By elimination, Ben owns the dog.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "hard",
     "text": "What is the next term: 1, 1, 2, 3, 5, 8, 13, ___?",
     "options": [{"label": "A", "value": "18"}, {"label": "B", "value": "20"}, {"label": "C", "value": "21"}, {"label": "D", "value": "26"}],
     "correct_answer": "C", "explanation": "Fibonacci: each term = sum of previous two. 8 + 13 = 21.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "hard",
     "text": "In a truth table for P XOR Q, when is the result TRUE?",
     "options": [{"label": "A", "value": "When both are true"}, {"label": "B", "value": "When both are false"}, {"label": "C", "value": "When exactly one is true"}, {"label": "D", "value": "Always"}],
     "correct_answer": "C", "explanation": "XOR (exclusive or) is true only when exactly one of the two inputs is true.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "hard",
     "text": "If 'Some S are P' and 'All P are Q', which conclusion is valid?",
     "options": [{"label": "A", "value": "All S are Q"}, {"label": "B", "value": "No S are Q"}, {"label": "C", "value": "Some S are Q"}, {"label": "D", "value": "All Q are S"}],
     "correct_answer": "C", "explanation": "Some S ⊆ P, and all P ⊆ Q → Those same S are also in Q → Some S are Q.", "active": True, "createdAt": datetime.now(timezone.utc)},

    {"type": "aptitude", "subject": "math", "topic": "logic", "difficulty": "hard",
     "text": "Find the pattern: 2, 6, 12, 20, 30, ___",
     "options": [{"label": "A", "value": "40"}, {"label": "B", "value": "42"}, {"label": "C", "value": "44"}, {"label": "D", "value": "36"}],
     "correct_answer": "B", "explanation": "Differences: 4, 6, 8, 10, 12. Next = 30 + 12 = 42.", "active": True, "createdAt": datetime.now(timezone.utc)},
]