"""50 exercises on Python conditionals."""
from .base import make_exercise

exercises = [
    # BEGINNER (1-10): Basic if, if/else, comparison operators
    make_exercise(
        "cond_01",
        "Simple if statement",
        "conditionals",
        1,
        "Write a function that returns True if a number is positive, False otherwise.",
        hints=[
            "Use the > operator to compare with 0",
            "Return the result of the comparison directly"
        ],
        solution="def is_positive(n):\n    return n > 0",
        function_name="is_positive",
        test_cases=[
            ((5,), True),
            ((-3,), False),
            ((0,), False),
            ((100,), True),
        ]
    ),
    make_exercise(
        "cond_02",
        "if/else with equality",
        "conditionals",
        1,
        "Write a function that returns 'even' if a number is even, 'odd' if odd.",
        hints=[
            "Use the modulo operator % to check remainder when divided by 2",
            "n % 2 == 0 means the number is even"
        ],
        solution="def even_or_odd(n):\n    if n % 2 == 0:\n        return 'even'\n    else:\n        return 'odd'",
        function_name="even_or_odd",
        test_cases=[
            ((4,), 'even'),
            ((7,), 'odd'),
            ((0,), 'even'),
            ((13,), 'odd'),
        ]
    ),
    make_exercise(
        "cond_03",
        "Comparison: less than and greater than",
        "conditionals",
        1,
        "Write a function that returns 'hot' if temperature >= 30, 'cold' if < 10, 'mild' otherwise.",
        hints=[
            "Use >= for greater-than-or-equal",
            "Use < for less-than",
            "Consider order of conditions carefully"
        ],
        solution="def temperature_description(temp):\n    if temp >= 30:\n        return 'hot'\n    elif temp < 10:\n        return 'cold'\n    else:\n        return 'mild'",
        function_name="temperature_description",
        test_cases=[
            ((35,), 'hot'),
            ((5,), 'cold'),
            ((20,), 'mild'),
            ((30,), 'hot'),
            ((9,), 'cold'),
        ]
    ),
    make_exercise(
        "cond_04",
        "Inequality operator !=",
        "conditionals",
        1,
        "Write a function that returns True if a string is not 'admin', False otherwise.",
        hints=[
            "Use the != operator for 'not equal'",
            "String comparison with == and != is case-sensitive"
        ],
        solution="def is_not_admin(username):\n    return username != 'admin'",
        function_name="is_not_admin",
        test_cases=[
            (('user',), True),
            (('admin',), False),
            (('Admin',), True),
            (('guest',), True),
        ]
    ),
    make_exercise(
        "cond_05",
        "if/elif/else chain with multiple conditions",
        "conditionals",
        1,
        "Write a function that returns a size category: 'small' (< 5), 'medium' (5-10), 'large' (> 10).",
        hints=[
            "Use < for less than and > for greater than",
            "elif handles the middle condition",
            "Order matters: check small first, then medium, then large"
        ],
        solution="def size_category(value):\n    if value < 5:\n        return 'small'\n    elif value <= 10:\n        return 'medium'\n    else:\n        return 'large'",
        function_name="size_category",
        test_cases=[
            ((2,), 'small'),
            ((5,), 'medium'),
            ((10,), 'medium'),
            ((15,), 'large'),
        ]
    ),
    make_exercise(
        "cond_06",
        "Boolean return from comparison",
        "conditionals",
        1,
        "Write a function that returns True if a number is between 1 and 100 inclusive, False otherwise.",
        hints=[
            "You need to check two conditions: >= 1 AND <= 100",
            "You can use 'and' or write two separate comparisons",
            "Return the boolean result directly"
        ],
        solution="def is_in_range(n):\n    return 1 <= n <= 100",
        function_name="is_in_range",
        test_cases=[
            ((50,), True),
            ((1,), True),
            ((100,), True),
            ((0,), False),
            ((101,), False),
        ]
    ),
    make_exercise(
        "cond_07",
        "Basic logical AND",
        "conditionals",
        1,
        "Write a function that returns True if a number is even AND positive, False otherwise.",
        hints=[
            "Use 'and' to combine two conditions",
            "Check n > 0 and n % 2 == 0",
            "Both conditions must be True for the result to be True"
        ],
        solution="def even_and_positive(n):\n    return n > 0 and n % 2 == 0",
        function_name="even_and_positive",
        test_cases=[
            ((4,), True),
            ((2,), True),
            ((-2,), False),
            ((3,), False),
            ((0,), False),
        ]
    ),
    make_exercise(
        "cond_08",
        "Basic logical OR",
        "conditionals",
        1,
        "Write a function that returns True if a number is less than 0 OR greater than 100, False otherwise.",
        hints=[
            "Use 'or' to combine two conditions",
            "Check n < 0 or n > 100",
            "At least one condition needs to be True"
        ],
        solution="def outside_range(n):\n    return n < 0 or n > 100",
        function_name="outside_range",
        test_cases=[
            ((-5,), True),
            ((150,), True),
            ((50,), False),
            ((0,), False),
            ((100,), False),
        ]
    ),
    make_exercise(
        "cond_09",
        "NOT operator",
        "conditionals",
        1,
        "Write a function that returns True if a string is empty (length 0), False otherwise.",
        hints=[
            "Use 'not' to negate a boolean",
            "len(s) == 0 checks if string is empty",
            "You could also use: not s"
        ],
        solution="def is_empty(s):\n    return len(s) == 0",
        function_name="is_empty",
        test_cases=[
            (('',), True),
            (('hello',), False),
            ((' ',), False),
        ]
    ),
    make_exercise(
        "cond_10",
        "Truthiness of values",
        "conditionals",
        1,
        "Write a function that returns True if a value is truthy (0, empty string, None, False are falsy), False if falsy.",
        hints=[
            "Empty collections, 0, None, and False are falsy",
            "Non-zero numbers and non-empty strings are truthy",
            "Use 'if value:' to check truthiness"
        ],
        solution="def is_truthy(value):\n    return bool(value)",
        function_name="is_truthy",
        test_cases=[
            ((1,), True),
            ((0,), False),
            (('hello',), True),
            (('',), False),
            ((None,), False),
        ]
    ),

    # EASY (11-20): Nested conditionals, ternary, chained comparisons
    make_exercise(
        "cond_11",
        "Nested if statements",
        "conditionals",
        2,
        "Write a function that returns 'adult' if age >= 18 and has_id is True, 'minor' otherwise.",
        hints=[
            "Use a nested if: first check age, then check has_id inside",
            "Both conditions must be True to return 'adult'",
            "Remember boolean parameters are either True or False"
        ],
        solution="def check_adult(age, has_id):\n    if age >= 18:\n        if has_id:\n            return 'adult'\n    return 'minor'",
        function_name="check_adult",
        test_cases=[
            ((25, True), 'adult'),
            ((25, False), 'minor'),
            ((16, True), 'minor'),
            ((18, True), 'adult'),
        ]
    ),
    make_exercise(
        "cond_12",
        "Ternary expression (inline if/else)",
        "conditionals",
        2,
        "Write a function that returns 'pass' if score >= 50 else 'fail' using a ternary expression.",
        hints=[
            "Use: x if condition else y syntax",
            "This is a one-liner alternative to if/else",
            "Read it as: 'x (if condition is true) else y'"
        ],
        solution="def pass_or_fail(score):\n    return 'pass' if score >= 50 else 'fail'",
        function_name="pass_or_fail",
        test_cases=[
            ((50,), 'pass'),
            ((75,), 'pass'),
            ((30,), 'fail'),
            ((49,), 'fail'),
        ]
    ),
    make_exercise(
        "cond_13",
        "Chained comparisons",
        "conditionals",
        2,
        "Write a function that returns True if a number is strictly between 10 and 20 (exclusive), False otherwise.",
        hints=[
            "Use chained comparison: 10 < n < 20",
            "This is more readable than (n > 10 and n < 20)",
            "Works for any number of comparisons"
        ],
        solution="def is_between_10_and_20(n):\n    return 10 < n < 20",
        function_name="is_between_10_and_20",
        test_cases=[
            ((15,), True),
            ((10,), False),
            ((20,), False),
            ((5,), False),
            ((25,), False),
        ]
    ),
    make_exercise(
        "cond_14",
        "Multiple elif branches",
        "conditionals",
        2,
        "Write a function that returns a day name given a number 1-7 ('Monday', 'Tuesday', etc.).",
        hints=[
            "Use if/elif/elif... chain for 7 different cases",
            "1='Monday', 2='Tuesday', ..., 7='Sunday'",
            "Return 'Invalid' if the number is outside 1-7"
        ],
        solution="def day_name(day_num):\n    if day_num == 1:\n        return 'Monday'\n    elif day_num == 2:\n        return 'Tuesday'\n    elif day_num == 3:\n        return 'Wednesday'\n    elif day_num == 4:\n        return 'Thursday'\n    elif day_num == 5:\n        return 'Friday'\n    elif day_num == 6:\n        return 'Saturday'\n    elif day_num == 7:\n        return 'Sunday'\n    else:\n        return 'Invalid'",
        function_name="day_name",
        test_cases=[
            ((1,), 'Monday'),
            ((7,), 'Sunday'),
            ((4,), 'Thursday'),
            ((8,), 'Invalid'),
        ]
    ),
    make_exercise(
        "cond_15",
        "Complex boolean logic with AND/OR/NOT",
        "conditionals",
        2,
        "Write a function that returns True if (age >= 18 AND has_license) OR age >= 16 AND in_driving_school is True.",
        hints=[
            "Use 'and' and 'or' operators",
            "Parentheses help clarify order: (A and B) or (C and D)",
            "Remember: 'and' has higher precedence than 'or'"
        ],
        solution="def can_drive(age, has_license, in_driving_school):\n    return (age >= 18 and has_license) or (age >= 16 and in_driving_school)",
        function_name="can_drive",
        test_cases=[
            ((20, True, False), True),
            ((17, False, True), True),
            ((18, False, False), False),
            ((16, False, False), False),
        ]
    ),
    make_exercise(
        "cond_16",
        "Guard clause (early return)",
        "conditionals",
        2,
        "Write a function that returns 'invalid' if password is empty or less than 6 chars, otherwise 'valid'.",
        hints=[
            "Use an early return for the invalid case",
            "Check len(password) < 6 or password == ''",
            "Return immediately if condition is True"
        ],
        solution="def validate_password(password):\n    if len(password) < 6:\n        return 'invalid'\n    return 'valid'",
        function_name="validate_password",
        test_cases=[
            (('',), 'invalid'),
            (('abc',), 'invalid'),
            (('123456',), 'valid'),
            (('password',), 'valid'),
        ]
    ),
    make_exercise(
        "cond_17",
        "Membership test with 'in'",
        "conditionals",
        2,
        "Write a function that returns True if a character is a vowel (a, e, i, o, u), False otherwise.",
        hints=[
            "Use the 'in' operator: char in 'aeiou'",
            "The 'in' operator checks if a value exists in a collection",
            "Consider case sensitivity; you might want to use .lower()"
        ],
        solution="def is_vowel(char):\n    return char.lower() in 'aeiou'",
        function_name="is_vowel",
        test_cases=[
            (('a',), True),
            (('E',), True),
            (('b',), False),
            (('i',), True),
        ]
    ),
    make_exercise(
        "cond_18",
        "Type checking with type()",
        "conditionals",
        2,
        "Write a function that returns 'int' if the value is an integer, 'float' if it's a float, 'other' otherwise.",
        hints=[
            "Use type(value) to get the type",
            "type(5) == int, type(5.0) == float",
            "Be aware: in Python 3, bool is a subclass of int"
        ],
        solution="def value_type(value):\n    if isinstance(value, bool):\n        return 'other'\n    elif isinstance(value, int):\n        return 'int'\n    elif isinstance(value, float):\n        return 'float'\n    else:\n        return 'other'",
        function_name="value_type",
        test_cases=[
            ((5,), 'int'),
            ((5.0,), 'float'),
            (('hello',), 'other'),
        ]
    ),
    make_exercise(
        "cond_19",
        "Multiple conditions in if",
        "conditionals",
        2,
        "Write a function that returns 'valid' if a person's age is 18-65 inclusive, 'invalid' otherwise.",
        hints=[
            "Check age >= 18 AND age <= 65",
            "You can use: 18 <= age <= 65",
            "Chained comparisons are elegant"
        ],
        solution="def is_working_age(age):\n    return 18 <= age <= 65",
        function_name="is_working_age",
        test_cases=[
            ((25,), True),
            ((18,), True),
            ((65,), True),
            ((17,), False),
            ((66,), False),
        ]
    ),
    make_exercise(
        "cond_20",
        "Short-circuit evaluation",
        "conditionals",
        2,
        "Write a function that checks if a list is non-empty AND its first element is positive, without IndexError.",
        hints=[
            "Use 'and' short-circuit: if lst is empty, the second part won't be checked",
            "len(lst) > 0 and lst[0] > 0 is safe because of short-circuit",
            "This avoids IndexError when list is empty"
        ],
        solution="def first_is_positive(lst):\n    return len(lst) > 0 and lst[0] > 0",
        function_name="first_is_positive",
        test_cases=[
            ((([5, 3],), True),),
            ((([],), False),),
            ((([0, 1],), False),),
            ((([1, -5],), True),),
        ]
    ),

    # MEDIUM (21-35): Real-world applications, match/case, complex logic
    make_exercise(
        "cond_21",
        "Grade calculator",
        "conditionals",
        3,
        "Write a function that returns a letter grade (A, B, C, D, F) given a numeric score (0-100).",
        hints=[
            "A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: < 60",
            "Use if/elif/else chain",
            "Consider boundary cases like 90, 80, 70"
        ],
        solution="def letter_grade(score):\n    if score >= 90:\n        return 'A'\n    elif score >= 80:\n        return 'B'\n    elif score >= 70:\n        return 'C'\n    elif score >= 60:\n        return 'D'\n    else:\n        return 'F'",
        function_name="letter_grade",
        test_cases=[
            ((95,), 'A'),
            ((85,), 'B'),
            ((75,), 'C'),
            ((65,), 'D'),
            ((55,), 'F'),
            ((90,), 'A'),
        ]
    ),
    make_exercise(
        "cond_22",
        "FizzBuzz (classic)",
        "conditionals",
        3,
        "Write a function that returns 'Fizz' if divisible by 3, 'Buzz' if divisible by 5, 'FizzBuzz' if both, otherwise the number as a string.",
        hints=[
            "Check divisibility using % operator",
            "Check 'both' first (n % 15 == 0)",
            "Order of conditions matters"
        ],
        solution="def fizzbuzz(n):\n    if n % 15 == 0:\n        return 'FizzBuzz'\n    elif n % 3 == 0:\n        return 'Fizz'\n    elif n % 5 == 0:\n        return 'Buzz'\n    else:\n        return str(n)",
        function_name="fizzbuzz",
        test_cases=[
            ((3,), 'Fizz'),
            ((5,), 'Buzz'),
            ((15,), 'FizzBuzz'),
            ((7,), '7'),
        ]
    ),
    make_exercise(
        "cond_23",
        "Leap year checker",
        "conditionals",
        3,
        "Write a function that returns True if a year is a leap year, False otherwise.",
        hints=[
            "Rule: divisible by 400 -> leap, else divisible by 100 -> not leap, else divisible by 4 -> leap, else not leap",
            "2000 is a leap year (divisible by 400)",
            "1900 is not a leap year (divisible by 100 but not 400)"
        ],
        solution="def is_leap_year(year):\n    if year % 400 == 0:\n        return True\n    elif year % 100 == 0:\n        return False\n    elif year % 4 == 0:\n        return True\n    else:\n        return False",
        function_name="is_leap_year",
        test_cases=[
            ((2000,), True),
            ((1900,), False),
            ((2004,), True),
            ((2001,), False),
        ]
    ),
    make_exercise(
        "cond_24",
        "BMI category",
        "conditionals",
        3,
        "Write a function that calculates BMI (weight/height^2) and returns 'underweight', 'normal', 'overweight', or 'obese'.",
        hints=[
            "BMI < 18.5: underweight, 18.5-24.9: normal, 25-29.9: overweight, >= 30: obese",
            "weight is in kg, height is in meters",
            "Use nested comparisons or if/elif chain"
        ],
        solution="def bmi_category(weight, height):\n    bmi = weight / (height ** 2)\n    if bmi < 18.5:\n        return 'underweight'\n    elif bmi < 25:\n        return 'normal'\n    elif bmi < 30:\n        return 'overweight'\n    else:\n        return 'obese'",
        function_name="bmi_category",
        test_cases=[
            ((50, 1.8), 'underweight'),
            ((70, 1.8), 'normal'),
            ((80, 1.8), 'normal'),
            ((100, 1.8), 'obese'),
        ]
    ),
    make_exercise(
        "cond_25",
        "Traffic light color action",
        "conditionals",
        3,
        "Write a function that takes a color and returns the action: 'go' (green), 'slow' (yellow), 'stop' (red), 'invalid' otherwise.",
        hints=[
            "Use if/elif/else",
            "Handle lowercase/uppercase with .lower()",
            "Only three valid colors"
        ],
        solution="def traffic_light(color):\n    color = color.lower()\n    if color == 'green':\n        return 'go'\n    elif color == 'yellow':\n        return 'slow'\n    elif color == 'red':\n        return 'stop'\n    else:\n        return 'invalid'",
        function_name="traffic_light",
        test_cases=[
            (('green',), 'go'),
            (('Yellow',), 'slow'),
            (('RED',), 'stop'),
            (('blue',), 'invalid'),
        ]
    ),
    make_exercise(
        "cond_26",
        "Password strength checker",
        "conditionals",
        3,
        "Write a function that returns 'weak', 'medium', or 'strong' based on password criteria.",
        hints=[
            "weak: length < 8",
            "medium: length >= 8 and (has uppercase or has digit)",
            "strong: length >= 12 and has uppercase and has digit",
            "Use any(c.isupper() for c in password) to check for uppercase"
        ],
        solution="def password_strength(password):\n    has_upper = any(c.isupper() for c in password)\n    has_digit = any(c.isdigit() for c in password)\n    length = len(password)\n    \n    if length < 8:\n        return 'weak'\n    elif length >= 12 and has_upper and has_digit:\n        return 'strong'\n    elif has_upper or has_digit:\n        return 'medium'\n    else:\n        return 'weak'",
        function_name="password_strength",
        test_cases=[
            (('abc',), 'weak'),
            (('abcdef12',), 'medium'),
            (('Abcdef12xyz',), 'medium'),
            (('Password1234',), 'strong'),
        ]
    ),
    make_exercise(
        "cond_27",
        "Discount calculator",
        "conditionals",
        3,
        "Write a function that applies a discount based on purchase amount: 5% off >= $100, 10% off >= $500, 15% off >= $1000.",
        hints=[
            "Use if/elif/else for different tiers",
            "Return the final price after discount",
            "Calculate: price * (1 - discount_rate)"
        ],
        solution="def apply_discount(price):\n    if price >= 1000:\n        return price * 0.85\n    elif price >= 500:\n        return price * 0.90\n    elif price >= 100:\n        return price * 0.95\n    else:\n        return price",
        function_name="apply_discount",
        test_cases=[
            ((50,), 50),
            ((100,), 95),
            ((500,), 450),
            ((1000,), 850),
        ]
    ),
    make_exercise(
        "cond_28",
        "Age category classification",
        "conditionals",
        3,
        "Write a function that returns an age category: 'child' (< 13), 'teen' (13-19), 'adult' (20-64), 'senior' (65+).",
        hints=[
            "Use if/elif/elif/else chain",
            "Remember: 13 <= teen < 20",
            "Boundary cases: 12, 13, 19, 20, 64, 65"
        ],
        solution="def age_category(age):\n    if age < 13:\n        return 'child'\n    elif age < 20:\n        return 'teen'\n    elif age < 65:\n        return 'adult'\n    else:\n        return 'senior'",
        function_name="age_category",
        test_cases=[
            ((5,), 'child'),
            ((13,), 'teen'),
            ((19,), 'teen'),
            ((20,), 'adult'),
            ((65,), 'senior'),
        ]
    ),
    make_exercise(
        "cond_29",
        "Shipping cost calculator",
        "conditionals",
        3,
        "Write a function that calculates shipping cost: base $5, +$2 per pound if weight > 5, +$3 if destination is 'international'.",
        hints=[
            "Start with base cost of $5",
            "Add $2 per pound for each pound over 5",
            "Add $3 if destination == 'international'",
            "Calculate: 5 + extra_weight_cost + international_cost"
        ],
        solution="def shipping_cost(weight, destination):\n    cost = 5\n    if weight > 5:\n        cost += (weight - 5) * 2\n    if destination == 'international':\n        cost += 3\n    return cost",
        function_name="shipping_cost",
        test_cases=[
            ((3, 'domestic'), 5),
            ((6, 'domestic'), 7),
            ((5, 'international'), 8),
            ((10, 'international'), 18),
        ]
    ),
    make_exercise(
        "cond_30",
        "Movie rating classifier",
        "conditionals",
        3,
        "Write a function that returns a movie rating category: 'G' (0-5), 'PG' (5-7), 'PG-13' (7-10), 'R' (10+).",
        hints=[
            "rating is a float from 0-10",
            "G: 0 <= rating <= 5, PG: 5 < rating <= 7, PG-13: 7 < rating <= 10, R: > 10",
            "Boundary: 5.0 is PG, 7.0 is PG-13"
        ],
        solution="def movie_rating(rating):\n    if rating <= 5:\n        return 'G'\n    elif rating <= 7:\n        return 'PG'\n    elif rating <= 10:\n        return 'PG-13'\n    else:\n        return 'R'",
        function_name="movie_rating",
        test_cases=[
            ((3.5,), 'G'),
            ((6.0,), 'PG'),
            ((8.5,), 'PG-13'),
            ((10,), 'PG-13'),
        ]
    ),
    make_exercise(
        "cond_31",
        "Vowel/consonant/other classifier",
        "conditionals",
        3,
        "Write a function that returns 'vowel' if the character is a vowel, 'consonant' if a letter, 'other' if not a letter.",
        hints=[
            "Vowels: a, e, i, o, u (case-insensitive)",
            "Use .isalpha() to check if it's a letter",
            "Use .lower() to handle uppercase"
        ],
        solution="def classify_char(char):\n    char = char.lower()\n    if char in 'aeiou':\n        return 'vowel'\n    elif char.isalpha():\n        return 'consonant'\n    else:\n        return 'other'",
        function_name="classify_char",
        test_cases=[
            (('a',), 'vowel'),
            (('b',), 'consonant'),
            (('3',), 'other'),
            (('E',), 'vowel'),
        ]
    ),
    make_exercise(
        "cond_32",
        "Triangle type classifier",
        "conditionals",
        3,
        "Write a function that returns 'equilateral' (all equal), 'isosceles' (2 equal), 'scalene' (none equal), or 'invalid' if not a valid triangle.",
        hints=[
            "Valid triangle: sum of any two sides > third side",
            "Check all three conditions for valid triangle",
            "Compare sides: a == b, b == c, a == c"
        ],
        solution="def triangle_type(a, b, c):\n    if a + b <= c or b + c <= a or a + c <= b:\n        return 'invalid'\n    if a == b == c:\n        return 'equilateral'\n    elif a == b or b == c or a == c:\n        return 'isosceles'\n    else:\n        return 'scalene'",
        function_name="triangle_type",
        test_cases=[
            ((3, 3, 3), 'equilateral'),
            ((3, 3, 4), 'isosceles'),
            ((3, 4, 5), 'scalene'),
            ((1, 2, 10), 'invalid'),
        ]
    ),
    make_exercise(
        "cond_33",
        "Number sign and magnitude",
        "conditionals",
        3,
        "Write a function that returns 'zero', 'small_pos', 'large_pos', 'small_neg', 'large_neg' based on the number.",
        hints=[
            "zero: == 0",
            "small_pos: 0 < n <= 10, large_pos: > 10",
            "small_neg: -10 <= n < 0, large_neg: < -10"
        ],
        solution="def classify_number(n):\n    if n == 0:\n        return 'zero'\n    elif n > 0 and n <= 10:\n        return 'small_pos'\n    elif n > 10:\n        return 'large_pos'\n    elif n >= -10:\n        return 'small_neg'\n    else:\n        return 'large_neg'",
        function_name="classify_number",
        test_cases=[
            ((0,), 'zero'),
            ((5,), 'small_pos'),
            ((20,), 'large_pos'),
            ((-5,), 'small_neg'),
            ((-20,), 'large_neg'),
        ]
    ),
    make_exercise(
        "cond_34",
        "Season from month number",
        "conditionals",
        3,
        "Write a function that returns the season ('winter', 'spring', 'summer', 'fall') given a month number 1-12.",
        hints=[
            "Winter: 12, 1, 2",
            "Spring: 3, 4, 5",
            "Summer: 6, 7, 8",
            "Fall: 9, 10, 11"
        ],
        solution="def month_to_season(month):\n    if month in [12, 1, 2]:\n        return 'winter'\n    elif month in [3, 4, 5]:\n        return 'spring'\n    elif month in [6, 7, 8]:\n        return 'summer'\n    elif month in [9, 10, 11]:\n        return 'fall'\n    else:\n        return 'invalid'",
        function_name="month_to_season",
        test_cases=[
            ((1,), 'winter'),
            ((4,), 'spring'),
            ((7,), 'summer'),
            ((10,), 'fall'),
        ]
    ),
    make_exercise(
        "cond_35",
        "Multiple-digit number analysis",
        "conditionals",
        3,
        "Write a function that returns 'small' (< 10), 'two_digit' (10-99), 'three_digit' (100-999), 'large' (>= 1000).",
        hints=[
            "Use absolute value: abs(n) to handle negatives",
            "Chained comparisons help: 10 <= abs(n) < 100",
            "Remember: 10 is two-digit, 100 is three-digit"
        ],
        solution="def digit_category(n):\n    n = abs(n)\n    if n < 10:\n        return 'small'\n    elif n < 100:\n        return 'two_digit'\n    elif n < 1000:\n        return 'three_digit'\n    else:\n        return 'large'",
        function_name="digit_category",
        test_cases=[
            ((5,), 'small'),
            ((42,), 'two_digit'),
            ((567,), 'three_digit'),
            ((1234,), 'large'),
        ]
    ),

    # HARD (36-45): Complex logic, real-world scenarios, match/case
    make_exercise(
        "cond_36",
        "Tax bracket calculator",
        "conditionals",
        4,
        "Write a function that calculates tax on income using brackets: 10% (0-10k), 12% (10k-40k), 22% (40k-85k), 24% (85k+).",
        hints=[
            "Tax is cumulative: first $10k at 10%, next $30k at 12%, etc.",
            "Use nested conditionals or separate calculations",
            "Example: $15k = (10k * 0.10) + (5k * 0.12) = $1600"
        ],
        solution="def calculate_tax(income):\n    if income <= 10000:\n        return income * 0.10\n    elif income <= 40000:\n        return 1000 + (income - 10000) * 0.12\n    elif income <= 85000:\n        return 1000 + 3600 + (income - 40000) * 0.22\n    else:\n        return 1000 + 3600 + 9900 + (income - 85000) * 0.24",
        function_name="calculate_tax",
        test_cases=[
            ((5000,), 500),
            ((15000,), 1600),
            ((50000,), 6800),
        ]
    ),
    make_exercise(
        "cond_37",
        "Complex eligibility checker",
        "conditionals",
        4,
        "Write a function that checks loan eligibility: age >= 21 AND (income >= 30k OR has_collateral) AND credit_score >= 650.",
        hints=[
            "All three major conditions must be true",
            "Use 'and' and 'or' together",
            "Parentheses: (A and B and C) structure"
        ],
        solution="def loan_eligible(age, income, has_collateral, credit_score):\n    return (age >= 21 and \n            (income >= 30000 or has_collateral) and \n            credit_score >= 650)",
        function_name="loan_eligible",
        test_cases=[
            ((25, 35000, False, 700), True),
            ((25, 25000, True, 700), True),
            ((20, 35000, False, 700), False),
            ((25, 25000, False, 600), False),
        ]
    ),
    make_exercise(
        "cond_38",
        "Game rock-paper-scissors",
        "conditionals",
        4,
        "Write a function that takes player1 and player2 moves and returns 'player1', 'player2', or 'tie'.",
        hints=[
            "Rock beats scissors, scissors beats paper, paper beats rock",
            "Use if/elif chain for outcomes",
            "Handle tie case separately"
        ],
        solution="def rps_winner(p1, p2):\n    if p1 == p2:\n        return 'tie'\n    if (p1 == 'rock' and p2 == 'scissors') or \\\n       (p1 == 'scissors' and p2 == 'paper') or \\\n       (p1 == 'paper' and p2 == 'rock'):\n        return 'player1'\n    return 'player2'",
        function_name="rps_winner",
        test_cases=[
            (('rock', 'rock'), 'tie'),
            (('rock', 'scissors'), 'player1'),
            (('paper', 'rock'), 'player1'),
            (('rock', 'paper'), 'player2'),
        ]
    ),
    make_exercise(
        "cond_39",
        "Email validation (basic)",
        "conditionals",
        4,
        "Write a function that validates an email: must have @ symbol, must have a dot after @, must have content before @, after @, and after dot.",
        hints=[
            "Check '@' in email",
            "Check '.' after '@': email.rfind('.') > email.find('@')",
            "Check length constraints: at least 1 char before @, between @&., after ."
        ],
        solution="def is_valid_email(email):\n    if '@' not in email:\n        return False\n    if '.' not in email:\n        return False\n    at_pos = email.find('@')\n    dot_pos = email.rfind('.')\n    if at_pos == 0 or at_pos == len(email) - 1:\n        return False\n    if dot_pos <= at_pos + 1 or dot_pos == len(email) - 1:\n        return False\n    return True",
        function_name="is_valid_email",
        test_cases=[
            (('user@example.com',), True),
            (('invalid.email',), False),
            (('@example.com',), False),
            (('user@.com',), False),
        ]
    ),
    make_exercise(
        "cond_40",
        "Nested conditionals with lists",
        "conditionals",
        4,
        "Write a function that takes a list and returns 'empty', 'single', or 'multi', and additionally if any element is negative, append '_has_neg'.",
        hints=[
            "First check length: 0, 1, or multiple",
            "Then check if any element is negative",
            "Use any(x < 0 for x in lst) to check",
            "Return appropriate string with or without '_has_neg'"
        ],
        solution="def list_summary(lst):\n    has_neg = any(x < 0 for x in lst)\n    \n    if len(lst) == 0:\n        result = 'empty'\n    elif len(lst) == 1:\n        result = 'single'\n    else:\n        result = 'multi'\n    \n    if has_neg:\n        result += '_has_neg'\n    return result",
        function_name="list_summary",
        test_cases=[
            ((([],), 'empty'),),
            ((([5],), 'single'),),
            ((([1, 2],), 'multi'),),
            ((([1, -2],), 'multi_has_neg'),),
        ]
    ),
    make_exercise(
        "cond_41",
        "Multi-level nested conditions",
        "conditionals",
        4,
        "Write a function that classifies numbers: 'small_even', 'small_odd', 'large_even', 'large_odd', where small is < 100.",
        hints=[
            "First level: check if < 100 (small) or >= 100 (large)",
            "Second level: check if even (n % 2 == 0) or odd",
            "Combine results into the appropriate category"
        ],
        solution="def classify_number_detailed(n):\n    if n < 100:\n        if n % 2 == 0:\n            return 'small_even'\n        else:\n            return 'small_odd'\n    else:\n        if n % 2 == 0:\n            return 'large_even'\n        else:\n            return 'large_odd'",
        function_name="classify_number_detailed",
        test_cases=[
            ((42,), 'small_even'),
            ((53,), 'small_odd'),
            ((200,), 'large_even'),
            ((201,), 'large_odd'),
        ]
    ),
    make_exercise(
        "cond_42",
        "String properties analysis",
        "conditionals",
        4,
        "Write a function that returns 'uppercase', 'lowercase', 'mixed', or 'non_alpha' based on string content.",
        hints=[
            "Use .isupper(), .islower(), .isalpha() methods",
            "non_alpha: string doesn't contain any letters",
            "mixed: contains both upper and lower case letters"
        ],
        solution="def string_case_type(s):\n    if not s:\n        return 'non_alpha'\n    if not any(c.isalpha() for c in s):\n        return 'non_alpha'\n    if s.isupper():\n        return 'uppercase'\n    elif s.islower():\n        return 'lowercase'\n    else:\n        return 'mixed'",
        function_name="string_case_type",
        test_cases=[
            (('HELLO',), 'uppercase'),
            (('hello',), 'lowercase'),
            (('Hello',), 'mixed'),
            (('12345',), 'non_alpha'),
        ]
    ),
    make_exercise(
        "cond_43",
        "Insurance premium calculator",
        "conditionals",
        4,
        "Write a function that calculates insurance premium: base $100, +$10 per year for age > 30, +$50 if high_risk, +15% if has_accidents.",
        hints=[
            "Base: $100",
            "Add $10 for each year over 30 (age - 30 if age > 30)",
            "Add $50 if high_risk is True",
            "Add 15% of total if has_accidents is True",
            "Order: base + age_surcharge + risk_surcharge, then apply accident multiplier"
        ],
        solution="def insurance_premium(age, high_risk, has_accidents):\n    premium = 100\n    if age > 30:\n        premium += (age - 30) * 10\n    if high_risk:\n        premium += 50\n    if has_accidents:\n        premium *= 1.15\n    return premium",
        function_name="insurance_premium",
        test_cases=[
            ((25, False, False), 100),
            ((35, False, False), 150),
            ((30, True, False), 150),
            ((35, True, True), 229.99999999999997),
        ]
    ),
    make_exercise(
        "cond_44",
        "Conditional string formatting",
        "conditionals",
        4,
        "Write a function that returns a message about a score: 'Excellent!' if >= 90, 'Good' if >= 80, 'Okay' if >= 70, 'Needs improvement' otherwise.",
        hints=[
            "Use if/elif/else with different string messages",
            "Each message is different, not just a grade letter",
            "Include punctuation in the returned strings"
        ],
        solution="def score_message(score):\n    if score >= 90:\n        return 'Excellent!'\n    elif score >= 80:\n        return 'Good'\n    elif score >= 70:\n        return 'Okay'\n    else:\n        return 'Needs improvement'",
        function_name="score_message",
        test_cases=[
            ((95,), 'Excellent!'),
            ((85,), 'Good'),
            ((75,), 'Okay'),
            ((60,), 'Needs improvement'),
        ]
    ),
    make_exercise(
        "cond_45",
        "Range-based categorization",
        "conditionals",
        4,
        "Write a function that categorizes a test score into percentile: 'top_10' (90+), 'top_25' (80-89), 'top_50' (70-79), 'below_50' (<70).",
        hints=[
            "Use >= and < carefully for boundaries",
            "90-99: top_10, 80-89: top_25, 70-79: top_50, 0-69: below_50",
            "Each range is mutually exclusive"
        ],
        solution="def percentile_category(score):\n    if score >= 90:\n        return 'top_10'\n    elif score >= 80:\n        return 'top_25'\n    elif score >= 70:\n        return 'top_50'\n    else:\n        return 'below_50'",
        function_name="percentile_category",
        test_cases=[
            ((95,), 'top_10'),
            ((85,), 'top_25'),
            ((75,), 'top_50'),
            ((65,), 'below_50'),
        ]
    ),

    # CHALLENGE (46-50): Complex real-world logic, match/case, edge cases
    make_exercise(
        "cond_46",
        "Comprehensive user access control",
        "conditionals",
        5,
        "Write a function that determines access level: 'admin' (role=='admin' AND is_active), 'moderator' (role=='moderator' AND is_active AND reputation>=50), 'user' (is_active), 'denied' otherwise.",
        hints=[
            "Order matters: check admin first, then moderator, then user",
            "All access levels require is_active == True",
            "Moderator also requires reputation >= 50"
        ],
        solution="def determine_access(role, is_active, reputation):\n    if role == 'admin' and is_active:\n        return 'admin'\n    elif role == 'moderator' and is_active and reputation >= 50:\n        return 'moderator'\n    elif is_active:\n        return 'user'\n    else:\n        return 'denied'",
        function_name="determine_access",
        test_cases=[
            (('admin', True, 100), 'admin'),
            (('moderator', True, 60), 'moderator'),
            (('moderator', True, 30), 'user'),
            (('user', True, 0), 'user'),
            (('user', False, 0), 'denied'),
        ]
    ),
    make_exercise(
        "cond_47",
        "Flight ticket pricing with multiple factors",
        "conditionals",
        5,
        "Write a function that calculates ticket price: base $200, -20% if advance_booking (>30 days), -10% if is_member, +50% if is_weekend.",
        hints=[
            "Base price: $200",
            "Discount for advance_booking: advance_days > 30",
            "Discount for membership: is_member == True",
            "Surcharge for weekend: is_weekend == True",
            "Apply discounts first, then surcharge"
        ],
        solution="def flight_ticket_price(advance_days, is_member, is_weekend):\n    price = 200\n    if advance_days > 30:\n        price *= 0.8\n    if is_member:\n        price *= 0.9\n    if is_weekend:\n        price *= 1.5\n    return price",
        function_name="flight_ticket_price",
        test_cases=[
            ((50, False, False), 160),
            ((10, False, False), 200),
            ((50, True, False), 144),
            ((50, True, True), 216),
        ]
    ),
    make_exercise(
        "cond_48",
        "Data validation with multiple checks",
        "conditionals",
        5,
        "Write a function that validates registration: returns list of errors if any, or ['valid'] if all checks pass.",
        hints=[
            "Check: age >= 18, email contains '@', password length >= 8, username length 3-20",
            "Collect errors in a list: 'age_error', 'email_error', 'password_error', 'username_error'",
            "Return ['valid'] if no errors, otherwise return the error list"
        ],
        solution="def validate_registration(age, email, password, username):\n    errors = []\n    if age < 18:\n        errors.append('age_error')\n    if '@' not in email:\n        errors.append('email_error')\n    if len(password) < 8:\n        errors.append('password_error')\n    if len(username) < 3 or len(username) > 20:\n        errors.append('username_error')\n    return errors if errors else ['valid']",
        function_name="validate_registration",
        test_cases=[
            ((25, 'user@example.com', 'password123', 'john'), ['valid']),
            ((17, 'user@example.com', 'password123', 'john'), ['age_error']),
            ((25, 'useremailcom', 'short', 'a'), ['email_error', 'password_error', 'username_error']),
        ]
    ),
    make_exercise(
        "cond_49",
        "Match statement (Python 3.10+)",
        "conditionals",
        5,
        "Write a function using match/case that maps HTTP status codes to descriptions: 200->'OK', 301->'Moved', 400->'Bad Request', 404->'Not Found', 500->'Server Error', default->'Unknown'.",
        hints=[
            "Use match status_code: ... case ...",
            "Cases can be single values or ranges (in this case, use if conditions inside case)",
            "Use _ as default case",
            "match/case is structural pattern matching in Python 3.10+"
        ],
        solution="def http_status(code):\n    match code:\n        case 200:\n            return 'OK'\n        case 301:\n            return 'Moved'\n        case 400:\n            return 'Bad Request'\n        case 404:\n            return 'Not Found'\n        case 500:\n            return 'Server Error'\n        case _:\n            return 'Unknown'",
        function_name="http_status",
        test_cases=[
            ((200,), 'OK'),
            ((404,), 'Not Found'),
            ((500,), 'Server Error'),
            ((999,), 'Unknown'),
        ]
    ),
    make_exercise(
        "cond_50",
        "Complex business logic: subscription tier upgrade",
        "conditionals",
        5,
        "Write a function that determines if a user can upgrade from tier1 to tier2: tier1 != tier2, account_age > 30 days, AND (payment_method_verified OR credit_balance > 100).",
        hints=[
            "Must not be upgrading from the same tier",
            "Account must be at least 31 days old",
            "Must either have verified payment OR sufficient credit balance",
            "All three conditions must be true"
        ],
        solution="def can_upgrade_tier(tier1, tier2, account_age, payment_verified, credit_balance):\n    return (tier1 != tier2 and \n            account_age > 30 and \n            (payment_verified or credit_balance > 100))",
        function_name="can_upgrade_tier",
        test_cases=[
            (('basic', 'premium', 60, True, 0), True),
            (('basic', 'premium', 60, False, 150), True),
            (('basic', 'premium', 60, False, 50), False),
            (('basic', 'basic', 60, True, 0), False),
            (('basic', 'premium', 20, True, 0), False),
        ]
    ),
]
