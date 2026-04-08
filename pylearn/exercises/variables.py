"""50 exercises on Python variables."""
from .base import make_exercise

exercises = [
    # ========================
    # BEGINNER (1-10)
    # ========================
    make_exercise(
        id="var_01",
        title="Basic Variable Assignment",
        topic="variables",
        difficulty=1,
        description="Create a variable named `name` and assign it your name as a string.",
        hints=[
            "Use the syntax: variable_name = value",
            "String values must be enclosed in quotes (single or double)"
        ],
        solution='name = "Alice"',
        starter_code="# Create a variable called name\n",
        check=lambda ns: (
            "name" in ns and isinstance(ns["name"], str) and len(ns["name"]) > 0,
            "Create a variable 'name' with a string value"
        ),
        concepts=["assignment", "strings", "variable naming"]
    ),

    make_exercise(
        id="var_02",
        title="Numeric Variable Assignment",
        topic="variables",
        difficulty=1,
        description="Create a variable named `age` and assign it the value 25.",
        hints=[
            "Numeric values (integers) don't need quotes",
            "The syntax is the same: variable_name = value"
        ],
        solution="age = 25",
        starter_code="# Create a variable called age\n",
        check=lambda ns: (
            "age" in ns and ns["age"] == 25 and isinstance(ns["age"], int),
            "Create a variable 'age' with the integer value 25"
        ),
        concepts=["assignment", "integers", "numeric variables"]
    ),

    make_exercise(
        id="var_03",
        title="Float Variable Assignment",
        topic="variables",
        difficulty=1,
        description="Create a variable named `height` and assign it the value 5.9 (representing height in feet).",
        hints=[
            "Floating-point numbers have a decimal point",
            "height = 5.9 will automatically create a float"
        ],
        solution="height = 5.9",
        starter_code="# Create a variable called height\n",
        check=lambda ns: (
            "height" in ns and ns["height"] == 5.9 and isinstance(ns["height"], float),
            "Create a variable 'height' with the float value 5.9"
        ),
        concepts=["assignment", "floats", "numeric variables"]
    ),

    make_exercise(
        id="var_04",
        title="Boolean Variable Assignment",
        topic="variables",
        difficulty=1,
        description="Create a variable named `is_student` and assign it the boolean value True.",
        hints=[
            "Boolean values are True or False (capital T and F)",
            "These represent true/false conditions"
        ],
        solution="is_student = True",
        starter_code="# Create a variable called is_student\n",
        check=lambda ns: (
            "is_student" in ns and ns["is_student"] is True and isinstance(ns["is_student"], bool),
            "Create a variable 'is_student' with the boolean value True"
        ),
        concepts=["assignment", "booleans", "logic"]
    ),

    make_exercise(
        id="var_05",
        title="Multiple Variable Assignment",
        topic="variables",
        difficulty=1,
        description="Assign the values 10, 20, and 30 to three variables: `x`, `y`, and `z` using a single line of code.",
        hints=[
            "You can assign multiple variables at once: a, b, c = 1, 2, 3",
            "The order matters: first value to first variable, etc."
        ],
        solution="x, y, z = 10, 20, 30",
        starter_code="# Assign 10, 20, 30 to x, y, z in one line\n",
        check=lambda ns: (
            all(k in ns for k in ["x", "y", "z"]) and ns["x"] == 10 and ns["y"] == 20 and ns["z"] == 30,
            "Assign x=10, y=20, z=30 using multiple assignment"
        ),
        concepts=["multiple assignment", "unpacking"]
    ),

    make_exercise(
        id="var_06",
        title="Variable Swapping",
        topic="variables",
        difficulty=1,
        description="Swap the values of two variables `a` and `b` (a=5, b=10) so that a=10 and b=5.",
        hints=[
            "Python allows you to swap without a temporary variable",
            "Use: a, b = b, a"
        ],
        solution="a, b = 5, 10\na, b = b, a",
        starter_code="a, b = 5, 10\n# Swap the values\n",
        check=lambda ns: (
            "a" in ns and "b" in ns and ns["a"] == 10 and ns["b"] == 5,
            "After swapping, a should be 10 and b should be 5"
        ),
        concepts=["swapping", "multiple assignment"]
    ),

    make_exercise(
        id="var_07",
        title="Variable Naming Conventions",
        topic="variables",
        difficulty=1,
        description="Create variables following snake_case naming convention for a person's first name, last name, and email address.",
        hints=[
            "snake_case uses lowercase letters and underscores (no spaces or hyphens)",
            "Examples: first_name, last_name, email_address"
        ],
        solution="first_name = \"John\"\nlast_name = \"Doe\"\nemail_address = \"john.doe@example.com\"",
        starter_code="# Create variables following snake_case convention\n",
        check=lambda ns: (
            all(k in ns for k in ["first_name", "last_name", "email_address"]) and
            isinstance(ns["first_name"], str) and isinstance(ns["last_name"], str) and isinstance(ns["email_address"], str),
            "Create first_name, last_name, and email_address variables"
        ),
        concepts=["naming conventions", "strings"]
    ),

    make_exercise(
        id="var_08",
        title="Reassigning Variables",
        topic="variables",
        difficulty=1,
        description="Create a variable `count` with value 0, then reassign it to 10.",
        hints=[
            "First assignment: count = 0",
            "Then reassign: count = 10"
        ],
        solution="count = 0\ncount = 10",
        starter_code="# Create count and reassign it\n",
        check=lambda ns: (
            "count" in ns and ns["count"] == 10,
            "The final value of count should be 10"
        ),
        concepts=["reassignment", "variable mutation"]
    ),

    make_exercise(
        id="var_09",
        title="None Type Variable",
        topic="variables",
        difficulty=1,
        description="Create a variable named `result` and assign it None (representing no value).",
        hints=[
            "None is a special value (not a string, not 0, not empty)",
            "result = None"
        ],
        solution="result = None",
        starter_code="# Create a variable with None value\n",
        check=lambda ns: (
            "result" in ns and ns["result"] is None,
            "Create a variable 'result' with value None"
        ),
        concepts=["None type", "null values"]
    ),

    make_exercise(
        id="var_10",
        title="Constant Naming Convention",
        topic="variables",
        difficulty=1,
        description="Create a constant variable for the speed of light (299792458 m/s) using ALL_CAPS naming convention.",
        hints=[
            "Constants are named in ALL_CAPS with underscores",
            "Example: SPEED_OF_LIGHT = 299792458"
        ],
        solution="SPEED_OF_LIGHT = 299792458",
        starter_code="# Create a constant for speed of light\n",
        check=lambda ns: (
            "SPEED_OF_LIGHT" in ns and ns["SPEED_OF_LIGHT"] == 299792458,
            "Create SPEED_OF_LIGHT constant"
        ),
        concepts=["constants", "naming conventions"]
    ),

    # ========================
    # EASY (11-20)
    # ========================
    make_exercise(
        id="var_11",
        title="String Concatenation",
        topic="variables",
        difficulty=2,
        description="Create two string variables `greeting` and `name`, then concatenate them with a space to create a full greeting.",
        hints=[
            "Use the + operator to concatenate strings",
            "greeting + ' ' + name"
        ],
        solution="greeting = \"Hello\"\nname = \"Alice\"\nfull_greeting = greeting + ' ' + name",
        starter_code="greeting = \"Hello\"\nname = \"Alice\"\n# Concatenate them\n",
        check=lambda ns: (
            "full_greeting" in ns and ns["full_greeting"] == "Hello Alice",
            "Create full_greeting by concatenating greeting, space, and name"
        ),
        concepts=["strings", "concatenation", "operators"]
    ),

    make_exercise(
        id="var_12",
        title="Augmented Assignment (+=)",
        topic="variables",
        difficulty=2,
        description="Start with `total = 100`, then add 50 to it using the += operator.",
        hints=[
            "total += 50 is shorthand for total = total + 50",
            "Augmented assignment operators work with other operators too (*=, -=, etc.)"
        ],
        solution="total = 100\ntotal += 50",
        starter_code="total = 100\n# Add 50 using +=\n",
        check=lambda ns: (
            "total" in ns and ns["total"] == 150,
            "After using +=, total should be 150"
        ),
        concepts=["augmented assignment", "operators"]
    ),

    make_exercise(
        id="var_13",
        title="F-String Formatting",
        topic="variables",
        difficulty=2,
        description="Create variables `name` and `age`, then use an f-string to print 'Name: [name], Age: [age]'.",
        hints=[
            "F-strings use f\" \" syntax",
            "Inside f-strings, use {variable_name} to insert values"
        ],
        solution='name = \"Bob\"\nage = 30\nmessage = f\"Name: {name}, Age: {age}\"',
        starter_code="name = \"Bob\"\nage = 30\n# Use f-string to create message\n",
        check=lambda ns: (
            "message" in ns and ns["message"] == "Name: Bob, Age: 30",
            "Use f-string to format name and age"
        ),
        concepts=["f-strings", "string formatting"]
    ),

    make_exercise(
        id="var_14",
        title="Type Inference in Python",
        topic="variables",
        difficulty=2,
        description="Create three variables with different types (string, integer, float), then verify each type using the type() function.",
        hints=[
            "Python automatically infers the type based on the value",
            "You can check types later: type(variable) returns <class 'type_name'>"
        ],
        solution="text = \"hello\"\nnum_int = 42\nnum_float = 3.14\ntype_text = type(text)\ntype_int = type(num_int)\ntype_float = type(num_float)",
        starter_code="text = \"hello\"\nnum_int = 42\nnum_float = 3.14\n# Check types\n",
        check=lambda ns: (
            all(k in ns for k in ["text", "num_int", "num_float"]) and
            isinstance(ns["text"], str) and isinstance(ns["num_int"], int) and isinstance(ns["num_float"], float),
            "Create variables of different types"
        ),
        concepts=["type inference", "dynamic typing"]
    ),

    make_exercise(
        id="var_15",
        title="Variable Reassignment with Calculation",
        topic="variables",
        difficulty=2,
        description="Create a variable `price = 100`, then reassign it by adding 25% tax to it.",
        hints=[
            "25% of 100 is 25",
            "price = price + (price * 0.25) or price *= 1.25"
        ],
        solution="price = 100\nprice = price * 1.25",
        starter_code="price = 100\n# Add 25% tax\n",
        check=lambda ns: (
            "price" in ns and ns["price"] == 125.0,
            "After adding 25% tax, price should be 125"
        ),
        concepts=["reassignment", "arithmetic", "percentages"]
    ),

    make_exercise(
        id="var_16",
        title="Multi-line String Variables",
        topic="variables",
        difficulty=2,
        description="Create a variable `poem` containing a multi-line string (at least 3 lines).",
        hints=[
            "Use triple quotes for multi-line strings: \"\"\" ... \"\"\"",
            "Or use \\n escape sequence for newlines"
        ],
        solution='poem = """Line one\\nLine two\\nLine three"""',
        starter_code="# Create a multi-line string variable\n",
        check=lambda ns: (
            "poem" in ns and isinstance(ns["poem"], str) and "\n" in ns["poem"],
            "Create a multi-line string variable"
        ),
        concepts=["strings", "multi-line strings", "escape sequences"]
    ),

    make_exercise(
        id="var_17",
        title="Using Underscore as Throwaway Variable",
        topic="variables",
        difficulty=2,
        description="Unpack a tuple (5, 10) into `x` and `_` (throwaway variable), ignoring the second value.",
        hints=[
            "Use _ when you don't care about a value",
            "x, _ = 5, 10"
        ],
        solution="x, _ = 5, 10",
        starter_code="# Unpack ignoring the second value\n",
        check=lambda ns: (
            "x" in ns and ns["x"] == 5,
            "Unpack the tuple so x = 5"
        ),
        concepts=["unpacking", "throwaway variables"]
    ),

    make_exercise(
        id="var_18",
        title="Variable in Expression",
        topic="variables",
        difficulty=2,
        description="Create variables `base = 5` and `exponent = 3`, then create `result` = base^exponent (5 to the power of 3).",
        hints=[
            "Use the ** operator for exponentiation",
            "result = base ** exponent"
        ],
        solution="base = 5\nexponent = 3\nresult = base ** exponent",
        starter_code="base = 5\nexponent = 3\n# Calculate base^exponent\n",
        check=lambda ns: (
            "result" in ns and ns["result"] == 125,
            "result should be 125 (5^3)"
        ),
        concepts=["exponentiation", "operators", "expressions"]
    ),

    make_exercise(
        id="var_19",
        title="Real-World: Restaurant Bill",
        topic="variables",
        difficulty=2,
        description="Create variables for a restaurant bill: `subtotal = 50`, `tax_rate = 0.1`, `tip_pct = 0.15`, then calculate the final total including tax and tip.",
        hints=[
            "Total = subtotal + tax + tip",
            "tax = subtotal * tax_rate; tip = subtotal * tip_pct"
        ],
        solution="subtotal = 50\ntax_rate = 0.1\ntip_pct = 0.15\ntax = subtotal * tax_rate\ntip = subtotal * tip_pct\ntotal = subtotal + tax + tip",
        starter_code="subtotal = 50\ntax_rate = 0.1\ntip_pct = 0.15\n# Calculate total\n",
        check=lambda ns: (
            "total" in ns and abs(ns["total"] - 62.5) < 0.01,
            "Total should be 62.5 (50 + 5 + 7.5)"
        ),
        concepts=["arithmetic", "real-world scenarios", "financial calculations"]
    ),

    make_exercise(
        id="var_20",
        title="Real-World: Temperature Conversion",
        topic="variables",
        difficulty=2,
        description="Create a variable `celsius = 25`, then calculate and store `fahrenheit` using the formula: F = (C × 9/5) + 32.",
        hints=[
            "The formula is: fahrenheit = (celsius * 9/5) + 32",
            "25°C should be 77°F"
        ],
        solution="celsius = 25\nfahrenheit = (celsius * 9/5) + 32",
        starter_code="celsius = 25\n# Convert to Fahrenheit\n",
        check=lambda ns: (
            "fahrenheit" in ns and ns["fahrenheit"] == 77.0,
            "25°C should convert to 77°F"
        ),
        concepts=["arithmetic", "formulas", "real-world scenarios"]
    ),

    # ========================
    # MEDIUM (21-35)
    # ========================
    make_exercise(
        id="var_21",
        title="String Methods on Variables",
        topic="variables",
        difficulty=3,
        description="Create a variable `text = \"python\"` and use string methods to create `upper_text` (uppercase) and `title_text` (title case).",
        hints=[
            "String methods: .upper(), .title(), .lower()",
            "Example: upper_text = text.upper()"
        ],
        solution="text = \"python\"\nupper_text = text.upper()\ntitle_text = text.title()",
        starter_code="text = \"python\"\n# Create uppercase and title case versions\n",
        check=lambda ns: (
            all(k in ns for k in ["upper_text", "title_text"]) and
            ns["upper_text"] == "PYTHON" and ns["title_text"] == "Python",
            "Use string methods to create uppercase and title versions"
        ),
        concepts=["string methods", "method calls"]
    ),

    make_exercise(
        id="var_22",
        title="List Variable with Multiple Elements",
        topic="variables",
        difficulty=3,
        description="Create a list variable `fruits = [\"apple\", \"banana\", \"cherry\"]` and access the first and last elements.",
        hints=[
            "Lists use square brackets: [element1, element2, ...]",
            "Index 0 is first, -1 is last"
        ],
        solution="fruits = [\"apple\", \"banana\", \"cherry\"]\nfirst = fruits[0]\nlast = fruits[-1]",
        starter_code="fruits = [\"apple\", \"banana\", \"cherry\"]\n# Access first and last\n",
        check=lambda ns: (
            all(k in ns for k in ["first", "last"]) and
            ns["first"] == "apple" and ns["last"] == "cherry",
            "first should be 'apple', last should be 'cherry'"
        ),
        concepts=["lists", "indexing", "sequences"]
    ),

    make_exercise(
        id="var_23",
        title="Dictionary Variable Access",
        topic="variables",
        difficulty=3,
        description="Create a dictionary `person = {\"name\": \"Alice\", \"age\": 30, \"city\": \"NYC\"}` and access the values for name and age.",
        hints=[
            "Dictionaries use curly braces: {key: value, ...}",
            "Access values: dict_var[\"key\"]"
        ],
        solution="person = {\"name\": \"Alice\", \"age\": 30, \"city\": \"NYC\"}\nname = person[\"name\"]\nage = person[\"age\"]",
        starter_code="person = {\"name\": \"Alice\", \"age\": 30, \"city\": \"NYC\"}\n# Access name and age\n",
        check=lambda ns: (
            all(k in ns for k in ["name", "age"]) and
            ns["name"] == "Alice" and ns["age"] == 30,
            "Extract name and age from dictionary"
        ),
        concepts=["dictionaries", "key-value pairs", "data structures"]
    ),

    make_exercise(
        id="var_24",
        title="Variable Scope: Global vs Local",
        topic="variables",
        difficulty=3,
        description="Create a global variable `global_var = 10`, then create a function that creates a local variable `local_var = 20` and returns their sum.",
        hints=[
            "Global variables exist outside functions",
            "Local variables exist only inside functions"
        ],
        solution="global_var = 10\ndef add_vars():\n    local_var = 20\n    return global_var + local_var\nresult = add_vars()",
        function_name="add_vars",
        test_cases=[
            ((), 30, "add_vars() should return 30")
        ],
        starter_code="global_var = 10\ndef add_vars():\n    # Create local variable and sum with global\n    pass\n",
        concepts=["scope", "global variables", "local variables", "functions"]
    ),

    make_exercise(
        id="var_25",
        title="Variable Shadowing",
        topic="variables",
        difficulty=3,
        description="Create a global variable `x = 5`, then create a function that creates a local variable `x = 10` and returns it (shadowing the global).",
        hints=[
            "Shadowing occurs when a local variable has the same name as a global",
            "Inside the function, the local x 'shadows' the global x"
        ],
        solution="x = 5\ndef shadow_test():\n    x = 10\n    return x\nresult = shadow_test()",
        function_name="shadow_test",
        test_cases=[
            ((), 10, "Should return 10 (local shadowing global)")
        ],
        starter_code="x = 5\ndef shadow_test():\n    # Create local x that shadows global\n    pass\n",
        concepts=["scope", "shadowing", "variable conflict"]
    ),

    make_exercise(
        id="var_26",
        title="Augmented Assignment with Strings",
        topic="variables",
        difficulty=3,
        description="Start with `text = \"Hello\"`, then use += to append \" World\" to it.",
        hints=[
            "The += operator works with strings to concatenate",
            "text += \" World\" appends to the existing string"
        ],
        solution="text = \"Hello\"\ntext += \" World\"",
        starter_code="text = \"Hello\"\n# Append using +=\n",
        check=lambda ns: (
            "text" in ns and ns["text"] == "Hello World",
            "text should be 'Hello World' after appending"
        ),
        concepts=["augmented assignment", "string concatenation"]
    ),

    make_exercise(
        id="var_27",
        title="Multiple Operations with Variables",
        topic="variables",
        difficulty=3,
        description="Create variables for a store: `item_price = 25`, `quantity = 4`, then calculate `subtotal`, then add `discount = 0.1` (10% off), and store final `price`.",
        hints=[
            "subtotal = item_price * quantity",
            "discount_amount = subtotal * discount; price = subtotal - discount_amount"
        ],
        solution="item_price = 25\nquantity = 4\nsubtotal = item_price * quantity\ndiscount = 0.1\ndiscount_amount = subtotal * discount\nprice = subtotal - discount_amount",
        starter_code="item_price = 25\nquantity = 4\n# Calculate with discount\n",
        check=lambda ns: (
            all(k in ns for k in ["subtotal", "price"]) and
            ns["subtotal"] == 100 and ns["price"] == 90,
            "subtotal=100, price=90 after 10% discount"
        ),
        concepts=["arithmetic", "multi-step calculations"]
    ),

    make_exercise(
        id="var_28",
        title="Dynamic Type Change",
        topic="variables",
        difficulty=3,
        description="Create a variable `value = \"123\"` (string), then reassign it to the integer 123, showing Python's dynamic typing.",
        hints=[
            "Python allows a variable to change types",
            "Use int(value) to convert or reassign directly"
        ],
        solution="value = \"123\"\nvalue = int(value)",
        starter_code="value = \"123\"\n# Convert to integer\n",
        check=lambda ns: (
            "value" in ns and isinstance(ns["value"], int) and ns["value"] == 123,
            "value should be integer 123"
        ),
        concepts=["dynamic typing", "type conversion"]
    ),

    make_exercise(
        id="var_29",
        title="Boolean Expression Result",
        topic="variables",
        difficulty=3,
        description="Create variables `a = 10` and `b = 5`, then create a boolean variable `is_greater = a > b` that stores the result of the comparison.",
        hints=[
            "Comparison operators: >, <, ==, !=, >=, <=",
            "is_greater = a > b will be True"
        ],
        solution="a = 10\nb = 5\nis_greater = a > b",
        starter_code="a = 10\nb = 5\n# Create boolean variable from comparison\n",
        check=lambda ns: (
            "is_greater" in ns and ns["is_greater"] is True,
            "is_greater should be True"
        ),
        concepts=["booleans", "comparisons", "operators"]
    ),

    make_exercise(
        id="var_30",
        title="F-String with Expressions",
        topic="variables",
        difficulty=3,
        description="Create variables `width = 10` and `height = 20`, then use an f-string to display 'Area: [calculated area]'.",
        hints=[
            "F-strings can contain expressions inside curly braces",
            "f\"Area: {width * height}\""
        ],
        solution="width = 10\nheight = 20\narea_message = f\"Area: {width * height}\"",
        starter_code="width = 10\nheight = 20\n# Use f-string with calculation\n",
        check=lambda ns: (
            "area_message" in ns and ns["area_message"] == "Area: 200",
            "area_message should be 'Area: 200'"
        ),
        concepts=["f-strings", "expressions", "formatting"]
    ),

    make_exercise(
        id="var_31",
        title="Tuple Unpacking with Rest",
        topic="variables",
        difficulty=3,
        description="Unpack the tuple (1, 2, 3, 4, 5) where `first = 1`, `second = 2`, and `rest = [3, 4, 5]` using * unpacking.",
        hints=[
            "Use the * operator to capture remaining elements",
            "first, second, *rest = (1, 2, 3, 4, 5)"
        ],
        solution="first, second, *rest = (1, 2, 3, 4, 5)",
        starter_code="# Unpack with * to capture rest\n",
        check=lambda ns: (
            all(k in ns for k in ["first", "second", "rest"]) and
            ns["first"] == 1 and ns["second"] == 2 and ns["rest"] == [3, 4, 5],
            "Unpack with rest pattern"
        ),
        concepts=["unpacking", "variadic unpacking", "advanced assignment"]
    ),

    make_exercise(
        id="var_32",
        title="Variable Swap Advanced",
        topic="variables",
        difficulty=3,
        description="Given three variables `a = 1`, `b = 2`, `c = 3`, rotate their values so that a=2, b=3, c=1.",
        hints=[
            "Multiple assignment allows rotation: a, b, c = b, c, a",
            "This shifts each value one position"
        ],
        solution="a, b, c = 1, 2, 3\na, b, c = b, c, a",
        starter_code="a, b, c = 1, 2, 3\n# Rotate values\n",
        check=lambda ns: (
            all(k in ns for k in ["a", "b", "c"]) and
            ns["a"] == 2 and ns["b"] == 3 and ns["c"] == 1,
            "After rotation: a=2, b=3, c=1"
        ),
        concepts=["multiple assignment", "rotation", "swapping"]
    ),

    make_exercise(
        id="var_33",
        title="Real-World: User Profile",
        topic="variables",
        difficulty=3,
        description="Create a user profile with variables: `first_name`, `last_name`, `email`, `age`, then use an f-string to create a profile summary.",
        hints=[
            "Combine multiple variables of different types",
            "Use f-string to format: f\"User: {first_name} {last_name}, Email: {email}, Age: {age}\""
        ],
        solution="first_name = \"John\"\nlast_name = \"Smith\"\nemail = \"john@example.com\"\nage = 28\nprofile = f\"User: {first_name} {last_name}, Email: {email}, Age: {age}\"",
        starter_code="# Create user profile variables\n",
        check=lambda ns: (
            "profile" in ns and "John" in ns["profile"] and "Smith" in ns["profile"] and "28" in ns["profile"],
            "Create a formatted profile summary"
        ),
        concepts=["multiple variables", "f-strings", "real-world scenarios"]
    ),

    make_exercise(
        id="var_34",
        title="Real-World: BMI Calculator",
        topic="variables",
        difficulty=3,
        description="Calculate BMI with variables: `weight_kg = 70`, `height_m = 1.75`. BMI = weight / (height²). Store in `bmi` variable.",
        hints=[
            "BMI formula: bmi = weight_kg / (height_m ** 2)",
            "Result should be approximately 22.86"
        ],
        solution="weight_kg = 70\nheight_m = 1.75\nbmi = weight_kg / (height_m ** 2)",
        starter_code="weight_kg = 70\nheight_m = 1.75\n# Calculate BMI\n",
        check=lambda ns: (
            "bmi" in ns and abs(ns["bmi"] - 22.857) < 0.01,
            "BMI should be approximately 22.86"
        ),
        concepts=["arithmetic", "formulas", "real-world scenarios"]
    ),

    make_exercise(
        id="var_35",
        title="Constants and Reuse",
        topic="variables",
        difficulty=3,
        description="Define mathematical constants `PI = 3.14159` and `E = 2.71828`, then use them to calculate `circle_area = PI * 5**2` and `exponential_e = E**2`.",
        hints=[
            "Define constants in ALL_CAPS",
            "Reuse them in multiple calculations"
        ],
        solution="PI = 3.14159\nE = 2.71828\ncircle_area = PI * 5**2\nexponential_e = E**2",
        starter_code="PI = 3.14159\nE = 2.71828\n# Use constants\n",
        check=lambda ns: (
            all(k in ns for k in ["circle_area", "exponential_e"]) and
            abs(ns["circle_area"] - 78.53975) < 0.01 and abs(ns["exponential_e"] - 7.3890) < 0.01,
            "Calculate with mathematical constants"
        ),
        concepts=["constants", "reuse", "arithmetic"]
    ),

    # ========================
    # HARD (36-45)
    # ========================
    make_exercise(
        id="var_36",
        title="List Comprehension Assignment",
        topic="variables",
        difficulty=4,
        description="Create a variable `squares` that stores squares of numbers 1-5 using list comprehension: [1, 4, 9, 16, 25].",
        hints=[
            "List comprehension syntax: [expression for item in iterable]",
            "[x**2 for x in range(1, 6)]"
        ],
        solution="squares = [x**2 for x in range(1, 6)]",
        starter_code="# Create list of squares using comprehension\n",
        check=lambda ns: (
            "squares" in ns and ns["squares"] == [1, 4, 9, 16, 25],
            "squares should be [1, 4, 9, 16, 25]"
        ),
        concepts=["list comprehension", "advanced assignment"]
    ),

    make_exercise(
        id="var_37",
        title="Dictionary from Variables",
        topic="variables",
        difficulty=4,
        description="Create variables `keys = [\"a\", \"b\", \"c\"]` and `values = [1, 2, 3]`, then create a dictionary `my_dict = {\"a\": 1, \"b\": 2, \"c\": 3}` using dict() or dict comprehension.",
        hints=[
            "Use zip() to pair keys and values: dict(zip(keys, values))",
            "Or use dict comprehension: {k: v for k, v in zip(keys, values)}"
        ],
        solution="keys = [\"a\", \"b\", \"c\"]\nvalues = [1, 2, 3]\nmy_dict = dict(zip(keys, values))",
        starter_code="keys = [\"a\", \"b\", \"c\"]\nvalues = [1, 2, 3]\n# Create dictionary\n",
        check=lambda ns: (
            "my_dict" in ns and ns["my_dict"] == {"a": 1, "b": 2, "c": 3},
            "my_dict should map keys to values"
        ),
        concepts=["dictionaries", "zip", "advanced data structures"]
    ),

    make_exercise(
        id="var_38",
        title="Mutable vs Immutable: List Assignment",
        topic="variables",
        difficulty=4,
        description="Create a list `original = [1, 2, 3]`, assign it to `copy = original`, then modify copy to [1, 2, 3, 4]. Show that both reference the same list.",
        hints=[
            "Lists are mutable and share references",
            "copy = original doesn't make a new list, it makes another reference"
        ],
        solution="original = [1, 2, 3]\ncopy = original\ncopy.append(4)\nsame_reference = original is copy",
        starter_code="original = [1, 2, 3]\ncopy = original\n# Modify and check\n",
        check=lambda ns: (
            all(k in ns for k in ["original", "copy"]) and
            ns["original"] == [1, 2, 3, 4] and ns["copy"] == [1, 2, 3, 4] and ns["original"] is ns["copy"],
            "Both original and copy should refer to same list"
        ),
        concepts=["mutability", "references", "object identity"]
    ),

    make_exercise(
        id="var_39",
        title="Mutable vs Immutable: String Assignment",
        topic="variables",
        difficulty=4,
        description="Create a string `original = \"hello\"`, assign it to `copy = original`, then try to modify copy (strings are immutable, so create a new string).",
        hints=[
            "Strings are immutable, so reassignment creates a new object",
            "copy = original + \" world\" creates a new string"
        ],
        solution="original = \"hello\"\ncopy = original\ncopy = copy + \" world\"\nsame_reference = original is copy",
        starter_code="original = \"hello\"\ncopy = original\n# Modify and check\n",
        check=lambda ns: (
            all(k in ns for k in ["original", "copy"]) and
            ns["original"] == "hello" and ns["copy"] == "hello world" and ns["original"] is not ns["copy"],
            "original and copy should be different objects"
        ),
        concepts=["immutability", "references", "object identity"]
    ),

    make_exercise(
        id="var_40",
        title="Nested Data Structure Assignment",
        topic="variables",
        difficulty=4,
        description="Create a nested dictionary `student = {\"name\": \"Alice\", \"grades\": {\"math\": 95, \"english\": 88}}` and access nested values.",
        hints=[
            "Nested structures: student[\"grades\"][\"math\"]",
            "Dictionaries inside dictionaries"
        ],
        solution="student = {\"name\": \"Alice\", \"grades\": {\"math\": 95, \"english\": 88}}\nmath_grade = student[\"grades\"][\"math\"]\nenglish_grade = student[\"grades\"][\"english\"]",
        starter_code="student = {\"name\": \"Alice\", \"grades\": {\"math\": 95, \"english\": 88}}\n# Access nested values\n",
        check=lambda ns: (
            all(k in ns for k in ["math_grade", "english_grade"]) and
            ns["math_grade"] == 95 and ns["english_grade"] == 88,
            "Extract nested dictionary values"
        ),
        concepts=["nested structures", "data structures", "access patterns"]
    ),

    make_exercise(
        id="var_41",
        title="Variable with Conditional Expression",
        topic="variables",
        difficulty=4,
        description="Create a variable `score = 85`, then use a conditional expression to assign `grade = \"A\" if score >= 90 else \"B\"` (ternary operator).",
        hints=[
            "Ternary conditional: value_if_true if condition else value_if_false",
            "grade = \"A\" if score >= 90 else \"B\""
        ],
        solution="score = 85\ngrade = \"A\" if score >= 90 else \"B\"",
        starter_code="score = 85\n# Use ternary operator\n",
        check=lambda ns: (
            "grade" in ns and ns["grade"] == "B",
            "grade should be 'B' for score 85"
        ),
        concepts=["conditional expressions", "ternary operator"]
    ),

    make_exercise(
        id="var_42",
        title="Generator Expression Assignment",
        topic="variables",
        difficulty=4,
        description="Create a generator `even_numbers = (x for x in range(1, 11) if x % 2 == 0)` that yields even numbers 1-10.",
        hints=[
            "Generator comprehension uses parentheses: (expression for ...)",
            "Similar to list comprehension but lazy (doesn't compute all at once)"
        ],
        solution="even_numbers = (x for x in range(1, 11) if x % 2 == 0)",
        starter_code="# Create a generator expression\n",
        check=lambda ns: (
            "even_numbers" in ns and list(ns["even_numbers"]) == [2, 4, 6, 8, 10],
            "Generator should yield [2, 4, 6, 8, 10]"
        ),
        concepts=["generators", "comprehensions", "lazy evaluation"]
    ),

    make_exercise(
        id="var_43",
        title="Real-World: Invoice with Multiple Variables",
        topic="variables",
        difficulty=4,
        description="Create an invoice: `items = [(\"Widget\", 10, 5), (\"Gadget\", 15, 2)]` (name, price, qty), calculate `total`, add `tax = 0.08`, and final `invoice_total`.",
        hints=[
            "items is a list of tuples",
            "total = sum(price * qty for each item); invoice_total = total * (1 + tax)"
        ],
        solution="items = [(\"Widget\", 10, 5), (\"Gadget\", 15, 2)]\ntotal = sum(price * qty for name, price, qty in items)\ntax = 0.08\ninvoice_total = total * (1 + tax)",
        starter_code="items = [(\"Widget\", 10, 5), (\"Gadget\", 15, 2)]\n# Calculate invoice\n",
        check=lambda ns: (
            all(k in ns for k in ["total", "invoice_total"]) and
            abs(ns["total"] - 80) < 0.01 and abs(ns["invoice_total"] - 86.4) < 0.01,
            "total=80, invoice_total=86.4"
        ),
        concepts=["real-world scenarios", "comprehensions", "calculations"]
    ),

    make_exercise(
        id="var_44",
        title="Variable Chain Assignment",
        topic="variables",
        difficulty=4,
        description="Use chain assignment to set three variables to the same value in one statement: `a = b = c = 42`.",
        hints=[
            "a = b = c = 42 assigns 42 to all three",
            "All three variables reference the same value (for immutables like int)"
        ],
        solution="a = b = c = 42",
        starter_code="# Chain assignment\n",
        check=lambda ns: (
            all(k in ns for k in ["a", "b", "c"]) and
            ns["a"] == 42 and ns["b"] == 42 and ns["c"] == 42,
            "All three should be 42"
        ),
        concepts=["chain assignment", "multiple variables"]
    ),

    make_exercise(
        id="var_45",
        title="Real-World: Weather Data Analysis",
        topic="variables",
        difficulty=4,
        description="Store daily temps: `temps = [72, 75, 68, 70, 73]`, then calculate `avg_temp`, `max_temp`, `min_temp`, and create a summary f-string.",
        hints=[
            "Use sum(), len(), max(), min() functions",
            "avg_temp = sum(temps) / len(temps)"
        ],
        solution="temps = [72, 75, 68, 70, 73]\navg_temp = sum(temps) / len(temps)\nmax_temp = max(temps)\nmin_temp = min(temps)\nsummary = f\"Avg: {avg_temp:.1f}, Max: {max_temp}, Min: {min_temp}\"",
        starter_code="temps = [72, 75, 68, 70, 73]\n# Analyze temperature data\n",
        check=lambda ns: (
            all(k in ns for k in ["avg_temp", "max_temp", "min_temp"]) and
            abs(ns["avg_temp"] - 71.6) < 0.1 and ns["max_temp"] == 75 and ns["min_temp"] == 68,
            "Calculate statistics correctly"
        ),
        concepts=["data analysis", "built-in functions", "aggregation"]
    ),

    # ========================
    # CHALLENGE (46-50)
    # ========================
    make_exercise(
        id="var_46",
        title="Global Keyword and Modification",
        topic="variables",
        difficulty=5,
        description="Create a global variable `counter = 0`, then create a function that uses the `global` keyword to increment it.",
        hints=[
            "Use `global variable_name` inside a function to modify global scope",
            "Without global, assignment creates a local variable"
        ],
        solution="counter = 0\ndef increment():\n    global counter\n    counter += 1\n    return counter",
        function_name="increment",
        test_cases=[
            ((), 1, "First call should return 1")
        ],
        starter_code="counter = 0\ndef increment():\n    # Use global to modify counter\n    pass\n",
        concepts=["global keyword", "scope modification", "state management"]
    ),

    make_exercise(
        id="var_47",
        title="Unpacking Nested Structures",
        topic="variables",
        difficulty=5,
        description="Unpack nested tuples: `data = ((1, 2), (3, 4))` to extract `a=1, b=2, c=3, d=4` in a single unpacking statement.",
        hints=[
            "Use nested unpacking: (a, b), (c, d) = data",
            "Each level can be unpacked independently"
        ],
        solution="data = ((1, 2), (3, 4))\n(a, b), (c, d) = data",
        starter_code="data = ((1, 2), (3, 4))\n# Unpack nested tuples\n",
        check=lambda ns: (
            all(k in ns for k in ["a", "b", "c", "d"]) and
            ns["a"] == 1 and ns["b"] == 2 and ns["c"] == 3 and ns["d"] == 4,
            "Unpack all values correctly"
        ),
        concepts=["nested unpacking", "advanced assignment", "destructuring"]
    ),

    make_exercise(
        id="var_48",
        title="Advanced: String Format Method",
        topic="variables",
        difficulty=5,
        description="Create variables `name = \"Bob\"`, `age = 25`, and use the `.format()` method with variable substitution: `\"My name is {} and I am {} years old\".format(name, age)`.",
        hints=[
            "The .format() method uses curly braces {} as placeholders",
            "Values are passed as arguments: .format(arg1, arg2, ...)"
        ],
        solution="name = \"Bob\"\nage = 25\nmessage = \"My name is {} and I am {} years old\".format(name, age)",
        starter_code="name = \"Bob\"\nage = 25\n# Use .format() method\n",
        check=lambda ns: (
            "message" in ns and ns["message"] == "My name is Bob and I am 25 years old",
            "Format string correctly"
        ),
        concepts=["string methods", "formatting", ".format()"]
    ),

    make_exercise(
        id="var_49",
        title="Real-World: Portfolio Calculation",
        topic="variables",
        difficulty=5,
        description="Simulate a portfolio: `holdings = {\"AAPL\": (150, 30), \"MSFT\": (300, 20)}` (price, shares), calculate total value of each holding and total portfolio.",
        hints=[
            "holdings structure: symbol -> (price, shares)",
            "Use dict comprehension or loops to calculate values"
        ],
        solution="holdings = {\"AAPL\": (150, 30), \"MSFT\": (300, 20)}\nvalues = {symbol: price * shares for symbol, (price, shares) in holdings.items()}\nportfolio_total = sum(values.values())",
        starter_code="holdings = {\"AAPL\": (150, 30), \"MSFT\": (300, 20)}\n# Calculate portfolio value\n",
        check=lambda ns: (
            all(k in ns for k in ["values", "portfolio_total"]) and
            ns["portfolio_total"] == 10500,
            "portfolio_total = 4500 + 6000 = 10500"
        ),
        concepts=["real-world scenarios", "dict comprehension", "complex calculations"]
    ),

    make_exercise(
        id="var_50",
        title="Comprehension with Conditional: Challenge",
        topic="variables",
        difficulty=5,
        description="Create a variable `result` that is a dictionary of numbers and their squares, but only for numbers 1-10 where the square is > 25: `{6: 36, 7: 49, 8: 64, ..., 10: 100}`.",
        hints=[
            "Use dict comprehension: {x: x**2 for x in range(1, 11) if x**2 > 25}",
            "Apply both iteration and filtering in one comprehension"
        ],
        solution="result = {x: x**2 for x in range(1, 11) if x**2 > 25}",
        starter_code="# Create dict comprehension with condition\n",
        check=lambda ns: (
            "result" in ns and ns["result"] == {6: 36, 7: 49, 8: 64, 9: 81, 10: 100},
            "result should contain squares > 25"
        ),
        concepts=["dict comprehension", "conditionals", "advanced filtering"]
    ),
]
