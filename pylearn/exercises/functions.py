"""50 exercises on Python functions."""

from .base import make_exercise

exercises = [
    # BEGINNER (1-10): Basic function definition, parameters, return values
    make_exercise(
        id="func_01",
        title="Define a Simple Function",
        topic="functions",
        difficulty=1,
        description="Define a function named `greet` that takes a name parameter and returns 'Hello, {name}!'",
        hints=[
            "Use the `def` keyword to define a function",
            "Use an f-string to interpolate the name into the greeting",
        ],
        solution="def greet(name):\n    return f'Hello, {name}!'",
        function_name="greet",
        test_cases=[
            (("Alice",), "Hello, Alice!"),
            (("Bob",), "Hello, Bob!"),
            (("World",), "Hello, World!"),
        ],
        concepts=["function definition", "parameters", "return values", "f-strings"],
    ),
    make_exercise(
        id="func_02",
        title="Function with Multiple Parameters",
        topic="functions",
        difficulty=1,
        description="Define a function `add` that takes two numbers and returns their sum.",
        hints=[
            "Define the function with two parameters",
            "Use the + operator to add them",
        ],
        solution="def add(a, b):\n    return a + b",
        function_name="add",
        test_cases=[
            ((2, 3), 5),
            ((10, 20), 30),
            ((-5, 3), -2),
            ((0, 0), 0),
        ],
        concepts=["parameters", "return values", "arithmetic"],
    ),
    make_exercise(
        id="func_03",
        title="Function with No Return Value",
        topic="functions",
        difficulty=1,
        description="Define a function `print_twice` that prints a message twice. It should not return anything.",
        hints=[
            "Use `print()` twice",
            "A function without an explicit return returns None",
        ],
        solution="def print_twice(msg):\n    print(msg)\n    print(msg)",
        function_name="print_twice",
        test_cases=[
            (("Hello",), None),
            (("Test",), None),
            (("Python",), None),
        ],
        concepts=["side effects", "print", "None return"],
    ),
    make_exercise(
        id="func_04",
        title="Function Returning Boolean",
        topic="functions",
        difficulty=1,
        description="Define a function `is_even` that takes an integer and returns True if it's even, False otherwise.",
        hints=[
            "Use the modulo operator % to check if a number is divisible by 2",
            "Return True if n % 2 == 0",
        ],
        solution="def is_even(n):\n    return n % 2 == 0",
        function_name="is_even",
        test_cases=[
            ((2,), True),
            ((3,), False),
            ((0,), True),
            ((100,), True),
            ((99,), False),
        ],
        concepts=["return values", "booleans", "conditionals"],
    ),
    make_exercise(
        id="func_05",
        title="Function with Conditional Logic",
        topic="functions",
        difficulty=1,
        description="Define a function `absolute_value` that returns the absolute value of a number without using abs().",
        hints=[
            "Use an if-else statement",
            "Return -n if n < 0, otherwise return n",
        ],
        solution="def absolute_value(n):\n    if n < 0:\n        return -n\n    else:\n        return n",
        function_name="absolute_value",
        test_cases=[
            ((5,), 5),
            ((-5,), 5),
            ((0,), 0),
            ((-100,), 100),
        ],
        concepts=["conditional logic", "if-else"],
    ),
    make_exercise(
        id="func_06",
        title="Default Parameter Values",
        topic="functions",
        difficulty=1,
        description="Define a function `greet_formal` that takes a name and an optional greeting. Default greeting is 'Hello'. Example: greet_formal('Alice', 'Hi') returns 'Hi, Alice!'",
        hints=[
            "Use a default parameter with =",
            "greeting='Hello' makes greeting optional",
        ],
        solution="def greet_formal(name, greeting='Hello'):\n    return f'{greeting}, {name}!'",
        function_name="greet_formal",
        test_cases=[
            (("Alice", "Hi"), "Hi, Alice!"),
            (("Bob",), "Hello, Bob!"),
            (("Eve", "Hey"), "Hey, Eve!"),
        ],
        concepts=["default parameters", "optional arguments"],
    ),
    make_exercise(
        id="func_07",
        title="Function Returning Multiple Values",
        topic="functions",
        difficulty=1,
        description="Define a function `swap` that takes two values and returns them swapped as a tuple.",
        hints=[
            "Return a tuple with both values in reversed order",
            "Use parentheses or just comma-separate the return values",
        ],
        solution="def swap(a, b):\n    return (b, a)",
        function_name="swap",
        test_cases=[
            ((1, 2), (2, 1)),
            (("x", "y"), ("y", "x")),
            ((10, 20), (20, 10)),
        ],
        concepts=["multiple return values", "tuples"],
    ),
    make_exercise(
        id="func_08",
        title="Function with String Operations",
        topic="functions",
        difficulty=1,
        description="Define a function `reverse_string` that takes a string and returns it reversed.",
        hints=[
            "Use string slicing with [::-1]",
            "Or iterate through and build the reversed string",
        ],
        solution="def reverse_string(s):\n    return s[::-1]",
        function_name="reverse_string",
        test_cases=[
            (("hello",), "olleh"),
            (("Python",), "nohtyP"),
            (("a",), "a"),
            (("",), ""),
        ],
        concepts=["string slicing", "strings"],
    ),
    make_exercise(
        id="func_09",
        title="Function with List Operations",
        topic="functions",
        difficulty=1,
        description="Define a function `sum_list` that takes a list of numbers and returns their sum.",
        hints=[
            "Use the built-in sum() function",
            "Or iterate through the list with a for loop and accumulate",
        ],
        solution="def sum_list(numbers):\n    return sum(numbers)",
        function_name="sum_list",
        test_cases=[
            (([1, 2, 3],), 6),
            (([10, 20],), 30),
            (([-1, 1],), 0),
            ((([],), 0)),
        ],
        concepts=["lists", "iteration", "sum"],
    ),
    make_exercise(
        id="func_10",
        title="Function with Dictionary Return",
        topic="functions",
        difficulty=1,
        description="Define a function `person_dict` that takes name and age, returning a dictionary with keys 'name' and 'age'.",
        hints=[
            "Create a dictionary with {'name': name, 'age': age}",
            "Return the dictionary",
        ],
        solution="def person_dict(name, age):\n    return {'name': name, 'age': age}",
        function_name="person_dict",
        test_cases=[
            (("Alice", 30), {"name": "Alice", "age": 30}),
            (("Bob", 25), {"name": "Bob", "age": 25}),
        ],
        concepts=["dictionaries", "return values"],
    ),
    # EASY (11-20): Keyword arguments, *args, **kwargs, scope
    make_exercise(
        id="func_11",
        title="Keyword Arguments",
        topic="functions",
        difficulty=2,
        description="Define a function `describe_pet` that takes breed and name as keyword arguments and returns '{name} is a {breed}'. Must work with describe_pet(breed='dog', name='Buddy').",
        hints=[
            "Define parameters that can be passed as keyword arguments",
            "Arguments with names can be passed in any order when using keywords",
        ],
        solution="def describe_pet(breed, name):\n    return f'{name} is a {breed}'",
        function_name="describe_pet",
        test_cases=[
            (("dog", "Buddy"), "Buddy is a dog"),
            (("cat", "Whiskers"), "Whiskers is a cat"),
        ],
        concepts=["keyword arguments", "named parameters"],
    ),
    make_exercise(
        id="func_12",
        title="*args: Variable Arguments",
        topic="functions",
        difficulty=2,
        description="Define a function `multiply_all` that takes any number of arguments and returns their product.",
        hints=[
            "Use *args to capture variable positional arguments",
            "*args is a tuple, so you can iterate over it",
        ],
        solution="def multiply_all(*args):\n    result = 1\n    for n in args:\n        result *= n\n    return result",
        check=lambda ns: (
            'multiply_all' in ns and callable(ns['multiply_all']) and
            ns['multiply_all'](2, 3, 4) == 24 and
            ns['multiply_all'](5) == 5 and
            ns['multiply_all'](2, 2, 2, 2) == 16,
            "multiply_all(2, 3, 4) should return 24, multiply_all(5) should return 5, multiply_all(2, 2, 2, 2) should return 16"
        ),
        concepts=["*args", "variable arguments", "iteration"],
    ),
    make_exercise(
        id="func_13",
        title="**kwargs: Keyword Arguments Dict",
        topic="functions",
        difficulty=2,
        description="Define a function `build_query` that takes **kwargs and returns a string of 'key=value' pairs joined by '&'. Example: build_query(name='Alice', age=30) returns 'name=Alice&age=30'.",
        hints=[
            "Use **kwargs to capture keyword arguments as a dictionary",
            "Iterate over kwargs.items() to get key-value pairs",
        ],
        solution="def build_query(**kwargs):\n    pairs = [f'{k}={v}' for k, v in kwargs.items()]\n    return '&'.join(pairs)",
        check=lambda ns: (
            'build_query' in ns and callable(ns['build_query']) and
            ns['build_query']() == "" and
            ns['build_query'](name='Alice', age=30) == "name=Alice&age=30",
            "build_query() should return '', build_query(name='Alice', age=30) should return 'name=Alice&age=30'"
        ),
        concepts=["**kwargs", "keyword arguments", "dictionaries"],
    ),
    make_exercise(
        id="func_14",
        title="Combining *args and **kwargs",
        topic="functions",
        difficulty=2,
        description="Define a function `print_all` that takes *args and **kwargs, and returns a string: 'Args: {args_list}\\nKwargs: {kwargs_dict}'.",
        hints=[
            "Define both *args and **kwargs in the function signature",
            "Convert them to strings for the output",
        ],
        solution="def print_all(*args, **kwargs):\n    return f'Args: {list(args)}\\nKwargs: {kwargs}'",
        check=lambda ns: (
            'print_all' in ns and callable(ns['print_all']) and
            ns['print_all']() == "Args: []\nKwargs: {}" and
            ns['print_all'](1, 2, x=10) == "Args: [1, 2]\nKwargs: {'x': 10}",
            "print_all() should return 'Args: []\\nKwargs: {}', print_all(1, 2, x=10) should return \"Args: [1, 2]\\nKwargs: {'x': 10}\""
        ),
        concepts=["*args", "**kwargs", "combined arguments"],
    ),
    make_exercise(
        id="func_15",
        title="Scope: Local vs Global",
        topic="functions",
        difficulty=2,
        description="Define a function `modify_outer` that takes x and returns x + y where y = 5 is defined outside the function. The outer y should be accessible.",
        hints=[
            "Variables defined outside a function are in the global scope",
            "A function can read global variables directly",
        ],
        solution="def modify_outer(x):\n    y = 5\n    return x + y",
        function_name="modify_outer",
        test_cases=[
            ((10,), 15),
            ((20,), 25),
        ],
        concepts=["scope", "local variables", "function variables"],
    ),
    make_exercise(
        id="func_16",
        title="Unpacking Arguments",
        topic="functions",
        difficulty=2,
        description="Define a function `add_three` that takes three numbers and returns their sum. Test it by unpacking a list: add_three(*[1, 2, 3]).",
        hints=[
            "Define the function normally with three parameters",
            "The * operator unpacks an iterable into positional arguments",
        ],
        solution="def add_three(a, b, c):\n    return a + b + c",
        function_name="add_three",
        test_cases=[
            ((1, 2, 3), 6),
            ((10, 20, 30), 60),
        ],
        concepts=["argument unpacking", "parameter passing"],
    ),
    make_exercise(
        id="func_17",
        title="Function with Type Checking in Check",
        topic="functions",
        difficulty=2,
        description="Write a function `is_positive_number` that checks if input is a number > 0.",
        hints=[
            "Use isinstance() to check if the value is int or float",
            "Check if the value is greater than 0",
        ],
        solution="def is_positive_number(x):\n    return isinstance(x, (int, float)) and x > 0",
        function_name="is_positive_number",
        test_cases=[
            ((5,), True),
            ((0,), False),
            ((-3,), False),
            ((3.5,), True),
        ],
        concepts=["type checking", "isinstance"],
    ),
    make_exercise(
        id="func_18",
        title="Function Returning Function Result",
        topic="functions",
        difficulty=2,
        description="Define `call_twice` that takes a function and a value, calls the function twice on the value, and returns the final result. Example: call_twice(lambda x: x * 2, 3) should return 12.",
        hints=[
            "Call the function once to get an intermediate result",
            "Call the function again with the intermediate result",
        ],
        solution="def call_twice(func, x):\n    x = func(x)\n    return func(x)",
        check=lambda ns: (
            'call_twice' in ns and callable(ns['call_twice']) and
            ns['call_twice'](lambda x: x * 2, 3) == 12 and
            ns['call_twice'](lambda x: x + 1, 5) == 7,
            "call_twice(lambda x: x * 2, 3) should return 12, call_twice(lambda x: x + 1, 5) should return 7"
        ),
        concepts=["higher-order functions", "function arguments"],
    ),
    make_exercise(
        id="func_19",
        title="List Comprehension with Function",
        topic="functions",
        difficulty=2,
        description="Define a function `square_even_numbers` that takes a list and returns a list of squares of only the even numbers.",
        hints=[
            "Use a list comprehension with a condition",
            "Check if n % 2 == 0 to filter even numbers",
        ],
        solution="def square_even_numbers(numbers):\n    return [n**2 for n in numbers if n % 2 == 0]",
        function_name="square_even_numbers",
        test_cases=[
            (([1, 2, 3, 4, 5, 6],), [4, 16, 36]),
            (([2, 4, 6],), [4, 16, 36]),
        ],
        concepts=["list comprehension", "filtering", "lambda"],
    ),
    make_exercise(
        id="func_20",
        title="Docstring and Help",
        topic="functions",
        difficulty=2,
        description="Define a function `divide` that takes two numbers and returns a / b. Include a docstring: 'Return a divided by b.'",
        hints=[
            "Add a docstring as the first line inside the function",
            "Use triple quotes for docstrings",
        ],
        solution='def divide(a, b):\n    """Return a divided by b."""\n    return a / b',
        function_name="divide",
        test_cases=[
            ((10, 2), 5.0),
            ((15, 3), 5.0),
        ],
        concepts=["docstrings", "documentation"],
    ),
    # MEDIUM (21-35): Lambda, closures, decorators, recursion
    make_exercise(
        id="func_21",
        title="Lambda Functions",
        topic="functions",
        difficulty=3,
        description="Use `map()` with a lambda to square all numbers in a list [1, 2, 3, 4]. Return as a list.",
        hints=[
            "Lambda syntax: lambda x: x**2",
            "map() returns an iterator, convert to list",
        ],
        solution="def square_with_map(numbers):\n    return list(map(lambda x: x**2, numbers))",
        function_name="square_with_map",
        test_cases=[
            (([1, 2, 3, 4],), [1, 4, 9, 16]),
            (([5, 10],), [25, 100]),
        ],
        concepts=["lambda functions", "map", "functional programming"],
    ),
    make_exercise(
        id="func_22",
        title="Filter with Lambda",
        topic="functions",
        difficulty=3,
        description="Use `filter()` with a lambda to keep only words longer than 3 characters from a list.",
        hints=[
            "Lambda syntax: lambda word: len(word) > 3",
            "filter() returns an iterator, convert to list",
        ],
        solution="def filter_long_words(words):\n    return list(filter(lambda word: len(word) > 3, words))",
        function_name="filter_long_words",
        test_cases=[
            ((["cat", "elephant", "dog", "ant"],), ["elephant"]),
            ((["hi", "hello", "hey", "python"],), ["hello", "python"]),
        ],
        concepts=["filter", "lambda", "functional programming"],
    ),
    make_exercise(
        id="func_23",
        title="Reduce with Lambda",
        topic="functions",
        difficulty=3,
        description="Use `functools.reduce()` with a lambda to multiply all numbers in a list [2, 3, 4].",
        hints=[
            "Import reduce from functools",
            "Lambda syntax: lambda a, b: a * b",
        ],
        solution="from functools import reduce\ndef multiply_list(numbers):\n    return reduce(lambda a, b: a * b, numbers)",
        function_name="multiply_list",
        test_cases=[
            (([2, 3, 4],), 24),
            (([5, 2],), 10),
        ],
        concepts=["reduce", "lambda", "functools"],
    ),
    make_exercise(
        id="func_24",
        title="Closure: Inner Function",
        topic="functions",
        difficulty=3,
        description="Define a function `make_adder` that takes x and returns a function that adds x to any number. Example: add_5 = make_adder(5); add_5(3) returns 8.",
        hints=[
            "Define an inner function inside make_adder",
            "The inner function uses the outer function's variable x",
        ],
        solution="def make_adder(x):\n    def adder(y):\n        return x + y\n    return adder",
        check=lambda ns: (
            'make_adder' in ns and callable(ns['make_adder']) and
            ns['make_adder'](5)(3) == 8 and
            ns['make_adder'](10)(20) == 30,
            "make_adder(5)(3) should return 8, make_adder(10)(20) should return 30"
        ),
        concepts=["closures", "nested functions", "lexical scope"],
    ),
    make_exercise(
        id="func_25",
        title="Closure with Counter",
        topic="functions",
        difficulty=3,
        description="Define a function `make_counter` that returns a function that increments and returns a counter each time it's called.",
        hints=[
            "Use a nonlocal variable to modify the counter in the outer scope",
            "Return the inner function",
        ],
        solution="def make_counter():\n    count = 0\n    def increment():\n        nonlocal count\n        count += 1\n        return count\n    return increment",
        check=lambda ns: (
            'make_counter' in ns and callable(ns['make_counter']) and
            (lambda c: c() == 1 and c() == 2 and c() == 3)(ns['make_counter']()),
            "make_counter() should return a function that increments: first call returns 1, second returns 2, third returns 3"
        ),
        concepts=["closures", "nonlocal", "state management"],
    ),
    make_exercise(
        id="func_26",
        title="Simple Decorator",
        topic="functions",
        difficulty=3,
        description="Write a decorator `add_exclamation` that wraps a function and adds '!' to its return value. Apply it to a function that returns 'hello'.",
        hints=[
            "A decorator is a function that takes a function and returns a modified function",
            "Use def decorator(func): ... return wrapper",
        ],
        solution="def add_exclamation(func):\n    def wrapper(*args, **kwargs):\n        result = func(*args, **kwargs)\n        return result + '!'\n    return wrapper",
        check=lambda ns: (
            'add_exclamation' in ns and callable(ns['add_exclamation']) and
            ns['add_exclamation'](lambda: 'hello')() == 'hello!',
            "add_exclamation should return a decorator that adds '!' to the result"
        ),
        concepts=["decorators", "higher-order functions", "function wrapping"],
    ),
    make_exercise(
        id="func_27",
        title="Decorator with Arguments",
        topic="functions",
        difficulty=3,
        description="Write a decorator `repeat` that takes n and repeats a function's return value n times. Example: @repeat(3) on func returning 'hi' would return 'hihihi'.",
        hints=[
            "Use nested functions: decorator(n) returns a decorator that takes func",
            "The innermost function is the actual wrapper",
        ],
        solution="def repeat(n):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            return func(*args, **kwargs) * n\n        return wrapper\n    return decorator",
        check=lambda ns: (
            'repeat' in ns and callable(ns['repeat']) and
            ns['repeat'](3)(lambda: 'hi')() == 'hihihi',
            "repeat(3) should return a decorator that repeats the function result 3 times"
        ),
        concepts=["decorators with arguments", "nested decorators"],
    ),
    make_exercise(
        id="func_28",
        title="Recursive Function: Factorial",
        topic="functions",
        difficulty=3,
        description="Define a function `factorial` that computes n! recursively. 5! = 5 * 4 * 3 * 2 * 1 = 120.",
        hints=[
            "Base case: factorial(0) = 1 or factorial(1) = 1",
            "Recursive case: factorial(n) = n * factorial(n-1)",
        ],
        solution="def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)",
        function_name="factorial",
        test_cases=[
            ((0,), 1),
            ((1,), 1),
            ((5,), 120),
            ((6,), 720),
        ],
        concepts=["recursion", "base case", "recursive calls"],
    ),
    make_exercise(
        id="func_29",
        title="Recursive Function: Fibonacci",
        topic="functions",
        difficulty=3,
        description="Define a function `fibonacci` that returns the nth Fibonacci number recursively. fibonacci(5) = 5.",
        hints=[
            "Base cases: fib(0) = 0, fib(1) = 1",
            "Recursive case: fib(n) = fib(n-1) + fib(n-2)",
        ],
        solution="def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)",
        function_name="fibonacci",
        test_cases=[
            ((0,), 0),
            ((1,), 1),
            ((5,), 5),
            ((6,), 8),
        ],
        concepts=["recursion", "fibonacci"],
    ),
    make_exercise(
        id="func_30",
        title="Recursive Function: Power",
        topic="functions",
        difficulty=3,
        description="Define a function `power` that computes x^n recursively without using **.",
        hints=[
            "Base case: power(x, 0) = 1",
            "Recursive case: power(x, n) = x * power(x, n-1)",
        ],
        solution="def power(x, n):\n    if n == 0:\n        return 1\n    return x * power(x, n - 1)",
        function_name="power",
        test_cases=[
            ((2, 0), 1),
            ((2, 3), 8),
            ((3, 4), 81),
        ],
        concepts=["recursion", "exponentiation"],
    ),
    make_exercise(
        id="func_31",
        title="Generator Function: Simple",
        topic="functions",
        difficulty=3,
        description="Define a generator function `count_up` that yields numbers from 1 to n (inclusive).",
        hints=[
            "Use the `yield` keyword to make it a generator",
            "yield produces values one at a time",
        ],
        solution="def count_up(n):\n    i = 1\n    while i <= n:\n        yield i\n        i += 1",
        check=lambda ns: (
            'count_up' in ns and callable(ns['count_up']) and
            list(ns['count_up'](3)) == [1, 2, 3] and
            list(ns['count_up'](5)) == [1, 2, 3, 4, 5],
            "count_up(3) should yield [1, 2, 3], count_up(5) should yield [1, 2, 3, 4, 5]"
        ),
        concepts=["generators", "yield", "iterators"],
    ),
    make_exercise(
        id="func_32",
        title="Generator Expression",
        topic="functions",
        difficulty=3,
        description="Use a generator expression (like list comprehension but with parens) to generate squares of numbers 1-5. Convert to list.",
        hints=[
            "Syntax: (x**2 for x in range(1, 6))",
            "Convert to list with list()",
        ],
        solution="def squares_generator():\n    return list(x**2 for x in range(1, 6))",
        function_name="squares_generator",
        test_cases=[
            ((), [1, 4, 9, 16, 25]),
        ],
        concepts=["generators", "generator expressions"],
    ),
    make_exercise(
        id="func_33",
        title="Type Hints: Basic",
        topic="functions",
        difficulty=3,
        description="Define a function `add_numbers(a: int, b: int) -> int:` that adds two integers and returns an int.",
        hints=[
            "Use : type for parameters and -> type for return",
            "Type hints are for documentation, not enforcement",
        ],
        solution="def add_numbers(a: int, b: int) -> int:\n    return a + b",
        function_name="add_numbers",
        test_cases=[
            ((3, 5), 8),
            ((10, -2), 8),
        ],
        concepts=["type hints", "annotations"],
    ),
    make_exercise(
        id="func_34",
        title="Type Hints with Collections",
        topic="functions",
        difficulty=3,
        description="Define a function `sum_numbers(numbers: list[int]) -> int:` that sums a list of integers.",
        hints=[
            "Use list[int] for a list of integers",
            "Return type is int",
        ],
        solution="def sum_numbers(numbers: list[int]) -> int:\n    return sum(numbers)",
        function_name="sum_numbers",
        test_cases=[
            (([1, 2, 3],), 6),
            (([10, 20],), 30),
        ],
        concepts=["type hints", "generics"],
    ),
    make_exercise(
        id="func_35",
        title="Nonlocal Scope",
        topic="functions",
        difficulty=3,
        description="Define a function `make_multiplier` that returns a function multiplying by a factor. Use nonlocal to modify a variable from the outer scope.",
        hints=[
            "Use nonlocal to allow inner function to modify outer variable",
            "Return the inner function",
        ],
        solution="def make_multiplier(factor):\n    def multiply(x):\n        return x * factor\n    return multiply",
        check=lambda ns: (
            'make_multiplier' in ns and callable(ns['make_multiplier']) and
            ns['make_multiplier'](5)(3) == 15 and
            ns['make_multiplier'](10)(2) == 20,
            "make_multiplier(5)(3) should return 15, make_multiplier(10)(2) should return 20"
        ),
        concepts=["nonlocal", "closures", "scope"],
    ),
    # HARD (36-45): Practical use cases, decorators, higher-order functions
    make_exercise(
        id="func_36",
        title="Retry Decorator",
        topic="functions",
        difficulty=4,
        description="Write a decorator `retry(n)` that retries a function up to n times if it raises an exception. On the nth failure, re-raise the exception.",
        hints=[
            "Use a loop to retry",
            "Catch exceptions and check if retries remain",
            "Use try-except",
        ],
        solution="def retry(n):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            for i in range(n):\n                try:\n                    return func(*args, **kwargs)\n                except:\n                    if i == n - 1:\n                        raise\n        return wrapper\n    return decorator",
        check=lambda ns: (
            'retry' in ns and callable(ns['retry']),
            "retry should be a callable decorator factory"
        ),
        concepts=["decorators", "exception handling", "retry logic"],
    ),
    make_exercise(
        id="func_37",
        title="Memoize Decorator",
        topic="functions",
        difficulty=4,
        description="Write a decorator `memoize` using a closure to cache function results. fibonacci(100) should be instant on second call.",
        hints=[
            "Use a dictionary to cache (args -> result)",
            "Check cache before calling the function",
        ],
        solution="def memoize(func):\n    cache = {}\n    def wrapper(*args):\n        if args not in cache:\n            cache[args] = func(*args)\n        return cache[args]\n    return wrapper",
        check=lambda ns: (
            'memoize' in ns and callable(ns['memoize']),
            "memoize should be a callable decorator"
        ),
        concepts=["memoization", "decorators", "closures", "performance"],
    ),
    make_exercise(
        id="func_38",
        title="Pipeline Function Composition",
        topic="functions",
        difficulty=4,
        description="Write a function `pipeline` that takes multiple functions and returns a function that applies them left-to-right. pipeline([str.upper, str.reverse]) should uppercase then reverse.",
        hints=[
            "Create a wrapper function that applies each function in order",
            "Use functools.reduce if desired",
        ],
        solution="def pipeline(functions):\n    def composed(x):\n        for func in functions:\n            x = func(x)\n        return x\n    return composed",
        check=lambda ns: (
            'pipeline' in ns and callable(ns['pipeline']) and
            ns['pipeline']([str.upper])('hello') == 'HELLO',
            "pipeline should compose functions left-to-right"
        ),
        concepts=["function composition", "higher-order functions"],
    ),
    make_exercise(
        id="func_39",
        title="Compound Interest Calculator",
        topic="functions",
        difficulty=4,
        description="Write a function `compound_interest(principal, rate, time, n=1)` that calculates final amount using A = P(1 + r/n)^(nt). Default n=1 (annual).",
        hints=[
            "Use ** for exponentiation",
            "rate should be decimal (5% = 0.05)",
        ],
        solution="def compound_interest(principal, rate, time, n=1):\n    return principal * (1 + rate / n) ** (n * time)",
        function_name="compound_interest",
        test_cases=[
            ((1000, 0.05, 1), 1050.0),
            ((1000, 0.05, 2, 4), 1000 * (1 + 0.05 / 4) ** (4 * 2)),
        ],
        concepts=["mathematical functions", "parameters", "formulas"],
    ),
    make_exercise(
        id="func_40",
        title="Email Validator Function",
        topic="functions",
        difficulty=4,
        description="Write a function `is_valid_email(email)` that returns True if email has format 'something@domain.com'. Use regex or simple string checks.",
        hints=[
            "Check for @ symbol",
            "Check for . after @",
            "Simple validation: '@' in email and '.' in email.split('@')[1]",
        ],
        solution="def is_valid_email(email):\n    return '@' in email and '.' in email.split('@')[1] if '@' in email else False",
        function_name="is_valid_email",
        test_cases=[
            (("user@example.com",), True),
            (("user@example",), False),
            (("invalid.email",), False),
        ],
        concepts=["validation", "string operations"],
    ),
    make_exercise(
        id="func_41",
        title="Text Processor: Title Case",
        topic="functions",
        difficulty=4,
        description="Write a function `title_case_words` that takes a sentence and returns it with each word capitalized, using title() or manual capitalization.",
        hints=[
            "Use str.title() or capitalize each word",
            "split() to get words, join() to reassemble",
        ],
        solution="def title_case_words(sentence):\n    return ' '.join(word.capitalize() for word in sentence.split())",
        function_name="title_case_words",
        test_cases=[
            (("hello world",), "Hello World"),
            (("python is fun",), "Python Is Fun"),
        ],
        concepts=["string processing", "text transformation"],
    ),
    make_exercise(
        id="func_42",
        title="Data Transformer: Parse CSV",
        topic="functions",
        difficulty=4,
        description="Write a function `parse_csv_line(line)` that takes 'name,age,city' and returns {'name': val, 'age': val, 'city': val}. Assume headers are ['name', 'age', 'city'].",
        hints=[
            "split() by comma to get values",
            "zip with headers to pair them",
        ],
        solution="def parse_csv_line(line, headers=['name', 'age', 'city']):\n    values = line.split(',')\n    return dict(zip(headers, values))",
        function_name="parse_csv_line",
        test_cases=[
            (("Alice,30,NYC",), {"name": "Alice", "age": "30", "city": "NYC"}),
        ],
        concepts=["data parsing", "dictionaries", "zip"],
    ),
    make_exercise(
        id="func_43",
        title="Higher-Order Function: Apply Twice",
        topic="functions",
        difficulty=4,
        description="Write a function `apply_twice(func, x)` that applies a function to x twice. Example: apply_twice(lambda x: x*2, 3) returns 12.",
        hints=[
            "Call func(x) to get intermediate result",
            "Call func again on the intermediate result",
        ],
        solution="def apply_twice(func, x):\n    return func(func(x))",
        check=lambda ns: (
            'apply_twice' in ns and callable(ns['apply_twice']) and
            ns['apply_twice'](lambda x: x * 2, 3) == 12 and
            ns['apply_twice'](lambda x: x + 5, 0) == 10,
            "apply_twice(lambda x: x * 2, 3) should return 12, apply_twice(lambda x: x + 5, 0) should return 10"
        ),
        concepts=["higher-order functions", "function arguments"],
    ),
    make_exercise(
        id="func_44",
        title="Partition Function",
        topic="functions",
        difficulty=4,
        description="Write a function `partition(pred, iterable)` that splits an iterable into two lists: items where pred is True and where it's False.",
        hints=[
            "Create two lists, true_list and false_list",
            "Iterate and append based on pred(item)",
        ],
        solution="def partition(pred, iterable):\n    true_list, false_list = [], []\n    for item in iterable:\n        if pred(item):\n            true_list.append(item)\n        else:\n            false_list.append(item)\n    return true_list, false_list",
        check=lambda ns: (
            'partition' in ns and callable(ns['partition']) and
            ns['partition'](lambda x: x > 3, [1, 2, 3, 4, 5]) == ([4, 5], [1, 2, 3]),
            "partition(lambda x: x > 3, [1, 2, 3, 4, 5]) should return ([4, 5], [1, 2, 3])"
        ),
        concepts=["higher-order functions", "filtering"],
    ),
    make_exercise(
        id="func_45",
        title="Function as Dictionary Value",
        topic="functions",
        difficulty=4,
        description="Create a function `calculate` that uses a dictionary of operations ('+': add, '-': subtract, '*': multiply) and returns the result of op(a, b).",
        hints=[
            "Store lambda or named functions in a dict",
            "Look up the operation by key",
        ],
        solution="def calculate(a, op, b):\n    operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}\n    return operations[op](a, b)",
        check=lambda ns: (
            'calculate' in ns and callable(ns['calculate']) and
            ns['calculate'](5, '+', 3) == 8 and
            ns['calculate'](5, '-', 3) == 2 and
            ns['calculate'](5, '*', 3) == 15,
            "calculate(5, '+', 3) should return 8, calculate(5, '-', 3) should return 2, calculate(5, '*', 3) should return 15"
        ),
        concepts=["functions as values", "dictionaries", "operations"],
    ),
    # CHALLENGE (46-50): Advanced patterns
    make_exercise(
        id="func_46",
        title="Currying Function",
        topic="functions",
        difficulty=5,
        description="Write a function `curry(func)` that converts a function of multiple arguments into nested single-argument functions. curry(add)(5)(3) should return 8.",
        hints=[
            "Return a function that takes one arg and returns another function",
            "The innermost function performs the actual operation",
        ],
        solution="def curry(func):\n    def curried(a):\n        def inner(b):\n            return func(a, b)\n        return inner\n    return curried",
        check=lambda ns: (
            'curry' in ns and callable(ns['curry']) and
            ns['curry'](lambda x, y: x + y)(5)(3) == 8,
            "curry(lambda x, y: x + y)(5)(3) should return 8"
        ),
        concepts=["currying", "function composition", "closures"],
    ),
    make_exercise(
        id="func_47",
        title="Recursive Tree Sum",
        topic="functions",
        difficulty=5,
        description="Write a function `sum_tree` that recursively sums all values in a nested list structure. Example: sum_tree([1, [2, [3, 4]]]) returns 10.",
        hints=[
            "Base case: if item is not a list, return its value",
            "Recursive case: sum the results of sum_tree on each element",
        ],
        solution="def sum_tree(tree):\n    total = 0\n    for item in tree:\n        if isinstance(item, list):\n            total += sum_tree(item)\n        else:\n            total += item\n    return total",
        function_name="sum_tree",
        test_cases=[
            (([1, [2, [3, 4]]],), 10),
            (([5, [10]],), 15),
        ],
        concepts=["recursion", "nested structures", "type checking"],
    ),
    make_exercise(
        id="func_48",
        title="Context Manager Decorator",
        topic="functions",
        difficulty=5,
        description="Write a decorator `measure_time` that wraps a function and prints the time it took to execute (in seconds).",
        hints=[
            "Import time module and use time.time()",
            "Record time before and after function call",
        ],
        solution="import time\ndef measure_time(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f'{func.__name__} took {end - start:.4f} seconds')\n        return result\n    return wrapper",
        check=lambda ns: (
            'measure_time' in ns and callable(ns['measure_time']),
            "measure_time should be a callable decorator"
        ),
        concepts=["decorators", "profiling", "side effects"],
    ),
    make_exercise(
        id="func_49",
        title="Chain Multiple Decorators",
        topic="functions",
        difficulty=5,
        description="Apply multiple decorators: @add_exclamation and @str.upper (or custom upper) to a function that returns 'hello'. Result should be 'HELLO!'.",
        hints=[
            "Decorators are applied bottom-to-top",
            "The first decorator applied receives the original function",
        ],
        solution="def to_upper(func):\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs).upper()\n    return wrapper\n\ndef add_exclamation(func):\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs) + '!'\n    return wrapper",
        check=lambda ns: (
            'to_upper' in ns and 'add_exclamation' in ns and callable(ns['to_upper']) and callable(ns['add_exclamation']),
            "Both to_upper and add_exclamation should be defined and callable"
        ),
        concepts=["multiple decorators", "composition", "order of execution"],
    ),
    make_exercise(
        id="func_50",
        title="Flexible Argument Unpacking",
        topic="functions",
        difficulty=5,
        description="Write a function `flexible_sum(*args, **kwargs)` that sums all positional arguments and all values in kwargs. Example: flexible_sum(1, 2, a=3, b=4) returns 10.",
        hints=[
            "Sum the args tuple",
            "Sum the values of kwargs dict",
            "Add them together",
        ],
        solution="def flexible_sum(*args, **kwargs):\n    return sum(args) + sum(kwargs.values())",
        check=lambda ns: (
            'flexible_sum' in ns and callable(ns['flexible_sum']) and
            ns['flexible_sum'](1, 2, a=3, b=4) == 10 and
            ns['flexible_sum'](5, x=10) == 15,
            "flexible_sum(1, 2, a=3, b=4) should return 10, flexible_sum(5, x=10) should return 15"
        ),
        concepts=["*args", "**kwargs", "argument unpacking"],
    ),
]
