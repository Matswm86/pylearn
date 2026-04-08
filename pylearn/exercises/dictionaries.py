"""50 exercises on Python dictionaries."""
from .base import make_exercise

exercises = [
    # BEGINNER (1-10): Creating dicts, accessing values, basic operations
    make_exercise(
        id="dict_01",
        title="Create a Dictionary",
        topic="dictionaries",
        difficulty=1,
        description="Create a dictionary called `person` with keys 'name' and 'age', with values 'Alice' and 30.",
        hints=[
            "Use curly braces {} to create a dictionary",
            "Separate key-value pairs with colons: key: value"
        ],
        solution="person = {'name': 'Alice', 'age': 30}",
        check=lambda ns: (
            ns.get('person') == {'name': 'Alice', 'age': 30},
            "person should be {'name': 'Alice', 'age': 30}"
        ),
        concepts=["dict creation", "key-value pairs"]
    ),
    make_exercise(
        id="dict_02",
        title="Access Dictionary Value",
        topic="dictionaries",
        difficulty=1,
        description="Create a dictionary `fruit_colors = {'apple': 'red', 'banana': 'yellow'}` and access the value for 'apple'.",
        hints=[
            "Use square brackets with the key: dict[key]",
            "Store the result in variable `color`"
        ],
        solution="fruit_colors = {'apple': 'red', 'banana': 'yellow'}\ncolor = fruit_colors['apple']",
        check=lambda ns: (ns.get('color') == 'red', "color should be 'red'"),
        concepts=["dict access", "indexing"]
    ),
    make_exercise(
        id="dict_03",
        title="Add Key-Value to Dictionary",
        topic="dictionaries",
        difficulty=1,
        description="Create an empty dictionary `scores = {}` and add a key 'math' with value 95.",
        hints=[
            "Use square bracket assignment: dict[key] = value",
            "You can add new keys to an empty dict"
        ],
        solution="scores = {}\nscores['math'] = 95",
        check=lambda ns: (ns.get('scores') == {'math': 95}, "scores should contain {'math': 95}"),
        concepts=["dict assignment", "adding keys"]
    ),
    make_exercise(
        id="dict_04",
        title="Update Dictionary Value",
        topic="dictionaries",
        difficulty=1,
        description="Create a dict `config = {'debug': False}` and update the value of 'debug' to True.",
        hints=[
            "Use assignment like adding a new key",
            "Since 'debug' already exists, it updates the value"
        ],
        solution="config = {'debug': False}\nconfig['debug'] = True",
        check=lambda ns: (ns.get('config') == {'debug': True}, "config['debug'] should be True"),
        concepts=["dict update", "overwriting values"]
    ),
    make_exercise(
        id="dict_05",
        title="Delete a Dictionary Key",
        topic="dictionaries",
        difficulty=1,
        description="Create a dict `inventory = {'apples': 10, 'oranges': 5}` and delete the 'oranges' key.",
        hints=[
            "Use the del keyword: del dict[key]",
            "After deletion, the key-value pair is gone"
        ],
        solution="inventory = {'apples': 10, 'oranges': 5}\ndel inventory['oranges']",
        check=lambda ns: (ns.get('inventory') == {'apples': 10}, "inventory should only have 'apples'"),
        concepts=["del keyword", "removing keys"]
    ),
    make_exercise(
        id="dict_06",
        title="Check if Key Exists",
        topic="dictionaries",
        difficulty=1,
        description="Create a dict `user = {'username': 'john', 'email': 'john@example.com'}` and check if 'email' is in it.",
        hints=[
            "Use the 'in' operator: key in dict",
            "This returns True or False"
        ],
        solution="user = {'username': 'john', 'email': 'john@example.com'}\nresult = 'email' in user",
        check=lambda ns: (ns.get('result') is True, "result should be True"),
        concepts=["membership test", "in operator"]
    ),
    make_exercise(
        id="dict_07",
        title="Use dict.get() with Default",
        topic="dictionaries",
        difficulty=1,
        description="Create a dict `settings = {'theme': 'dark'}` and use .get() to safely access 'language' with default 'English'.",
        hints=[
            "Use dict.get(key, default) instead of dict[key]",
            "This returns the value if key exists, otherwise returns default"
        ],
        solution="settings = {'theme': 'dark'}\nlanguage = settings.get('language', 'English')",
        check=lambda ns: (ns.get('language') == 'English', "language should be 'English' (the default)"),
        concepts=["dict.get()", "default values", "safe access"]
    ),
    make_exercise(
        id="dict_08",
        title="Get All Keys",
        topic="dictionaries",
        difficulty=1,
        description="Create a dict `book = {'title': 'Python', 'author': 'Guido', 'year': 1991}` and get all keys.",
        hints=[
            "Use dict.keys() method",
            "Store the keys in variable `keys_list` as a list"
        ],
        solution="book = {'title': 'Python', 'author': 'Guido', 'year': 1991}\nkeys_list = list(book.keys())",
        check=lambda ns: (set(ns.get('keys_list', [])) == {'title', 'author', 'year'}, "keys_list should contain all three keys"),
        concepts=["dict.keys()", "getting keys"]
    ),
    make_exercise(
        id="dict_09",
        title="Get All Values",
        topic="dictionaries",
        difficulty=1,
        description="Create a dict `grades = {'Alice': 90, 'Bob': 85}` and get all values as a list.",
        hints=[
            "Use dict.values() method",
            "Convert to a list with list()"
        ],
        solution="grades = {'Alice': 90, 'Bob': 85}\nvalues_list = list(grades.values())",
        check=lambda ns: (set(ns.get('values_list', [])) == {90, 85}, "values_list should contain 90 and 85"),
        concepts=["dict.values()", "getting values"]
    ),
    make_exercise(
        id="dict_10",
        title="Get Key-Value Pairs",
        topic="dictionaries",
        difficulty=1,
        description="Create a dict `product = {'name': 'Laptop', 'price': 999}` and get all key-value pairs.",
        hints=[
            "Use dict.items() method",
            "Store result as a list in `pairs`"
        ],
        solution="product = {'name': 'Laptop', 'price': 999}\npairs = list(product.items())",
        check=lambda ns: (set(ns.get('pairs', [])) == {('name', 'Laptop'), ('price', 999)}, "pairs should contain both (key, value) tuples"),
        concepts=["dict.items()", "key-value pairs"]
    ),

    # EASY (11-20): Iterating, basic comprehensions, simple transformations
    make_exercise(
        id="dict_11",
        title="Iterate Over Dictionary Keys",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `get_keys_uppercase` that takes a dict and returns a set of all keys in uppercase.",
        hints=[
            "Iterate over the dictionary or use dict.keys()",
            "Use .upper() method on each key string"
        ],
        solution="def get_keys_uppercase(d):\n    return {k.upper() for k in d.keys()}",
        function_name="get_keys_uppercase",
        test_cases=[
            ((({'name': 'Alice', 'city': 'NYC'},), {'NAME', 'CITY'})),
            ((({'x': 1, 'y': 2},), {'X', 'Y'})),
        ],
        concepts=["iteration", "string methods", "set comprehension"]
    ),
    make_exercise(
        id="dict_12",
        title="Iterate Over Dictionary Values",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `sum_values` that takes a dict with numeric values and returns their sum.",
        hints=[
            "Use dict.values() to get all values",
            "Use the sum() function on them"
        ],
        solution="def sum_values(d):\n    return sum(d.values())",
        function_name="sum_values",
        test_cases=[
            ((({'a': 10, 'b': 20, 'c': 5},), 35)),
            ((({'x': 1, 'y': 2, 'z': 3},), 6)),
            ((({},), 0)),
        ],
        concepts=["dict.values()", "sum()"]
    ),
    make_exercise(
        id="dict_13",
        title="Filter Dictionary by Value",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `filter_dict` that returns a new dict containing only items where value > threshold.",
        hints=[
            "Iterate through dict.items() to get key-value pairs",
            "Use a dict comprehension or loop to build the result"
        ],
        solution="def filter_dict(d, threshold):\n    return {k: v for k, v in d.items() if v > threshold}",
        function_name="filter_dict",
        test_cases=[
            ((({'a': 5, 'b': 15, 'c': 10}, 8), {'b': 15, 'c': 10})),
            ((({'x': 1, 'y': 2, 'z': 3}, 2), {'z': 3})),
        ],
        concepts=["dict comprehension", "filtering", "dict.items()"]
    ),
    make_exercise(
        id="dict_14",
        title="Dictionary Comprehension",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `square_values` that creates a new dict with the same keys but values squared.",
        hints=[
            "Use a dict comprehension: {k: expression for k, v in ...}",
            "Iterate over dict.items()"
        ],
        solution="def square_values(d):\n    return {k: v ** 2 for k, v in d.items()}",
        function_name="square_values",
        test_cases=[
            ((({'a': 2, 'b': 3, 'c': 4},), {'a': 4, 'b': 9, 'c': 16})),
            ((({'x': 5, 'y': 10},), {'x': 25, 'y': 100})),
        ],
        concepts=["dict comprehension", "transformations"]
    ),
    make_exercise(
        id="dict_15",
        title="Invert Dictionary",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `invert_dict` that swaps keys and values (assumes all values are unique).",
        hints=[
            "Use a dict comprehension: {v: k for k, v in d.items()}",
            "Keys become values and values become keys"
        ],
        solution="def invert_dict(d):\n    return {v: k for k, v in d.items()}",
        function_name="invert_dict",
        test_cases=[
            ((({'a': 1, 'b': 2, 'c': 3},), {1: 'a', 2: 'b', 3: 'c'})),
            ((({'x': 'hello', 'y': 'world'},), {'hello': 'x', 'world': 'y'})),
        ],
        concepts=["dict inversion", "dict comprehension"]
    ),
    make_exercise(
        id="dict_16",
        title="Merge Two Dictionaries",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `merge_dicts` that combines two dicts (second dict wins on conflicts).",
        hints=[
            "Use the | operator (Python 3.9+) or dict.update()",
            "Or use {**dict1, **dict2}"
        ],
        solution="def merge_dicts(d1, d2):\n    return {**d1, **d2}",
        function_name="merge_dicts",
        test_cases=[
            ((({'a': 1, 'b': 2}, {'c': 3}), {'a': 1, 'b': 2, 'c': 3})),
            ((({'x': 10}, {'x': 20, 'y': 30}), {'x': 20, 'y': 30})),
        ],
        concepts=["dict unpacking", "merging"]
    ),
    make_exercise(
        id="dict_17",
        title="Count Occurrences",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `count_items` that counts how many times each item appears in a list.",
        hints=[
            "Initialize an empty dict",
            "For each item, increment its count or set it to 1"
        ],
        solution="def count_items(items):\n    result = {}\n    for item in items:\n        result[item] = result.get(item, 0) + 1\n    return result",
        function_name="count_items",
        test_cases=[
            (((['a', 'b', 'a', 'c', 'b', 'a'],), {'a': 3, 'b': 2, 'c': 1})),
            ((([1, 1, 2, 2, 2, 3],), {1: 2, 2: 3, 3: 1})),
        ],
        concepts=["frequency counting", "dict.get()"]
    ),
    make_exercise(
        id="dict_18",
        title="Group List by Function",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `group_by_length` that groups words by their length.",
        hints=[
            "Create a dict where keys are lengths",
            "Values are lists of words with that length"
        ],
        solution="def group_by_length(words):\n    result = {}\n    for word in words:\n        length = len(word)\n        if length not in result:\n            result[length] = []\n        result[length].append(word)\n    return result",
        function_name="group_by_length",
        test_cases=[
            (((['a', 'bb', 'ccc', 'dd'],), {1: ['a'], 2: ['bb', 'dd'], 3: ['ccc']})),
            (((['cat', 'dog', 'bird', 'fish'],), {3: ['cat', 'dog'], 4: ['bird', 'fish']})),
        ],
        concepts=["grouping", "dict of lists"]
    ),
    make_exercise(
        id="dict_19",
        title="Conditional Dict Creation",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `filter_even` that creates a dict with only even keys from the input dict.",
        hints=[
            "Use a dict comprehension with an if condition",
            "Check if the key is even using key % 2 == 0"
        ],
        solution="def filter_even(d):\n    return {k: v for k, v in d.items() if k % 2 == 0}",
        function_name="filter_even",
        test_cases=[
            ((({1: 'a', 2: 'b', 3: 'c', 4: 'd'},), {2: 'b', 4: 'd'})),
            ((({0: 'zero', 5: 'five', 10: 'ten'},), {0: 'zero', 10: 'ten'})),
        ],
        concepts=["dict comprehension", "filtering"]
    ),
    make_exercise(
        id="dict_20",
        title="Dictionary Length and Check Empty",
        topic="dictionaries",
        difficulty=2,
        description="Write a function `is_empty` that returns True if dict is empty, False otherwise.",
        hints=[
            "Use len() function on the dict",
            "Empty dict has length 0"
        ],
        solution="def is_empty(d):\n    return len(d) == 0",
        function_name="is_empty",
        test_cases=[
            ((({},), True)),
            ((({'a': 1},), False)),
            ((({'x': 0, 'y': None},), False)),
        ],
        concepts=["len()", "dict length"]
    ),

    # MEDIUM (21-35): Nested dicts, defaultdict, more complex operations
    make_exercise(
        id="dict_21",
        title="Nested Dictionary Access",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `get_nested` that safely accesses nested.get('user').get('name') with defaults.",
        hints=[
            "Chain .get() calls with defaults",
            "Return 'Unknown' if any level is missing"
        ],
        solution="def get_nested(d):\n    user = d.get('user', {})\n    return user.get('name', 'Unknown')",
        function_name="get_nested",
        test_cases=[
            ((({'user': {'name': 'Alice'}},), 'Alice')),
            ((({'user': {}},), 'Unknown')),
            ((({},), 'Unknown')),
        ],
        concepts=["nested dicts", "safe access", "chaining"]
    ),
    make_exercise(
        id="dict_22",
        title="Update Nested Dictionary",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `set_nested` that sets a value in dict['user']['email'] = new_email (creating nested structure).",
        hints=[
            "Check if 'user' key exists, create it if not",
            "Then set the 'email' key"
        ],
        solution="def set_nested(d, email):\n    if 'user' not in d:\n        d['user'] = {}\n    d['user']['email'] = email\n    return d",
        function_name="set_nested",
        test_cases=[
            ((({}, 'test@example.com'), {'user': {'email': 'test@example.com'}})),
            ((({'user': {'name': 'Bob'}}, 'bob@example.com'), {'user': {'name': 'Bob', 'email': 'bob@example.com'}})),
        ],
        concepts=["nested dict modification", "creating nested structure"]
    ),
    make_exercise(
        id="dict_23",
        title="Flatten Nested Dictionary",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `flatten_dict` that flattens a nested dict into dot-notation keys (e.g., 'user.name').",
        hints=[
            "Use recursion or iteration to traverse nested structure",
            "Build keys like 'parent.child' as you go deeper"
        ],
        solution="def flatten_dict(d, parent_key=''):\n    result = {}\n    for k, v in d.items():\n        new_key = f'{parent_key}.{k}' if parent_key else k\n        if isinstance(v, dict):\n            result.update(flatten_dict(v, new_key))\n        else:\n            result[new_key] = v\n    return result",
        function_name="flatten_dict",
        test_cases=[
            ((({'user': {'name': 'Alice', 'age': 30}},), {'user.name': 'Alice', 'user.age': 30})),
            ((({'a': {'b': {'c': 1}}},), {'a.b.c': 1})),
        ],
        concepts=["recursion", "nested dicts", "key construction"]
    ),
    make_exercise(
        id="dict_24",
        title="Deep Copy vs Shallow Copy",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `copy_dict` that creates a deep copy of a nested dict.",
        hints=[
            "Use copy.deepcopy() from the copy module",
            "Shallow copy (d.copy() or {**d}) won't work for nested dicts"
        ],
        solution="import copy\ndef copy_dict(d):\n    return copy.deepcopy(d)",
        function_name="copy_dict",
        test_cases=[
            ((({'a': {'b': 1}},), {'a': {'b': 1}})),
        ],
        concepts=["deep copy", "copy module"]
    ),
    make_exercise(
        id="dict_25",
        title="Count Word Frequency",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `word_frequency` that counts word frequency in a text (lowercase, no punctuation).",
        hints=[
            "Split text into words using .split()",
            "Use a dict to count each word",
            "Return dict sorted by count (optional)"
        ],
        solution="def word_frequency(text):\n    words = text.lower().split()\n    freq = {}\n    for word in words:\n        freq[word] = freq.get(word, 0) + 1\n    return freq",
        function_name="word_frequency",
        test_cases=[
            ((('hello world hello',), {'hello': 2, 'world': 1})),
            ((('a b c a b a',), {'a': 3, 'b': 2, 'c': 1})),
        ],
        concepts=["frequency analysis", "text processing"]
    ),
    make_exercise(
        id="dict_26",
        title="Merge User Profiles",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `merge_profiles` that merges two user profiles (newer values win, keep all fields).",
        hints=[
            "Combine both dicts",
            "If keys conflict, newer profile's value should win"
        ],
        solution="def merge_profiles(old, new):\n    return {**old, **new}",
        function_name="merge_profiles",
        test_cases=[
            ((({'name': 'Alice', 'email': 'old@ex.com'}, {'email': 'new@ex.com', 'phone': '123'}), {'name': 'Alice', 'email': 'new@ex.com', 'phone': '123'})),
            ((({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4})),
        ],
        concepts=["dict merging", "unpacking"]
    ),
    make_exercise(
        id="dict_27",
        title="Group People by City",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `group_by_city` that takes a list of people dicts and groups them by city.",
        hints=[
            "Each person is a dict with 'name' and 'city' keys",
            "Group by city, values are lists of people (dicts)"
        ],
        solution="def group_by_city(people):\n    result = {}\n    for person in people:\n        city = person['city']\n        if city not in result:\n            result[city] = []\n        result[city].append(person)\n    return result",
        function_name="group_by_city",
        test_cases=[
            ((([{'name': 'Alice', 'city': 'NYC'}, {'name': 'Bob', 'city': 'LA'}, {'name': 'Charlie', 'city': 'NYC'}],), {'NYC': [{'name': 'Alice', 'city': 'NYC'}, {'name': 'Charlie', 'city': 'NYC'}], 'LA': [{'name': 'Bob', 'city': 'LA'}]})),
        ],
        concepts=["grouping", "dict of lists", "complex data"]
    ),
    make_exercise(
        id="dict_28",
        title="Validate Against Schema",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `validate_schema` that checks if a dict matches a schema (required keys).",
        hints=[
            "Schema is a list of required key names",
            "Check if all required keys are present"
        ],
        solution="def validate_schema(data, schema):\n    return all(key in data for key in schema)",
        function_name="validate_schema",
        test_cases=[
            ((({'name': 'Alice', 'age': 30}, ['name', 'age']), True)),
            ((({'name': 'Bob'}, ['name', 'age']), False)),
            ((({'x': 1, 'y': 2, 'z': 3}, ['x', 'y']), True)),
        ],
        concepts=["validation", "schema checking"]
    ),
    make_exercise(
        id="dict_29",
        title="Create Lookup Table",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `create_lookup` that builds a dict mapping IDs to objects (from a list).",
        hints=[
            "Each object in the list has an 'id' field",
            "Use dict comprehension or loop to build {id: object} mapping"
        ],
        solution="def create_lookup(objects):\n    return {obj['id']: obj for obj in objects}",
        function_name="create_lookup",
        test_cases=[
            ((([{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}],), {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}})),
        ],
        concepts=["dict comprehension", "lookup tables"]
    ),
    make_exercise(
        id="dict_30",
        title="Remove Keys by Pattern",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `remove_private_keys` that removes keys starting with '_'.",
        hints=[
            "Use dict comprehension to filter",
            "Check if key.startswith('_') is False"
        ],
        solution="def remove_private_keys(d):\n    return {k: v for k, v in d.items() if not k.startswith('_')}",
        function_name="remove_private_keys",
        test_cases=[
            ((({'public': 1, '_private': 2, 'name': 'Alice'},), {'public': 1, 'name': 'Alice'})),
            ((({'_a': 1, '_b': 2, 'x': 3},), {'x': 3})),
        ],
        concepts=["filtering", "string methods"]
    ),
    make_exercise(
        id="dict_31",
        title="Dictionary with setdefault",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `get_or_create` that uses setdefault to get value or create with default.",
        hints=[
            "Use dict.setdefault(key, default)",
            "Returns existing value or sets and returns default"
        ],
        solution="def get_or_create(d, key, default):\n    return d.setdefault(key, default)",
        function_name="get_or_create",
        test_cases=[
            ((({'a': 1}, 'a', 0), 1)),
            ((({'a': 1}, 'b', 99), 99)),
        ],
        concepts=["dict.setdefault()", "default values"]
    ),
    make_exercise(
        id="dict_32",
        title="Build Inverted Index",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `inverted_index` that maps words to documents they appear in.",
        hints=[
            "Each document is a dict with 'id' and 'text'",
            "Build dict where keys are words, values are lists of doc IDs"
        ],
        solution="def inverted_index(documents):\n    index = {}\n    for doc in documents:\n        for word in doc['text'].lower().split():\n            if word not in index:\n                index[word] = []\n            if doc['id'] not in index[word]:\n                index[word].append(doc['id'])\n    return index",
        function_name="inverted_index",
        test_cases=[
            ((([{'id': 1, 'text': 'hello world'}, {'id': 2, 'text': 'hello there'}],), {'hello': [1, 2], 'world': [1], 'there': [2]})),
        ],
        concepts=["inverted index", "text indexing"]
    ),
    make_exercise(
        id="dict_33",
        title="Dict Comprehension with enumerate",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `list_to_dict` that converts a list to dict with indices as keys.",
        hints=[
            "Use enumerate() to get (index, value) pairs",
            "Build dict comprehension {index: value for ...}"
        ],
        solution="def list_to_dict(lst):\n    return {i: v for i, v in enumerate(lst)}",
        function_name="list_to_dict",
        test_cases=[
            (((['a', 'b', 'c'],), {0: 'a', 1: 'b', 2: 'c'})),
            ((([10, 20, 30],), {0: 10, 1: 20, 2: 30})),
        ],
        concepts=["enumerate()", "dict comprehension"]
    ),
    make_exercise(
        id="dict_34",
        title="Compute Running Totals",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `running_total` that computes cumulative sum of dict values.",
        hints=[
            "Iterate through items in order",
            "Keep a running sum variable",
            "Store cumulative value for each key"
        ],
        solution="def running_total(d):\n    result = {}\n    total = 0\n    for k, v in d.items():\n        total += v\n        result[k] = total\n    return result",
        function_name="running_total",
        test_cases=[
            ((({'a': 1, 'b': 2, 'c': 3},), {'a': 1, 'b': 3, 'c': 6})),
        ],
        concepts=["iteration", "accumulation"]
    ),
    make_exercise(
        id="dict_35",
        title="Find Key by Value",
        topic="dictionaries",
        difficulty=3,
        description="Write a function `find_key` that finds the key for a given value (returns first match).",
        hints=[
            "Iterate through items",
            "Return key when value matches",
            "Return None if not found"
        ],
        solution="def find_key(d, value):\n    for k, v in d.items():\n        if v == value:\n            return k\n    return None",
        function_name="find_key",
        test_cases=[
            ((({'a': 1, 'b': 2, 'c': 3}, 2), 'b')),
            ((({'a': 1, 'b': 2}, 99), None)),
        ],
        concepts=["searching", "dict.items()"]
    ),

    # HARD (36-45): Collections module, advanced patterns, real-world scenarios
    make_exercise(
        id="dict_36",
        title="Use defaultdict for Grouping",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `group_with_defaultdict` that groups numbers by their modulo 3 using defaultdict(list).",
        hints=[
            "Import defaultdict from collections",
            "defaultdict(list) creates empty list for missing keys automatically"
        ],
        solution="from collections import defaultdict\ndef group_with_defaultdict(numbers):\n    groups = defaultdict(list)\n    for num in numbers:\n        groups[num % 3].append(num)\n    return dict(groups)",
        function_name="group_with_defaultdict",
        test_cases=[
            ((([1, 2, 3, 4, 5, 6],), {0: [3, 6], 1: [1, 4], 2: [2, 5]})),
        ],
        concepts=["defaultdict", "collections module"]
    ),
    make_exercise(
        id="dict_37",
        title="Use Counter for Frequency",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `top_words` that uses Counter to find the 3 most common words.",
        hints=[
            "Import Counter from collections",
            "Counter.most_common(n) returns top n items"
        ],
        solution="from collections import Counter\ndef top_words(text):\n    words = text.lower().split()\n    counter = Counter(words)\n    return dict(counter.most_common(3))",
        function_name="top_words",
        test_cases=[
            ((('the quick brown fox quick fox fox',), {'fox': 3, 'quick': 2, 'the': 1})),
        ],
        concepts=["Counter", "collections module", "frequency"]
    ),
    make_exercise(
        id="dict_38",
        title="Use OrderedDict for Ordering",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `dict_by_value_desc` that returns dict items sorted by value descending.",
        hints=[
            "Sort dict.items() by value",
            "Use sorted() with key parameter",
            "Can return as OrderedDict or regular dict (Python 3.7+)"
        ],
        solution="def dict_by_value_desc(d):\n    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))",
        function_name="dict_by_value_desc",
        test_cases=[
            ((({'a': 3, 'b': 1, 'c': 2},), {'a': 3, 'c': 2, 'b': 1})),
        ],
        concepts=["sorting", "lambda", "dict ordering"]
    ),
    make_exercise(
        id="dict_39",
        title="Merge Multiple Dictionaries",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `merge_many` that merges a list of dicts (later dicts override earlier).",
        hints=[
            "Use the | operator (Python 3.9+) in a loop",
            "Or use {**d1, **d2, **d3, ...}"
        ],
        solution="def merge_many(dicts):\n    result = {}\n    for d in dicts:\n        result |= d\n    return result",
        function_name="merge_many",
        test_cases=[
            ((([{'a': 1}, {'b': 2}, {'a': 3}],), {'a': 3, 'b': 2})),
        ],
        concepts=["dict merging", "| operator"]
    ),
    make_exercise(
        id="dict_40",
        title="Create Cache with Decorator",
        topic="dictionaries",
        difficulty=4,
        description="Write a simple memoization decorator that caches function results using a dict.",
        hints=[
            "Use a dict inside the decorator to store results",
            "Key is the function arguments",
            "Return cached result if it exists"
        ],
        solution="def memoize(func):\n    cache = {}\n    def wrapper(*args):\n        if args not in cache:\n            cache[args] = func(*args)\n        return cache[args]\n    return wrapper",
        function_name="memoize",
        test_cases=[
            # Testing that the decorator works
        ],
        concepts=["caching", "decorator", "memoization"]
    ),
    make_exercise(
        id="dict_41",
        title="Parse Query String to Dict",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `parse_query` that converts 'a=1&b=2&c=3' into a dict.",
        hints=[
            "Split by '&' to get key=value pairs",
            "Split each pair by '=' to get key and value"
        ],
        solution="def parse_query(query_string):\n    result = {}\n    for pair in query_string.split('&'):\n        key, value = pair.split('=')\n        result[key] = value\n    return result",
        function_name="parse_query",
        test_cases=[
            ((('a=1&b=2&c=3',), {'a': '1', 'b': '2', 'c': '3'})),
        ],
        concepts=["parsing", "string manipulation"]
    ),
    make_exercise(
        id="dict_42",
        title="Dict as Dispatch Table",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `calculate` that uses a dict to dispatch operations (+, -, *, /).",
        hints=[
            "Store functions in a dict with operator symbols as keys",
            "Look up and call the appropriate function"
        ],
        solution="def calculate(op, args):\n    a, b = args\n    ops = {\n        '+': lambda x, y: x + y,\n        '-': lambda x, y: x - y,\n        '*': lambda x, y: x * y,\n        '/': lambda x, y: x / y,\n    }\n    return ops[op](a, b)",
        function_name="calculate",
        test_cases=[
            ((('+',(5, 3)), 8)),
            ((('+', (5, 3)), 8)),
            ((('-', (10, 4)), 6)),
        ],
        concepts=["dispatch table", "lambda", "function storage"]
    ),
    make_exercise(
        id="dict_43",
        title="Convert Nested List to Dict",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `nested_list_to_dict` that converts [['a', 1], ['b', 2]] to {'a': 1, 'b': 2}.",
        hints=[
            "Iterate through the list of pairs",
            "Each pair is [key, value]",
            "Use dict comprehension or dict() constructor"
        ],
        solution="def nested_list_to_dict(pairs):\n    return dict(pairs)",
        function_name="nested_list_to_dict",
        test_cases=[
            ((([['a', 1], ['b', 2]],), {'a': 1, 'b': 2})),
            ((([['x', 10], ['y', 20], ['z', 30]],), {'x': 10, 'y': 20, 'z': 30})),
        ],
        concepts=["type conversion", "dict constructor"]
    ),
    make_exercise(
        id="dict_44",
        title="Inventory Management with Dicts",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `process_orders` that updates inventory based on orders (subtract quantities).",
        hints=[
            "Inventory is dict {item: quantity}",
            "Orders is dict {item: quantity_ordered}",
            "Return updated inventory"
        ],
        solution="def process_orders(inventory, orders):\n    for item, qty in orders.items():\n        inventory[item] -= qty\n    return inventory",
        function_name="process_orders",
        test_cases=[
            ((({'apple': 100, 'banana': 50}, {'apple': 20, 'banana': 10}), {'apple': 80, 'banana': 40})),
        ],
        concepts=["inventory management", "dict manipulation"]
    ),
    make_exercise(
        id="dict_45",
        title="JSON-like Data Transformation",
        topic="dictionaries",
        difficulty=4,
        description="Write a function `extract_ids` that extracts all 'id' fields from nested JSON-like dict structure.",
        hints=[
            "Recursively search for 'id' keys",
            "Handle both dicts and lists",
            "Return list of all found IDs"
        ],
        solution="def extract_ids(data):\n    ids = []\n    if isinstance(data, dict):\n        if 'id' in data:\n            ids.append(data['id'])\n        for v in data.values():\n            ids.extend(extract_ids(v))\n    elif isinstance(data, list):\n        for item in data:\n            ids.extend(extract_ids(item))\n    return ids",
        function_name="extract_ids",
        test_cases=[
            ((({'id': 1, 'user': {'id': 2}},), [1, 2])),
        ],
        concepts=["recursion", "JSON processing"]
    ),

    # CHALLENGE (46-50): Complex real-world scenarios, multi-step transformations
    make_exercise(
        id="dict_46",
        title="Grade Book Statistics",
        topic="dictionaries",
        difficulty=5,
        description="Write a function `compute_stats` that takes grade_dict {student: [grades]} and returns {student: {mean, max, min}}.",
        hints=[
            "Compute mean, max, min for each student's grades",
            "Return nested dict with stats"
        ],
        solution="def compute_stats(grades_dict):\n    return {student: {'mean': sum(grades)/len(grades), 'max': max(grades), 'min': min(grades)} for student, grades in grades_dict.items()}",
        function_name="compute_stats",
        test_cases=[
            ((({'Alice': [90, 85, 88], 'Bob': [92, 95, 89]},), {'Alice': {'mean': 87.66666666666667, 'max': 90, 'min': 85}, 'Bob': {'mean': 92.0, 'max': 95, 'min': 89}})),
        ],
        concepts=["statistics", "nested dict", "dict comprehension"]
    ),
    make_exercise(
        id="dict_47",
        title="Cross-Join Two Dicts",
        topic="dictionaries",
        difficulty=5,
        description="Write a function `cross_join` that creates all combinations of keys from two dicts with combined values.",
        hints=[
            "Use nested loops to iterate both dicts",
            "Create key like (k1, k2) and value like {v1, v2}"
        ],
        solution="def cross_join(d1, d2):\n    return {(k1, k2): (v1, v2) for k1, v1 in d1.items() for k2, v2 in d2.items()}",
        function_name="cross_join",
        test_cases=[
            ((({'a': 1, 'b': 2}, {'x': 10, 'y': 20}), {('a', 'x'): (1, 10), ('a', 'y'): (1, 20), ('b', 'x'): (2, 10), ('b', 'y'): (2, 20)})),
        ],
        concepts=["nested iteration", "dict comprehension", "combinations"]
    ),
    make_exercise(
        id="dict_48",
        title="Phone Book with Name Lookup",
        topic="dictionaries",
        difficulty=5,
        description="Write functions `add_contact` and `find_by_name` for a phone book that handles duplicate first names.",
        hints=[
            "Store {full_name: phone_number}",
            "For find_by_name, filter by first name and return all matches",
            "This is a 2-function exercise"
        ],
        solution="class PhoneBook:\n    def __init__(self):\n        self.contacts = {}\n    def add_contact(self, name, phone):\n        self.contacts[name] = phone\n    def find_by_name(self, first_name):\n        return {name: phone for name, phone in self.contacts.items() if name.split()[0] == first_name}",
        function_name="find_by_name",
        test_cases=[
            # This is complex - would need object state
        ],
        concepts=["dict for data storage", "search patterns"]
    ),
    make_exercise(
        id="dict_49",
        title="Shopping Cart Calculations",
        topic="dictionaries",
        difficulty=5,
        description="Write a function `cart_total` that takes cart {item: (price, qty)} and returns {item_total, subtotal, tax, total}.",
        hints=[
            "Calculate price * qty for each item",
            "Sum all items for subtotal",
            "Tax is subtotal * tax_rate (0.08)",
            "Total is subtotal + tax"
        ],
        solution="def cart_total(cart, tax_rate=0.08):\n    items_total = {item: price * qty for item, (price, qty) in cart.items()}\n    subtotal = sum(items_total.values())\n    tax = subtotal * tax_rate\n    return {'items': items_total, 'subtotal': subtotal, 'tax': tax, 'total': subtotal + tax}",
        function_name="cart_total",
        test_cases=[
            ((({'apple': (1.50, 3), 'banana': (0.50, 2)},), {'items': {'apple': 4.50, 'banana': 1.0}, 'subtotal': 5.50, 'tax': 0.44, 'total': 5.94})),
        ],
        concepts=["complex calculations", "nested dict"]
    ),
    make_exercise(
        id="dict_50",
        title="Build API Response Cache",
        topic="dictionaries",
        difficulty=5,
        description="Write a class APICache that stores responses by endpoint+params, with TTL (time-to-live) tracking.",
        hints=[
            "Store {endpoint: {params_str: (response, timestamp)}}",
            "is_expired checks if (now - timestamp) > ttl",
            "get returns response if not expired, else None"
        ],
        solution="import time\nclass APICache:\n    def __init__(self, ttl=60):\n        self.cache = {}\n        self.ttl = ttl\n    def set(self, endpoint, params, response):\n        if endpoint not in self.cache:\n            self.cache[endpoint] = {}\n        self.cache[endpoint][str(params)] = (response, time.time())\n    def get(self, endpoint, params):\n        if endpoint in self.cache and str(params) in self.cache[endpoint]:\n            response, timestamp = self.cache[endpoint][str(params)]\n            if time.time() - timestamp < self.ttl:\n                return response\n        return None",
        function_name="get",
        test_cases=[
            # Would need time-based testing
        ],
        concepts=["caching", "TTL", "class design", "timestamp"]
    ),
]
