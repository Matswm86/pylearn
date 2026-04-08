"""50 exercises on Python lists and sets."""
from .base import make_exercise

exercises = [
    # BEGINNER: 1-10 (Creating lists, accessing, basic operations)
    make_exercise(
        id="ls_01",
        title="Create a list",
        topic="lists_sets",
        difficulty=1,
        description="Create a list containing the integers 1, 2, 3, 4, 5 and assign it to a variable called 'my_list'.",
        hints=[
            "Use square brackets [] to create a list.",
            "Separate elements with commas."
        ],
        solution="my_list = [1, 2, 3, 4, 5]",
        starter_code="my_list = ",
        check=lambda ns: (
            ns.get("my_list") == [1, 2, 3, 4, 5],
            "my_list should be [1, 2, 3, 4, 5]"
        ),
        concepts=["list literals", "variable assignment"]
    ),
    make_exercise(
        id="ls_02",
        title="Access list elements by index",
        topic="lists_sets",
        difficulty=1,
        description="Given the list items = ['apple', 'banana', 'cherry'], get the first element.",
        hints=[
            "List indices start at 0 in Python.",
            "Use square brackets with the index number to access an element."
        ],
        solution="items = ['apple', 'banana', 'cherry']\nfirst = items[0]",
        starter_code="items = ['apple', 'banana', 'cherry']\nfirst = ",
        check=lambda ns: (
            ns.get("first") == "apple",
            "first should be 'apple'"
        ),
        concepts=["indexing", "zero-based indexing"]
    ),
    make_exercise(
        id="ls_03",
        title="Negative indexing",
        topic="lists_sets",
        difficulty=1,
        description="Given the list colors = ['red', 'green', 'blue', 'yellow'], get the last element using negative indexing.",
        hints=[
            "Negative indices count from the end of the list.",
            "-1 refers to the last element, -2 to the second-to-last, etc."
        ],
        solution="colors = ['red', 'green', 'blue', 'yellow']\nlast = colors[-1]",
        starter_code="colors = ['red', 'green', 'blue', 'yellow']\nlast = ",
        check=lambda ns: (
            ns.get("last") == "yellow",
            "last should be 'yellow'"
        ),
        concepts=["negative indexing"]
    ),
    make_exercise(
        id="ls_04",
        title="Get list length",
        topic="lists_sets",
        difficulty=1,
        description="Write a function that returns the number of elements in a list.",
        hints=[
            "Use the len() function to get the length.",
            "Don't count manually."
        ],
        solution="def get_length(items):\n    return len(items)",
        starter_code="def get_length(items):\n    pass",
        function_name="get_length",
        test_cases=[
            (([1, 2, 3],), 3),
            (([],), 0),
            ((['a', 'b', 'c', 'd'],), 4),
        ],
        concepts=["len() function"]
    ),
    make_exercise(
        id="ls_05",
        title="Append to a list",
        topic="lists_sets",
        difficulty=1,
        description="Write a function that appends an element to a list and returns the modified list.",
        hints=[
            "Use the .append() method to add an element to the end.",
            "The method modifies the list in place."
        ],
        solution="def add_element(items, element):\n    items.append(element)\n    return items",
        starter_code="def add_element(items, element):\n    pass",
        function_name="add_element",
        test_cases=[
            (([1, 2, 3], 4), [1, 2, 3, 4]),
            (([], 'first'), ['first']),
            ((['a', 'b'], 'c'), ['a', 'b', 'c']),
        ],
        concepts=["append() method"]
    ),
    make_exercise(
        id="ls_06",
        title="Remove an element",
        topic="lists_sets",
        difficulty=1,
        description="Write a function that removes the first occurrence of an element from a list and returns the modified list.",
        hints=[
            "Use the .remove() method.",
            "If the element is not found, it raises an error."
        ],
        solution="def remove_element(items, element):\n    items.remove(element)\n    return items",
        starter_code="def remove_element(items, element):\n    pass",
        function_name="remove_element",
        test_cases=[
            (([1, 2, 3, 2], 2), [1, 3, 2]),
            ((['a', 'b', 'c'], 'b'), ['a', 'c']),
            (([5], 5), []),
        ],
        concepts=["remove() method"]
    ),
    make_exercise(
        id="ls_07",
        title="Pop an element by index",
        topic="lists_sets",
        difficulty=1,
        description="Write a function that removes and returns an element at a specific index.",
        hints=[
            "Use the .pop() method with an index.",
            "pop() both removes and returns the element."
        ],
        solution="def pop_at_index(items, index):\n    return items.pop(index)",
        starter_code="def pop_at_index(items, index):\n    pass",
        function_name="pop_at_index",
        test_cases=[
            (([1, 2, 3], 1), 2),
            ((['a', 'b', 'c'], 0), 'a'),
            (([10, 20, 30], 2), 30),
        ],
        concepts=["pop() method"]
    ),
    make_exercise(
        id="ls_08",
        title="Check if element in list",
        topic="lists_sets",
        difficulty=1,
        description="Write a function that checks if an element exists in a list and returns True or False.",
        hints=[
            "Use the 'in' operator.",
            "It returns a boolean value."
        ],
        solution="def is_in_list(items, element):\n    return element in items",
        starter_code="def is_in_list(items, element):\n    pass",
        function_name="is_in_list",
        test_cases=[
            (([1, 2, 3], 2), True),
            (([1, 2, 3], 5), False),
            ((['a', 'b'], 'a'), True),
        ],
        concepts=["membership test", "in operator"]
    ),
    make_exercise(
        id="ls_09",
        title="List index of element",
        topic="lists_sets",
        difficulty=1,
        description="Write a function that returns the index of the first occurrence of an element in a list.",
        hints=[
            "Use the .index() method.",
            "It raises an error if the element is not found."
        ],
        solution="def find_index(items, element):\n    return items.index(element)",
        starter_code="def find_index(items, element):\n    pass",
        function_name="find_index",
        test_cases=[
            (([1, 2, 3, 2], 2), 1),
            ((['a', 'b', 'c'], 'c'), 2),
            (([10, 20, 30], 10), 0),
        ],
        concepts=["index() method"]
    ),
    make_exercise(
        id="ls_10",
        title="Insert element at position",
        topic="lists_sets",
        difficulty=1,
        description="Write a function that inserts an element at a specific index in a list.",
        hints=[
            "Use the .insert() method with index and element.",
            "insert(index, element) adds the element BEFORE the given index."
        ],
        solution="def insert_at(items, index, element):\n    items.insert(index, element)\n    return items",
        starter_code="def insert_at(items, index, element):\n    pass",
        function_name="insert_at",
        test_cases=[
            (([1, 2, 3], 1, 10), [1, 10, 2, 3]),
            (([1, 2], 0, 0), [0, 1, 2]),
            ((['a', 'b'], 2, 'c'), ['a', 'b', 'c']),
        ],
        concepts=["insert() method"]
    ),

    # EASY: 11-20 (Slicing, basic comprehensions, nested lists)
    make_exercise(
        id="ls_11",
        title="List slicing basics",
        topic="lists_sets",
        difficulty=2,
        description="Write a function that returns elements from index 1 to 2 (inclusive of 1, exclusive of 2).",
        hints=[
            "Use slicing syntax: list[start:stop].",
            "start is inclusive, stop is exclusive."
        ],
        solution="def slice_list(items):\n    return items[1:2]",
        starter_code="def slice_list(items):\n    pass",
        function_name="slice_list",
        test_cases=[
            (([1, 2, 3, 4, 5],), [2]),
            ((['a', 'b', 'c', 'd'],), ['b']),
            (([10, 20, 30],), [20]),
        ],
        concepts=["list slicing", "slice syntax"]
    ),
    make_exercise(
        id="ls_12",
        title="Slice with step",
        topic="lists_sets",
        difficulty=2,
        description="Write a function that returns every second element from a list using slicing.",
        hints=[
            "Use slicing with a step: list[start:stop:step].",
            "step=2 means every second element."
        ],
        solution="def every_second(items):\n    return items[::2]",
        starter_code="def every_second(items):\n    pass",
        function_name="every_second",
        test_cases=[
            (([1, 2, 3, 4, 5],), [1, 3, 5]),
            (([0, 1, 2, 3, 4, 5, 6],), [0, 2, 4, 6]),
            ((['a', 'b', 'c', 'd'],), ['a', 'c']),
        ],
        concepts=["step in slicing"]
    ),
    make_exercise(
        id="ls_13",
        title="Reverse a list with slicing",
        topic="lists_sets",
        difficulty=2,
        description="Write a function that reverses a list using slicing (not the reverse() method).",
        hints=[
            "Use negative step: [::-1].",
            "This creates a new reversed list without modifying the original."
        ],
        solution="def reverse_list(items):\n    return items[::-1]",
        starter_code="def reverse_list(items):\n    pass",
        function_name="reverse_list",
        test_cases=[
            (([1, 2, 3, 4, 5],), [5, 4, 3, 2, 1]),
            ((['a', 'b', 'c'],), ['c', 'b', 'a']),
            (([1],), [1]),
        ],
        concepts=["negative step slicing"]
    ),
    make_exercise(
        id="ls_14",
        title="Basic list comprehension",
        topic="lists_sets",
        difficulty=2,
        description="Write a list comprehension that squares all numbers in a list.",
        hints=[
            "Use the syntax [expression for item in iterable].",
            "The expression here is x**2."
        ],
        solution="def square_all(numbers):\n    return [x**2 for x in numbers]",
        starter_code="def square_all(numbers):\n    pass",
        function_name="square_all",
        test_cases=[
            (([1, 2, 3],), [1, 4, 9]),
            (([0, 1, 2, 3],), [0, 1, 4, 9]),
            (([5],), [25]),
        ],
        concepts=["list comprehension"]
    ),
    make_exercise(
        id="ls_15",
        title="List comprehension with condition",
        topic="lists_sets",
        difficulty=2,
        description="Write a list comprehension that filters a list to keep only even numbers.",
        hints=[
            "Use [expression for item in iterable if condition].",
            "The condition is x % 2 == 0."
        ],
        solution="def filter_even(numbers):\n    return [x for x in numbers if x % 2 == 0]",
        starter_code="def filter_even(numbers):\n    pass",
        function_name="filter_even",
        test_cases=[
            (([1, 2, 3, 4, 5],), [2, 4]),
            (([2, 4, 6, 8],), [2, 4, 6, 8]),
            (([1, 3, 5],), []),
        ],
        concepts=["list comprehension with if"]
    ),
    make_exercise(
        id="ls_16",
        title="Nested lists",
        topic="lists_sets",
        difficulty=2,
        description="Write a function that accesses the element at position [1][2] in a 2D list (matrix).",
        hints=[
            "Use nested indexing: list[row][col].",
            "First index is the row, second is the column."
        ],
        solution="def get_element_2d(matrix):\n    return matrix[1][2]",
        starter_code="def get_element_2d(matrix):\n    pass",
        function_name="get_element_2d",
        test_cases=[
            (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), 6),
            (([[0, 1, 10], [2, 3, 5], [4, 5, 6]],), 5),
        ],
        concepts=["nested lists", "2D indexing"]
    ),
    make_exercise(
        id="ls_17",
        title="Sum of list elements",
        topic="lists_sets",
        difficulty=2,
        description="Write a function that returns the sum of all elements in a list.",
        hints=[
            "Use the sum() built-in function.",
            "Or use a loop or comprehension."
        ],
        solution="def sum_list(numbers):\n    return sum(numbers)",
        starter_code="def sum_list(numbers):\n    pass",
        function_name="sum_list",
        test_cases=[
            (([1, 2, 3, 4],), 10),
            (([0],), 0),
            (([10, 20, 30],), 60),
        ],
        concepts=["sum() function"]
    ),
    make_exercise(
        id="ls_18",
        title="Min and max of list",
        topic="lists_sets",
        difficulty=2,
        description="Write a function that returns a tuple of (min, max) from a list.",
        hints=[
            "Use min() and max() built-in functions.",
            "They work on any iterable."
        ],
        solution="def min_max(numbers):\n    return (min(numbers), max(numbers))",
        starter_code="def min_max(numbers):\n    pass",
        function_name="min_max",
        test_cases=[
            (([1, 5, 3, 9, 2],), (1, 9)),
            (([100],), (100, 100)),
            (([0, -5, 10],), (-5, 10)),
        ],
        concepts=["min() and max() functions"]
    ),
    make_exercise(
        id="ls_19",
        title="Count occurrences",
        topic="lists_sets",
        difficulty=2,
        description="Write a function that counts how many times an element appears in a list.",
        hints=[
            "Use the .count() method.",
            "It returns an integer."
        ],
        solution="def count_element(items, element):\n    return items.count(element)",
        starter_code="def count_element(items, element):\n    pass",
        function_name="count_element",
        test_cases=[
            (([1, 2, 2, 3, 2], 2), 3),
            ((['a', 'b', 'a'], 'a'), 2),
            (([1, 1, 1], 1), 3),
        ],
        concepts=["count() method"]
    ),
    make_exercise(
        id="ls_20",
        title="Copy a list",
        topic="lists_sets",
        difficulty=2,
        description="Write a function that creates a shallow copy of a list.",
        hints=[
            "Use .copy() method or slicing [:].",
            "A copy is independent from the original."
        ],
        solution="def copy_list(items):\n    return items.copy()",
        starter_code="def copy_list(items):\n    pass",
        function_name="copy_list",
        test_cases=[
            (([1, 2, 3],), [1, 2, 3]),
            (([],), []),
            ((['a', 'b'],), ['a', 'b']),
        ],
        concepts=["shallow copy", "copy() method"]
    ),

    # MEDIUM: 21-35 (Sorting, unpacking, zip, enumerate, map/filter, stack/queue)
    make_exercise(
        id="ls_21",
        title="Sort a list",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that sorts a list in ascending order and returns it.",
        hints=[
            "Use .sort() method (modifies in place) or sorted() function (returns new list).",
            "For this exercise, use sorted()."
        ],
        solution="def sort_list(items):\n    return sorted(items)",
        starter_code="def sort_list(items):\n    pass",
        function_name="sort_list",
        test_cases=[
            (([3, 1, 4, 1, 5],), [1, 1, 3, 4, 5]),
            ((['c', 'a', 'b'],), ['a', 'b', 'c']),
            (([-5, 0, 3],), [-5, 0, 3]),
        ],
        concepts=["sorted() function"]
    ),
    make_exercise(
        id="ls_22",
        title="Sort with reverse",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that sorts a list in descending order.",
        hints=[
            "Use sorted() with reverse=True parameter.",
            "Or use .sort(reverse=True)."
        ],
        solution="def sort_descending(items):\n    return sorted(items, reverse=True)",
        starter_code="def sort_descending(items):\n    pass",
        function_name="sort_descending",
        test_cases=[
            (([3, 1, 4, 1, 5],), [5, 4, 3, 1, 1]),
            ((['a', 'c', 'b'],), ['c', 'b', 'a']),
        ],
        concepts=["reverse parameter in sorted()"]
    ),
    make_exercise(
        id="ls_23",
        title="Sort by length",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that sorts a list of strings by their length.",
        hints=[
            "Use sorted() with key=len.",
            "The key parameter specifies a function to extract comparison value."
        ],
        solution="def sort_by_length(words):\n    return sorted(words, key=len)",
        starter_code="def sort_by_length(words):\n    pass",
        function_name="sort_by_length",
        test_cases=[
            ((['apple', 'pie', 'banana'],), ['pie', 'apple', 'banana']),
            ((['a', 'bb', 'ccc'],), ['a', 'bb', 'ccc']),
        ],
        concepts=["key parameter", "sorted with function"]
    ),
    make_exercise(
        id="ls_24",
        title="Unpack a list",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that unpacks a 3-element list into three variables and returns their sum.",
        hints=[
            "Use a, b, c = items.",
            "Unpacking assigns each element to a variable."
        ],
        solution="def unpack_three(items):\n    a, b, c = items\n    return a + b + c",
        starter_code="def unpack_three(items):\n    pass",
        function_name="unpack_three",
        test_cases=[
            (([1, 2, 3],), 6),
            (([10, 20, 30],), 60),
        ],
        concepts=["tuple unpacking", "list unpacking"]
    ),
    make_exercise(
        id="ls_25",
        title="Unpack with *",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that unpacks a list with a leading element and captures the rest in a variable.",
        hints=[
            "Use a, *rest = items.",
            "The * operator captures remaining elements as a list."
        ],
        solution="def unpack_rest(items):\n    first, *rest = items\n    return first, rest",
        starter_code="def unpack_rest(items):\n    pass",
        function_name="unpack_rest",
        test_cases=[
            (([1, 2, 3, 4],), (1, [2, 3, 4])),
            (([10],), (10, [])),
        ],
        concepts=["extended unpacking", "* operator"]
    ),
    make_exercise(
        id="ls_26",
        title="Zip two lists",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that pairs elements from two lists using zip().",
        hints=[
            "Use zip(list1, list2) to pair elements.",
            "Convert to list if needed for the test."
        ],
        solution="def zip_lists(a, b):\n    return list(zip(a, b))",
        starter_code="def zip_lists(a, b):\n    pass",
        function_name="zip_lists",
        test_cases=[
            (([1, 2, 3], ['a', 'b', 'c']), [(1, 'a'), (2, 'b'), (3, 'c')]),
            (([1, 2], ['x', 'y']), [(1, 'x'), (2, 'y')]),
        ],
        concepts=["zip() function"]
    ),
    make_exercise(
        id="ls_27",
        title="Enumerate a list",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that uses enumerate to create a list of (index, value) tuples.",
        hints=[
            "Use enumerate(items) to get index-value pairs.",
            "Convert to list for the test."
        ],
        solution="def enumerate_list(items):\n    return list(enumerate(items))",
        starter_code="def enumerate_list(items):\n    pass",
        function_name="enumerate_list",
        test_cases=[
            ((['a', 'b', 'c'],), [(0, 'a'), (1, 'b'), (2, 'c')]),
            (([10, 20],), [(0, 10), (1, 20)]),
        ],
        concepts=["enumerate() function"]
    ),
    make_exercise(
        id="ls_28",
        title="Map function",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that applies a function to each element using map().",
        hints=[
            "Use map(func, list) to apply a function.",
            "Convert to list for the result."
        ],
        solution="def map_square(numbers):\n    return list(map(lambda x: x**2, numbers))",
        starter_code="def map_square(numbers):\n    pass",
        function_name="map_square",
        test_cases=[
            (([1, 2, 3],), [1, 4, 9]),
            (([0, 1, 2],), [0, 1, 4]),
        ],
        concepts=["map() function", "lambda"]
    ),
    make_exercise(
        id="ls_29",
        title="Filter function",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that filters a list to keep only elements that satisfy a condition using filter().",
        hints=[
            "Use filter(func, list) where func returns True/False.",
            "Convert to list for the result."
        ],
        solution="def filter_positive(numbers):\n    return list(filter(lambda x: x > 0, numbers))",
        starter_code="def filter_positive(numbers):\n    pass",
        function_name="filter_positive",
        test_cases=[
            (([-1, 2, -3, 4],), [2, 4]),
            (([-5, 0, 5],), [5]),
        ],
        concepts=["filter() function"]
    ),
    make_exercise(
        id="ls_30",
        title="Flatten a nested list",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that flattens a 2D list (list of lists) into a single list.",
        hints=[
            "Use list comprehension with nested iteration.",
            "Or use sum() with an empty list as start: sum(list, [])."
        ],
        solution="def flatten(matrix):\n    return [item for row in matrix for item in row]",
        starter_code="def flatten(matrix):\n    pass",
        function_name="flatten",
        test_cases=[
            (([[1, 2], [3, 4]],), [1, 2, 3, 4]),
            (([['a', 'b'], ['c']],), ['a', 'b', 'c']),
        ],
        concepts=["nested list comprehension", "flattening"]
    ),
    make_exercise(
        id="ls_31",
        title="Rotate a list",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that rotates a list to the right by n positions.",
        hints=[
            "Use slicing: last n elements + first (len-n) elements.",
            "If n=2 and list=[1,2,3,4], result is [3,4,1,2]."
        ],
        solution="def rotate_right(items, n):\n    n = n % len(items) if items else 0\n    return items[-n:] + items[:-n] if n else items[:]",
        starter_code="def rotate_right(items, n):\n    pass",
        function_name="rotate_right",
        test_cases=[
            (([1, 2, 3, 4], 2), [3, 4, 1, 2]),
            (([1, 2, 3], 1), [3, 1, 2]),
            (([1, 2], 0), [1, 2]),
        ],
        concepts=["list slicing", "rotation"]
    ),
    make_exercise(
        id="ls_32",
        title="Remove duplicates (order preserved)",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that removes duplicates from a list while preserving the original order.",
        hints=[
            "Use a set to track seen elements.",
            "Iterate through and keep only the first occurrence."
        ],
        solution="def remove_duplicates(items):\n    seen = set()\n    result = []\n    for item in items:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result",
        starter_code="def remove_duplicates(items):\n    pass",
        function_name="remove_duplicates",
        test_cases=[
            (([1, 2, 2, 3, 1, 4],), [1, 2, 3, 4]),
            ((['a', 'b', 'a'],), ['a', 'b']),
            (([1, 2, 3],), [1, 2, 3]),
        ],
        concepts=["deduplication", "set usage"]
    ),
    make_exercise(
        id="ls_33",
        title="Find common elements",
        topic="lists_sets",
        difficulty=3,
        description="Write a function that finds common elements between two lists and returns a set.",
        hints=[
            "Convert to sets and use intersection.",
            "Or use a loop with membership test."
        ],
        solution="def common_elements(list1, list2):\n    return set(list1) & set(list2)",
        starter_code="def common_elements(list1, list2):\n    pass",
        function_name="common_elements",
        test_cases=[
            (([1, 2, 3], [2, 3, 4]), {2, 3}),
            (([1, 2], [3, 4]), set()),
        ],
        concepts=["set intersection"]
    ),
    make_exercise(
        id="ls_34",
        title="Stack with list (LIFO)",
        topic="lists_sets",
        difficulty=3,
        description="Write a Stack class using a list that supports push and pop operations.",
        hints=[
            "Use append() for push (add to end).",
            "Use pop() for pop (remove from end)."
        ],
        solution="""class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()""",
        starter_code="class Stack:\n    pass",
        function_name="Stack",
        test_cases=[],
        check=lambda ns: (
            hasattr(ns.get("Stack"), "push") and hasattr(ns.get("Stack"), "pop"),
            "Stack should have push and pop methods"
        ),
        concepts=["stack pattern", "LIFO"]
    ),
    make_exercise(
        id="ls_35",
        title="Queue with list (FIFO)",
        topic="lists_sets",
        difficulty=3,
        description="Write a Queue class using a list that supports enqueue and dequeue operations.",
        hints=[
            "Use append() for enqueue (add to end).",
            "Use pop(0) for dequeue (remove from beginning)."
        ],
        solution="""class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)""",
        starter_code="class Queue:\n    pass",
        function_name="Queue",
        test_cases=[],
        check=lambda ns: (
            hasattr(ns.get("Queue"), "enqueue") and hasattr(ns.get("Queue"), "dequeue"),
            "Queue should have enqueue and dequeue methods"
        ),
        concepts=["queue pattern", "FIFO"]
    ),

    # HARD: 36-45 (Set operations, frozenset, complex comprehensions, performance)
    make_exercise(
        id="ls_36",
        title="Create a set",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that creates a set from a list and returns its length.",
        hints=[
            "Use set(list) to create a set.",
            "Sets remove duplicates automatically."
        ],
        solution="def make_set(items):\n    return len(set(items))",
        starter_code="def make_set(items):\n    pass",
        function_name="make_set",
        test_cases=[
            (([1, 1, 2, 3],), 3),
            (([1, 2, 3],), 3),
            (([], ), 0),
        ],
        concepts=["set creation"]
    ),
    make_exercise(
        id="ls_37",
        title="Set union",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that returns the union of two sets.",
        hints=[
            "Use | operator or .union() method.",
            "Union includes all elements from both sets."
        ],
        solution="def set_union(set1, set2):\n    return set1 | set2",
        starter_code="def set_union(set1, set2):\n    pass",
        function_name="set_union",
        test_cases=[
            (({1, 2}, {2, 3}), {1, 2, 3}),
            (({1}, {2}), {1, 2}),
        ],
        concepts=["set union", "| operator"]
    ),
    make_exercise(
        id="ls_38",
        title="Set intersection",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that returns the intersection of two sets.",
        hints=[
            "Use & operator or .intersection() method.",
            "Intersection includes only common elements."
        ],
        solution="def set_intersection(set1, set2):\n    return set1 & set2",
        starter_code="def set_intersection(set1, set2):\n    pass",
        function_name="set_intersection",
        test_cases=[
            (({1, 2, 3}, {2, 3, 4}), {2, 3}),
            (({1, 2}, {3, 4}), set()),
        ],
        concepts=["set intersection", "& operator"]
    ),
    make_exercise(
        id="ls_39",
        title="Set difference",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that returns elements in set1 but not in set2.",
        hints=[
            "Use - operator or .difference() method.",
            "a - b = elements in a but not in b."
        ],
        solution="def set_difference(set1, set2):\n    return set1 - set2",
        starter_code="def set_difference(set1, set2):\n    pass",
        function_name="set_difference",
        test_cases=[
            (({1, 2, 3}, {2, 3, 4}), {1}),
            (({1, 2}, {3, 4}), {1, 2}),
        ],
        concepts=["set difference", "- operator"]
    ),
    make_exercise(
        id="ls_40",
        title="Set symmetric difference",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that returns elements in either set but not both.",
        hints=[
            "Use ^ operator or .symmetric_difference() method.",
            "a ^ b = (a - b) | (b - a)."
        ],
        solution="def set_sym_diff(set1, set2):\n    return set1 ^ set2",
        starter_code="def set_sym_diff(set1, set2):\n    pass",
        function_name="set_sym_diff",
        test_cases=[
            (({1, 2, 3}, {2, 3, 4}), {1, 4}),
            (({1, 2}, {1, 2}), set()),
        ],
        concepts=["symmetric difference", "^ operator"]
    ),
    make_exercise(
        id="ls_41",
        title="Set add and discard",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that adds an element to a set, then discards another, returning the modified set.",
        hints=[
            "Use .add() to add an element.",
            "Use .discard() to remove without error if not present."
        ],
        solution="def modify_set(s, add_elem, discard_elem):\n    s.add(add_elem)\n    s.discard(discard_elem)\n    return s",
        starter_code="def modify_set(s, add_elem, discard_elem):\n    pass",
        function_name="modify_set",
        test_cases=[
            (({1, 2}, 3, 1), {2, 3}),
            (({1}, 2, 3), {1, 2}),
        ],
        concepts=["add() and discard() methods"]
    ),
    make_exercise(
        id="ls_42",
        title="Set comprehension",
        topic="lists_sets",
        difficulty=4,
        description="Write a set comprehension that creates a set of squares of numbers.",
        hints=[
            "Use {expression for item in iterable}.",
            "Similar to list comprehension but with braces and produces a set."
        ],
        solution="def square_set(numbers):\n    return {x**2 for x in numbers}",
        starter_code="def square_set(numbers):\n    pass",
        function_name="square_set",
        test_cases=[
            (([1, 2, 3],), {1, 4, 9}),
            (([1, 2, 2, 3],), {1, 4, 9}),
        ],
        concepts=["set comprehension"]
    ),
    make_exercise(
        id="ls_43",
        title="Frozenset basics",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that creates an immutable frozenset from a list.",
        hints=[
            "Use frozenset(iterable) to create an immutable set.",
            "Frozensets can be used as dictionary keys."
        ],
        solution="def make_frozenset(items):\n    return frozenset(items)",
        starter_code="def make_frozenset(items):\n    pass",
        function_name="make_frozenset",
        test_cases=[
            (([1, 2, 3],), frozenset({1, 2, 3})),
            (([],), frozenset()),
        ],
        concepts=["frozenset"]
    ),
    make_exercise(
        id="ls_44",
        title="Subset and superset",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that checks if set1 is a subset of set2.",
        hints=[
            "Use <= operator or .issubset() method.",
            "a <= b means all elements of a are in b."
        ],
        solution="def is_subset(set1, set2):\n    return set1 <= set2",
        starter_code="def is_subset(set1, set2):\n    pass",
        function_name="is_subset",
        test_cases=[
            (({1, 2}, {1, 2, 3}), True),
            (({1, 2}, {2, 3}), False),
            (({1}, {1}), True),
        ],
        concepts=["subset", "<= operator"]
    ),
    make_exercise(
        id="ls_45",
        title="Group by value (dict with lists)",
        topic="lists_sets",
        difficulty=4,
        description="Write a function that groups students by their grade, returning a dict where keys are grades and values are lists of student names.",
        hints=[
            "Use a dictionary comprehension or loop.",
            "Collect students with the same grade in a list."
        ],
        solution="""def group_by_grade(students):
    # students is a list of (name, grade) tuples
    groups = {}
    for name, grade in students:
        if grade not in groups:
            groups[grade] = []
        groups[grade].append(name)
    return groups""",
        starter_code="def group_by_grade(students):\n    pass",
        function_name="group_by_grade",
        test_cases=[
            (([('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A')],), {'A': ['Alice', 'Charlie'], 'B': ['Bob']}),
        ],
        concepts=["grouping", "dictionary construction"]
    ),

    # CHALLENGE: 46-50 (Advanced scenarios, real-world applications)
    make_exercise(
        id="ls_46",
        title="Leaderboard ranking",
        topic="lists_sets",
        difficulty=5,
        description="Write a function that takes a list of (player, score) tuples and returns a sorted leaderboard as a list of player names, highest score first. Players with the same score maintain original order.",
        hints=[
            "Use sorted() with a key function that sorts by score in reverse.",
            "Use key=lambda x: -x[1] or key=lambda x: x[1], reverse=True."
        ],
        solution="def leaderboard(players):\n    return [name for name, score in sorted(players, key=lambda x: x[1], reverse=True)]",
        starter_code="def leaderboard(players):\n    pass",
        function_name="leaderboard",
        test_cases=[
            (([('Alice', 100), ('Bob', 90), ('Charlie', 100)],), ['Alice', 'Charlie', 'Bob']),
            (([('Eve', 50)],), ['Eve']),
        ],
        concepts=["sorting with key", "unpacking"]
    ),
    make_exercise(
        id="ls_47",
        title="Find unique tags",
        topic="lists_sets",
        difficulty=5,
        description="Write a function that takes a list of posts (each is a dict with 'tags' key containing a list), and returns a sorted list of all unique tags across all posts.",
        hints=[
            "Flatten all tags from all posts.",
            "Use a set to get unique tags."
        ],
        solution="""def unique_tags(posts):
    all_tags = set()
    for post in posts:
        all_tags.update(post['tags'])
    return sorted(list(all_tags))""",
        starter_code="def unique_tags(posts):\n    pass",
        function_name="unique_tags",
        test_cases=[
            (([{'tags': ['python', 'coding']}, {'tags': ['python', 'ai']}],), ['ai', 'coding', 'python']),
        ],
        concepts=["set operations", "dict iteration"]
    ),
    make_exercise(
        id="ls_48",
        title="Shopping cart operations",
        topic="lists_sets",
        difficulty=5,
        description="Write a function that takes two lists of item IDs: 'cart' and 'wishlist'. Return items that are in cart but not in wishlist (things to remove) as a set.",
        hints=[
            "Convert to sets and use set difference.",
            "cart - wishlist gives items in cart but not in wishlist."
        ],
        solution="def items_to_remove(cart, wishlist):\n    return set(cart) - set(wishlist)",
        starter_code="def items_to_remove(cart, wishlist):\n    pass",
        function_name="items_to_remove",
        test_cases=[
            (([1, 2, 3, 4], [1, 2]), {3, 4}),
        ],
        concepts=["set difference", "practical application"]
    ),
    make_exercise(
        id="ls_49",
        title="Matrix transpose",
        topic="lists_sets",
        difficulty=5,
        description="Write a function that transposes a 2D list (matrix). Rows become columns and columns become rows.",
        hints=[
            "Use zip() with unpacking: list(zip(*matrix)).",
            "zip unpacks rows and pairs columns together."
        ],
        solution="def transpose(matrix):\n    return [list(row) for row in zip(*matrix)]",
        starter_code="def transpose(matrix):\n    pass",
        function_name="transpose",
        test_cases=[
            (([[1, 2], [3, 4]],), [[1, 3], [2, 4]]),
            (([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
        ],
        concepts=["zip with unpacking", "matrix operations"]
    ),
    make_exercise(
        id="ls_50",
        title="Inventory management",
        topic="lists_sets",
        difficulty=5,
        description="Write a function that manages inventory: given a list of purchases (item_id, quantity), return a dict counting total quantity per item, ignoring items with negative quantity (returns/refunds).",
        hints=[
            "Filter out negative quantities first.",
            "Use a dict or defaultdict to accumulate quantities."
        ],
        solution="""def inventory_total(purchases):
    inventory = {}
    for item_id, qty in purchases:
        if qty > 0:
            if item_id not in inventory:
                inventory[item_id] = 0
            inventory[item_id] += qty
    return inventory""",
        starter_code="def inventory_total(purchases):\n    pass",
        function_name="inventory_total",
        test_cases=[
            (([('A', 5), ('B', 3), ('A', 2), ('B', -1)],), {'A': 7, 'B': 3}),
            (([('X', 10)],), {'X': 10}),
        ],
        concepts=["dict accumulation", "filtering", "real-world scenario"]
    ),
]
