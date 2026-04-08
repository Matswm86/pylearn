"""50 exercises on Python data types."""
from .base import make_exercise

exercises = [
    # BEGINNER (1-10): Basic type recognition and simple conversions
    make_exercise(
        id="dt_01",
        title="Identify Integer Type",
        topic="data_types",
        difficulty=1,
        description="Create a variable `x` that holds the integer value 42 and use the `type()` function to verify it's an int.",
        hints=[
            "Use the assignment operator to assign 42 to x",
            "Call type(x) and compare it to int"
        ],
        solution="x = 42\nresult = type(x) == int",
        check=lambda ns: (ns.get('result') is True, "x should be an int and result should be True"),
        concepts=["int", "type()"]
    ),
    make_exercise(
        id="dt_02",
        title="Identify Float Type",
        topic="data_types",
        difficulty=1,
        description="Create a variable `y` that holds the float value 3.14 and verify it's a float using type().",
        hints=[
            "Use a decimal point to make it a float",
            "Compare type(y) to float"
        ],
        solution="y = 3.14\nresult = type(y) == float",
        check=lambda ns: (ns.get('result') is True, "y should be a float"),
        concepts=["float", "type()"]
    ),
    make_exercise(
        id="dt_03",
        title="Identify String Type",
        topic="data_types",
        difficulty=1,
        description="Create a variable `message` with the string 'Hello' and verify it's a string.",
        hints=[
            "Wrap text in quotes to make it a string",
            "Use type() to check the type"
        ],
        solution="message = 'Hello'\nresult = type(message) == str",
        check=lambda ns: (ns.get('result') is True, "message should be a string"),
        concepts=["str", "type()"]
    ),
    make_exercise(
        id="dt_04",
        title="Identify Boolean Type",
        topic="data_types",
        difficulty=1,
        description="Create a variable `flag` with the boolean value True and verify its type.",
        hints=[
            "Use True (capital T) for boolean true",
            "Compare the type to bool"
        ],
        solution="flag = True\nresult = type(flag) == bool",
        check=lambda ns: (ns.get('result') is True, "flag should be a boolean"),
        concepts=["bool", "type()"]
    ),
    make_exercise(
        id="dt_05",
        title="Convert String to Integer",
        topic="data_types",
        difficulty=1,
        description="Convert the string '123' to an integer using the int() function and store in variable `num`.",
        hints=[
            "Use the int() function with a string argument",
            "Make sure to pass the string '123' not the number 123"
        ],
        solution="num = int('123')\nresult = num == 123 and type(num) == int",
        check=lambda ns: (ns.get('result') is True, "num should be 123 as an integer"),
        concepts=["int()", "type conversion"]
    ),
    make_exercise(
        id="dt_06",
        title="Convert Integer to String",
        topic="data_types",
        difficulty=1,
        description="Convert the integer 456 to a string using str() and store in variable `text`.",
        hints=[
            "Use the str() function with the integer",
            "After conversion, it should have type str"
        ],
        solution="text = str(456)\nresult = text == '456' and type(text) == str",
        check=lambda ns: (ns.get('result') is True, "text should be '456' as a string"),
        concepts=["str()", "type conversion"]
    ),
    make_exercise(
        id="dt_07",
        title="Convert String to Float",
        topic="data_types",
        difficulty=1,
        description="Convert the string '3.14' to a float using float() and store in variable `pi_approx`.",
        hints=[
            "Use the float() function",
            "It should work with decimal notation in strings"
        ],
        solution="pi_approx = float('3.14')\nresult = abs(pi_approx - 3.14) < 0.0001 and type(pi_approx) == float",
        check=lambda ns: (ns.get('result') is True, "pi_approx should be 3.14 as a float"),
        concepts=["float()", "type conversion"]
    ),
    make_exercise(
        id="dt_08",
        title="Convert to Boolean",
        topic="data_types",
        difficulty=1,
        description="Convert the integer 1 to a boolean using bool() and store in variable `b`.",
        hints=[
            "Use the bool() function",
            "Non-zero numbers convert to True"
        ],
        solution="b = bool(1)\nresult = b is True and type(b) == bool",
        check=lambda ns: (ns.get('result') is True, "b should be True"),
        concepts=["bool()", "type conversion"]
    ),
    make_exercise(
        id="dt_09",
        title="String Length with len()",
        topic="data_types",
        difficulty=1,
        description="Find the length of the string 'Python' using len() and store in variable `length`.",
        hints=[
            "The len() function counts characters in a string",
            "'Python' has 6 characters"
        ],
        solution="length = len('Python')\nresult = length == 6",
        check=lambda ns: (ns.get('result') is True, "length should be 6"),
        concepts=["len()", "str"]
    ),
    make_exercise(
        id="dt_10",
        title="Check Type with isinstance()",
        topic="data_types",
        difficulty=1,
        description="Use isinstance() to check if the variable `x = 100` is an integer. Store the result in `check_result`.",
        hints=[
            "isinstance() takes an object and a type as arguments",
            "The syntax is isinstance(object, type)"
        ],
        solution="x = 100\ncheck_result = isinstance(x, int)",
        check=lambda ns: (ns.get('check_result') is True, "check_result should be True"),
        concepts=["isinstance()", "type checking"]
    ),

    # EASY (11-20): String methods and operations
    make_exercise(
        id="dt_11",
        title="String Upper Method",
        topic="data_types",
        difficulty=2,
        description="Convert the string 'hello world' to uppercase using the upper() method and store in `upper_text`.",
        hints=[
            "Use the .upper() method on the string",
            "String methods are called with a dot"
        ],
        solution="upper_text = 'hello world'.upper()\nresult = upper_text == 'HELLO WORLD'",
        check=lambda ns: (ns.get('result') is True, "upper_text should be 'HELLO WORLD'"),
        concepts=["str.upper()", "string methods"]
    ),
    make_exercise(
        id="dt_12",
        title="String Lower Method",
        topic="data_types",
        difficulty=2,
        description="Convert 'PYTHON ROCKS' to lowercase using lower() and store in `lower_text`.",
        hints=[
            "Use the .lower() method",
            "The result should be all lowercase"
        ],
        solution="lower_text = 'PYTHON ROCKS'.lower()\nresult = lower_text == 'python rocks'",
        check=lambda ns: (ns.get('result') is True, "lower_text should be 'python rocks'"),
        concepts=["str.lower()", "string methods"]
    ),
    make_exercise(
        id="dt_13",
        title="String Strip Method",
        topic="data_types",
        difficulty=2,
        description="Remove leading and trailing whitespace from '  hello  ' using strip() and store in `stripped`.",
        hints=[
            "The .strip() method removes whitespace from both ends",
            "It doesn't modify the middle of the string"
        ],
        solution="stripped = '  hello  '.strip()\nresult = stripped == 'hello'",
        check=lambda ns: (ns.get('result') is True, "stripped should be 'hello'"),
        concepts=["str.strip()", "whitespace"]
    ),
    make_exercise(
        id="dt_14",
        title="String Replace Method",
        topic="data_types",
        difficulty=2,
        description="Replace 'cat' with 'dog' in 'the cat sat on the mat' and store in `replaced`.",
        hints=[
            "Use the .replace() method with two arguments",
            "The syntax is .replace(old, new)"
        ],
        solution="replaced = 'the cat sat on the mat'.replace('cat', 'dog')\nresult = replaced == 'the dog sat on the mat'",
        check=lambda ns: (ns.get('result') is True, "replaced should be 'the dog sat on the mat'"),
        concepts=["str.replace()", "string methods"]
    ),
    make_exercise(
        id="dt_15",
        title="String Find Method",
        topic="data_types",
        difficulty=2,
        description="Find the index of 'world' in 'hello world' using find() and store in `index`.",
        hints=[
            "The .find() method returns the starting index of the substring",
            "'hello ' is 6 characters, so 'world' starts at index 6"
        ],
        solution="index = 'hello world'.find('world')\nresult = index == 6",
        check=lambda ns: (ns.get('result') is True, "index should be 6"),
        concepts=["str.find()", "string indexing"]
    ),
    make_exercise(
        id="dt_16",
        title="String Indexing",
        topic="data_types",
        difficulty=2,
        description="Get the character at index 0 from 'Python' and store in `first_char`.",
        hints=[
            "Use bracket notation: string[index]",
            "Index 0 is the first character"
        ],
        solution="first_char = 'Python'[0]\nresult = first_char == 'P'",
        check=lambda ns: (ns.get('result') is True, "first_char should be 'P'"),
        concepts=["str indexing", "indexing"]
    ),
    make_exercise(
        id="dt_17",
        title="String Slicing",
        topic="data_types",
        difficulty=2,
        description="Get characters from index 0 to 3 (exclusive) from 'Python' using slicing and store in `slice_text`.",
        hints=[
            "Use the syntax string[start:end]",
            "[0:3] gives characters at indices 0, 1, 2"
        ],
        solution="slice_text = 'Python'[0:3]\nresult = slice_text == 'Pyt'",
        check=lambda ns: (ns.get('result') is True, "slice_text should be 'Pyt'"),
        concepts=["str slicing", "slicing"]
    ),
    make_exercise(
        id="dt_18",
        title="String Split Method",
        topic="data_types",
        difficulty=2,
        description="Split 'apple,banana,orange' by comma using split() and store in `fruits`.",
        hints=[
            "Use the .split() method with the delimiter",
            "The result should be a list of strings"
        ],
        solution="fruits = 'apple,banana,orange'.split(',')\nresult = fruits == ['apple', 'banana', 'orange']",
        check=lambda ns: (ns.get('result') is True, "fruits should be ['apple', 'banana', 'orange']"),
        concepts=["str.split()", "string parsing"]
    ),
    make_exercise(
        id="dt_19",
        title="String Join Method",
        topic="data_types",
        difficulty=2,
        description="Join the list ['one', 'two', 'three'] with hyphens using join() and store in `joined`.",
        hints=[
            "Use the .join() method on the separator string",
            "The syntax is separator.join(list)"
        ],
        solution="joined = '-'.join(['one', 'two', 'three'])\nresult = joined == 'one-two-three'",
        check=lambda ns: (ns.get('result') is True, "joined should be 'one-two-three'"),
        concepts=["str.join()", "list operations"]
    ),
    make_exercise(
        id="dt_20",
        title="Format with f-string",
        topic="data_types",
        difficulty=2,
        description="Use an f-string to format 'Hello, Alice!' where 'Alice' is stored in variable `name = 'Alice'`.",
        hints=[
            "Use the f'' syntax with variables in curly braces",
            "The syntax is f'Hello, {name}!'"
        ],
        solution="name = 'Alice'\ngreeting = f'Hello, {name}!'\nresult = greeting == 'Hello, Alice!'",
        check=lambda ns: (ns.get('result') is True, "greeting should be 'Hello, Alice!'"),
        concepts=["f-strings", "string formatting"]
    ),

    # MEDIUM (21-35): Numeric operations and advanced conversions
    make_exercise(
        id="dt_21",
        title="Integer Division",
        topic="data_types",
        difficulty=3,
        description="Divide 17 by 5 using integer division (//) and store the result in `int_div`.",
        hints=[
            "Use the // operator for integer division",
            "17 // 5 gives 3 (not 3.4)"
        ],
        solution="int_div = 17 // 5\nresult = int_div == 3",
        check=lambda ns: (ns.get('result') is True, "int_div should be 3"),
        concepts=["integer division", "//", "operators"]
    ),
    make_exercise(
        id="dt_22",
        title="Modulo Operator",
        topic="data_types",
        difficulty=3,
        description="Find the remainder when 17 is divided by 5 using the modulo operator (%) and store in `remainder`.",
        hints=[
            "Use the % operator",
            "17 % 5 gives 2 (the remainder)"
        ],
        solution="remainder = 17 % 5\nresult = remainder == 2",
        check=lambda ns: (ns.get('result') is True, "remainder should be 2"),
        concepts=["modulo", "%", "operators"]
    ),
    make_exercise(
        id="dt_23",
        title="Exponentiation",
        topic="data_types",
        difficulty=3,
        description="Calculate 2 to the power of 8 using the exponentiation operator (**) and store in `power`.",
        hints=[
            "Use the ** operator",
            "2 ** 8 equals 256"
        ],
        solution="power = 2 ** 8\nresult = power == 256",
        check=lambda ns: (ns.get('result') is True, "power should be 256"),
        concepts=["exponentiation", "**", "operators"]
    ),
    make_exercise(
        id="dt_24",
        title="Absolute Value Function",
        topic="data_types",
        difficulty=3,
        description="Find the absolute value of -42 using abs() and store in `absolute`.",
        hints=[
            "The abs() function returns the non-negative value",
            "abs(-42) is 42"
        ],
        solution="absolute = abs(-42)\nresult = absolute == 42",
        check=lambda ns: (ns.get('result') is True, "absolute should be 42"),
        concepts=["abs()", "functions"]
    ),
    make_exercise(
        id="dt_25",
        title="Round Function",
        topic="data_types",
        difficulty=3,
        description="Round 3.7 to the nearest integer using round() and store in `rounded`.",
        hints=[
            "The round() function rounds to the nearest integer by default",
            "3.7 rounds to 4"
        ],
        solution="rounded = round(3.7)\nresult = rounded == 4",
        check=lambda ns: (ns.get('result') is True, "rounded should be 4"),
        concepts=["round()", "functions"]
    ),
    make_exercise(
        id="dt_26",
        title="Round to Decimal Places",
        topic="data_types",
        difficulty=3,
        description="Round 3.14159 to 2 decimal places using round() and store in `rounded_pi`.",
        hints=[
            "Use round() with a second argument for decimal places",
            "round(3.14159, 2) gives 3.14"
        ],
        solution="rounded_pi = round(3.14159, 2)\nresult = rounded_pi == 3.14",
        check=lambda ns: (ns.get('result') is True, "rounded_pi should be 3.14"),
        concepts=["round()", "precision"]
    ),
    make_exercise(
        id="dt_27",
        title="Float String Formatting",
        topic="data_types",
        difficulty=3,
        description="Format the float 99.5 as a string with 1 decimal place using an f-string.",
        hints=[
            "Use f-string with format specifier: f'{value:.1f}'",
            "The result should be '99.5'"
        ],
        solution="value = 99.5\nformatted = f'{value:.1f}'\nresult = formatted == '99.5'",
        check=lambda ns: (ns.get('result') is True, "formatted should be '99.5'"),
        concepts=["f-strings", "format specifiers"]
    ),
    make_exercise(
        id="dt_28",
        title="Format Currency",
        topic="data_types",
        difficulty=3,
        description="Create a function `format_price(amount)` that returns a price formatted as '$X.XX' (e.g., $12.50).",
        hints=[
            "Use an f-string with the format specifier .2f",
            "Prepend '$' to the formatted number"
        ],
        solution="def format_price(amount):\n    return f'${amount:.2f}'",
        function_name="format_price",
        test_cases=[
            (12.5, "$12.50"),
            (100, "$100.00"),
            (3.1, "$3.10"),
        ],
        concepts=["f-strings", "practical formatting"]
    ),
    make_exercise(
        id="dt_29",
        title="Escape Characters",
        topic="data_types",
        difficulty=3,
        description="Create a string with a newline using the escape sequence \\n and store in `multi_line`.",
        hints=[
            "Use \\n for newline within a single-quoted string",
            "The string should be 'Hello\\nWorld' which displays on two lines"
        ],
        solution="multi_line = 'Hello\\nWorld'\nresult = multi_line == 'Hello\\nWorld'",
        check=lambda ns: (ns.get('result') is True, "multi_line should contain newline"),
        concepts=["escape sequences", "\\n"]
    ),
    make_exercise(
        id="dt_30",
        title="Tab Escape Sequence",
        topic="data_types",
        difficulty=3,
        description="Create a string with a tab using \\t between two words and store in `tabbed`.",
        hints=[
            "Use \\t for tab",
            "'Name\\tAge' displays as 'Name' then tab then 'Age'"
        ],
        solution="tabbed = 'Name\\tAge'\nresult = '\\t' in tabbed",
        check=lambda ns: (ns.get('result') is True, "tabbed should contain tab character"),
        concepts=["escape sequences", "\\t"]
    ),
    make_exercise(
        id="dt_31",
        title="Multiline String with Triple Quotes",
        topic="data_types",
        difficulty=3,
        description="Create a multiline string using triple quotes (''') that spans 3 lines and store in `poem`.",
        hints=[
            "Use ''' or triple double quotes",
            "You can press Enter to go to the next line inside triple quotes"
        ],
        solution="poem = '''Line one\nLine two\nLine three'''\nresult = poem.count('\\n') >= 2",
        check=lambda ns: (ns.get('result') is True, "poem should have multiple lines"),
        concepts=["multiline strings", "triple quotes"]
    ),
    make_exercise(
        id="dt_32",
        title="Complex Number Basics",
        topic="data_types",
        difficulty=3,
        description="Create a complex number with real part 3 and imaginary part 4 and store in `c`.",
        hints=[
            "Use 3 + 4j notation for complex numbers",
            "The j represents the imaginary unit (not i)"
        ],
        solution="c = 3 + 4j\nresult = c.real == 3 and c.imag == 4",
        check=lambda ns: (ns.get('result') is True, "c should be 3+4j"),
        concepts=["complex numbers", "imaginary unit"]
    ),
    make_exercise(
        id="dt_33",
        title="Check Boolean Truthiness",
        topic="data_types",
        difficulty=3,
        description="In Python, determine which of these is falsy: 0, '', None, and []. Check if 0 is falsy by storing `bool(0)` in `is_falsy`.",
        hints=[
            "Use bool() to check truthiness",
            "0 converts to False"
        ],
        solution="is_falsy = bool(0) == False\nresult = is_falsy",
        check=lambda ns: (ns.get('result') is True, "0 should be falsy"),
        concepts=["truthiness", "falsy values"]
    ),
    make_exercise(
        id="dt_34",
        title="None Type Basics",
        topic="data_types",
        difficulty=3,
        description="Create a variable `x = None` and check its type using type().",
        hints=[
            "None is a special keyword in Python",
            "type(None) is NoneType"
        ],
        solution="x = None\nresult = x is None and type(x) == type(None)",
        check=lambda ns: (ns.get('result') is True, "x should be None"),
        concepts=["None", "null value"]
    ),
    make_exercise(
        id="dt_35",
        title="Character Code with ord()",
        topic="data_types",
        difficulty=3,
        description="Find the Unicode code point of 'A' using ord() and store in `code`.",
        hints=[
            "ord() converts a character to its Unicode value",
            "ord('A') is 65"
        ],
        solution="code = ord('A')\nresult = code == 65",
        check=lambda ns: (ns.get('result') is True, "code should be 65"),
        concepts=["ord()", "Unicode"]
    ),

    # HARD (36-45): Complex practical scenarios
    make_exercise(
        id="dt_36",
        title="Character from Code with chr()",
        topic="data_types",
        difficulty=4,
        description="Convert the Unicode code point 65 back to a character using chr() and store in `char`.",
        hints=[
            "chr() is the inverse of ord()",
            "chr(65) gives 'A'"
        ],
        solution="char = chr(65)\nresult = char == 'A'",
        check=lambda ns: (ns.get('result') is True, "char should be 'A'"),
        concepts=["chr()", "Unicode"]
    ),
    make_exercise(
        id="dt_37",
        title="Temperature Conversion Function",
        topic="data_types",
        difficulty=4,
        description="Create a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit using the formula F = C * 9/5 + 32.",
        hints=[
            "Use the exact formula: (celsius * 9/5) + 32",
            "0°C should equal 32°F"
        ],
        solution="def celsius_to_fahrenheit(c):\n    return c * 9/5 + 32",
        function_name="celsius_to_fahrenheit",
        test_cases=[
            (0, 32),
            (100, 212),
            (-40, -40),
        ],
        concepts=["numeric operations", "formulas"]
    ),
    make_exercise(
        id="dt_38",
        title="Validate Email Format",
        topic="data_types",
        difficulty=4,
        description="Create a function `is_valid_email(email)` that returns True if the string contains exactly one '@' and at least one '.' after the '@'.",
        hints=[
            "Use string methods like count() and find()",
            "Check that '@' appears exactly once and '.' appears after it"
        ],
        solution="def is_valid_email(email):\n    return email.count('@') == 1 and '.' in email.split('@')[1]",
        function_name="is_valid_email",
        test_cases=[
            ('test@example.com', True),
            ('invalid@email', False),
            ('test@@@example.com', False),
            ('notanemail.com', False),
        ],
        concepts=["string validation", "string methods"]
    ),
    make_exercise(
        id="dt_39",
        title="Reverse a String",
        topic="data_types",
        difficulty=4,
        description="Create a function `reverse_string(s)` that returns the string reversed using slicing.",
        hints=[
            "Use slice notation with negative step: s[::-1]",
            "'hello' reversed is 'olleh'"
        ],
        solution="def reverse_string(s):\n    return s[::-1]",
        function_name="reverse_string",
        test_cases=[
            ('hello', 'olleh'),
            ('Python', 'nohtyP'),
            ('a', 'a'),
        ],
        concepts=["string slicing", "string manipulation"]
    ),
    make_exercise(
        id="dt_40",
        title="Count Vowels in String",
        topic="data_types",
        difficulty=4,
        description="Create a function `count_vowels(text)` that returns the number of vowels (a, e, i, o, u) in the text (case-insensitive).",
        hints=[
            "Convert to lowercase first with .lower()",
            "Loop through characters and count those in 'aeiou'"
        ],
        solution="def count_vowels(text):\n    return sum(1 for c in text.lower() if c in 'aeiou')",
        function_name="count_vowels",
        test_cases=[
            ('Hello', 2),
            ('AEIOUaeiou', 10),
            ('xyz', 0),
        ],
        concepts=["string iteration", "counting"]
    ),
    make_exercise(
        id="dt_41",
        title="Parse Integer from String with Error Handling",
        topic="data_types",
        difficulty=4,
        description="Create a function `safe_int(value)` that converts a string to int, returning -1 if conversion fails.",
        hints=[
            "Use try/except to catch ValueError",
            "Return the converted integer or -1 on error"
        ],
        solution="def safe_int(value):\n    try:\n        return int(value)\n    except ValueError:\n        return -1",
        function_name="safe_int",
        test_cases=[
            ('123', 123),
            ('abc', -1),
            ('45.6', -1),
        ],
        concepts=["type conversion", "error handling"]
    ),
    make_exercise(
        id="dt_42",
        title="Truncate Float to N Decimals",
        topic="data_types",
        difficulty=4,
        description="Create a function `truncate_float(value, decimals)` that truncates (not rounds) a float to N decimal places.",
        hints=[
            "Use int() and multiplication: int(value * 10**decimals) / 10**decimals",
            "3.14159 truncated to 2 places is 3.14, not 3.15"
        ],
        solution="def truncate_float(value, decimals):\n    multiplier = 10 ** decimals\n    return int(value * multiplier) / multiplier",
        function_name="truncate_float",
        test_cases=[
            ((3.14159, 2), 3.14),
            ((99.9999, 1), 99.9),
            ((5, 2), 5.0),
        ],
        concepts=["numeric precision", "type conversion"]
    ),
    make_exercise(
        id="dt_43",
        title="Check if String is Numeric",
        topic="data_types",
        difficulty=4,
        description="Create a function `is_numeric(s)` that returns True if the string can be converted to a float.",
        hints=[
            "Try converting with float() and catch ValueError",
            "Handle both integers and floats: '123' and '3.14' should both return True"
        ],
        solution="def is_numeric(s):\n    try:\n        float(s)\n        return True\n    except ValueError:\n        return False",
        function_name="is_numeric",
        test_cases=[
            ('123', True),
            ('3.14', True),
            ('abc', False),
            ('12.34.56', False),
        ],
        concepts=["string validation", "type conversion"]
    ),
    make_exercise(
        id="dt_44",
        title="Extract Numbers from String",
        topic="data_types",
        difficulty=4,
        description="Create a function `extract_digits(text)` that returns a string containing only the digits from the input.",
        hints=[
            "Use a loop or generator to filter characters",
            "Check if c.isdigit() for each character"
        ],
        solution="def extract_digits(text):\n    return ''.join(c for c in text if c.isdigit())",
        function_name="extract_digits",
        test_cases=[
            ('abc123def456', '123456'),
            ('no digits here', ''),
            ('2024-04-08', '20240408'),
        ],
        concepts=["string filtering", "character methods"]
    ),
    make_exercise(
        id="dt_45",
        title="Capitalize First Letter Only",
        topic="data_types",
        difficulty=4,
        description="Create a function `capitalize_first(text)` that capitalizes only the first character, leaving the rest unchanged.",
        hints=[
            "Use indexing and slicing: text[0].upper() + text[1:]",
            "Handle empty strings gracefully"
        ],
        solution="def capitalize_first(text):\n    return text[0].upper() + text[1:] if text else text",
        function_name="capitalize_first",
        test_cases=[
            ('hello world', 'Hello world'),
            ('HELLO', 'HELLO'),
            ('a', 'A'),
        ],
        concepts=["string slicing", "string methods"]
    ),

    # CHALLENGE (46-50): Advanced real-world scenarios
    make_exercise(
        id="dt_46",
        title="Format Large Numbers with Commas",
        topic="data_types",
        difficulty=5,
        description="Create a function `format_number(n)` that formats an integer with thousand separators, e.g., 1000000 becomes '1,000,000'.",
        hints=[
            "Use Python's built-in format() function or string method",
            "format(1000000, ',') works, or use f'{n:,}'"
        ],
        solution="def format_number(n):\n    return f'{n:,}'",
        function_name="format_number",
        test_cases=[
            (1000, '1,000'),
            (1000000, '1,000,000'),
            (42, '42'),
        ],
        concepts=["number formatting", "format specifiers"]
    ),
    make_exercise(
        id="dt_47",
        title="Build Query String from Dictionary",
        topic="data_types",
        difficulty=5,
        description="Create a function `build_query_string(params)` that takes a dictionary and returns a URL query string, e.g., {'name': 'Alice', 'age': 30} becomes 'name=Alice&age=30'.",
        hints=[
            "Iterate through dictionary items",
            "Join with '&' separator and use '=' between key and value"
        ],
        solution="def build_query_string(params):\n    return '&'.join(f'{k}={v}' for k, v in params.items())",
        function_name="build_query_string",
        test_cases=[
            (({'name': 'Alice', 'age': '30'},), 'name=Alice&age=30'),
            (({'x': '1'},), 'x=1'),
        ],
        concepts=["string building", "dict iteration"]
    ),
    make_exercise(
        id="dt_48",
        title="Type-Based Processing",
        topic="data_types",
        difficulty=5,
        description="Create a function `describe_value(val)` that returns a description string based on the type: 'int' for int, 'float' for float, 'str' for str, or 'other' for anything else.",
        hints=[
            "Use type() or isinstance() to check types",
            "Return appropriate strings based on the type"
        ],
        solution="def describe_value(val):\n    if isinstance(val, bool):\n        return 'bool'\n    elif isinstance(val, int):\n        return 'int'\n    elif isinstance(val, float):\n        return 'float'\n    elif isinstance(val, str):\n        return 'str'\n    else:\n        return 'other'",
        function_name="describe_value",
        test_cases=[
            (42, 'int'),
            (3.14, 'float'),
            ('hello', 'str'),
            (True, 'bool'),
            ([], 'other'),
        ],
        concepts=["type checking", "isinstance()"]
    ),
    make_exercise(
        id="dt_49",
        title="Parse CSV Line into Typed Values",
        topic="data_types",
        difficulty=5,
        description="Create a function `parse_csv_line(line, types)` that splits a CSV line and converts each field to the specified type. E.g., parse_csv_line('1,3.14,hello', [int, float, str]) returns [1, 3.14, 'hello'].",
        hints=[
            "Use split(',') to split the line",
            "Use a list comprehension to convert each value with its type",
            "handle the conversion: type(value_string)"
        ],
        solution="def parse_csv_line(line, types):\n    values = line.split(',')\n    return [t(v) for t, v in zip(types, values)]",
        function_name="parse_csv_line",
        test_cases=[
            (('1,3.14,hello', [int, float, str]), [1, 3.14, 'hello']),
            (('42,true,test', [int, str, str]), [42, 'true', 'test']),
        ],
        concepts=["type conversion", "list comprehension"]
    ),
    make_exercise(
        id="dt_50",
        title="Robust Type Conversion Pipeline",
        topic="data_types",
        difficulty=5,
        description="Create a function `safe_convert(value, target_type)` that attempts to convert value to target_type, returning None on any error. It should handle int, float, str, and bool types.",
        hints=[
            "Use try/except for each type conversion",
            "For bool, convert non-empty strings and non-zero numbers to True",
            "Return None if conversion fails"
        ],
        solution="def safe_convert(value, target_type):\n    try:\n        if target_type == bool:\n            if isinstance(value, bool):\n                return value\n            if isinstance(value, str):\n                return value.lower() in ('true', '1', 'yes')\n            return bool(value)\n        return target_type(value)\n    except (ValueError, TypeError):\n        return None",
        function_name="safe_convert",
        test_cases=[
            (('123', int), 123),
            (('3.14', float), 3.14),
            (('hello', str), 'hello'),
            (('abc', int), None),
            (('true', bool), True),
        ],
        concepts=["type conversion", "error handling", "practical processing"]
    ),
]
