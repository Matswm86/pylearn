window.PYLEARN_LESSONS = {
  "variables": {
    icon: "📦",
    subtitle: "Learn how to store and name your data",
    sections: [
      {
        title: "What Is a Variable?",
        content: `<p>Imagine you have a labeled box where you can store things. That's what a <strong>variable</strong> is — it's a container with a name that holds information.</p>
<p>In real life, you might label a box "WINTER CLOTHES" and put sweaters inside. In Python, you might create a box called <code>name</code> and put the text "Alice" inside it. The box remembers what's in it, and whenever you need that information, you just use the label.</p>
<p>Why do we need variables? Because it's way easier to write <code>name</code> than to type out "Alice" a hundred times!</p>`,
        examples: [
          {
            code: "favorite_food = \"pizza\"\nprint(favorite_food)",
            output: "pizza",
            explanation: "We created a variable called <code>favorite_food</code> and put the text \"pizza\" inside it. Then we used <code>print()</code> to display what's in the box."
          },
          {
            code: "age = 25\nprint(age)",
            output: "25",
            explanation: "This time we put a number (25) into a variable called <code>age</code>. Variables can hold numbers too!"
          }
        ]
      },
      {
        title: "Creating Your First Variable",
        content: `<p>To create a variable, you use the <strong>equals sign (=)</strong>. But here's the key: <code>=</code> does NOT mean \"equals\" like in math class. It means <strong>\"put this in the box.\"</strong></p>
<p>The format is always: <code>box_name = what_to_put_in</code>.</p>
<p>Once you've created a variable, you can use it anytime you want.</p>`,
        examples: [
          {
            code: "city = \"Paris\"\nprint(city)\nprint(city)\nprint(city)",
            output: "Paris\nParis\nParis",
            explanation: "We created a variable <code>city</code> with \"Paris\" inside. Now we can print it three times without typing \"Paris\" three times!"
          },
          {
            code: "temperature = 72\nprint(temperature)",
            output: "72",
            explanation: "Variable names can describe what's inside them. <code>temperature = 72</code> is way clearer than just writing 72 everywhere."
          }
        ]
      },
      {
        title: "Different Types of Boxes",
        content: `<p>Variables can hold different kinds of information. The main types are:</p>
<ul>
<li><strong>Numbers (integers)</strong> — whole numbers like 5, 100, -3</li>
<li><strong>Decimals (floats)</strong> — numbers with a decimal point like 3.14, 2.5</li>
<li><strong>Text (strings)</strong> — anything in quotes like \"hello\" or \"42 Main Street\"</li>
<li><strong>True/False (booleans)</strong> — just two options: True or False</li>
</ul>
<p>Python figures out which type based on what you put in. Numbers without quotes are numbers. Anything in quotes is text.</p>`,
        examples: [
          {
            code: "count = 5\nprice = 19.99\nname = \"Sarah\"\nis_raining = True\nprint(count, price, name, is_raining)",
            output: "5 19.99 Sarah True",
            explanation: "We created four variables with four different types: a whole number, a decimal, text, and True/False."
          },
          {
            code: "score = 100\nhigh_score = \"100\"\nprint(score)\nprint(high_score)",
            output: "100\n100",
            explanation: "Both look the same when printed, but <code>score</code> is a number (we can do math with it) and <code>high_score</code> is text (we can't do math with text)."
          }
        ]
      },
      {
        title: "Variable Naming Rules",
        content: `<p>You can't name variables anything you want. Python has a few rules:</p>
<ul>
<li>Use <strong>snake_case</strong> — lowercase with underscores like <code>favorite_color</code> or <code>user_age</code></li>
<li>Names can have letters, numbers, and underscores</li>
<li>Can't start with a number</li>
<li>Can't use spaces (that's why we use underscores)</li>
<li>Can't use special characters like <code>!</code> or <code>@</code></li>
<li>Variable names are <strong>case-sensitive</strong> — <code>name</code> and <code>Name</code> are different boxes</li>
</ul>
<p>Pick names that describe what's inside. \"user_age\" is better than \"x\" because future-you will know what it contains.</p>`,
        examples: [
          {
            code: "# Good variable names\nfavorite_color = \"blue\"\nuser_age = 30\nteam_members = 5\n\n# Less helpful\nx = \"blue\"\ny = 30\nz = 5",
            output: "(No output, just comments)",
            explanation: "The first set of variable names tells you exactly what they contain. The second set (x, y, z) makes you guess. Use descriptive names!"
          },
          {
            code: "first_name = \"Alex\"\nLast_name = \"Jones\"\nprint(first_name, Last_name)",
            output: "Alex Jones",
            explanation: "Python treats <code>first_name</code> and <code>Last_name</code> as completely different variables because of capitalization. Stick to lowercase with underscores for consistency."
          }
        ]
      },
      {
        title: "Changing What's in the Box (Reassignment)",
        content: `<p>Variables aren't locked. You can change what's inside anytime by using <code>=</code> again.</p>
<p>This is super useful when you want to update information — like changing your password or moving to a new city.</p>
<p>When you assign a new value, the old value is thrown away. The variable now holds something different.</p>`,
        examples: [
          {
            code: "score = 10\nprint(score)\nscore = 15\nprint(score)",
            output: "10\n15",
            explanation: "First, <code>score</code> contains 10. Then we change it to 15. The first value is gone."
          },
          {
            code: "location = \"New York\"\nprint(\"I live in\", location)\nlocation = \"London\"\nprint(\"I live in\", location)",
            output: "I live in New York\nI live in London",
            explanation: "We moved! We updated the variable to the new location."
          }
        ]
      },
      {
        title: "Using Variables Together",
        content: `<p>The real power of variables comes when you combine them. You can add numbers together, join text together, or create messages.</p>
<p>One powerful trick is called an <strong>f-string</strong> (formatted string). It lets you put variables inside text using curly braces: <code>f\"Hello, {name}!\"</code></p>`,
        examples: [
          {
            code: "first = 5\nsecond = 3\ntotal = first + second\nprint(total)",
            output: "8",
            explanation: "We stored two numbers in variables, added them together, and stored the result in a new variable."
          },
          {
            code: "name = \"Alex\"\nage = 28\nmessage = f\"My name is {name} and I'm {age} years old\"\nprint(message)",
            output: "My name is Alex and I'm 28 years old",
            explanation: "The f-string puts the values of <code>name</code> and <code>age</code> directly into the text. The curly braces <code>{}</code> are placeholders."
          }
        ]
      }
    ],
    tips: [
      "Variable names should describe what's inside. Use clear names so you remember what each box contains.",
      "Use snake_case (lowercase with underscores) for all variable names. It's the Python tradition.",
      "When you assign a new value to a variable, the old value disappears forever.",
      "F-strings (the f before quotes) are your best friend when you want to combine variables and text.",
      "Don't be afraid to use long variable names. <code>user_email</code> is better than <code>ue</code>, even if it takes longer to type."
    ],
    common_mistakes: [
      {
        mistake: "Using = to check if two things are equal",
        fix: "Use == to compare (two equals signs). Use = to assign (one equals sign).",
        code: "Wrong: if name = \"Alice\":\nRight: if name == \"Alice\":"
      },
      {
        mistake: "Using spaces in variable names",
        fix: "Use underscores instead of spaces. Python won't let you have spaces.",
        code: "Wrong: my age = 25\nRight: my_age = 25"
      },
      {
        mistake: "Starting a variable name with a number",
        fix: "Always start with a letter. Numbers can come after.",
        code: "Wrong: 1st_name = \"Alice\"\nRight: first_name = \"Alice\""
      },
      {
        mistake: "Forgetting to use the variable",
        fix: "Create the variable first, then use it in your code.",
        code: "Wrong: print(name)\nRight: name = \"Alice\"\\nprint(name)"
      },
      {
        mistake: "Mixing up text and numbers",
        fix: "Text goes in quotes. Numbers don't.",
        code: "Wrong: age = \"25\" (now you can't do math with it)\nRight: age = 25"
      }
    ]
  },

  "data_types": {
    icon: "🎭",
    subtitle: "Understand the different kinds of data Python can work with",
    sections: [
      {
        title: "The 4 Main Data Types",
        content: `<p>Python groups information into four main types. Think of them as different containers in a kitchen:</p>
<ul>
<li><strong>int (integer)</strong> — whole numbers, no decimal point (like counting apples: 5, 10, -3)</li>
<li><strong>float</strong> — numbers with decimals (like measuring liquid: 2.5 liters, 3.14)</li>
<li><strong>str (string)</strong> — text (like a grocery list: \"milk\", \"eggs\", \"bread\")</li>
<li><strong>bool (boolean)</strong> — True or False (like a light switch: on or off)</li>
</ul>
<p>Python automatically figures out which type based on what you write. 5 is an int. \"5\" is a string. 5.0 is a float.</p>`,
        examples: [
          {
            code: "apples = 5\nprice = 2.50\nstore = \"Whole Foods\"\nis_open = True\n\nprint(apples)\nprint(price)\nprint(store)\nprint(is_open)",
            output: "5\n2.5\nWhole Foods\nTrue",
            explanation: "Four different types, four different containers. The integer is a whole count. The float has a decimal. The string is text. The boolean is just True or False."
          },
          {
            code: "temperature = 72\nbalance = 100.50\nusername = \"alex_42\"\nhas_premium = False\n\nprint(temperature, balance, username, has_premium)",
            output: "72 100.5 alex_42 False",
            explanation: "Each variable holds a different type. Python keeps track automatically."
          }
        ]
      },
      {
        title: "Checking Data Types with type()",
        content: `<p>Sometimes you need to know what type a variable is. Use the <code>type()</code> function and Python will tell you.</p>
<p>This is super helpful when things aren't working the way you expect. Maybe you thought you had a number, but it's actually text!</p>`,
        examples: [
          {
            code: "age = 25\nprice = \"19.99\"\nis_student = True\n\nprint(type(age))\nprint(type(price))\nprint(type(is_student))",
            output: "<class 'int'>\n<class 'str'>\n<class 'bool'>",
            explanation: "We created three variables and checked their types. Age is an integer. Price is text (a string), even though it looks like a number. is_student is a boolean."
          },
          {
            code: "x = 5\ny = 5.0\nz = \"5\"\n\nprint(type(x), type(y), type(z))",
            output: "<class 'int'> <class 'float'> <class 'str'>",
            explanation: "5 without quotes is an int. 5.0 with a decimal point is a float. \"5\" in quotes is a string. Same value, three different types!"
          }
        ]
      },
      {
        title: "Converting Between Types",
        content: `<p>Sometimes you need to change a variable from one type to another. Imagine ordering pizza: you might say \"3 pizzas\" (a number) but someone wrote it down as \"three pizzas\" (text). You need to convert.</p>
<p>Use <code>int()</code>, <code>float()</code>, and <code>str()</code> to convert between types.</p>`,
        examples: [
          {
            code: "# String to integer\nage_text = \"30\"\nage_number = int(age_text)\nprint(age_number)\nprint(type(age_number))",
            output: "30\n<class 'int'>",
            explanation: "We had the text \"30\" and converted it to the number 30. Now we can do math with it!"
          },
          {
            code: "# Integer to string\ncount = 42\ncount_text = str(count)\nprint(count_text)\nprint(type(count_text))",
            output: "42\n<class 'str'>",
            explanation: "We converted the number 42 to the text \"42\". Now it's a string we can put in sentences."
          }
        ]
      },
      {
        title: "String Superpowers",
        content: `<p>Strings have special abilities. You can:</p>
<ul>
<li><code>.upper()</code> — convert to UPPERCASE</li>
<li><code>.lower()</code> — convert to lowercase</li>
<li><code>.replace(old, new)</code> — swap one part for another</li>
<li><code>.split()</code> — break a string into pieces</li>
<li><code>.join()</code> — glue pieces back together</li>
<li><code>.strip()</code> — remove extra spaces</li>
</ul>
<p>Notice the dot (.). It means \"use this ability on this string.\"</p>`,
        examples: [
          {
            code: "sentence = \"hello world\"\nprint(sentence.upper())\nprint(sentence.lower())\nprint(sentence.replace(\"world\", \"Python\"))",
            output: "HELLO WORLD\nhello world\nhello Python",
            explanation: "String methods transform text. <code>.upper()</code> makes it big. <code>.replace()</code> swaps parts. These don't change the original variable."
          },
          {
            code: "ingredients = \"apples, bananas, oranges\"\nlist_of_items = ingredients.split(\", \")\nprint(list_of_items)\n\nback_together = \" and \".join(list_of_items)\nprint(back_together)",
            output: "['apples', 'bananas', 'oranges']\napples and bananas and oranges",
            explanation: "<code>.split()</code> breaks the text into pieces (we'll learn about lists soon). <code>.join()</code> glues pieces together with \"and\" between them."
          }
        ]
      },
      {
        title: "Number Tricks",
        content: `<p>Numbers have special abilities too. You can round them, divide them, and find remainders:</p>
<ul>
<li><code>round(number)</code> — round to nearest whole number</li>
<li><code>//</code> — integer division (divide and throw away the decimal)</li>
<li><code>%</code> — modulo (find the remainder after dividing)</li>
<li><code>**</code> — exponent (power)</li>
</ul>`,
        examples: [
          {
            code: "price = 19.99\nprint(round(price))\nprint(round(price, 1))",
            output: "20\n20.0",
            explanation: "<code>round(price)</code> rounds to the nearest whole number. <code>round(price, 1)</code> rounds to 1 decimal place."
          },
          {
            code: "# Integer division\nprint(7 // 2)  # How many 2s go into 7?\nprint(7 % 2)   # What's left over?\nprint(10 ** 2) # 10 to the power of 2",
            output: "3\n1\n100",
            explanation: "7 divided by 2 is 3 with remainder 1. So <code>7 // 2</code> gives 3. <code>7 % 2</code> gives 1. <code>**</code> is exponent: 10 × 10 = 100."
          }
        ]
      },
      {
        title: "Truthiness: True and False",
        content: `<p>In Python, some things are <strong>truthy</strong> (count as True) and some are <strong>falsy</strong> (count as False).</p>
<ul>
<li><strong>False:</strong> False, 0, 0.0, empty strings, empty lists, None</li>
<li><strong>True:</strong> True, any non-zero number, non-empty strings, non-empty lists</li>
</ul>
<p>This matters when you use variables in if statements. An empty string <code>\"\"</code> counts as False. A string with text counts as True.</p>`,
        examples: [
          {
            code: "name = \"Alice\"\nif name:\n    print(\"Name exists\")\n\nempty_name = \"\"\nif empty_name:\n    print(\"This won't print\")\nelse:\n    print(\"Name is empty\")",
            output: "Name exists\nName is empty",
            explanation: "A non-empty string is truthy, so the if runs. An empty string is falsy, so the else runs."
          },
          {
            code: "count = 0\nif count:\n    print(\"We have items\")\nelse:\n    print(\"No items\")\n\ncount = 5\nif count:\n    print(\"We have items\")",
            output: "No items\nWe have items",
            explanation: "Zero is falsy. Five is truthy. This is why checking <code>if items</code> works — empty lists are false, lists with stuff are true."
          }
        ]
      }
    ],
    tips: [
      "Remember: 5 is different from \"5\" from 5.0. All different types with different abilities.",
      "Use int() for whole numbers you'll do math with. Use str() when you need text for messages or display.",
      "F-strings automatically convert numbers to text inside {} so you don't have to use str().",
      "Test types with type() when things aren't working. It's often a type mismatch!",
      "Empty things are falsy: \"\", [], 0. Non-empty things are truthy. This is super useful for checking if something exists."
    ],
    common_mistakes: [
      {
        mistake: "Forgetting quotes around text",
        fix: "Always use quotes for text. Without quotes, Python thinks it's a variable name.",
        code: "Wrong: name = Alice\nRight: name = \"Alice\""
      },
      {
        mistake: "Trying to do math with text",
        fix: "Convert text to numbers first using int() or float().",
        code: "Wrong: result = \"10\" + \"5\" (gives \"105\", not 15)\nRight: result = int(\"10\") + int(\"5\")"
      },
      {
        mistake: "Using int() on a float that has decimals",
        fix: "If you need to preserve decimals, use float(). int() cuts off everything after the decimal.",
        code: "int(3.99) gives 3, not 4. Use round(3.99) if you want to round."
      },
      {
        mistake: "Not remembering what type you have",
        fix: "When confused, use type() to check. Takes two seconds and saves hours of debugging.",
        code: "print(type(your_variable))"
      },
      {
        mistake: "Changing a variable's type without realizing it",
        fix: "Be intentional. If you mean to convert, use int(), str(), etc. explicitly.",
        code: "Wrong: price = 10; price = \"10\" (oops, now it's text)\nRight: price_text = str(price)"
      }
    ]
  },

  "conditionals": {
    icon: "🚦",
    subtitle: "Make decisions in your code with if, else, and elif",
    sections: [
      {
        title: "Making Decisions: The Traffic Light",
        content: `<p>Real life is full of decisions. If it's raining, take an umbrella. If it's sunny, wear sunscreen. If it's cold, wear a jacket.</p>
<p>Code works the same way. You give Python a condition to check, and it decides what to do based on the answer: True or False.</p>
<p>This is the foundation of making your programs smart — they don't do the same thing every time; they react to situations.</p>`,
        examples: [
          {
            code: "age = 18\nif age >= 18:\n    print(\"You can vote\")",
            output: "You can vote",
            explanation: "We check if age is 18 or more. It is, so the code inside the if block runs. If age was 15, nothing would print."
          },
          {
            code: "score = 45\nif score > 50:\n    print(\"You passed\")",
            output: "(nothing prints)",
            explanation: "The score is 45, which is NOT greater than 50. The condition is False, so the code doesn't run."
          }
        ]
      },
      {
        title: "if/else: Two Paths",
        content: `<p>Sometimes you want to do one thing if a condition is True and something else if it's False.</p>
<p>Use <code>if</code> for when the condition is True, and <code>else</code> for when it's False. It's like: \"If it's raining, take an umbrella. Else, wear sunglasses.\"</p>
<p>Notice the colon (:) at the end and the indentation (spaces) before the code inside the blocks.</p>`,
        examples: [
          {
            code: "age = 15\nif age >= 16:\n    print(\"You can drive\")\nelse:\n    print(\"You're too young to drive\")",
            output: "You're too young to drive",
            explanation: "Age is 15, which is less than 16. The if condition is False, so the else block runs."
          },
          {
            code: "password = \"secret123\"\nif password == \"secret123\":\n    print(\"Welcome!\")\nelse:\n    print(\"Wrong password\")",
            output: "Welcome!",
            explanation: "The password matches, so the if block runs. Notice: we use == to check if two things are equal (not =, which assigns)."
          }
        ]
      },
      {
        title: "if/elif/else: Multiple Paths",
        content: `<p>What if you have more than two choices? Use <code>elif</code> (else if) to check additional conditions.</p>
<p>Think of a restaurant menu: If you want Italian, go to the Italian section. Else if you want Chinese, go there. Else if you want Mexican... and so on.</p>
<p>Python checks conditions from top to bottom. Once one is True, it stops and skips the rest.</p>`,
        examples: [
          {
            code: "score = 85\nif score >= 90:\n    grade = \"A\"\nelif score >= 80:\n    grade = \"B\"\nelif score >= 70:\n    grade = \"C\"\nelse:\n    grade = \"F\"\n\nprint(f\"Your grade is {grade}\")",
            output: "Your grade is B",
            explanation: "Score is 85. It's not >= 90, so we skip the first if. It IS >= 80, so the first elif is True. We assign \"B\" and stop checking."
          },
          {
            code: "time = 14  # 2 PM\nif time < 12:\n    greeting = \"Good morning\"\nelif time < 18:\n    greeting = \"Good afternoon\"\nelse:\n    greeting = \"Good evening\"\n\nprint(greeting)",
            output: "Good afternoon",
            explanation: "Time is 14. It's not less than 12. But it IS less than 18, so the first elif matches."
          }
        ]
      },
      {
        title: "Comparison Operators",
        content: `<p>To make decisions, you need to compare things. Here are the comparison operators:</p>
<ul>
<li><code>==</code> — equals (two things are the same)</li>
<li><code>!=</code> — not equals (two things are different)</li>
<li><code>&lt;</code> — less than</li>
<li><code>&gt;</code> — greater than</li>
<li><code>&lt;=</code> — less than or equal to</li>
<li><code>&gt;=</code> — greater than or equal to</li>
</ul>
<p><strong>CRITICAL:</strong> Remember: <code>=</code> assigns a value. <code>==</code> compares two values. This is the #1 beginner mistake!</p>`,
        examples: [
          {
            code: "x = 5\ny = 5\n\nprint(x == y)  # Are they equal?\nprint(x != y)  # Are they different?\nprint(x < 10)  # Is x less than 10?\nprint(x >= 5)  # Is x greater than or equal to 5?",
            output: "True\nFalse\nTrue\nTrue",
            explanation: "x and y are both 5, so they're equal (True). They're not different (False). 5 is less than 10 (True). 5 is >= 5 (True)."
          },
          {
            code: "name = \"Alice\"\nif name == \"Alice\":\n    print(\"Hello Alice\")\nelse:\n    print(\"I don't know you\")",
            output: "Hello Alice",
            explanation: "We compare the string name to \"Alice\". They match, so the if runs. Notice: == compares, not = which would assign."
          }
        ]
      },
      {
        title: "Combining Conditions: and, or, not",
        content: `<p>Sometimes you need to check multiple conditions. Think of a security guard checking your ID: \"Do you have an ID AND a ticket?\" Both must be true.</p>
<ul>
<li><code>and</code> — BOTH conditions must be True</li>
<li><code>or</code> — AT LEAST ONE condition must be True</li>
<li><code>not</code> — flip True to False (and vice versa)</li>
</ul>`,
        examples: [
          {
            code: "age = 25\nhas_license = True\n\nif age >= 18 and has_license:\n    print(\"You can rent a car\")\nelse:\n    print(\"You can't rent a car\")",
            output: "You can rent a car",
            explanation: "Both conditions must be true: age >= 18 (True) AND has_license is True (True). Both are true, so the if runs."
          },
          {
            code: "is_student = False\nis_senior = True\n\nif is_student or is_senior:\n    print(\"You get a discount\")\nelse:\n    print(\"No discount\")",
            output: "You get a discount",
            explanation: "Only ONE needs to be true: is_student (False) OR is_senior (True). One is true, so the if runs."
          }
        ]
      },
      {
        title: "Nested ifs and Guard Clauses",
        content: `<p>Sometimes you'll have ifs inside ifs (called nested ifs). But there's a cleaner way: <strong>guard clauses</strong>.</p>
<p>Instead of nesting, check for the \"wrong\" condition first and exit early. This makes code easier to read.</p>`,
        examples: [
          {
            code: "# Nested (harder to read)\nage = 20\nhas_money = True\nif age >= 18:\n    if has_money:\n        print(\"You can buy a ticket\")",
            output: "You can buy a ticket",
            explanation: "This works but requires two levels of nesting. Hard to follow when there are many conditions."
          },
          {
            code: "# Guard clause (easier to read)\nage = 20\nhas_money = True\nif age < 18:\n    print(\"You're too young\")\nelse:\n    if not has_money:\n        print(\"You don't have money\")\n    else:\n        print(\"You can buy a ticket\")",
            output: "You can buy a ticket",
            explanation: "Check the bad cases first and handle them. If none of the bad cases apply, do the main thing. Cleaner flow!"
          }
        ]
      }
    ],
    tips: [
      "Always use == (two equals) to compare, never = (one equals). Single = assigns; double == checks.",
      "Remember the colon (:) at the end of if/elif/else lines. Python won't work without it.",
      "Indentation (spaces) matters! Code inside the if block must be indented. If it's not indented, Python thinks it's outside the block.",
      "When you have many elif statements, consider using a dictionary instead. It's faster and cleaner.",
      "Use and/or to combine conditions. Don't write nested ifs when one condition with and/or will do."
    ],
    common_mistakes: [
      {
        mistake: "Using = instead of == in comparisons",
        fix: "Use == to compare. Use = to assign.",
        code: "Wrong: if name = \"Alice\":\nRight: if name == \"Alice\":"
      },
      {
        mistake: "Forgetting the colon at the end of if/elif/else",
        fix: "Always end if, elif, else lines with a colon.",
        code: "Wrong: if age >= 18\nRight: if age >= 18:"
      },
      {
        mistake: "Not indenting code inside the if block",
        fix: "Code inside if/else blocks must be indented (4 spaces usually).",
        code: "Wrong: if x > 5:\\nprint(\"bigger\")\nRight: if x > 5:\\n    print(\"bigger\")"
      },
      {
        mistake: "Checking conditions in the wrong order",
        fix: "With elif, Python checks from top to bottom. Put more specific conditions before general ones.",
        code: "Wrong: if x >= 0 elif x >= 5 (second never triggers if x is 5)\nRight: if x >= 5 elif x >= 0"
      },
      {
        mistake: "Forgetting to combine conditions with and/or",
        fix: "If you need multiple conditions true, use 'and'. If at least one, use 'or'.",
        code: "Wrong: if x > 5: if y < 10:\nRight: if x > 5 and y < 10:"
      }
    ]
  },

  "functions": {
    icon: "🧩",
    subtitle: "Create reusable blocks of code with functions",
    sections: [
      {
        title: "What Is a Function?",
        content: `<p>A <strong>function</strong> is like a recipe. A recipe has ingredients (inputs), steps to follow, and a finished dish (output).</p>
<p>In code, a function is a reusable block that takes in some information, does something with it, and gives back a result.</p>
<p>Why use functions? Because if you need the same thing done 100 times, you write it once as a function and reuse it 100 times!</p>`,
        examples: [
          {
            code: "def greet(name):\n    message = f\"Hello, {name}!\"\n    return message\n\nresult = greet(\"Alice\")\nprint(result)",
            output: "Hello, Alice!",
            explanation: "<code>def greet(name):</code> defines a function. <code>name</code> is the ingredient (parameter). <code>return</code> is what the function gives back."
          },
          {
            code: "def add(a, b):\n    total = a + b\n    return total\n\nprint(add(5, 3))\nprint(add(10, 20))",
            output: "8\n30",
            explanation: "This function takes two ingredients (a, b) and returns the total. We call it twice with different inputs."
          }
        ]
      },
      {
        title: "Your First Function",
        content: `<p>To create a function:</p>
<ol>
<li>Start with <code>def</code> (short for \"define\")</li>
<li>Give it a name (same naming rules as variables)</li>
<li>Put parentheses with ingredients inside: <code>(ingredient1, ingredient2)</code></li>
<li>End with a colon: <code>:</code></li>
<li>Indent the code inside (the recipe steps)</li>
<li>Use <code>return</code> to give back the result</li>
</ol>
<p>To use a function, write the name with parentheses and put ingredients inside.</p>`,
        examples: [
          {
            code: "def get_full_name(first, last):\n    full = f\"{first} {last}\"\n    return full\n\nname = get_full_name(\"John\", \"Doe\")\nprint(name)",
            output: "John Doe",
            explanation: "Function takes two ingredients (first, last), combines them, and returns the result. We call it and store the result in a variable."
          },
          {
            code: "def multiply(x, y):\n    result = x * y\n    return result\n\nprint(multiply(4, 5))\nprint(multiply(2, 8))",
            output: "20\n16",
            explanation: "Every time we call the function with different inputs, it runs with those inputs and returns a different result."
          }
        ]
      },
      {
        title: "Parameters: The Function's Ingredients",
        content: `<p>Parameters are the pieces of information a function needs to do its job. They're like ingredients in a recipe.</p>
<p>A function can have zero parameters, one parameter, or many parameters.</p>
<p>When you call a function, you provide values (called arguments) for the parameters.</p>`,
        examples: [
          {
            code: "def print_twice(text):\n    print(text)\n    print(text)\n\nprint_twice(\"Hello\")\nprint_twice(\"Python\")",
            output: "Hello\nHello\nPython\nPython",
            explanation: "The function takes one parameter <code>text</code>. Each time we call it, we provide a different argument."
          },
          {
            code: "def calculate_total(price, quantity, tax):\n    subtotal = price * quantity\n    total = subtotal + (subtotal * tax)\n    return total\n\nprint(calculate_total(10, 5, 0.1))\nprint(calculate_total(20, 2, 0.08))",
            output: "55.0\n43.2",
            explanation: "This function needs three ingredients. We provide all three when calling. Without them, it can't work."
          }
        ]
      },
      {
        title: "Return Values: The Finished Dish",
        content: `<p>A function gives back a <strong>return value</strong> — the result of the recipe.</p>
<p>Without <code>return</code>, a function does something but doesn't give you the result.</p>
<p>You can return anything: a number, text, True/False, a list, or even nothing (which returns <code>None</code>).</p>`,
        examples: [
          {
            code: "def is_even(number):\n    if number % 2 == 0:\n        return True\n    else:\n        return False\n\nprint(is_even(4))\nprint(is_even(7))",
            output: "True\nFalse",
            explanation: "This function returns True or False depending on whether the number is even."
          },
          {
            code: "def no_return_example():\n    print(\"I do something\")\n\nresult = no_return_example()\nprint(f\"Result is: {result}\")",
            output: "I do something\nResult is: None",
            explanation: "This function doesn't return anything. It just prints. So <code>result</code> is <code>None</code> (nothing)."
          }
        ]
      },
      {
        title: "Default Parameters: Pre-Set Ingredients",
        content: `<p>Sometimes you want a function to have a default value for a parameter. If someone doesn't provide that ingredient, it uses the default.</p>
<p>Think of it like ordering pizza: If you don't say what size, the restaurant assumes medium.</p>`,
        examples: [
          {
            code: "def greet(name, greeting=\"Hello\"):\n    return f\"{greeting}, {name}!\"\n\nprint(greet(\"Alice\"))\nprint(greet(\"Bob\", \"Hi\"))",
            output: "Hello, Alice!\nHi, Bob!",
            explanation: "<code>greeting</code> has a default value \"Hello\". If we don't provide it, it uses the default. If we do, it uses what we provided."
          },
          {
            code: "def order_pizza(size=\"medium\", toppings=\"cheese\"):\n    return f\"{size} pizza with {toppings}\"\n\nprint(order_pizza())\nprint(order_pizza(\"large\"))\nprint(order_pizza(\"small\", \"pepperoni\"))",
            output: "medium pizza with cheese\nlarge pizza with cheese\nsmall pizza with pepperoni",
            explanation: "Both parameters have defaults. We can call with no arguments, one, or both."
          }
        ]
      },
      {
        title: "Why Functions Matter",
        content: `<p>Functions are about three things:</p>
<ul>
<li><strong>Reuse:</strong> Write once, use many times. Don't repeat code.</li>
<li><strong>Organization:</strong> Break big problems into small, named pieces. Easier to understand and fix.</li>
<li><strong>Testing:</strong> You can test one function separately. Find bugs faster.</li>
</ul>
<p>Every real program uses functions. Without them, code becomes messy and hard to maintain.</p>`,
        examples: [
          {
            code: "# Without a function (repetitive)\nprint(\"User 1 is Alice\")\nprint(\"User 1 can vote: True\")\nprint(\"User 2 is Bob\")\nprint(\"User 2 can vote: True\")\nprint(\"User 3 is Charlie\")\nprint(\"User 3 can vote: False\")",
            output: "User 1 is Alice\nUser 1 can vote: True\nUser 2 is Bob\nUser 2 can vote: True\nUser 3 is Charlie\nUser 3 can vote: False",
            explanation: "We're repeating the same pattern. If we need to change it, we change it in three places. Bad!"
          },
          {
            code: "# With a function (reusable)\ndef display_user(name, can_vote):\n    print(f\"{name} can vote: {can_vote}\")\n\ndisplay_user(\"Alice\", True)\ndisplay_user(\"Bob\", True)\ndisplay_user(\"Charlie\", False)",
            output: "Alice can vote: True\nBob can vote: True\nCharlie can vote: False",
            explanation: "One function, called three times. Change the function once, and all three calls change. Much better!"
          }
        ]
      }
    ],
    tips: [
      "Function names should describe what they do. Use <code>calculate_total</code> not <code>do_thing</code>.",
      "Keep functions small. If a function does too much, break it into smaller functions.",
      "Every function should do ONE thing well. Don't mix multiple unrelated tasks.",
      "Use default parameters when there's a sensible default value that most callers will use.",
      "Test your functions with different inputs. Make sure they work with edge cases (empty strings, zero, negative numbers, etc.)."
    ],
    common_mistakes: [
      {
        mistake: "Forgetting the colon at the end of def",
        fix: "Always end the def line with a colon.",
        code: "Wrong: def greet(name)\nRight: def greet(name):"
      },
      {
        mistake: "Not indenting the code inside the function",
        fix: "Indent all code inside the function. Python uses indentation to know what's part of the function.",
        code: "Wrong: def add(a, b):\\nreturn a + b\nRight: def add(a, b):\\n    return a + b"
      },
      {
        mistake: "Forgetting to return a value",
        fix: "If your function should give back a result, use return.",
        code: "Wrong: def double(x):\\n    x * 2\nRight: def double(x):\\n    return x * 2"
      },
      {
        mistake: "Providing the wrong number of arguments",
        fix: "Count the parameters in the def line. Provide that many arguments when calling.",
        code: "Wrong: def add(a, b): add(5) (only one argument)\nRight: add(5, 3) (two arguments)"
      },
      {
        mistake: "Using a variable name inside a function that doesn't exist",
        fix: "Variables inside a function are local (only exist inside). Use parameters to pass values in.",
        code: "Wrong: def greet(): print(name)\nRight: def greet(name): print(name)"
      }
    ]
  },

  "lists_sets": {
    icon: "📋",
    subtitle: "Store and organize multiple items with lists and sets",
    sections: [
      {
        title: "What Is a List?",
        content: `<p>A <strong>list</strong> is like a shopping list. One variable holds multiple items, and you access them by position.</p>
<p>Lists are ordered (item 1, item 2, item 3...) and can contain anything: numbers, text, True/False, even other lists!</p>
<p>Use square brackets <code>[</code> and <code>]</code> to create a list.</p>`,
        examples: [
          {
            code: "shopping = [\"milk\", \"eggs\", \"bread\", \"cheese\"]\nprint(shopping)\nprint(len(shopping))",
            output: "[\"milk\", \"eggs\", \"bread\", \"cheese\"]\n4",
            explanation: "We created a list with four items. <code>len()</code> tells us how many items are in the list."
          },
          {
            code: "numbers = [1, 2, 3, 4, 5]\nprices = [19.99, 5.50, 12.00]\nmixed = [\"Alice\", 25, True, 3.14]\n\nprint(numbers)\nprint(prices)\nprint(mixed)",
            output: "[1, 2, 3, 4, 5]\n[19.99, 5.5, 12.0]\n[\"Alice\", 25, True, 3.14]",
            explanation: "Lists can hold numbers, floats, text, booleans, or a mix of everything."
          }
        ]
      },
      {
        title: "Accessing List Items by Position (Index)",
        content: `<p>To get an item from a list, use its <strong>position number</strong> (called an <strong>index</strong>).</p>
<p><strong>CRITICAL:</strong> Positions start at 0, not 1! The first item is at position 0.</p>
<p>You can also use negative numbers to count from the end: -1 is the last item, -2 is second-to-last, etc.</p>`,
        examples: [
          {
            code: "fruits = [\"apple\", \"banana\", \"orange\", \"grape\"]\n\nprint(fruits[0])  # First item\nprint(fruits[1])  # Second item\nprint(fruits[3])  # Fourth item",
            output: "apple\nbanana\ngrape",
            explanation: "Position 0 is \"apple\" (first). Position 1 is \"banana\" (second). Position 3 is \"grape\" (fourth). Notice we count from 0!"
          },
          {
            code: "fruits = [\"apple\", \"banana\", \"orange\", \"grape\"]\n\nprint(fruits[-1])  # Last item\nprint(fruits[-2])  # Second-to-last\nprint(fruits[-4])  # First (same as [0])",
            output: "grape\norange\napple",
            explanation: "Negative indices count from the end. -1 is the last item. -2 is second-to-last. Super useful!"
          }
        ]
      },
      {
        title: "Adding and Removing Items",
        content: `<p>Lists are changeable. You can add items, remove items, or replace items.</p>
<ul>
<li><code>.append(item)</code> — add to the end</li>
<li><code>.remove(item)</code> — remove a specific item by value</li>
<li><code>.pop()</code> — remove the last item</li>
<li><code>.insert(index, item)</code> — insert at a specific position</li>
</ul>`,
        examples: [
          {
            code: "tasks = [\"sleep\", \"eat\", \"code\"]\nprint(tasks)\n\ntasks.append(\"exercise\")\nprint(tasks)\n\ntasks.remove(\"sleep\")\nprint(tasks)",
            output: "[\"sleep\", \"eat\", \"code\"]\n[\"sleep\", \"eat\", \"code\", \"exercise\"]\n[\"eat\", \"code\", \"exercise\"]",
            explanation: "<code>.append()</code> adds to the end. <code>.remove()</code> takes out a specific item. The list changes each time."
          },
          {
            code: "numbers = [1, 2, 3, 4, 5]\nprint(numbers)\n\nremoved = numbers.pop()\nprint(f\"Removed {removed}\")\nprint(numbers)\n\nnumbers.insert(2, 99)\nprint(numbers)",
            output: "[1, 2, 3, 4, 5]\nRemoved 5\n[1, 2, 3, 4]\n[1, 2, 99, 3, 4]",
            explanation: "<code>.pop()</code> removes the last item AND returns it. <code>.insert(2, 99)</code> puts 99 at position 2."
          }
        ]
      },
      {
        title: "Slicing: Getting a Portion of a List",
        content: `<p>You can grab multiple items at once using <strong>slicing</strong>. Use square brackets with a start and end: <code>list[start:end]</code></p>
<p>Slicing is powerful! It's like saying \"give me items 2 through 5.\"</p>
<p>Remember: the start is included, but the end is NOT included.</p>`,
        examples: [
          {
            code: "letters = [\"a\", \"b\", \"c\", \"d\", \"e\", \"f\"]\n\nprint(letters[1:4])  # Items 1, 2, 3\nprint(letters[:3])   # First 3 items\nprint(letters[3:])   # Items from 3 to the end\nprint(letters[::2])  # Every other item",
            output: "[\"b\", \"c\", \"d\"]\n[\"a\", \"b\", \"c\"]\n[\"d\", \"e\", \"f\"]\n[\"a\", \"c\", \"e\"]",
            explanation: "[1:4] gets positions 1, 2, 3 (not 4!). [:3] is shorthand for \"from the start to 3\". [::2] means \"every 2nd item.\""
          },
          {
            code: "numbers = list(range(1, 11))  # [1, 2, 3, ..., 10]\nprint(numbers)\nprint(numbers[::2])   # Every other\nprint(numbers[::-1])  # Reversed!",
            output: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[1, 3, 5, 7, 9]\n[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]",
            explanation: "[::2] every 2nd item. [::-1] reverses the list! Slicing is incredibly powerful."
          }
        ]
      },
      {
        title: "List Comprehensions",
        content: `<p>A <strong>list comprehension</strong> is a fast way to create a new list by transforming an old list.</p>
<p>Instead of writing a loop, you write: <code>[new_value for item in old_list]</code></p>
<p>This looks strange at first, but it's incredibly useful and becomes second nature.</p>`,
        examples: [
          {
            code: "# Without list comprehension\nnumbers = [1, 2, 3, 4, 5]\nsquared = []\nfor num in numbers:\n    squared.append(num * num)\n\nprint(squared)",
            output: "[1, 4, 9, 16, 25]",
            explanation: "We loop through numbers and square each one. Works, but requires 4 lines."
          },
          {
            code: "# With list comprehension\nnumbers = [1, 2, 3, 4, 5]\nsquared = [num * num for num in numbers]\nprint(squared)\n\n# Even with a filter\neven_squared = [num * num for num in numbers if num % 2 == 0]\nprint(even_squared)",
            output: "[1, 4, 9, 16, 25]\n[4, 16]",
            explanation: "One line to square all numbers! The second example only squares EVEN numbers. Super concise."
          }
        ]
      },
      {
        title: "What Is a Set?",
        content: `<p>A <strong>set</strong> is like a list, but with a big difference: <strong>no duplicates allowed</strong>.</p>
<p>Sets are useful when you care about unique items (no repeats). Use curly braces: <code>{item1, item2}</code></p>
<p>Sets are unordered, so you can't access by position like lists. But checking if something is in a set is super fast!</p>`,
        examples: [
          {
            code: "colors = {\"red\", \"blue\", \"green\", \"red\", \"blue\"}\nprint(colors)\nprint(len(colors))",
            output: "{\"red\", \"green\", \"blue\"}\n3",
            explanation: "We put 5 colors but two were duplicates. The set keeps only 3 unique colors. Duplicates are automatically removed!"
          },
          {
            code: "numbers = {1, 2, 2, 3, 3, 3, 4, 5}\nprint(numbers)\nprint(4 in numbers)  # Is 4 in the set?\nprint(10 in numbers) # Is 10 in the set?",
            output: "{1, 2, 3, 4, 5}\nTrue\nFalse",
            explanation: "Duplicates removed automatically. Checking if something is in a set is fast and easy."
          }
        ]
      },
      {
        title: "Set Operations: Union and Intersection",
        content: `<p>Sets support special operations:</p>
<ul>
<li><code>set1 | set2</code> (union) — combine all items from both sets</li>
<li><code>set1 &amp; set2</code> (intersection) — only items in both sets</li>
<li><code>set1 - set2</code> (difference) — items in set1 but not set2</li>
</ul>
<p>These are like set operations you learned in math class!</p>`,
        examples: [
          {
            code: "teachers_morning = {\"Alice\", \"Bob\", \"Charlie\"}\nteachers_afternoon = {\"Bob\", \"Charlie\", \"Diana\"}\n\nprint(teachers_morning | teachers_afternoon)  # All teachers\nprint(teachers_morning & teachers_afternoon)  # Teachers in both",
            output: "{\"Alice\", \"Bob\", \"Charlie\", \"Diana\"}\n{\"Bob\", \"Charlie\"}",
            explanation: "Union (|) combines both sets. Intersection (&) shows only what's in both."
          },
          {
            code: "pizza_toppings = {\"pepperoni\", \"sausage\", \"mushroom\"}\nvegetarian = {\"mushroom\", \"peppers\", \"olives\"}\n\navailable_vegetarian = pizza_toppings & vegetarian\nprint(available_vegetarian)",
            output: "{\"mushroom\"}",
            explanation: "Only \"mushroom\" is both a pizza topping we have AND vegetarian. Intersection finds items in common."
          }
        ]
      }
    ],
    tips: [
      "Remember: lists start at index 0. The first item is at position 0, not 1. This trips up everyone at first!",
      "Use lists when order matters or you need duplicates. Use sets when you only care about unique items.",
      "List slicing [start:end] is super powerful. Practice it. The end is NOT included, only start through end-1.",
      "List comprehensions look weird at first, but they're worth learning. [x*2 for x in list] is much cleaner than a loop.",
      "For large lists, checking 'item in set' is MUCH faster than 'item in list'. Sets are optimized for lookups."
    ],
    common_mistakes: [
      {
        mistake: "Forgetting that lists start at index 0, not 1",
        fix: "The first item is at position 0. If you have 5 items, valid positions are 0, 1, 2, 3, 4.",
        code: "Wrong: first = mylist[1]\nRight: first = mylist[0]"
      },
      {
        mistake: "Using slicing wrong: [start:end] includes start but NOT end",
        fix: "Remember: [0:3] gets items 0, 1, 2. Item 3 is NOT included.",
        code: "list[0:3] gets items at positions 0, 1, 2 (three items total)"
      },
      {
        mistake: "Trying to access an item that doesn't exist",
        fix: "Check the length first with len(). If the list has 5 items, valid indices are 0-4.",
        code: "Wrong: items = [1, 2, 3]; print(items[5])\nRight: print(items[2]) or check len(items) first"
      },
      {
        mistake: "Confusing sets and lists or using sets when order matters",
        fix: "Sets are unordered. If you need order, use a list. If you need unique items, use a set.",
        code: "Wrong: colors = {\"red\", \"blue\", \"green\"}; print(colors[0])\nRight: colors = [\"red\", \"blue\", \"green\"]"
      },
      {
        mistake: "Forgetting that list comprehensions are equivalent to loops",
        fix: "[x*2 for x in list] is the same as: for x in list: new_list.append(x*2)",
        code: "Understand what the comprehension does before using it"
      }
    ]
  },

  "dictionaries": {
    icon: "📖",
    subtitle: "Store and look up data with key-value pairs",
    sections: [
      {
        title: "What Is a Dictionary?",
        content: `<p>A <strong>dictionary</strong> is like a phone book. Instead of looking up a person by position (like a list), you look them up by name.</p>
<p>In Python, you use a <strong>key</strong> (the name) to find a <strong>value</strong> (the phone number). It's the ultimate real-world data structure!</p>
<p>Use curly braces and colons: <code>{\"key\": \"value\", \"key2\": \"value2\"}</code></p>`,
        examples: [
          {
            code: "phone_book = {\n    \"Alice\": \"555-1234\",\n    \"Bob\": \"555-5678\",\n    \"Charlie\": \"555-9999\"\n}\n\nprint(phone_book[\"Alice\"])\nprint(phone_book[\"Bob\"])",
            output: "555-1234\n555-5678",
            explanation: "We created a dictionary with names as keys and phone numbers as values. We look up Alice and get her number."
          },
          {
            code: "student = {\n    \"name\": \"Alice\",\n    \"age\": 20,\n    \"major\": \"Computer Science\",\n    \"gpa\": 3.8\n}\n\nprint(student[\"name\"])\nprint(student[\"gpa\"])",
            output: "Alice\n3.8",
            explanation: "Dictionaries can hold any type of value: text, numbers, etc. Keys are usually strings."
          }
        ]
      },
      {
        title: "Keys and Values: The Name and Number",
        content: `<p>Every item in a dictionary has two parts:</p>
<ul>
<li><strong>Key:</strong> The label (like a name). Must be unique. Usually text.</li>
<li><strong>Value:</strong> The data (like a phone number). Can be anything.</li>
</ul>
<p>You access values by key: <code>dictionary[key]</code></p>
<p>Don't worry about position — you look things up by name, not by position!</p>`,
        examples: [
          {
            code: "person = {\n    \"name\": \"Alex\",\n    \"age\": 25,\n    \"city\": \"Paris\",\n    \"employed\": True\n}\n\nprint(person[\"name\"])      # Get the name\nprint(person[\"age\"])       # Get the age\nprint(person[\"employed\"])  # Get employed status",
            output: "Alex\n25\nTrue",
            explanation: "We access values by their key. No position numbers needed. Much more intuitive!"
          },
          {
            code: "inventory = {\n    \"apples\": 50,\n    \"oranges\": 30,\n    \"bananas\": 20,\n    \"grapes\": 15\n}\n\nprint(inventory[\"apples\"])\nprint(inventory[\"bananas\"])",
            output: "50\n20",
            explanation: "Keys are product names. Values are quantities. Look up \"apples\" and get 50."
          }
        ]
      },
      {
        title: "Creating, Reading, Updating, Deleting",
        content: `<p>Dictionaries are changeable. You can:</p>
<ul>
<li><strong>Create:</strong> <code>dict = {\"key\": \"value\"}</code></li>
<li><strong>Read:</strong> <code>dict[\"key\"]</code></li>
<li><strong>Update:</strong> <code>dict[\"key\"] = \"new value\"</code></li>
<li><strong>Delete:</strong> <code>del dict[\"key\"]</code></li>
</ul>
<p>You can also add new keys that didn't exist before!</p>`,
        examples: [
          {
            code: "user = {\"name\": \"Alice\", \"age\": 30}\nprint(user)\n\nuser[\"age\"] = 31  # Update\nprint(user)\n\nuser[\"city\"] = \"New York\"  # Add new key\nprint(user)\n\ndel user[\"age\"]  # Delete\nprint(user)",
            output: "{\"name\": \"Alice\", \"age\": 30}\n{\"name\": \"Alice\", \"age\": 31}\n{\"name\": \"Alice\", \"age\": 31, \"city\": \"New York\"}\n{\"name\": \"Alice\", \"city\": \"New York\"}",
            explanation: "We update age, add city, then delete age. The dictionary changes each time."
          },
          {
            code: "scores = {}\nscores[\"Alice\"] = 100\nscores[\"Bob\"] = 95\nscores[\"Alice\"] = 105  # Update Alice's score\n\nprint(scores)",
            output: "{\"Alice\": 105, \"Bob\": 95}",
            explanation: "We started with an empty dictionary and added keys one by one."
          }
        ]
      },
      {
        title: "Why .get() Is Your Best Friend",
        content: `<p><code>.get()</code> is the safe way to look up a key. If the key doesn't exist, it returns <code>None</code> instead of crashing.</p>
<p>Regular dictionary access <code>dict[key]</code> crashes if the key doesn't exist. <code>dict.get(key)</code> is safer!</p>
<p>You can provide a default value: <code>dict.get(key, default)</code></p>`,
        examples: [
          {
            code: "phone_book = {\"Alice\": \"555-1234\", \"Bob\": \"555-5678\"}\n\n# Using regular access (risky)\nprint(phone_book[\"Alice\"])  # Works\n# print(phone_book[\"Charlie\"])  # CRASH! Key doesn't exist\n\n# Using .get() (safe)\nprint(phone_book.get(\"Alice\"))    # Works, returns value\nprint(phone_book.get(\"Charlie\"))  # Returns None (no crash)",
            output: "555-1234\n555-1234\nNone",
            explanation: "Regular access crashes if the key is missing. .get() is safe — it returns None instead."
          },
          {
            code: "settings = {\"theme\": \"dark\", \"language\": \"English\"}\n\nprint(settings.get(\"theme\", \"light\"))        # theme exists, returns \"dark\"\nprint(settings.get(\"notifications\", True))   # doesn't exist, returns default True\nprint(settings.get(\"volume\", 50))            # doesn't exist, returns default 50",
            output: "dark\nTrue\n50",
            explanation: "If the key exists, return its value. If not, return the default. Perfect for optional settings!"
          }
        ]
      },
      {
        title: "Looping Through Dictionaries",
        content: `<p>You can loop through a dictionary three ways:</p>
<ul>
<li><code>for key in dict:</code> — loop through keys</li>
<li><code>for value in dict.values():</code> — loop through values</li>
<li><code>for key, value in dict.items():</code> — loop through both</li>
</ul>
<p><code>.items()</code> is usually the most useful because you get both key and value at once.</p>`,
        examples: [
          {
            code: "person = {\"name\": \"Alice\", \"age\": 30, \"city\": \"Paris\"}\n\nprint(\"Keys:\")\nfor key in person:\n    print(key)\n\nprint(\"\\nValues:\")\nfor value in person.values():\n    print(value)\n\nprint(\"\\nBoth:\")\nfor key, value in person.items():\n    print(f\"{key}: {value}\")",
            output: "Keys:\nname\nage\ncity\n\nValues:\nAlice\n30\nParis\n\nBoth:\nname: Alice\nage: 30\ncity: Paris",
            explanation: "Three different ways to loop. The third way (.items()) is most useful because you get both parts."
          },
          {
            code: "inventory = {\"apples\": 50, \"oranges\": 30, \"bananas\": 20}\n\nfor item, count in inventory.items():\n    print(f\"We have {count} {item}\")",
            output: "We have 50 apples\nWe have 30 oranges\nWe have 20 bananas",
            explanation: "Using .items() with unpacking. Each loop iteration gives us the item name and count."
          }
        ]
      },
      {
        title: "Nested Dictionaries: Dictionaries Inside Dictionaries",
        content: `<p>Dictionaries can contain other dictionaries! Imagine a phone book where each person has multiple phone numbers.</p>
<p>Access nested values by chaining keys: <code>dict[\"key1\"][\"key2\"]</code></p>
<p>This is perfect for complex real-world data like user profiles or API responses.</p>`,
        examples: [
          {
            code: "people = {\n    \"Alice\": {\n        \"age\": 30,\n        \"phone\": \"555-1234\",\n        \"email\": \"alice@example.com\"\n    },\n    \"Bob\": {\n        \"age\": 25,\n        \"phone\": \"555-5678\",\n        \"email\": \"bob@example.com\"\n    }\n}\n\nprint(people[\"Alice\"][\"age\"])    # Alice's age\nprint(people[\"Bob\"][\"email\"])    # Bob's email",
            output: "30\nbob@example.com",
            explanation: "We have two dictionaries nested inside a main dictionary. Access nested data by chaining keys."
          },
          {
            code: "company = {\n    \"name\": \"TechCorp\",\n    \"employees\": {\n        \"Alice\": {\"title\": \"Manager\", \"salary\": 80000},\n        \"Bob\": {\"title\": \"Developer\", \"salary\": 60000}\n    }\n}\n\nprint(company[\"employees\"][\"Alice\"][\"title\"])",
            output: "Manager",
            explanation: "Three levels deep! company → employees → Alice → title. Nested dictionaries are powerful."
          }
        ]
      },
      {
        title: "Real-World Uses: Config, Users, API Data, Counting",
        content: `<p>Dictionaries are everywhere in real programs:</p>
<ul>
<li><strong>Configuration files:</strong> settings = {\"theme\": \"dark\", \"language\": \"EN\"}</li>
<li><strong>User profiles:</strong> user = {\"id\": 1, \"name\": \"Alice\", \"premium\": True}</li>
<li><strong>API responses:</strong> data from websites is usually formatted as dictionaries</li>
<li><strong>Counting things:</strong> word_count = {\"hello\": 5, \"world\": 3}</li>
</ul>`,
        examples: [
          {
            code: "# Counting word frequencies\ntext = \"hello world hello python hello\"\nword_count = {}\n\nfor word in text.split():\n    if word in word_count:\n        word_count[word] += 1\n    else:\n        word_count[word] = 1\n\nprint(word_count)",
            output: "{\"hello\": 3, \"world\": 1, \"python\": 1}",
            explanation: "We loop through words and count how many times each appears. Dictionaries are perfect for this!"
          },
          {
            code: "# Configuration file\nconfig = {\n    \"debug\": True,\n    \"database\": {\n        \"host\": \"localhost\",\n        \"port\": 5432\n    },\n    \"api_key\": \"abc123\"\n}\n\nif config[\"debug\"]:\n    print(f\"Connecting to {config['database']['host']}\")",
            output: "Connecting to localhost",
            explanation: "Configuration data naturally fits in nested dictionaries. Look up values as needed."
          }
        ]
      }
    ],
    tips: [
      "Use .get() for safe lookups. dict.get(key, default) never crashes, even if the key is missing.",
      "Use .items() when you need both keys and values. It's cleaner than looping through keys and then looking up values.",
      "Dictionary keys should be unique. If you assign the same key twice, the second value overwrites the first.",
      "Keys are usually strings, but can be numbers or tuples. Values can be anything: numbers, text, booleans, lists, other dictionaries.",
      "Nested dictionaries are powerful but can get hard to read. Use clear variable names and comments to explain structure."
    ],
    common_mistakes: [
      {
        mistake: "Using square brackets to access a key that doesn't exist",
        fix: "Use .get() instead, or check if the key exists first.",
        code: "Wrong: age = person[\"age\"] (crashes if \"age\" missing)\nRight: age = person.get(\"age\", 0) (returns 0 if missing)"
      },
      {
        mistake: "Forgetting the colon when creating a dictionary",
        fix: "Dictionaries use key:value syntax with colons.",
        code: "Wrong: {\"name\" = \"Alice\"}\nRight: {\"name\": \"Alice\"}"
      },
      {
        mistake: "Using a mutable type as a key (like a list)",
        fix: "Keys must be immutable. Use strings, numbers, or tuples. Never lists or dictionaries.",
        code: "Wrong: {[\"a\", \"b\"]: \"value\"}\nRight: {\"key\": \"value\"}"
      },
      {
        mistake: "Confusing dict[key] = value with dict.get(key, default)",
        fix: "Use = to set a value. Use .get() to safely read a value.",
        code: "Setting: dict[\"key\"] = \"value\"\nReading: dict.get(\"key\", \"default\")"
      },
      {
        mistake: "Not using .items() when you need both keys and values",
        fix: "Use for key, value in dict.items(): instead of looping and looking up.",
        code: "Wrong: for key in dict: value = dict[key]\nRight: for key, value in dict.items():"
      }
    ]
  },

  "fastapi_ex": {
    icon: "⚡",
    subtitle: "Build web APIs with FastAPI",
    sections: [
      {
        title: "What Is an API?",
        content: `<p>An <strong>API</strong> is like a waiter in a restaurant. The waiter takes your order, goes to the kitchen, and brings back food.</p>
<p>In web APIs, you make a <strong>request</strong> (like ordering), and the server sends back a <strong>response</strong> (like food).</p>
<p><strong>FastAPI</strong> is a Python tool that makes it super easy to build APIs. It handles taking orders and sending responses for you.</p>`,
        examples: [
          {
            code: "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get(\"/hello\")\ndef say_hello():\n    return {\"message\": \"Hello, world!\"}\n\n# Start with: uvicorn main:app --reload",
            output: "When you visit /hello, you get:\n{\"message\": \"Hello, world!\"}",
            explanation: "@app.get(\"/hello\") means \"when someone visits /hello, run this function.\" Return a dictionary as JSON."
          }
        ]
      },
      {
        title: "HTTP Methods: GET, POST, PUT, DELETE",
        content: `<p>HTTP has four main methods for different actions:</p>
<ul>
<li><strong>GET:</strong> Read data (no changes)</li>
<li><strong>POST:</strong> Create new data</li>
<li><strong>PUT:</strong> Update existing data</li>
<li><strong>DELETE:</strong> Remove data</li>
</ul>
<p>Think of a restaurant: GET = read the menu, POST = place an order, PUT = change your order, DELETE = cancel your order.</p>`,
        examples: [
          {
            code: "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get(\"/items\")          # Read items\ndef get_items():\n    return {\"items\": [\"apple\", \"banana\"]}\n\n@app.post(\"/items\")         # Create new item\ndef create_item(item: str):\n    return {\"created\": item}\n\n@app.put(\"/items/0\")        # Update item\ndef update_item(new_item: str):\n    return {\"updated\": new_item}\n\n@app.delete(\"/items/0\")     # Delete item\ndef delete_item():\n    return {\"deleted\": True}",
            output: "GET /items → {\"items\": [\"apple\", \"banana\"]}\nPOST /items → {\"created\": item_name}\nPUT /items/0 → {\"updated\": new_name}\nDELETE /items/0 → {\"deleted\": true}",
            explanation: "Different methods for different actions. CRUD: Create (POST), Read (GET), Update (PUT), Delete (DELETE)."
          }
        ]
      },
      {
        title: "Pydantic Models: Defining Data Structure",
        content: `<p>A <strong>Pydantic model</strong> is like a form. It defines what fields are required, what type each field is, and validates the data.</p>
<p>Use models to make sure people send you good data, not garbage.</p>`,
        examples: [
          {
            code: "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass User(BaseModel):\n    name: str\n    age: int\n    email: str\n\n@app.post(\"/users\")\ndef create_user(user: User):\n    return {\"message\": f\"Created user {user.name}\"}\n\n# Valid request: {\"name\": \"Alice\", \"age\": 30, \"email\": \"alice@example.com\"}\n# Invalid request: {\"name\": \"Alice\", \"age\": \"thirty\"}  # age must be int!",
            output: "Valid: {\"message\": \"Created user Alice\"}\nInvalid: Error! age must be an integer.",
            explanation: "Pydantic models validate data. If someone sends wrong types, FastAPI rejects it automatically."
          }
        ]
      },
      {
        title: "Validation: Making Sure Data Is Good",
        content: `<p><strong>Validation</strong> means checking that data is correct before using it.</p>
<p>Pydantic validates automatically based on types. But you can add custom rules too.</p>
<p>This prevents bugs — if you expect a number, you get a number. If you expect a non-empty string, it's non-empty.</p>`,
        examples: [
          {
            code: "from fastapi import FastAPI\nfrom pydantic import BaseModel, Field\n\napp = FastAPI()\n\nclass Product(BaseModel):\n    name: str = Field(..., min_length=1)      # name required, at least 1 char\n    price: float = Field(..., gt=0)           # price required, must be > 0\n    quantity: int = Field(default=1, ge=0)   # quantity optional, default 1, >= 0\n\n@app.post(\"/products\")\ndef create_product(product: Product):\n    return {\"created\": product.name, \"price\": product.price}",
            output: "Valid: {\"created\": \"Laptop\", \"price\": 999.99}\nInvalid: {\"name\": \"\", \"price\": -10}  → Validation errors!",
            explanation: "Field validators ensure data is correct. min_length, gt, ge are common validators."
          }
        ]
      },
      {
        title: "Building a Simple CRUD API",
        content: `<p><strong>CRUD</strong> = Create, Read, Update, Delete. The four basic operations.</p>
<p>Let's build a simple to-do API with all four operations.</p>`,
        examples: [
          {
            code: "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass Task(BaseModel):\n    title: str\n    completed: bool = False\n\ntasks = []  # Simple storage\n\n@app.post(\"/tasks\")  # CREATE\ndef create_task(task: Task):\n    tasks.append(task)\n    return task\n\n@app.get(\"/tasks\")   # READ all\ndef read_tasks():\n    return tasks\n\n@app.get(\"/tasks/{task_id}\")  # READ one\ndef read_task(task_id: int):\n    return tasks[task_id]\n\n@app.put(\"/tasks/{task_id}\")   # UPDATE\ndef update_task(task_id: int, task: Task):\n    tasks[task_id] = task\n    return task\n\n@app.delete(\"/tasks/{task_id}\")  # DELETE\ndef delete_task(task_id: int):\n    removed = tasks.pop(task_id)\n    return {\"deleted\": removed}",
            output: "POST /tasks with {\"title\": \"Learn Python\"} → creates task\nGET /tasks → returns all tasks\nGET /tasks/0 → returns first task\nPUT /tasks/0 with new data → updates task\nDELETE /tasks/0 → removes task",
            explanation: "A complete CRUD API in ~30 lines! Create, read, update, delete — all four operations."
          }
        ]
      },
      {
        title: "Error Handling: What Happens When Things Go Wrong",
        content: `<p>Real APIs need to handle errors gracefully. Don't crash — send a helpful error message instead.</p>
<p>Use HTTP status codes: 400 (bad request), 404 (not found), 500 (server error).</p>`,
        examples: [
          {
            code: "from fastapi import FastAPI, HTTPException\n\napp = FastAPI()\ntasks = [\"Buy milk\", \"Learn Python\"]\n\n@app.get(\"/tasks/{task_id}\")\ndef get_task(task_id: int):\n    if task_id < 0 or task_id >= len(tasks):\n        raise HTTPException(status_code=404, detail=\"Task not found\")\n    return {\"task\": tasks[task_id]}\n\n@app.post(\"/tasks\")\ndef add_task(task: str):\n    if not task or len(task) < 1:\n        raise HTTPException(status_code=400, detail=\"Task cannot be empty\")\n    tasks.append(task)\n    return {\"added\": task}",
            output: "GET /tasks/999 → 404 error: Task not found\nPOST /tasks with empty task → 400 error: Task cannot be empty\nGET /tasks/0 → 200 success: {\"task\": \"Buy milk\"}",
            explanation: "Check for bad cases and raise HTTPException with appropriate status codes."
          }
        ]
      }
    ],
    tips: [
      "Start simple. Build GET one route at a time. Once it works, add more.",
      "Use Pydantic models for all data. They automatically validate and convert types.",
      "Test with Swagger UI: run uvicorn and visit /docs. It's built-in and free!",
      "Use meaningful names for routes: /users, /products, /tasks. Not /api1, /api2.",
      "Return clear error messages. Help your users (and yourself!) debug issues."
    ],
    common_mistakes: [
      {
        mistake: "Forgetting to use type hints in function parameters",
        fix: "Always specify parameter types. FastAPI uses them to validate and document.",
        code: "Wrong: def get_user(user_id):\nRight: def get_user(user_id: int):"
      },
      {
        mistake: "Not using Pydantic models for POST/PUT bodies",
        fix: "Create a BaseModel for every request body. It validates automatically.",
        code: "Wrong: def create_user(name, age):\nRight: def create_user(user: User):"
      },
      {
        mistake: "Not handling errors; letting code crash",
        fix: "Check for bad cases and raise HTTPException with appropriate status codes.",
        code: "Wrong: return items[index] (crashes if index invalid)\nRight: if index invalid: raise HTTPException(status_code=404)"
      },
      {
        mistake: "Storing data in memory (lost when server restarts)",
        fix: "Use a database! FastAPI is just the frontend. Real apps need persistent storage.",
        code: "Good for learning, but add a database in production"
      },
      {
        mistake: "Not documenting your API",
        fix: "FastAPI auto-generates docs at /docs. Add docstrings to functions for better docs.",
        code: "def get_user(id: int):\\n    \"\"\"Get a user by ID\"\"\""
      }
    ]
  },

  "api_calling": {
    icon: "🔗",
    subtitle: "Call other APIs and handle responses",
    sections: [
      {
        title: "What Does \"Calling an API\" Mean?",
        content: `<p>When you \"call an API,\" you're asking another computer to do something and get the result back.</p>
<p>It's like ordering food via a delivery app: you send your order to the restaurant (API call), they prepare it, and it gets delivered (API response).</p>
<p>You'll use the <code>requests</code> library (or <code>httpx</code>) to make these calls.</p>`,
        examples: [
          {
            code: "import requests\n\n# Call an API\nresponse = requests.get(\"https://api.example.com/users/1\")\n\nprint(response.status_code)  # 200 = success\nprint(response.json())       # Get the data",
            output: "200\n{\"id\": 1, \"name\": \"Alice\", \"email\": \"alice@example.com\"}",
            explanation: "We called an API endpoint. If status_code is 200, the call succeeded. .json() gives us the data."
          }
        ]
      },
      {
        title: "JSON: The Universal Language",
        content: `<p><strong>JSON</strong> is how computers talk to each other. It's like a form that's easy for both humans and computers to understand.</p>
<p>JSON has:</p>
<ul>
<li><strong>Objects:</strong> {} (like dictionaries) with key:value pairs</li>
<li><strong>Arrays:</strong> [] (like lists) of items</li>
<li><strong>Strings:</strong> \"text\" (in quotes)</li>
<li><strong>Numbers:</strong> 42, 3.14 (no quotes)</li>
<li><strong>True/False:</strong> true, false (lowercase!)</li>
</ul>`,
        examples: [
          {
            code: "import requests\nimport json\n\n# Example JSON response from an API\ndata = {\n    \"users\": [\n        {\"id\": 1, \"name\": \"Alice\", \"active\": True},\n        {\"id\": 2, \"name\": \"Bob\", \"active\": False}\n    ]\n}\n\nprint(data[\"users\"][0][\"name\"])\nprint(data[\"users\"][0][\"active\"])",
            output: "Alice\nTrue",
            explanation: "JSON is nested dictionaries and lists. Access data with square brackets and dots."
          },
          {
            code: "import json\n\njson_text = '{\"name\": \"Alice\", \"age\": 30}'\ndata = json.loads(json_text)  # String → Python dict\nprint(data[\"name\"])\n\ndata_dict = {\"name\": \"Bob\", \"age\": 25}\njson_str = json.dumps(data_dict)  # Python dict → JSON string\nprint(json_str)",
            output: "Alice\n{\"name\": \"Bob\", \"age\": 25}",
            explanation: "json.loads() converts JSON text to Python dict. json.dumps() converts dict to JSON text."
          }
        ]
      },
      {
        title: "Making Your First API Call",
        content: `<p>The <code>requests</code> library makes calling APIs easy.</p>
<ul>
<li><code>requests.get(url)</code> — fetch data</li>
<li><code>requests.post(url, data=...)</code> — send data and create something</li>
<li><code>requests.put(url, data=...)</code> — update something</li>
<li><code>requests.delete(url)</code> — delete something</li>
</ul>`,
        examples: [
          {
            code: "import requests\n\n# GET request (fetch data)\nresponse = requests.get(\"https://jsonplaceholder.typicode.com/posts/1\")\nprint(f\"Status: {response.status_code}\")\nprint(response.json())",
            output: "Status: 200\n{\"userId\": 1, \"id\": 1, \"title\": \"...\", \"body\": \"...\"}",
            explanation: "We made a GET request to a test API. Status 200 means success. .json() gives us the data."
          },
          {
            code: "import requests\n\n# POST request (create something)\ndata = {\"name\": \"Alice\", \"email\": \"alice@example.com\"}\nresponse = requests.post(\"https://jsonplaceholder.typicode.com/users\", json=data)\nprint(response.status_code)\nprint(response.json())",
            output: "201\n{\"id\": 11, \"name\": \"Alice\", \"email\": \"alice@example.com\"}",
            explanation: "We POSTed data to create a new user. Status 201 means created. The API assigned an ID."
          }
        ]
      },
      {
        title: "Reading Nested API Responses",
        content: `<p>API responses are often nested (objects inside objects). You navigate them like dictionaries.</p>
<p>If a key might not exist, use .get() to avoid crashes!</p>`,
        examples: [
          {
            code: "import requests\n\n# Nested API response\nresponse = requests.get(\"https://api.example.com/company/1\")\ndata = response.json()\n\nprint(data[\"name\"])                    # Company name\nprint(data[\"address\"][\"city\"])         # Company city\nprint(data[\"employees\"][0][\"name\"])   # First employee's name",
            output: "TechCorp\nNew York\nAlice",
            explanation: "We navigate nested data with chained square brackets."
          },
          {
            code: "import requests\n\nresponse = requests.get(\"https://api.example.com/user/1\")\ndata = response.json()\n\n# Unsafe (crashes if key missing)\n# name = data[\"profile\"][\"name\"]\n\n# Safe (returns None if missing)\nname = data.get(\"profile\", {}).get(\"name\", \"Unknown\")\nprint(name)",
            output: "Unknown (if missing)\nActual name (if present)",
            explanation: "Use .get() to safely navigate nested data without crashing."
          }
        ]
      },
      {
        title: "Authentication: Showing Your ID",
        content: `<p>Many APIs require authentication — showing your ID at the door.</p>
<p>Common methods:</p>
<ul>
<li><strong>API Key:</strong> Special token in a header: <code>Authorization: Bearer your_key</code></li>
<li><strong>Basic Auth:</strong> Username + password (encoded)</li>
<li><strong>OAuth:</strong> Complex, used by big services like Google</li>
</ul>`,
        examples: [
          {
            code: "import requests\n\n# API with API key\nheaders = {\"Authorization\": \"Bearer your_api_key_here\"}\nresponse = requests.get(\n    \"https://api.example.com/data\",\n    headers=headers\n)\nprint(response.json())",
            output: "Data from authenticated API",
            explanation: "Pass your API key in the Authorization header. The API checks it and grants access."
          },
          {
            code: "import requests\nfrom requests.auth import HTTPBasicAuth\n\n# Basic authentication\nresponse = requests.get(\n    \"https://api.example.com/secure\",\n    auth=HTTPBasicAuth(\"username\", \"password\")\n)\nprint(response.json())",
            output: "Data from secure endpoint",
            explanation: "BasicAuth sends username and password. The server verifies and grants access."
          }
        ]
      },
      {
        title: "Error Handling: What If The Restaurant Is Closed?",
        content: `<p>API calls can fail for many reasons: network down, server error, bad request, etc.</p>
<p>Always check the status code. If it's not 200-299 (success range), something went wrong.</p>`,
        examples: [
          {
            code: "import requests\n\nresponse = requests.get(\"https://api.example.com/invalid\")\n\nif response.status_code == 200:\n    print(response.json())\nelif response.status_code == 404:\n    print(\"Resource not found\")\nelif response.status_code == 500:\n    print(\"Server error\")\nelse:\n    print(f\"Error: {response.status_code}\")",
            output: "Error: 404",
            explanation: "Check status_code. 200 = success. 400s = client error. 500s = server error."
          },
          {
            code: "import requests\n\ntry:\n    response = requests.get(\"https://api.example.com/data\", timeout=5)\n    response.raise_for_status()  # Raise exception if status_code >= 400\n    data = response.json()\n    print(data)\nexcept requests.exceptions.ConnectionError:\n    print(\"Network error\")\nexcept requests.exceptions.HTTPError as e:\n    print(f\"HTTP error: {e}\")\nexcept requests.exceptions.Timeout:\n    print(\"Request timed out\")\nexcept Exception as e:\n    print(f\"Unexpected error: {e}\")",
            output: "Data (if successful)\nError message (if failed)",
            explanation: "Use try/except to handle network errors, timeouts, and HTTP errors gracefully."
          }
        ]
      },
      {
        title: "Pagination: The Menu Comes in Multiple Pages",
        content: `<p>Huge API responses are split into pages. You can only get 20 items at a time, then ask for the next page.</p>
<p>Pagination parameters: <code>?page=1</code>, <code>?limit=20</code>, <code>?offset=0</code></p>`,
        examples: [
          {
            code: "import requests\n\n# Paginate through results\npage = 1\nall_items = []\n\nwhile page <= 5:  # Get first 5 pages\n    response = requests.get(\n        \"https://api.example.com/items\",\n        params={\"page\": page, \"limit\": 20}\n    )\n    data = response.json()\n    all_items.extend(data[\"items\"])\n    page += 1\n\nprint(f\"Got {len(all_items)} items\")",
            output: "Got 100 items",
            explanation: "Loop through pages. Each page has 20 items. We fetch pages 1-5 (100 total)."
          },
          {
            code: "import requests\n\n# Get all pages (keep going until empty)\npage = 1\nall_items = []\n\nwhile True:\n    response = requests.get(\n        \"https://api.example.com/items\",\n        params={\"page\": page}\n    )\n    data = response.json()\n    \n    if not data[\"items\"]:\n        break  # No more items\n    \n    all_items.extend(data[\"items\"])\n    page += 1\n\nprint(f\"Got {len(all_items)} items total\")",
            output: "Got 500 items total",
            explanation: "Keep fetching until we get an empty page. That means we've got everything."
          }
        ]
      }
    ],
    tips: [
      "Always check response.status_code first. 200-299 = success. Anything else = problem.",
      "Use requests.get() for reading, requests.post() for creating, requests.put() for updating, requests.delete() for deleting.",
      "Use .json() to parse JSON responses into Python dictionaries. Everything comes back as JSON.",
      "Use .get() when navigating nested responses to avoid KeyError crashes.",
      "Handle errors gracefully with try/except. Network calls can fail — that's normal."
    ],
    common_mistakes: [
      {
        mistake: "Not checking status_code and assuming the call succeeded",
        fix: "Always check if status_code is in the 200-299 range before accessing data.",
        code: "Wrong: data = response.json()\nRight: if response.status_code == 200: data = response.json()"
      },
      {
        mistake: "Crashing when accessing nested keys that might not exist",
        fix: "Use .get() method instead of direct brackets.",
        code: "Wrong: name = data[\"user\"][\"name\"]\nRight: name = data.get(\"user\", {}).get(\"name\", \"Unknown\")"
      },
      {
        mistake: "Forgetting to pass API key or credentials",
        fix: "Read the API documentation. Most require headers or auth parameter.",
        code: "Always check docs for auth requirements"
      },
      {
        mistake: "Not handling timeouts or network errors",
        fix: "Use try/except for requests. Networks are unreliable.",
        code: "try: requests.get(..., timeout=5)\nexcept requests.exceptions.Timeout:"
      },
      {
        mistake: "Making requests in a loop without handling rate limits",
        fix: "Many APIs limit how many requests per minute. Add delays or check rate limit headers.",
        code: "Use time.sleep(1) between requests if needed"
      }
    ]
  }
};
