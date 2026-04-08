"""50 exercises on FastAPI concepts and patterns."""
from .base import make_exercise

exercises = [
    # BEGINNER: HTTP Basics & API Concepts (1-10)
    make_exercise(
        id="fapi_01",
        title="What is an API?",
        topic="fastapi_ex",
        difficulty=1,
        description="Explain in 1-2 sentences what an API is. Provide a variable `api_explanation` containing your answer.",
        hints=[
            "API stands for Application Programming Interface",
            "Think about how programs communicate with each other"
        ],
        solution="api_explanation = 'An API is a set of rules and protocols that allows different software applications to communicate and exchange data. It defines the methods and data formats that applications can use to request and provide information.'",
        starter_code="# Define api_explanation as a string\napi_explanation = ...",
        check=lambda ns: (
            isinstance(ns.get("api_explanation"), str) and len(ns["api_explanation"]) > 20,
            "api_explanation must be a string with a clear explanation"
        ),
        concepts=["API fundamentals"]
    ),
    make_exercise(
        id="fapi_02",
        title="HTTP GET Request",
        topic="fastapi_ex",
        difficulty=1,
        description="Create a dict called `get_request` that describes what a GET request does. Include 'method' and 'purpose' keys.",
        hints=[
            "GET is used to retrieve data",
            "It's read-only and should not modify server state"
        ],
        solution="""get_request = {
    'method': 'GET',
    'purpose': 'Retrieve data from the server',
    'modifies_data': False,
    'has_request_body': False
}""",
        starter_code="get_request = {...}",
        check=lambda ns: (
            isinstance(ns.get("get_request"), dict) and
            ns["get_request"].get("method") == "GET" and
            "purpose" in ns["get_request"],
            "get_request must be a dict with 'method' and 'purpose' keys"
        ),
        concepts=["HTTP GET"]
    ),
    make_exercise(
        id="fapi_03",
        title="HTTP POST Request",
        topic="fastapi_ex",
        difficulty=1,
        description="Create a dict called `post_request` that describes what a POST request does. Include 'method', 'purpose', and 'has_body' keys.",
        hints=[
            "POST is used to create new data",
            "POST requests typically include a request body with data"
        ],
        solution="""post_request = {
    'method': 'POST',
    'purpose': 'Create new data on the server',
    'has_body': True,
    'modifies_data': True
}""",
        starter_code="post_request = {...}",
        check=lambda ns: (
            isinstance(ns.get("post_request"), dict) and
            ns["post_request"].get("method") == "POST" and
            ns["post_request"].get("has_body") == True,
            "post_request must describe POST with has_body=True"
        ),
        concepts=["HTTP POST"]
    ),
    make_exercise(
        id="fapi_04",
        title="HTTP PUT Request",
        topic="fastapi_ex",
        difficulty=1,
        description="Create a dict called `put_request` describing PUT. Include 'method' and 'action' keys.",
        hints=[
            "PUT is used to replace/update existing data",
            "It replaces the entire resource"
        ],
        solution="""put_request = {
    'method': 'PUT',
    'action': 'Update or replace existing data',
    'requires_id': True
}""",
        starter_code="put_request = {...}",
        check=lambda ns: (
            isinstance(ns.get("put_request"), dict) and
            ns["put_request"].get("method") == "PUT",
            "put_request must have method='PUT'"
        ),
        concepts=["HTTP PUT"]
    ),
    make_exercise(
        id="fapi_05",
        title="HTTP DELETE Request",
        topic="fastapi_ex",
        difficulty=1,
        description="Create a dict called `delete_request` describing DELETE. Include 'method' and 'action' keys.",
        hints=[
            "DELETE is used to remove data",
            "It removes a resource from the server"
        ],
        solution="""delete_request = {
    'method': 'DELETE',
    'action': 'Remove data from the server',
    'requires_id': True
}""",
        starter_code="delete_request = {...}",
        check=lambda ns: (
            isinstance(ns.get("delete_request"), dict) and
            ns["delete_request"].get("method") == "DELETE",
            "delete_request must have method='DELETE'"
        ),
        concepts=["HTTP DELETE"]
    ),
    make_exercise(
        id="fapi_06",
        title="REST API Endpoints",
        topic="fastapi_ex",
        difficulty=1,
        description="Create a dict called `rest_endpoints` mapping HTTP methods to example endpoints for a TODO app.",
        hints=[
            "Map GET, POST, PUT, DELETE to their typical paths",
            "Use /todos as the base path"
        ],
        solution="""rest_endpoints = {
    'GET': '/todos',
    'POST': '/todos',
    'PUT': '/todos/{id}',
    'DELETE': '/todos/{id}'
}""",
        starter_code="rest_endpoints = {...}",
        check=lambda ns: (
            isinstance(ns.get("rest_endpoints"), dict) and
            len(ns["rest_endpoints"]) == 4,
            "rest_endpoints must map 4 HTTP methods"
        ),
        concepts=["REST principles"]
    ),
    make_exercise(
        id="fapi_07",
        title="HTTP Status Codes",
        topic="fastapi_ex",
        difficulty=1,
        description="Create a dict called `status_codes` with at least 5 common HTTP status codes and their meanings.",
        hints=[
            "Include 200, 201, 400, 404, 500",
            "200 = OK, 201 = Created, 400 = Bad Request, 404 = Not Found, 500 = Server Error"
        ],
        solution="""status_codes = {
    200: 'OK',
    201: 'Created',
    204: 'No Content',
    400: 'Bad Request',
    401: 'Unauthorized',
    404: 'Not Found',
    500: 'Internal Server Error'
}""",
        starter_code="status_codes = {...}",
        check=lambda ns: (
            isinstance(ns.get("status_codes"), dict) and
            ns["status_codes"].get(200) == "OK" and
            ns["status_codes"].get(404) == "Not Found",
            "status_codes must include 200 and 404"
        ),
        concepts=["HTTP status codes"]
    ),
    make_exercise(
        id="fapi_08",
        title="Pydantic BaseModel Basics",
        topic="fastapi_ex",
        difficulty=1,
        description="Create a Pydantic model called `Item` with fields: name (str), price (float), description (str).",
        hints=[
            "Import BaseModel from pydantic",
            "Use type hints for each field"
        ],
        solution="""from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str""",
        starter_code="""from pydantic import BaseModel

class Item(BaseModel):
    ...""",
        check=lambda ns: (
            'Item' in ns and hasattr(ns['Item'], 'model_fields') and
            'name' in ns['Item'].model_fields and
            'price' in ns['Item'].model_fields,
            "Item must be a Pydantic model with name, price, description"
        ),
        concepts=["Pydantic BaseModel", "Type hints"]
    ),
    make_exercise(
        id="fapi_09",
        title="Pydantic Model Instantiation",
        topic="fastapi_ex",
        difficulty=1,
        description="Create an Item instance with name='Widget', price=19.99, description='A useful widget'.",
        hints=[
            "Use the Item class from previous exercise",
            "Pass values as keyword arguments"
        ],
        solution="""from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str

item = Item(
    name='Widget',
    price=19.99,
    description='A useful widget'
)""",
        starter_code="""# From previous exercise
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str

# Create instance
item = ...""",
        check=lambda ns: (
            'item' in ns and
            ns['item'].name == 'Widget' and
            ns['item'].price == 19.99,
            "item must be an Item with correct values"
        ),
        concepts=["Pydantic instantiation"]
    ),
    make_exercise(
        id="fapi_10",
        title="Pydantic Model to Dict",
        topic="fastapi_ex",
        difficulty=1,
        description="Convert a Pydantic Item model to a Python dict using model_dump().",
        hints=[
            "Call model_dump() on the instance",
            "It returns a regular Python dict"
        ],
        solution="""from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    description: str

item = Item(name='Gadget', price=29.99, description='A cool gadget')
item_dict = item.model_dump()""",
        starter_code="""# ... Item class from before
item_dict = ...""",
        check=lambda ns: (
            isinstance(ns.get('item_dict'), dict) and
            ns['item_dict'].get('name') == 'Gadget',
            "item_dict must be a dict created from model_dump()"
        ),
        concepts=["Pydantic serialization"]
    ),

    # EASY: Field Validation & Pydantic (11-20)
    make_exercise(
        id="fapi_11",
        title="Field with Constraints",
        topic="fastapi_ex",
        difficulty=2,
        description="Create a Pydantic model `Product` with: name (str, min 1 char), price (float, gt=0).",
        hints=[
            "Import Field from pydantic",
            "Use min_length for strings, gt for greater-than"
        ],
        solution="""from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)""",
        starter_code="""from pydantic import BaseModel, Field

class Product(BaseModel):
    ...""",
        check=lambda ns: (
            'Product' in ns and
            'price' in ns['Product'].model_fields,
            "Product must have name and price fields"
        ),
        concepts=["Field constraints", "Validation"]
    ),
    make_exercise(
        id="fapi_12",
        title="Email Validation",
        topic="fastapi_ex",
        difficulty=2,
        description="Create a Pydantic `User` model with email field that validates email format.",
        hints=[
            "Use EmailStr from pydantic",
            "Or use Field with pattern validation"
        ],
        solution="""from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr""",
        starter_code="""from pydantic import BaseModel

class User(BaseModel):
    ...""",
        check=lambda ns: (
            'User' in ns and
            'email' in ns['User'].model_fields,
            "User must have email field"
        ),
        concepts=["Email validation", "Pydantic validators"]
    ),
    make_exercise(
        id="fapi_13",
        title="Optional Fields",
        topic="fastapi_ex",
        difficulty=2,
        description="Create a Pydantic `Article` with: title (str), content (str), tags (optional list of str).",
        hints=[
            "Use Optional[list[str]] or list[str] | None",
            "Optional fields should have default=None"
        ],
        solution="""from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    title: str
    content: str
    tags: Optional[list[str]] = None""",
        starter_code="""from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    ...""",
        check=lambda ns: (
            'Article' in ns and
            'tags' in ns['Article'].model_fields,
            "Article must have optional tags field"
        ),
        concepts=["Optional fields", "Default values"]
    ),
    make_exercise(
        id="fapi_14",
        title="Nested Pydantic Models",
        topic="fastapi_ex",
        difficulty=2,
        description="Create two models: `Address` (street, city, zip) and `Person` (name, age, address).",
        hints=[
            "Person.address should be of type Address",
            "Nesting enables complex data structures"
        ],
        solution="""from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip: str

class Person(BaseModel):
    name: str
    age: int
    address: Address""",
        starter_code="""from pydantic import BaseModel

class Address(BaseModel):
    ...

class Person(BaseModel):
    ...""",
        check=lambda ns: (
            'Person' in ns and 'Address' in ns and
            'address' in ns['Person'].model_fields,
            "Person must have Address nested model"
        ),
        concepts=["Nested models", "Complex types"]
    ),
    make_exercise(
        id="fapi_15",
        title="Default Values in Pydantic",
        topic="fastapi_ex",
        difficulty=2,
        description="Create a `Config` model with: host (str, default='localhost'), port (int, default=8000).",
        hints=[
            "Use default parameter in field definition",
            "Fields with defaults are optional in instantiation"
        ],
        solution="""from pydantic import BaseModel

class Config(BaseModel):
    host: str = 'localhost'
    port: int = 8000""",
        starter_code="""from pydantic import BaseModel

class Config(BaseModel):
    ...""",
        check=lambda ns: (
            'Config' in ns and
            ns['Config'].model_fields['host'].default == 'localhost',
            "Config must have default values"
        ),
        concepts=["Default values"]
    ),
    make_exercise(
        id="fapi_16",
        title="Custom Validators",
        topic="fastapi_ex",
        difficulty=2,
        description="Create a `Password` model with password field that validates length >= 8.",
        hints=[
            "Use field_validator from pydantic",
            "The validator should check string length"
        ],
        solution="""from pydantic import BaseModel, field_validator

class Password(BaseModel):
    password: str

    @field_validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v""",
        starter_code="""from pydantic import BaseModel, field_validator

class Password(BaseModel):
    ...""",
        check=lambda ns: (
            'Password' in ns and
            hasattr(ns['Password'], 'model_fields'),
            "Password must be a Pydantic model"
        ),
        concepts=["Custom validators", "Field validation"]
    ),
    make_exercise(
        id="fapi_17",
        title="List Validation",
        topic="fastapi_ex",
        difficulty=2,
        description="Create a `TagList` model with tags field: list of strings, min 1 item, each string min 1 char.",
        hints=[
            "Use Field with min_length for the list",
            "Each string in the list also needs validation"
        ],
        solution="""from pydantic import BaseModel, Field

class TagList(BaseModel):
    tags: list[str] = Field(..., min_length=1)""",
        starter_code="""from pydantic import BaseModel, Field

class TagList(BaseModel):
    ...""",
        check=lambda ns: (
            'TagList' in ns and
            'tags' in ns['TagList'].model_fields,
            "TagList must have tags field"
        ),
        concepts=["List validation", "Constraints"]
    ),
    make_exercise(
        id="fapi_18",
        title="Enum Fields in Pydantic",
        topic="fastapi_ex",
        difficulty=2,
        description="Create a `Task` model with status field: Enum('pending', 'in_progress', 'completed').",
        hints=[
            "Import Enum from enum module",
            "Define an Enum class for status values"
        ],
        solution="""from pydantic import BaseModel
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

class Task(BaseModel):
    title: str
    status: TaskStatus""",
        starter_code="""from pydantic import BaseModel
from enum import Enum

class Task(BaseModel):
    ...""",
        check=lambda ns: (
            'Task' in ns and
            'status' in ns['Task'].model_fields,
            "Task must have status field"
        ),
        concepts=["Enum types", "Type safety"]
    ),
    make_exercise(
        id="fapi_19",
        title="Response Model Exclusion",
        topic="fastapi_ex",
        difficulty=2,
        description="Create a `User` model with password field. Write a function that returns user data excluding password.",
        hints=[
            "Use model_dump(exclude={'password'})",
            "This prevents sensitive data exposure"
        ],
        solution="""from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    email: str

def get_user_public(user: User) -> dict:
    return user.model_dump(exclude={'password'})""",
        starter_code="""from pydantic import BaseModel

class User(BaseModel):
    ...

def get_user_public(user: User) -> dict:
    ...""",
        check=lambda ns: (
            'get_user_public' in ns and 'User' in ns and
            callable(ns['get_user_public']) and
            ns['get_user_public'](ns['User'](username='john', password='secret123', email='john@example.com')) == {'username': 'john', 'email': 'john@example.com'},
            "Define User model and get_user_public that excludes password"
        ),
        concepts=["Security", "Field exclusion"]
    ),
    make_exercise(
        id="fapi_20",
        title="Pagination Helper Function",
        topic="fastapi_ex",
        difficulty=2,
        description="Write a function paginate(items: list, page: int, per_page: int) that returns paginated slice.",
        hints=[
            "Calculate skip = (page - 1) * per_page",
            "Return items[skip:skip+per_page]"
        ],
        solution="""def paginate(items: list, page: int, per_page: int) -> list:
    skip = (page - 1) * per_page
    return items[skip:skip + per_page]""",
        starter_code="""def paginate(items: list, page: int, per_page: int) -> list:
    ...""",
        function_name="paginate",
        test_cases=[
            (([1, 2, 3, 4, 5], 1, 2), [1, 2]),
            (([1, 2, 3, 4, 5], 2, 2), [3, 4]),
            (([1, 2, 3, 4, 5], 3, 2), [5]),
        ],
        concepts=["Pagination", "List slicing"]
    ),

    # MEDIUM: Handlers & CRUD (21-35)
    make_exercise(
        id="fapi_21",
        title="Path Parameter Handler",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function get_user(user_id: int, users: dict) that retrieves a user by ID from a dict.",
        hints=[
            "users is a dict with user_id as key",
            "Return the user dict or None if not found"
        ],
        solution="""def get_user(user_id: int, users: dict) -> dict | None:
    return users.get(user_id)""",
        starter_code="""def get_user(user_id: int, users: dict) -> dict | None:
    ...""",
        function_name="get_user",
        test_cases=[
            ((1, {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}), {'id': 1, 'name': 'Alice'}),
            ((3, {1: {'id': 1, 'name': 'Alice'}}), None),
        ],
        concepts=["Path parameters", "Lookups"]
    ),
    make_exercise(
        id="fapi_22",
        title="Query Parameter Handler",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function filter_items(items: list, category: str) that filters by category field.",
        hints=[
            "items is a list of dicts with 'category' key",
            "Return only matching items"
        ],
        solution="""def filter_items(items: list, category: str) -> list:
    return [item for item in items if item.get('category') == category]""",
        starter_code="""def filter_items(items: list, category: str) -> list:
    ...""",
        function_name="filter_items",
        test_cases=[
            (([{'id': 1, 'category': 'A'}, {'id': 2, 'category': 'B'}], 'A'), [{'id': 1, 'category': 'A'}]),
            (([{'id': 1, 'category': 'A'}], 'Z'), []),
        ],
        concepts=["Query parameters", "Filtering"]
    ),
    make_exercise(
        id="fapi_23",
        title="Create Handler (POST)",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function create_item(db: dict, next_id: int, name: str, price: float) that adds item to db.",
        hints=[
            "Generate new ID from next_id",
            "Add to db dict and return the created item with ID"
        ],
        solution="""def create_item(db: dict, next_id: int, name: str, price: float) -> dict:
    item = {'id': next_id, 'name': name, 'price': price}
    db[next_id] = item
    return item""",
        starter_code="""def create_item(db: dict, next_id: int, name: str, price: float) -> dict:
    ...""",
        function_name="create_item",
        test_cases=[
            (({}, 1, 'Widget', 9.99), {'id': 1, 'name': 'Widget', 'price': 9.99}),
        ],
        concepts=["POST handlers", "CRUD Create"]
    ),
    make_exercise(
        id="fapi_24",
        title="Update Handler (PUT)",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function update_item(db: dict, item_id: int, name: str, price: float) that updates an item.",
        hints=[
            "Find item in db by item_id",
            "Update fields and return updated item"
        ],
        solution="""def update_item(db: dict, item_id: int, name: str, price: float) -> dict | None:
    if item_id not in db:
        return None
    db[item_id].update({'name': name, 'price': price})
    return db[item_id]""",
        starter_code="""def update_item(db: dict, item_id: int, name: str, price: float) -> dict | None:
    ...""",
        function_name="update_item",
        test_cases=[
            (({1: {'id': 1, 'name': 'A', 'price': 5}}, 1, 'B', 10), {'id': 1, 'name': 'B', 'price': 10}),
            (({}, 1, 'B', 10), None),
        ],
        concepts=["PUT handlers", "CRUD Update"]
    ),
    make_exercise(
        id="fapi_25",
        title="Delete Handler (DELETE)",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function delete_item(db: dict, item_id: int) that removes item and returns True if deleted.",
        hints=[
            "Check if item_id exists in db",
            "Delete it and return True, or return False if not found"
        ],
        solution="""def delete_item(db: dict, item_id: int) -> bool:
    if item_id in db:
        del db[item_id]
        return True
    return False""",
        starter_code="""def delete_item(db: dict, item_id: int) -> bool:
    ...""",
        function_name="delete_item",
        test_cases=[
            (({1: {'id': 1}}, 1), True),
            (({}, 1), False),
        ],
        concepts=["DELETE handlers", "CRUD Delete"]
    ),
    make_exercise(
        id="fapi_26",
        title="CRUD Operations Dict",
        topic="fastapi_ex",
        difficulty=3,
        description="Implement a simple CRUD operations dict with 4 functions: create, read, update, delete.",
        hints=[
            "Each function takes db dict as first arg",
            "Return appropriate values per operation"
        ],
        solution="""db = {}
next_id = 1

def create(name, price):
    global next_id
    item = {'id': next_id, 'name': name, 'price': price}
    db[next_id] = item
    next_id += 1
    return item

def read(item_id):
    return db.get(item_id)

def update(item_id, name, price):
    if item_id not in db:
        return None
    db[item_id].update({'name': name, 'price': price})
    return db[item_id]

def delete(item_id):
    if item_id in db:
        del db[item_id]
        return True
    return False""",
        starter_code="""db = {}
next_id = 1

def create(name, price):
    ...

def read(item_id):
    ...

def update(item_id, name, price):
    ...

def delete(item_id):
    ...""",
        check=lambda ns: (
            callable(ns.get('create')) and
            callable(ns.get('read')) and
            callable(ns.get('update')) and
            callable(ns.get('delete')),
            "Must define create, read, update, delete functions"
        ),
        concepts=["CRUD operations", "In-memory database"]
    ),
    make_exercise(
        id="fapi_27",
        title="Request Body Validation",
        topic="fastapi_ex",
        difficulty=3,
        description="Create a Pydantic model for a POST request body: CreateItem with name, price, description.",
        hints=[
            "Use BaseModel with type hints",
            "Add validation: name min length 1, price > 0"
        ],
        solution="""from pydantic import BaseModel, Field

class CreateItem(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    description: str = Field(..., min_length=1)""",
        starter_code="""from pydantic import BaseModel, Field

class CreateItem(BaseModel):
    ...""",
        check=lambda ns: (
            'CreateItem' in ns and
            'name' in ns['CreateItem'].model_fields,
            "CreateItem must have name, price, description"
        ),
        concepts=["Request bodies", "Validation"]
    ),
    make_exercise(
        id="fapi_28",
        title="Response Model",
        topic="fastapi_ex",
        difficulty=3,
        description="Create two models: ItemRequest (without id) and ItemResponse (with id). Show the pattern.",
        hints=[
            "ItemResponse includes the id field",
            "ItemRequest is for input, ItemResponse for output"
        ],
        solution="""from pydantic import BaseModel

class ItemRequest(BaseModel):
    name: str
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float""",
        starter_code="""from pydantic import BaseModel

class ItemRequest(BaseModel):
    ...

class ItemResponse(BaseModel):
    ...""",
        check=lambda ns: (
            'ItemRequest' in ns and 'ItemResponse' in ns,
            "Must define both ItemRequest and ItemResponse"
        ),
        concepts=["Request/response models"]
    ),
    make_exercise(
        id="fapi_29",
        title="Error Handler - Not Found",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function that raises an HTTPException for 404 Not Found.",
        hints=[
            "Import HTTPException from fastapi",
            "Raise with status_code=404 and detail message"
        ],
        solution="""from fastapi import HTTPException

def get_item_or_404(item_id: int, db: dict):
    if item_id not in db:
        raise HTTPException(status_code=404, detail='Item not found')
    return db[item_id]""",
        starter_code="""from fastapi import HTTPException

def get_item_or_404(item_id: int, db: dict):
    ...""",
        function_name="get_item_or_404",
        test_cases=[
            ((1, {1: {'id': 1, 'name': 'A'}}), {'id': 1, 'name': 'A'}),
        ],
        concepts=["Error handling", "HTTP exceptions"]
    ),
    make_exercise(
        id="fapi_30",
        title="Dependency Injection Pattern",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function get_db() that returns a sample db dict. Show how it could be a dependency.",
        hints=[
            "Dependency injection is a pattern of passing dependencies as parameters",
            "In FastAPI, you'd use Depends() to inject this at runtime"
        ],
        solution="""def get_db() -> dict:
    return {
        1: {'id': 1, 'name': 'Item A', 'price': 9.99},
        2: {'id': 2, 'name': 'Item B', 'price': 19.99}
    }""",
        starter_code="""def get_db() -> dict:
    ...""",
        function_name="get_db",
        test_cases=[
            ((), {1: {'id': 1, 'name': 'Item A', 'price': 9.99}, 2: {'id': 2, 'name': 'Item B', 'price': 19.99}}),
        ],
        concepts=["Dependency injection"]
    ),
    make_exercise(
        id="fapi_31",
        title="API Key Validation",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function verify_api_key(api_key: str) that validates the key. Valid key is 'secret-key-123'.",
        hints=[
            "Compare api_key with expected value",
            "Raise HTTPException if invalid"
        ],
        solution="""from fastapi import HTTPException

def verify_api_key(api_key: str) -> bool:
    if api_key != 'secret-key-123':
        raise HTTPException(status_code=401, detail='Invalid API key')
    return True""",
        starter_code="""from fastapi import HTTPException

def verify_api_key(api_key: str) -> bool:
    ...""",
        function_name="verify_api_key",
        test_cases=[
            (('secret-key-123',), True),
        ],
        concepts=["API key auth", "Validation"]
    ),
    make_exercise(
        id="fapi_32",
        title="Sorting Handler",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function sort_items(items: list, sort_by: str) that sorts by 'name' or 'price' field.",
        hints=[
            "Use sorted() with a key function",
            "sort_by parameter indicates which field to sort by"
        ],
        solution="""def sort_items(items: list, sort_by: str) -> list:
    if sort_by not in ['name', 'price']:
        return items
    return sorted(items, key=lambda x: x.get(sort_by, 0))""",
        starter_code="""def sort_items(items: list, sort_by: str) -> list:
    ...""",
        function_name="sort_items",
        test_cases=[
            (([{'name': 'B', 'price': 10}, {'name': 'A', 'price': 5}], 'name'), [{'name': 'A', 'price': 5}, {'name': 'B', 'price': 10}]),
            (([{'name': 'B', 'price': 10}, {'name': 'A', 'price': 5}], 'price'), [{'name': 'A', 'price': 5}, {'name': 'B', 'price': 10}]),
        ],
        concepts=["Sorting", "Query parameters"]
    ),
    make_exercise(
        id="fapi_33",
        title="Pagination with Offset",
        topic="fastapi_ex",
        difficulty=3,
        description="Write paginate_with_offset(items: list, skip: int, limit: int) using skip/limit pattern.",
        hints=[
            "skip = number of items to skip from start",
            "limit = max number of items to return"
        ],
        solution="""def paginate_with_offset(items: list, skip: int, limit: int) -> list:
    return items[skip:skip + limit]""",
        starter_code="""def paginate_with_offset(items: list, skip: int, limit: int) -> list:
    ...""",
        function_name="paginate_with_offset",
        test_cases=[
            (([1, 2, 3, 4, 5], 0, 2), [1, 2]),
            (([1, 2, 3, 4, 5], 2, 2), [3, 4]),
        ],
        concepts=["Pagination", "Skip/limit pattern"]
    ),
    make_exercise(
        id="fapi_34",
        title="Timestamp Tracking",
        topic="fastapi_ex",
        difficulty=3,
        description="Create a Pydantic model for a blog Post with created_at and updated_at timestamp fields.",
        hints=[
            "Use datetime from typing/datetime module",
            "Optional or use default_factory for auto-generation"
        ],
        solution="""from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime""",
        starter_code="""from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    ...""",
        check=lambda ns: (
            'Post' in ns and
            'created_at' in ns['Post'].model_fields,
            "Post must have timestamp fields"
        ),
        concepts=["Timestamps", "Datetime handling"]
    ),
    make_exercise(
        id="fapi_35",
        title="Search Query Handler",
        topic="fastapi_ex",
        difficulty=3,
        description="Write a function search_items(items: list, q: str) that searches name field (case-insensitive).",
        hints=[
            "Use lower() for case-insensitive comparison",
            "Check if search term is in the name"
        ],
        solution="""def search_items(items: list, q: str) -> list:
    return [item for item in items if q.lower() in item.get('name', '').lower()]""",
        starter_code="""def search_items(items: list, q: str) -> list:
    ...""",
        function_name="search_items",
        test_cases=[
            (([{'name': 'Apple'}, {'name': 'Banana'}], 'app'), [{'name': 'Apple'}]),
            (([{'name': 'Apple'}, {'name': 'Apricot'}], 'ap'), [{'name': 'Apple'}, {'name': 'Apricot'}]),
        ],
        concepts=["Search", "Query filtering"]
    ),

    # HARD: Advanced Patterns (36-45)
    make_exercise(
        id="fapi_36",
        title="Authentication Token Validation",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a function decode_token(token: str) that extracts username from 'Bearer username' format.",
        hints=[
            "Token format is 'Bearer <username>'",
            "Split on space and validate format"
        ],
        solution="""def decode_token(token: str) -> str | None:
    parts = token.split()
    if len(parts) != 2 or parts[0] != 'Bearer':
        return None
    return parts[1]""",
        starter_code="""def decode_token(token: str) -> str | None:
    ...""",
        function_name="decode_token",
        test_cases=[
            (('Bearer alice',), 'alice'),
            (('Bearer bob',), 'bob'),
            (('InvalidToken',), None),
        ],
        concepts=["Authentication", "Token parsing"]
    ),
    make_exercise(
        id="fapi_37",
        title="Rate Limiting Counter",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a function check_rate_limit(user_id: int, limit: int) using a dict to track requests.",
        hints=[
            "Maintain a dict tracking user request counts",
            "Increment count, return True if under limit"
        ],
        solution="""request_counts = {}

def check_rate_limit(user_id: int, limit: int) -> bool:
    current = request_counts.get(user_id, 0)
    if current >= limit:
        return False
    request_counts[user_id] = current + 1
    return True""",
        starter_code="""request_counts = {}

def check_rate_limit(user_id: int, limit: int) -> bool:
    ...""",
        function_name="check_rate_limit",
        test_cases=[
            ((1, 5), True),
            ((1, 5), True),
        ],
        concepts=["Rate limiting", "State tracking"]
    ),
    make_exercise(
        id="fapi_38",
        title="Batch Insert Handler",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a function batch_create(db: dict, items: list, start_id: int) that creates multiple items.",
        hints=[
            "Iterate over items list",
            "Assign incrementing IDs starting from start_id"
        ],
        solution="""def batch_create(db: dict, items: list, start_id: int) -> list:
    created = []
    for i, item_data in enumerate(items):
        item_id = start_id + i
        db[item_id] = {'id': item_id, **item_data}
        created.append(db[item_id])
    return created""",
        starter_code="""def batch_create(db: dict, items: list, start_id: int) -> list:
    ...""",
        function_name="batch_create",
        test_cases=[
            (({}, [{'name': 'A'}, {'name': 'B'}], 1), [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]),
        ],
        concepts=["Batch operations", "Bulk inserts"]
    ),
    make_exercise(
        id="fapi_39",
        title="Partial Update (PATCH) Logic",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a function partial_update(db: dict, item_id: int, updates: dict) that applies only provided fields.",
        hints=[
            "Only update fields that are in the updates dict",
            "Don't overwrite missing fields"
        ],
        solution="""def partial_update(db: dict, item_id: int, updates: dict) -> dict | None:
    if item_id not in db:
        return None
    for key, value in updates.items():
        if value is not None:
            db[item_id][key] = value
    return db[item_id]""",
        starter_code="""def partial_update(db: dict, item_id: int, updates: dict) -> dict | None:
    ...""",
        function_name="partial_update",
        test_cases=[
            (({1: {'id': 1, 'name': 'A', 'price': 5}}, 1, {'name': 'B'}), {'id': 1, 'name': 'B', 'price': 5}),
        ],
        concepts=["PATCH operations", "Partial updates"]
    ),
    make_exercise(
        id="fapi_40",
        title="Middleware Pattern - Request Logging",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a simple request logging function log_request(method: str, path: str) that formats a log entry.",
        hints=[
            "Return a formatted string with timestamp, method, path",
            "Use datetime.now() for timestamp"
        ],
        solution="""from datetime import datetime

def log_request(method: str, path: str) -> str:
    timestamp = datetime.now().isoformat()
    return f'{timestamp} {method} {path}'""",
        starter_code="""from datetime import datetime

def log_request(method: str, path: str) -> str:
    ...""",
        function_name="log_request",
        test_cases=[
            (('GET', '/items'), lambda result: 'GET' in result and '/items' in result),
        ],
        concepts=["Middleware", "Logging"]
    ),
    make_exercise(
        id="fapi_41",
        title="Permission Check Function",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a function check_permission(user_role: str, resource: str) that validates access.",
        hints=[
            "Admin has access to all resources",
            "User can access 'public' resource only"
        ],
        solution="""def check_permission(user_role: str, resource: str) -> bool:
    if user_role == 'admin':
        return True
    if user_role == 'user' and resource == 'public':
        return True
    return False""",
        starter_code="""def check_permission(user_role: str, resource: str) -> bool:
    ...""",
        function_name="check_permission",
        test_cases=[
            (('admin', 'private'), True),
            (('user', 'public'), True),
            (('user', 'private'), False),
        ],
        concepts=["Authorization", "Access control"]
    ),
    make_exercise(
        id="fapi_42",
        title="Data Transformation Pipeline",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a function transform_response(items: list) that formats items with uppercase names.",
        hints=[
            "Apply transformation to each item",
            "Return new list without mutating originals"
        ],
        solution="""def transform_response(items: list) -> list:
    return [{'id': item['id'], 'name': item['name'].upper(), 'price': item['price']} for item in items]""",
        starter_code="""def transform_response(items: list) -> list:
    ...""",
        function_name="transform_response",
        test_cases=[
            (([{'id': 1, 'name': 'widget', 'price': 10}],), [{'id': 1, 'name': 'WIDGET', 'price': 10}]),
        ],
        concepts=["Data transformation", "Response formatting"]
    ),
    make_exercise(
        id="fapi_43",
        title="Multi-level Filtering",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a function filter_by_multiple(items: list, category: str, min_price: float) that filters on both.",
        hints=[
            "Both filters must pass for item to be included",
            "Use multiple conditions in list comprehension"
        ],
        solution="""def filter_by_multiple(items: list, category: str, min_price: float) -> list:
    return [item for item in items if item.get('category') == category and item.get('price', 0) >= min_price]""",
        starter_code="""def filter_by_multiple(items: list, category: str, min_price: float) -> list:
    ...""",
        function_name="filter_by_multiple",
        test_cases=[
            (([{'category': 'A', 'price': 10}, {'category': 'A', 'price': 5}, {'category': 'B', 'price': 10}], 'A', 7), [{'category': 'A', 'price': 10}]),
        ],
        concepts=["Complex filtering", "Multiple conditions"]
    ),
    make_exercise(
        id="fapi_44",
        title="Response Status Code Mapping",
        topic="fastapi_ex",
        difficulty=4,
        description="Create a dict mapping actions to HTTP status codes: created→201, updated→200, deleted→204.",
        hints=[
            "Map action names to appropriate status codes",
            "201=Created, 200=OK, 204=No Content"
        ],
        solution="""status_code_map = {
    'created': 201,
    'updated': 200,
    'deleted': 204,
    'retrieved': 200,
    'error': 400
}""",
        starter_code="""status_code_map = {...}""",
        check=lambda ns: (
            isinstance(ns.get('status_code_map'), dict) and
            ns['status_code_map'].get('created') == 201,
            "status_code_map must map actions to status codes"
        ),
        concepts=["Status codes", "Response design"]
    ),
    make_exercise(
        id="fapi_45",
        title="Aggregate Query (Count/Sum)",
        topic="fastapi_ex",
        difficulty=4,
        description="Write a function aggregate_stats(items: list) that returns count and sum of prices.",
        hints=[
            "Count the items",
            "Sum the price field"
        ],
        solution="""def aggregate_stats(items: list) -> dict:
    return {
        'count': len(items),
        'total_price': sum(item.get('price', 0) for item in items),
        'avg_price': sum(item.get('price', 0) for item in items) / len(items) if items else 0
    }""",
        starter_code="""def aggregate_stats(items: list) -> dict:
    ...""",
        function_name="aggregate_stats",
        test_cases=[
            (([{'price': 10}, {'price': 20}],), {'count': 2, 'total_price': 30, 'avg_price': 15}),
        ],
        concepts=["Aggregation", "Statistics"]
    ),

    # CHALLENGE: Real-world Patterns (46-50)
    make_exercise(
        id="fapi_46",
        title="Todo API - Complete CRUD",
        topic="fastapi_ex",
        difficulty=5,
        description="Implement a complete TODO API with create, read, list, update, delete, and complete operations.",
        hints=[
            "Use in-memory dict as database",
            "Support marking todos as complete",
            "Generate IDs automatically"
        ],
        solution="""class TodoAPI:
    def __init__(self):
        self.db = {}
        self.next_id = 1

    def create(self, title: str, description: str = '') -> dict:
        todo = {
            'id': self.next_id,
            'title': title,
            'description': description,
            'completed': False
        }
        self.db[self.next_id] = todo
        self.next_id += 1
        return todo

    def get(self, todo_id: int) -> dict | None:
        return self.db.get(todo_id)

    def list_all(self) -> list:
        return list(self.db.values())

    def update(self, todo_id: int, title: str, description: str) -> dict | None:
        if todo_id not in self.db:
            return None
        self.db[todo_id]['title'] = title
        self.db[todo_id]['description'] = description
        return self.db[todo_id]

    def complete(self, todo_id: int) -> dict | None:
        if todo_id not in self.db:
            return None
        self.db[todo_id]['completed'] = True
        return self.db[todo_id]

    def delete(self, todo_id: int) -> bool:
        if todo_id in self.db:
            del self.db[todo_id]
            return True
        return False""",
        starter_code="""class TodoAPI:
    def __init__(self):
        self.db = {}
        self.next_id = 1

    def create(self, title: str, description: str = '') -> dict:
        ...

    def get(self, todo_id: int) -> dict | None:
        ...

    def list_all(self) -> list:
        ...

    def update(self, todo_id: int, title: str, description: str) -> dict | None:
        ...

    def complete(self, todo_id: int) -> dict | None:
        ...

    def delete(self, todo_id: int) -> bool:
        ...""",
        check=lambda ns: (
            'TodoAPI' in ns and
            all(hasattr(ns['TodoAPI'], m) for m in ['create', 'get', 'list_all', 'update', 'complete', 'delete']),
            "TodoAPI must have all CRUD methods"
        ),
        concepts=["Full CRUD", "Real-world API", "State management"]
    ),
    make_exercise(
        id="fapi_47",
        title="User Management API",
        topic="fastapi_ex",
        difficulty=5,
        description="Create User model with validation, and implement a UserManager class with registration and login.",
        hints=[
            "User: email, password, username validation",
            "UserManager: register (checks email exists), get_by_email, authenticate"
        ],
        solution="""from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str

class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def register(self, username: str, email: str, password: str) -> dict | None:
        # Check if email already exists
        if any(u['email'] == email for u in self.users.values()):
            return None
        user = {
            'id': self.next_id,
            'username': username,
            'email': email,
            'password': password  # In real app, hash this!
        }
        self.users[self.next_id] = user
        self.next_id += 1
        return user

    def authenticate(self, email: str, password: str) -> dict | None:
        for user in self.users.values():
            if user['email'] == email and user['password'] == password:
                return user
        return None""",
        starter_code="""from pydantic import BaseModel, EmailStr

class User(BaseModel):
    ...

class UserManager:
    def __init__(self):
        ...

    def register(self, username: str, email: str, password: str) -> dict | None:
        ...

    def authenticate(self, email: str, password: str) -> dict | None:
        ...""",
        check=lambda ns: (
            'User' in ns and 'UserManager' in ns,
            "Must define User and UserManager classes"
        ),
        concepts=["User management", "Authentication", "Email validation"]
    ),
    make_exercise(
        id="fapi_48",
        title="Blog API with Categories",
        topic="fastapi_ex",
        difficulty=5,
        description="Implement a BlogAPI with posts that belong to categories. Support create, filter by category, search.",
        hints=[
            "Post model: title, content, category",
            "BlogAPI: create_post, get_by_category, search_posts",
            "Store in dict with auto-incrementing IDs"
        ],
        solution="""class BlogAPI:
    def __init__(self):
        self.posts = {}
        self.next_id = 1

    def create_post(self, title: str, content: str, category: str) -> dict:
        post = {
            'id': self.next_id,
            'title': title,
            'content': content,
            'category': category
        }
        self.posts[self.next_id] = post
        self.next_id += 1
        return post

    def get_by_category(self, category: str) -> list:
        return [p for p in self.posts.values() if p['category'] == category]

    def search_posts(self, query: str) -> list:
        q = query.lower()
        return [p for p in self.posts.values() if q in p['title'].lower() or q in p['content'].lower()]

    def list_all(self) -> list:
        return list(self.posts.values())""",
        starter_code="""class BlogAPI:
    def __init__(self):
        self.posts = {}
        self.next_id = 1

    def create_post(self, title: str, content: str, category: str) -> dict:
        ...

    def get_by_category(self, category: str) -> list:
        ...

    def search_posts(self, query: str) -> list:
        ...

    def list_all(self) -> list:
        ...""",
        check=lambda ns: (
            'BlogAPI' in ns and
            all(hasattr(ns['BlogAPI'], m) for m in ['create_post', 'get_by_category', 'search_posts']),
            "BlogAPI must have post management methods"
        ),
        concepts=["Categories", "Search", "Complex queries"]
    ),
    make_exercise(
        id="fapi_49",
        title="Shopping Cart API",
        topic="fastapi_ex",
        difficulty=5,
        description="Build a CartAPI with add_item, remove_item, get_total, apply_discount operations.",
        hints=[
            "Cart: items dict with item_id: quantity",
            "Store price info for calculation",
            "calculate_total with optional discount percentage"
        ],
        solution="""class CartAPI:
    def __init__(self):
        self.items = {}
        self.prices = {}

    def set_price(self, item_id: int, price: float):
        self.prices[item_id] = price

    def add_item(self, item_id: int, quantity: int = 1):
        self.items[item_id] = self.items.get(item_id, 0) + quantity

    def remove_item(self, item_id: int):
        if item_id in self.items:
            del self.items[item_id]

    def get_total(self, discount_percent: float = 0) -> float:
        total = sum(self.prices.get(item_id, 0) * qty for item_id, qty in self.items.items())
        if discount_percent > 0:
            total = total * (1 - discount_percent / 100)
        return total

    def get_items_count(self) -> int:
        return sum(self.items.values())""",
        starter_code="""class CartAPI:
    def __init__(self):
        self.items = {}
        self.prices = {}

    def set_price(self, item_id: int, price: float):
        ...

    def add_item(self, item_id: int, quantity: int = 1):
        ...

    def remove_item(self, item_id: int):
        ...

    def get_total(self, discount_percent: float = 0) -> float:
        ...

    def get_items_count(self) -> int:
        ...""",
        check=lambda ns: (
            'CartAPI' in ns and
            all(hasattr(ns['CartAPI'], m) for m in ['add_item', 'remove_item', 'get_total']),
            "CartAPI must have cart operations"
        ),
        concepts=["E-commerce", "Cart logic", "Discounts"]
    ),
    make_exercise(
        id="fapi_50",
        title="Inventory Management API",
        topic="fastapi_ex",
        difficulty=5,
        description="Implement an InventoryAPI with stock tracking, restock, and low-stock alerts.",
        hints=[
            "Track item_id: (name, quantity, reorder_level)",
            "Methods: restock, consume (reduce), get_low_stock, get_inventory",
            "Low stock = quantity < reorder_level"
        ],
        solution="""class InventoryAPI:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id: int, name: str, quantity: int, reorder_level: int = 10):
        self.inventory[item_id] = {
            'name': name,
            'quantity': quantity,
            'reorder_level': reorder_level
        }

    def restock(self, item_id: int, quantity: int) -> dict | None:
        if item_id not in self.inventory:
            return None
        self.inventory[item_id]['quantity'] += quantity
        return self.inventory[item_id]

    def consume(self, item_id: int, quantity: int) -> dict | None:
        if item_id not in self.inventory:
            return None
        if self.inventory[item_id]['quantity'] < quantity:
            return None
        self.inventory[item_id]['quantity'] -= quantity
        return self.inventory[item_id]

    def get_low_stock(self) -> list:
        return [
            {**v, 'item_id': k}
            for k, v in self.inventory.items()
            if v['quantity'] < v['reorder_level']
        ]

    def get_inventory(self) -> list:
        return [{**v, 'item_id': k} for k, v in self.inventory.items()]""",
        starter_code="""class InventoryAPI:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id: int, name: str, quantity: int, reorder_level: int = 10):
        ...

    def restock(self, item_id: int, quantity: int) -> dict | None:
        ...

    def consume(self, item_id: int, quantity: int) -> dict | None:
        ...

    def get_low_stock(self) -> list:
        ...

    def get_inventory(self) -> list:
        ...""",
        check=lambda ns: (
            'InventoryAPI' in ns and
            all(hasattr(ns['InventoryAPI'], m) for m in ['add_item', 'restock', 'consume', 'get_low_stock']),
            "InventoryAPI must have inventory operations"
        ),
        concepts=["Inventory", "Stock tracking", "Real-world API"]
    ),
]
