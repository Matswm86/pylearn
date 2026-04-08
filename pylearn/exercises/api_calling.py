"""50 exercises on calling APIs with Python."""

import json
from urllib.parse import urlencode, quote, parse_qs
from base64 import b64encode
import hashlib
import hmac

from .base import make_exercise

exercises = [
    # BEGINNER (1-10): Foundational API concepts
    make_exercise(
        id="api_01",
        title="What is an API? REST Basics",
        topic="api_calling",
        difficulty=1,
        description="Understand what an API is. API stands for Application Programming Interface. REST APIs use HTTP methods (GET, POST, PUT, DELETE) to interact with resources. Given a description of what an action should do, identify the correct HTTP method.",
        hints=[
            "GET retrieves data (safe, idempotent)",
            "POST creates new data (not idempotent)",
            "PUT updates existing data (idempotent)",
            "DELETE removes data (idempotent)",
        ],
        solution="""
def identify_http_method(action):
    mapping = {
        "fetch a user profile": "GET",
        "create a new post": "POST",
        "update user settings": "PUT",
        "remove a comment": "DELETE",
        "retrieve a list of items": "GET",
    }
    return mapping.get(action, "UNKNOWN")
""",
        function_name="identify_http_method",
        test_cases=[
            (("fetch a user profile",), "GET"),
            (("create a new post",), "POST"),
            (("update user settings",), "PUT"),
            (("remove a comment",), "DELETE"),
            (("retrieve a list of items",), "GET"),
        ],
        concepts=["REST", "HTTP methods", "GET", "POST", "PUT", "DELETE"],
    ),
    make_exercise(
        id="api_02",
        title="Parse a JSON String",
        topic="api_calling",
        difficulty=1,
        description="APIs return data as JSON. Learn to parse JSON strings into Python objects using json.loads(). Convert a JSON string into a Python dictionary.",
        hints=[
            "Use json.loads() to convert a string to a Python dict",
            "The result will be a dictionary with the same keys as the JSON",
        ],
        solution="""
import json

def parse_json_response(json_string):
    return json.loads(json_string)
""",
        function_name="parse_json_response",
        test_cases=[
            ('{"name": "Alice", "age": 30}', {"name": "Alice", "age": 30}),
            ('{"status": "success"}', {"status": "success"}),
            ('{"users": [1, 2, 3]}', {"users": [1, 2, 3]}),
        ],
        concepts=["json.loads", "JSON parsing", "Python dicts"],
    ),
    make_exercise(
        id="api_03",
        title="Convert Python Object to JSON",
        topic="api_calling",
        difficulty=1,
        description="When sending data to an API, convert Python objects to JSON using json.dumps(). Convert a Python dictionary to a JSON string.",
        hints=[
            "Use json.dumps() to convert a Python dict to a string",
            "The result will be a valid JSON string",
        ],
        solution="""
import json

def dict_to_json(data):
    return json.dumps(data)
""",
        function_name="dict_to_json",
        test_cases=[
            ({"name": "Bob", "age": 25}, '{"name": "Bob", "age": 25}'),
            ({"status": "error"}, '{"status": "error"}'),
            ({"items": [1, 2, 3]}, '{"items": [1, 2, 3]}'),
        ],
        concepts=["json.dumps", "JSON serialization", "Data encoding"],
    ),
    make_exercise(
        id="api_04",
        title="Extract Nested Data from JSON",
        topic="api_calling",
        difficulty=1,
        description="API responses often have nested data. Extract a specific value from a nested JSON structure.",
        hints=[
            "Chain dictionary accesses: dict['key1']['key2']",
            "Consider using .get() for safe access with defaults",
        ],
        solution="""
def extract_user_email(response):
    return response['user']['email']
""",
        function_name="extract_user_email",
        test_cases=[
            ({"user": {"email": "alice@example.com"}}, "alice@example.com"),
            ({"user": {"email": "bob@test.org"}}, "bob@test.org"),
            ({"user": {"email": "charlie@api.io"}}, "charlie@api.io"),
        ],
        concepts=["Nested dictionaries", "Data extraction", "JSON navigation"],
    ),
    make_exercise(
        id="api_05",
        title="Build a Simple URL with Query Parameters",
        topic="api_calling",
        difficulty=1,
        description="API endpoints often accept query parameters. Build a complete URL with parameters like ?name=value&other=value2.",
        hints=[
            "Base URL ends before the ?",
            "Parameters are key=value pairs joined by &",
            "Start parameters section with ?",
        ],
        solution="""
def build_url(base, params):
    param_str = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base}?{param_str}"
""",
        function_name="build_url",
        test_cases=[
            (("https://api.example.com/users", {"id": "123"}), "https://api.example.com/users?id=123"),
            (("https://api.example.com/search", {"q": "python"}), "https://api.example.com/search?q=python"),
            (("https://api.example.com/data", {"x": "1", "y": "2"}), "https://api.example.com/data?x=1&y=2"),
        ],
        concepts=["Query strings", "URL building", "Parameters"],
    ),
    make_exercise(
        id="api_06",
        title="Extract Data from a List in Response",
        topic="api_calling",
        difficulty=1,
        description="Many APIs return a list of items. Extract all names from a list of user objects.",
        hints=[
            "Use a list comprehension: [item['name'] for item in list]",
            "Or use a for loop to iterate and collect names",
        ],
        solution="""
def extract_user_names(response):
    return [user['name'] for user in response['users']]
""",
        function_name="extract_user_names",
        test_cases=[
            ({"users": [{"name": "Alice"}, {"name": "Bob"}]}, ["Alice", "Bob"]),
            ({"users": [{"name": "Charlie"}, {"name": "Diana"}, {"name": "Eve"}]}, ["Charlie", "Diana", "Eve"]),
            ({"users": [{"name": "Frank"}]}, ["Frank"]),
        ],
        concepts=["List comprehension", "Iteration", "Data extraction"],
    ),
    make_exercise(
        id="api_07",
        title="Check HTTP Status Code",
        topic="api_calling",
        difficulty=1,
        description="HTTP responses have status codes. 200 = success, 404 = not found, 500 = server error, 401 = unauthorized. Given a status code, identify its meaning.",
        hints=[
            "200-299: Success",
            "400-499: Client error",
            "500-599: Server error",
        ],
        solution="""
def check_status(code):
    if code == 200:
        return "OK"
    elif code == 404:
        return "Not Found"
    elif code == 500:
        return "Server Error"
    elif code == 401:
        return "Unauthorized"
    else:
        return "Unknown"
""",
        function_name="check_status",
        test_cases=[
            ((200,), "OK"),
            ((404,), "Not Found"),
            ((500,), "Server Error"),
            ((401,), "Unauthorized"),
        ],
        concepts=["HTTP status codes", "Error handling", "Response validation"],
    ),
    make_exercise(
        id="api_08",
        title="Build a Content-Type Header",
        topic="api_calling",
        difficulty=1,
        description="HTTP headers tell the server about the request. Build a headers dictionary with Content-Type set to application/json.",
        hints=[
            "Headers are dictionaries with string keys and values",
            "Content-Type for JSON is 'application/json'",
        ],
        solution="""
def build_headers(content_type="application/json"):
    return {"Content-Type": content_type}
""",
        function_name="build_headers",
        test_cases=[
            ((), {"Content-Type": "application/json"}),
            (("application/xml",), {"Content-Type": "application/xml"}),
            (("text/plain",), {"Content-Type": "text/plain"}),
        ],
        concepts=["HTTP headers", "Content-Type", "Request metadata"],
    ),
    make_exercise(
        id="api_09",
        title="Parse List from API Response",
        topic="api_calling",
        difficulty=1,
        description="Extract a paginated list of items from an API response. Given a response with 'data' key containing items, return the count.",
        hints=[
            "Access the 'data' key from the response dict",
            "Use len() to count items in the list",
        ],
        solution="""
def count_items(response):
    return len(response['data'])
""",
        function_name="count_items",
        test_cases=[
            ({"data": [1, 2, 3]}, 3),
            ({"data": []}, 0),
            ({"data": [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]}, 4),
        ],
        concepts=["List access", "Counting", "Data aggregation"],
    ),
    make_exercise(
        id="api_10",
        title="Build Basic Auth Header",
        topic="api_calling",
        difficulty=1,
        description="Many APIs use Basic Authentication: combine username and password into a base64-encoded header. Build an Authorization header for Basic auth.",
        hints=[
            "Basic auth format: 'username:password'",
            "Encode to base64: b64encode(b'username:password')",
            "Header format: 'Basic ' + base64_string",
        ],
        solution="""
from base64 import b64encode

def build_basic_auth(username, password):
    credentials = f"{username}:{password}"
    encoded = b64encode(credentials.encode()).decode()
    return f"Basic {encoded}"
""",
        function_name="build_basic_auth",
        test_cases=[
            (("user", "pass"), "Basic dXNlcjpwYXNz"),
            (("admin", "secret"), "Basic YWRtaW46c2VjcmV0"),
            (("test", "123"), "Basic dGVzdDoxMjM="),
        ],
        concepts=["Basic Auth", "Base64 encoding", "Authentication"],
    ),
    # EASY (11-20): URL and header building
    make_exercise(
        id="api_11",
        title="URL Encode Query Parameters",
        topic="api_calling",
        difficulty=2,
        description="Special characters in query parameters must be URL-encoded. Use urllib.parse.urlencode() to safely encode parameters.",
        hints=[
            "Use urlencode() from urllib.parse",
            "Spaces become %20, special chars are encoded",
        ],
        solution="""
from urllib.parse import urlencode

def encode_params(params):
    return urlencode(params)
""",
        function_name="encode_params",
        test_cases=[
            (({"q": "hello world"},), "q=hello+world"),
            (({"name": "John Doe", "age": "30"},), "name=John+Doe&age=30"),
            (({"search": "api & integration"},), "search=api+%26+integration"),
        ],
        concepts=["URL encoding", "urlencode", "Parameter escaping"],
    ),
    make_exercise(
        id="api_12",
        title="Build Complete API Request URL",
        topic="api_calling",
        difficulty=2,
        description="Combine base URL, endpoint, and query parameters to build a complete API request URL.",
        hints=[
            "Pattern: base_url + '/' + endpoint + '?' + encoded_params",
            "Use urlencode() for params",
        ],
        solution="""
from urllib.parse import urlencode

def build_api_url(base_url, endpoint, params):
    encoded = urlencode(params)
    return f"{base_url}/{endpoint}?{encoded}"
""",
        function_name="build_api_url",
        test_cases=[
            (("https://api.github.com", "users", {"per_page": "10"}), "https://api.github.com/users?per_page=10"),
            (("https://api.example.com", "search", {"q": "python"}), "https://api.example.com/search?q=python"),
            (("https://api.test.org", "data", {"id": "123", "format": "json"}), "https://api.test.org/data?id=123&format=json"),
        ],
        concepts=["URL construction", "API endpoints", "urlencode"],
    ),
    make_exercise(
        id="api_13",
        title="Bearer Token Authorization",
        topic="api_calling",
        difficulty=2,
        description="OAuth2 APIs use Bearer tokens for authorization. Build an Authorization header with a Bearer token.",
        hints=[
            "Bearer auth format: 'Bearer ' + token",
            "Token is usually a JWT or API key",
        ],
        solution="""
def build_bearer_auth(token):
    return f"Bearer {token}"
""",
        function_name="build_bearer_auth",
        test_cases=[
            (("abc123def456",), "Bearer abc123def456"),
            (("eyJhbGc...",), "Bearer eyJhbGc..."),
            (("sk_test_123",), "Bearer sk_test_123"),
        ],
        concepts=["Bearer Token", "OAuth2", "Authorization headers"],
    ),
    make_exercise(
        id="api_14",
        title="Extract Status and Message from Error Response",
        topic="api_calling",
        difficulty=2,
        description="When an API call fails, extract error details. Parse an error response to get the status code and error message.",
        hints=[
            "Error responses typically have 'status' or 'error' keys",
            "Messages might be in 'message' or 'detail' fields",
        ],
        solution="""
def extract_error(response):
    return (response.get('status'), response.get('message'))
""",
        function_name="extract_error",
        test_cases=[
            ({"status": 400, "message": "Invalid request"}, (400, "Invalid request")),
            ({"status": 401, "message": "Unauthorized"}, (401, "Unauthorized")),
            ({"status": 404, "message": "Not found"}, (404, "Not found")),
        ],
        concepts=["Error handling", "Response parsing", "Debugging"],
    ),
    make_exercise(
        id="api_15",
        title="Build Request Headers Dictionary",
        topic="api_calling",
        difficulty=2,
        description="Combine multiple headers (Content-Type, Authorization, Accept) into a single headers dictionary.",
        hints=[
            "Headers is a dict: {key: value, ...}",
            "Common headers: Content-Type, Authorization, Accept, User-Agent",
        ],
        solution="""
def build_request_headers(auth_token, content_type="application/json"):
    return {
        "Content-Type": content_type,
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/json",
    }
""",
        function_name="build_request_headers",
        test_cases=[
            (("token123",), {"Content-Type": "application/json", "Authorization": "Bearer token123", "Accept": "application/json"}),
            (("abc", "text/plain"), {"Content-Type": "text/plain", "Authorization": "Bearer abc", "Accept": "application/json"}),
        ],
        concepts=["HTTP headers", "Authorization", "Content negotiation"],
    ),
    make_exercise(
        id="api_16",
        title="Parse Pagination Metadata",
        topic="api_calling",
        difficulty=2,
        description="APIs use pagination to limit response size. Extract pagination info (current page, total pages, next URL) from a response.",
        hints=[
            "Look for 'pagination' or 'meta' key in response",
            "Check for 'page', 'per_page', 'total', 'next_url' keys",
        ],
        solution="""
def get_pagination_info(response):
    meta = response.get('pagination', {})
    return (meta.get('page'), meta.get('per_page'), meta.get('total'), meta.get('next_url'))
""",
        function_name="get_pagination_info",
        test_cases=[
            ({"pagination": {"page": 1, "per_page": 10, "total": 100, "next_url": "?page=2"}}, (1, 10, 100, "?page=2")),
            ({"pagination": {"page": 2, "per_page": 20, "total": 50, "next_url": None}}, (2, 20, 50, None)),
        ],
        concepts=["Pagination", "Metadata extraction", "API design"],
    ),
    make_exercise(
        id="api_17",
        title="Build JSON Request Body",
        topic="api_calling",
        difficulty=2,
        description="When sending data to an API via POST/PUT, create a JSON request body. Convert a Python dict to JSON string.",
        hints=[
            "Use json.dumps() to serialize the dict",
            "Include required fields for the API endpoint",
        ],
        solution="""
import json

def build_request_body(user_data):
    return json.dumps({
        "name": user_data['name'],
        "email": user_data['email'],
        "age": user_data['age'],
    })
""",
        function_name="build_request_body",
        test_cases=[
            ({"name": "Alice", "email": "alice@example.com", "age": 30}, '{"name": "Alice", "email": "alice@example.com", "age": 30}'),
            ({"name": "Bob", "email": "bob@test.org", "age": 25}, '{"name": "Bob", "email": "bob@test.org", "age": 25}'),
        ],
        concepts=["JSON serialization", "Request bodies", "Data formatting"],
    ),
    make_exercise(
        id="api_18",
        title="Filter Data from API Response",
        topic="api_calling",
        difficulty=2,
        description="Extract and filter specific items from an API response. Get all users with age > 25.",
        hints=[
            "Use list comprehension: [item for item in list if condition]",
            "Filter based on a field value",
        ],
        solution="""
def filter_users_by_age(response, min_age):
    return [user for user in response['users'] if user['age'] > min_age]
""",
        function_name="filter_users_by_age",
        test_cases=[
            (({"users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 20}]}, 25), [{"name": "Alice", "age": 30}]),
            (({"users": [{"name": "Charlie", "age": 26}, {"name": "Diana", "age": 28}, {"name": "Eve", "age": 22}]}, 25), [{"name": "Charlie", "age": 26}, {"name": "Diana", "age": 28}]),
        ],
        concepts=["List filtering", "Conditional logic", "Data transformation"],
    ),
    make_exercise(
        id="api_19",
        title="Build Query String Manually",
        topic="api_calling",
        difficulty=2,
        description="Build a query string from parameters without urlencode(). Manually join key=value pairs with &.",
        hints=[
            "Start with empty string",
            "Join pairs with '&'",
            "Format: key1=value1&key2=value2",
        ],
        solution="""
def build_query_string(params):
    pairs = [f"{k}={v}" for k, v in params.items()]
    return "&".join(pairs)
""",
        function_name="build_query_string",
        test_cases=[
            ({"id": "1"}, "id=1"),
            ({"name": "test", "page": "2"}, "name=test&page=2"),
        ],
        concepts=["Query strings", "String joining", "Manual URL building"],
    ),
    make_exercise(
        id="api_20",
        title="Combine User Agent Header",
        topic="api_calling",
        difficulty=2,
        description="User-Agent headers identify the client. Build a User-Agent string for your API client.",
        hints=[
            "Format: 'AppName/Version (Language; Platform)'",
            "Example: 'MyApp/1.0 (Python; Linux)'",
        ],
        solution="""
def build_user_agent(app_name, version, language="Python", platform="Linux"):
    return f"{app_name}/{version} ({language}; {platform})"
""",
        function_name="build_user_agent",
        test_cases=[
            (("MyApp", "1.0"), "MyApp/1.0 (Python; Linux)"),
            (("APIClient", "2.5", "Python", "Windows"), "APIClient/2.5 (Python; Windows)"),
        ],
        concepts=["User-Agent", "HTTP headers", "Client identification"],
    ),
    # MEDIUM (21-35): Pagination, response handling, validation
    make_exercise(
        id="api_21",
        title="Implement Pagination Loop",
        topic="api_calling",
        difficulty=3,
        description="Collect all items across multiple pages. Given responses with next_page_url, simulate fetching all pages and collecting all items.",
        hints=[
            "Start with first page response",
            "Check for next_page_url in pagination metadata",
            "Collect items from each page until no next_page_url",
        ],
        solution="""
def collect_all_pages(responses):
    all_items = []
    for response in responses:
        all_items.extend(response.get('items', []))
    return all_items
""",
        function_name="collect_all_pages",
        test_cases=[
            ([{"items": [1, 2], "next_url": "page2"}, {"items": [3, 4], "next_url": None}], [1, 2, 3, 4]),
            ([{"items": ["a", "b", "c"]}], ["a", "b", "c"]),
        ],
        concepts=["Pagination", "Loops", "Data aggregation"],
    ),
    make_exercise(
        id="api_22",
        title="Transform API Response to Internal Format",
        topic="api_calling",
        difficulty=3,
        description="APIs return data in their format. Transform it to match your application's internal format.",
        hints=[
            "Map API field names to your field names",
            "Extract only needed fields",
            "Use list comprehension for lists",
        ],
        solution="""
def transform_users(api_response):
    return [
        {"id": u['user_id'], "full_name": u['name'], "contact": u['email']}
        for u in api_response['users']
    ]
""",
        function_name="transform_users",
        test_cases=[
            ({"users": [{"user_id": 1, "name": "Alice", "email": "alice@ex.com"}]}, [{"id": 1, "full_name": "Alice", "contact": "alice@ex.com"}]),
            ({"users": [{"user_id": 2, "name": "Bob", "email": "bob@ex.com"}, {"user_id": 3, "name": "Charlie", "email": "charlie@ex.com"}]}, [{"id": 2, "full_name": "Bob", "contact": "bob@ex.com"}, {"id": 3, "full_name": "Charlie", "contact": "charlie@ex.com"}]),
        ],
        concepts=["Data transformation", "Schema mapping", "List comprehension"],
    ),
    make_exercise(
        id="api_23",
        title="Validate Required Fields in Response",
        topic="api_calling",
        difficulty=3,
        description="Ensure API response has required fields. Check if 'status' and 'data' keys exist; return True if valid, False otherwise.",
        hints=[
            "Check if keys exist in dict using 'in' operator",
            "All required fields must be present",
        ],
        solution="""
def validate_response(response, required_fields):
    return all(field in response for field in required_fields)
""",
        function_name="validate_response",
        test_cases=[
            (({"status": "ok", "data": [1, 2]}, ["status", "data"]), True),
            (({"status": "ok"}, ["status", "data"]), False),
            (({"status": "error", "message": "fail", "timestamp": 123}, ["status", "message", "timestamp"]), True),
        ],
        concepts=["Validation", "Error checking", "Data integrity"],
    ),
    make_exercise(
        id="api_24",
        title="Build Webhook Signature (HMAC-SHA256)",
        topic="api_calling",
        difficulty=3,
        description="APIs send webhooks to your server. Validate webhook payload authenticity using HMAC-SHA256 signature.",
        hints=[
            "Use hmac.new(key, msg, hashlib.sha256)",
            "Key is usually the API secret",
            "Message is the webhook payload (as bytes)",
        ],
        solution="""
import hmac
import hashlib

def compute_webhook_signature(secret, payload):
    return hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
""",
        function_name="compute_webhook_signature",
        test_cases=[
            (("secret123", "payload"), "6db7b2948f10a9a0edeebcfa6cfd43b0ebac5fadd6c131fb2b7842ee2c30f15f"),
        ],
        concepts=["Webhooks", "HMAC", "Security"],
    ),
    make_exercise(
        id="api_25",
        title="Extract Errors from Validation Response",
        topic="api_calling",
        difficulty=3,
        description="When data validation fails, APIs return detailed error messages. Extract all field errors from response.",
        hints=[
            "Errors might be in 'errors' dict or 'validation_errors' list",
            "Each error has field name and error message",
        ],
        solution="""
def extract_field_errors(response):
    return response.get('errors', {})
""",
        function_name="extract_field_errors",
        test_cases=[
            ({"errors": {"email": "Invalid format", "name": "Required"}}, {"email": "Invalid format", "name": "Required"}),
            ({"errors": {}}, {}),
        ],
        concepts=["Error handling", "Validation", "User feedback"],
    ),
    make_exercise(
        id="api_26",
        title="Build Batch Request Payload",
        topic="api_calling",
        difficulty=3,
        description="Some APIs accept batch requests. Build a payload with multiple operations.",
        hints=[
            "Batch payload is usually a list of operation dicts",
            "Each operation has type, data, etc.",
        ],
        solution="""
def build_batch_request(operations):
    return {
        "requests": [
            {"method": op['method'], "endpoint": op['endpoint'], "data": op.get('data')}
            for op in operations
        ]
    }
""",
        function_name="build_batch_request",
        test_cases=[
            ([{"method": "POST", "endpoint": "/users", "data": {"name": "Alice"}}], {"requests": [{"method": "POST", "endpoint": "/users", "data": {"name": "Alice"}}]}),
        ],
        concepts=["Batch requests", "API design", "Optimization"],
    ),
    make_exercise(
        id="api_27",
        title="Exponential Backoff Delay Calculation",
        topic="api_calling",
        difficulty=3,
        description="When rate limited, retry with increasing delays. Calculate exponential backoff: delay = base * (multiplier ^ attempt).",
        hints=[
            "Formula: base * (multiplier ** attempt)",
            "Common: base=1, multiplier=2 (1, 2, 4, 8, 16...)",
        ],
        solution="""
def calculate_backoff(attempt, base=1, multiplier=2):
    return base * (multiplier ** attempt)
""",
        function_name="calculate_backoff",
        test_cases=[
            ((0, 1, 2), 1),
            ((1, 1, 2), 2),
            ((3, 1, 2), 8),
            ((2, 2, 3), 18),
        ],
        concepts=["Rate limiting", "Retry logic", "Exponential backoff"],
    ),
    make_exercise(
        id="api_28",
        title="Build API Cache Key",
        topic="api_calling",
        difficulty=3,
        description="Implement response caching by building unique cache keys from request parameters.",
        hints=[
            "Cache key should include base URL and all params",
            "Use stable string representation (sorted dicts)",
        ],
        solution="""
def build_cache_key(endpoint, params):
    sorted_params = sorted(params.items())
    param_str = "&".join(f"{k}={v}" for k, v in sorted_params)
    return f"{endpoint}?{param_str}"
""",
        function_name="build_cache_key",
        test_cases=[
            (("https://api.example.com/users", {"id": "1"}), "https://api.example.com/users?id=1"),
            (("https://api.example.com/search", {"q": "test", "page": "1"}), "https://api.example.com/search?page=1&q=test"),
        ],
        concepts=["Caching", "Performance", "Data consistency"],
    ),
    make_exercise(
        id="api_29",
        title="Parse Timestamp from API Response",
        topic="api_calling",
        difficulty=3,
        description="APIs return timestamps in ISO 8601 format. Extract and validate timestamp from response.",
        hints=[
            "ISO format: '2024-04-08T12:30:45Z'",
            "Could be string or Unix timestamp",
            "Validate presence before using",
        ],
        solution="""
def get_response_timestamp(response):
    return response.get('timestamp') or response.get('created_at')
""",
        function_name="get_response_timestamp",
        test_cases=[
            ({"timestamp": "2024-04-08T12:30:45Z"}, "2024-04-08T12:30:45Z"),
            ({"created_at": "2024-04-08T10:00:00Z"}, "2024-04-08T10:00:00Z"),
        ],
        concepts=["Timestamp handling", "Data parsing", "Time zones"],
    ),
    make_exercise(
        id="api_30",
        title="Count Items with Specific Status",
        topic="api_calling",
        difficulty=3,
        description="Count items matching a status from paginated API responses.",
        hints=[
            "Iterate through items in response",
            "Check status field",
            "Count matches",
        ],
        solution="""
def count_status(response, status):
    return sum(1 for item in response['items'] if item['status'] == status)
""",
        function_name="count_status",
        test_cases=[
            (({"items": [{"status": "active"}, {"status": "active"}, {"status": "inactive"}]}, "active"), 2),
            (({"items": [{"status": "pending"}, {"status": "completed"}]}, "pending"), 1),
        ],
        concepts=["Filtering", "Aggregation", "Data analysis"],
    ),
    make_exercise(
        id="api_31",
        title="Build Conditional Request Headers",
        topic="api_calling",
        difficulty=3,
        description="Build headers conditionally: include auth only if token provided, include custom headers based on conditions.",
        hints=[
            "Start with base headers",
            "Add optional headers conditionally",
            "Use dict.update() or dict unpacking",
        ],
        solution="""
def build_conditional_headers(has_auth=False, token=None, is_json=True):
    headers = {}
    if is_json:
        headers['Content-Type'] = 'application/json'
    if has_auth and token:
        headers['Authorization'] = f'Bearer {token}'
    return headers
""",
        function_name="build_conditional_headers",
        test_cases=[
            ((False, None, True), {"Content-Type": "application/json"}),
            ((True, "abc123", True), {"Content-Type": "application/json", "Authorization": "Bearer abc123"}),
            ((True, None, False), {}),
        ],
        concepts=["Conditional logic", "Headers", "API flexibility"],
    ),
    make_exercise(
        id="api_32",
        title="Extract Links from Response (HATEOAS)",
        topic="api_calling",
        difficulty=3,
        description="HATEOAS APIs include links to related resources. Extract all links from response.",
        hints=[
            "Links are typically in '_links' or 'links' object",
            "Each link has 'rel' and 'href' properties",
        ],
        solution="""
def extract_links(response):
    links = response.get('_links', {})
    return {rel: link['href'] for rel, link in links.items()}
""",
        function_name="extract_links",
        test_cases=[
            ({"_links": {"self": {"href": "/users/1"}, "next": {"href": "/users/2"}}}, {"self": "/users/1", "next": "/users/2"}),
        ],
        concepts=["HATEOAS", "Resource linking", "API discovery"],
    ),
    make_exercise(
        id="api_33",
        title="Aggregate Data from Multiple API Calls",
        topic="api_calling",
        difficulty=3,
        description="Combine results from multiple API responses. Sum values across responses.",
        hints=[
            "Each response contains items with values",
            "Sum all values from all responses",
        ],
        solution="""
def aggregate_totals(responses):
    return sum(item['value'] for response in responses for item in response['items'])
""",
        function_name="aggregate_totals",
        test_cases=[
            ([{"items": [{"value": 10}, {"value": 20}]}, {"items": [{"value": 5}]}], 35),
        ],
        concepts=["Data aggregation", "Multiple sources", "Calculation"],
    ),
    make_exercise(
        id="api_34",
        title="Detect Rate Limit Headers",
        topic="api_calling",
        difficulty=3,
        description="APIs send rate limit info in response headers. Extract limit, remaining, and reset time.",
        hints=[
            "Common headers: X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset",
            "Access headers dict to get values",
        ],
        solution="""
def get_rate_limit_info(headers):
    return {
        "limit": int(headers.get("X-RateLimit-Limit", 0)),
        "remaining": int(headers.get("X-RateLimit-Remaining", 0)),
        "reset": int(headers.get("X-RateLimit-Reset", 0)),
    }
""",
        function_name="get_rate_limit_info",
        test_cases=[
            ({"X-RateLimit-Limit": "60", "X-RateLimit-Remaining": "30", "X-RateLimit-Reset": "1234567890"}, {"limit": 60, "remaining": 30, "reset": 1234567890}),
        ],
        concepts=["Rate limiting", "HTTP headers", "API quotas"],
    ),
    make_exercise(
        id="api_35",
        title="Build OAuth Authorization URL",
        topic="api_calling",
        difficulty=3,
        description="OAuth requires redirecting user to authorization URL. Build the full authorization URL with params.",
        hints=[
            "Include: client_id, redirect_uri, scope, response_type='code'",
            "Use urlencode for params",
        ],
        solution="""
from urllib.parse import urlencode

def build_oauth_url(base_url, client_id, redirect_uri, scope):
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "response_type": "code",
    }
    return f"{base_url}?{urlencode(params)}"
""",
        function_name="build_oauth_url",
        test_cases=[
            (("https://auth.example.com/authorize", "abc123", "https://myapp.com/callback", "read write"), "https://auth.example.com/authorize?client_id=abc123&redirect_uri=https%3A%2F%2Fmyapp.com%2Fcallback&scope=read+write&response_type=code"),
        ],
        concepts=["OAuth2", "Authorization", "URL parameters"],
    ),
    # HARD (36-45): Complex scenarios, retry logic, real-world patterns
    make_exercise(
        id="api_36",
        title="Implement Retry Logic with Exponential Backoff",
        topic="api_calling",
        difficulty=4,
        description="Simulate retry logic with exponential backoff. Given a list of (status_code, attempt_number), determine if retry is needed and calculate next wait time.",
        hints=[
            "Retry on 429 (rate limit), 5xx errors",
            "Calculate wait using exponential backoff",
            "Max retries typically 3-5",
        ],
        solution="""
def should_retry(status_code, attempt, max_attempts=3):
    if status_code in [429, 500, 502, 503, 504]:
        return attempt < max_attempts
    return False

def get_wait_time(attempt, base=1, multiplier=2):
    return base * (multiplier ** attempt)
""",
        function_name="should_retry",
        test_cases=[
            ((429, 0, 3), True),
            ((429, 3, 3), False),
            ((200, 0, 3), False),
            ((503, 1, 3), True),
        ],
        concepts=["Retry logic", "Rate limiting", "Error recovery"],
    ),
    make_exercise(
        id="api_37",
        title="Parse Complex Nested JSON",
        topic="api_calling",
        difficulty=4,
        description="Extract deeply nested data: user.profile.contact.email from complex API response.",
        hints=[
            "Use .get() for safe navigation",
            "Chain multiple .get() calls",
            "Provide defaults for missing keys",
        ],
        solution="""
def get_user_email(response):
    user = response.get('user')
    if not isinstance(user, dict):
        return None
    profile = user.get('profile', {})
    contact = profile.get('contact', {})
    return contact.get('email')
""",
        function_name="get_user_email",
        test_cases=[
            ({"user": {"profile": {"contact": {"email": "alice@example.com"}}}}, "alice@example.com"),
            ({"user": {"profile": {}}}, None),
            ({"user": None}, None),
        ],
        concepts=["Nested data", "Safe navigation", "Error prevention"],
    ),
    make_exercise(
        id="api_38",
        title="Validate and Normalize Phone Number from API",
        topic="api_calling",
        difficulty=4,
        description="APIs return phone numbers in various formats. Validate and normalize to standard format.",
        hints=[
            "Remove non-digit characters",
            "Check length (usually 10+ digits)",
            "Return normalized format",
        ],
        solution="""
def normalize_phone(phone):
    if not phone:
        return None
    digits = ''.join(c for c in phone if c.isdigit())
    if len(digits) >= 10:
        return digits
    return None
""",
        function_name="normalize_phone",
        test_cases=[
            ("+1 (555) 123-4567", "15551234567"),
            ("555.123.4567", "5551234567"),
            ("123", None),
        ],
        concepts=["Data validation", "Normalization", "String processing"],
    ),
    make_exercise(
        id="api_39",
        title="Build Cursor-Based Pagination Request",
        topic="api_calling",
        difficulty=4,
        description="Cursor-based pagination uses opaque cursors instead of page numbers. Build request with cursor.",
        hints=[
            "Use 'cursor' parameter instead of 'page'",
            "Next cursor comes from previous response",
            "First request has no cursor or cursor=null",
        ],
        solution="""
from urllib.parse import urlencode

def build_cursor_request(base_url, cursor=None):
    params = {"limit": 10}
    if cursor:
        params["cursor"] = cursor
    return f"{base_url}?{urlencode(params)}"
""",
        function_name="build_cursor_request",
        test_cases=[
            (("https://api.example.com/items",), "https://api.example.com/items?limit=10"),
            (("https://api.example.com/items", "abc123"), "https://api.example.com/items?limit=10&cursor=abc123"),
        ],
        concepts=["Cursor pagination", "API design", "Stateless iteration"],
    ),
    make_exercise(
        id="api_40",
        title="Handle API Response Errors with Fallback",
        topic="api_calling",
        difficulty=4,
        description="When API fails, use cached or default data. Return API data if valid, else fallback.",
        hints=[
            "Check if response has errors",
            "Use cached data if API response is invalid",
            "Provide sensible defaults",
        ],
        solution="""
def get_data_with_fallback(api_response, cached_data, default_data=None):
    if api_response.get('status') == 'success' and api_response.get('data'):
        return api_response['data']
    elif cached_data:
        return cached_data
    return default_data or {}
""",
        function_name="get_data_with_fallback",
        test_cases=[
            (({"status": "success", "data": {"id": 1}}, [1, 2], []), {"id": 1}),
            (({"status": "error"}, [1, 2], []), [1, 2]),
            (({"error": "failed"}, None, {"default": True}), {"default": True}),
        ],
        concepts=["Error handling", "Caching", "Resilience"],
    ),
    make_exercise(
        id="api_41",
        title="Transform Flat Response to Nested Structure",
        topic="api_calling",
        difficulty=4,
        description="API returns flat data. Transform to nested structure (e.g., group by category).",
        hints=[
            "Use dict comprehension or defaultdict",
            "Group items by a field",
            "Create nested structure",
        ],
        solution="""
def group_by_category(items):
    result = {}
    for item in items:
        cat = item['category']
        if cat not in result:
            result[cat] = []
        result[cat].append(item)
    return result
""",
        function_name="group_by_category",
        test_cases=[
            ([{"category": "A", "name": "Item1"}, {"category": "B", "name": "Item2"}, {"category": "A", "name": "Item3"}], {"A": [{"category": "A", "name": "Item1"}, {"category": "A", "name": "Item3"}], "B": [{"category": "B", "name": "Item2"}]}),
        ],
        concepts=["Data restructuring", "Grouping", "Transformation"],
    ),
    make_exercise(
        id="api_42",
        title="Calculate Request Signature (AWS Signature V4)",
        topic="api_calling",
        difficulty=4,
        description="AWS APIs require signature. Understand signature building process (simplified).",
        hints=[
            "Create canonical request from HTTP method, path, query, headers, body",
            "Sign with secret key using HMAC-SHA256",
            "Include timestamp in header",
        ],
        solution="""
def build_aws_signature_parts(method, path, params):
    # Simplified: just verify structure
    return {
        "method": method,
        "path": path,
        "params": sorted(params.items()),
    }
""",
        function_name="build_aws_signature_parts",
        test_cases=[
            (("GET", "/api/users", {"id": "1"}), {"method": "GET", "path": "/api/users", "params": [("id", "1")]}),
        ],
        concepts=["AWS", "Signature", "Security"],
    ),
    make_exercise(
        id="api_43",
        title="Handle Webhook Retry Validation",
        topic="api_calling",
        difficulty=4,
        description="Webhook request includes attempt number and max attempts. Validate that retry attempt is valid.",
        hints=[
            "Check X-Webhook-Attempt header",
            "Check X-Webhook-Retry-Count header",
            "Validate attempt <= max_attempts",
        ],
        solution="""
def validate_webhook_attempt(headers):
    attempt = int(headers.get('X-Webhook-Attempt', 1))
    max_attempts = int(headers.get('X-Webhook-Retry-Count', 3))
    return attempt <= max_attempts
""",
        function_name="validate_webhook_attempt",
        test_cases=[
            ({"X-Webhook-Attempt": "1", "X-Webhook-Retry-Count": "3"}, True),
            ({"X-Webhook-Attempt": "4", "X-Webhook-Retry-Count": "3"}, False),
        ],
        concepts=["Webhooks", "Retry handling", "Validation"],
    ),
    make_exercise(
        id="api_44",
        title="Build Search Query with Filters",
        topic="api_calling",
        difficulty=4,
        description="Build complex search query: keyword + multiple filters (date range, status, etc.).",
        hints=[
            "Include search term",
            "Add filter parameters",
            "Handle optional filters",
        ],
        solution="""
from urllib.parse import urlencode

def build_search_query(base_url, keyword, filters):
    params = {"q": keyword}
    params.update(filters)
    return f"{base_url}?{urlencode(params)}"
""",
        function_name="build_search_query",
        test_cases=[
            (("https://api.example.com/search", "python", {"status": "active"}), "https://api.example.com/search?q=python&status=active"),
            (("https://api.example.com/search", "test", {"from": "2024-01-01", "to": "2024-12-31"}), "https://api.example.com/search?q=test&from=2024-01-01&to=2024-12-31"),
        ],
        concepts=["Search", "Filtering", "Complex queries"],
    ),
    make_exercise(
        id="api_45",
        title="Merge Paginated Results into Single Dataset",
        topic="api_calling",
        difficulty=4,
        description="Collect results from multiple pages and merge into single deduplicated dataset.",
        hints=[
            "Iterate through all responses",
            "Collect items from each",
            "Deduplicate by id",
        ],
        solution="""
def merge_paginated_results(responses):
    items_dict = {}
    for response in responses:
        for item in response.get('items', []):
            items_dict[item['id']] = item
    return list(items_dict.values())
""",
        function_name="merge_paginated_results",
        test_cases=[
            ([{"items": [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]}, {"items": [{"id": 2, "name": "B"}, {"id": 3, "name": "C"}]}], [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}, {"id": 3, "name": "C"}]),
        ],
        concepts=["Pagination", "Deduplication", "Data merging"],
    ),
    # CHALLENGE (46-50): Advanced scenarios
    make_exercise(
        id="api_46",
        title="Implement Sliding Window Rate Limiter",
        topic="api_calling",
        difficulty=5,
        description="Implement sliding window rate limiter: track requests in time window, reject if exceeds limit.",
        hints=[
            "Keep list of request timestamps",
            "Remove timestamps outside window",
            "Check count against limit",
        ],
        solution="""
def sliding_window_ratelimit(requests, limit, window_seconds):
    # requests is list of timestamps
    # Remove old timestamps - keep only those within the window
    if not requests:
        return True
    cutoff = requests[-1] - window_seconds
    recent = [r for r in requests if r > cutoff]
    # Return True if count exceeds limit
    return len(recent) > limit
""",
        function_name="sliding_window_ratelimit",
        test_cases=[
            (([1, 2, 3, 4, 5], 3, 10), True),
            (([1, 2, 3, 4, 5, 6, 7], 5, 3), False),
        ],
        concepts=["Rate limiting", "Sliding window", "Algorithms"],
    ),
    make_exercise(
        id="api_47",
        title="Build GraphQL Query",
        topic="api_calling",
        difficulty=5,
        description="GraphQL APIs use queries instead of URLs. Build a GraphQL query string.",
        hints=[
            "GraphQL syntax: query { field { subfield } }",
            "Variables can be passed separately",
        ],
        solution="""
def build_graphql_query(fields, filters):
    filter_str = ", ".join(f"{k}: {v}" for k, v in filters.items())
    field_str = " ".join(fields)
    return f"query {{ users({filter_str}) {{ {field_str} }} }}"
""",
        function_name="build_graphql_query",
        test_cases=[
            ((["id", "name"], {"limit": "10"}), 'query { users(limit: 10) { id name } }'),
        ],
        concepts=["GraphQL", "Query language", "API design"],
    ),
    make_exercise(
        id="api_48",
        title="Implement Request Deduplication",
        topic="api_calling",
        difficulty=5,
        description="Prevent duplicate requests by tracking request IDs. Return true if request is duplicate, false if new.",
        hints=[
            "Keep set of seen request IDs",
            "Generate ID from method, path, params",
            "Check if ID already exists",
        ],
        solution="""
def is_duplicate_request(request_id, seen_requests):
    if request_id in seen_requests:
        return True
    seen_requests.add(request_id)
    return False
""",
        function_name="is_duplicate_request",
        test_cases=[
            (("req_1", {"req_1"}), True),
            (("req_2", {"req_1"}), False),
        ],
        concepts=["Idempotency", "Request deduplication", "State management"],
    ),
    make_exercise(
        id="api_49",
        title="Process Streaming API Response",
        topic="api_calling",
        difficulty=5,
        description="Streaming APIs send data in chunks. Process each chunk and accumulate results.",
        hints=[
            "Each chunk is a JSON line or partial response",
            "Accumulate into final result",
            "Handle incomplete chunks",
        ],
        solution="""
import json

def process_stream(*chunks):
    result = []
    for chunk in chunks:
        data = json.loads(chunk)
        result.append(data)
    return result
""",
        function_name="process_stream",
        test_cases=[
            (('{"id": 1}', '{"id": 2}', '{"id": 3}'), [{"id": 1}, {"id": 2}, {"id": 3}]),
        ],
        concepts=["Streaming", "Chunked responses", "Real-time data"],
    ),
    make_exercise(
        id="api_50",
        title="Build Complete API Client Pattern",
        topic="api_calling",
        difficulty=5,
        description="Combine all skills: build a function that makes a simulated API request with all proper components.",
        hints=[
            "Include URL building, headers, body, validation, error handling",
            "Simulate response with mock data",
            "Return structured result",
        ],
        solution="""
import json

def simulated_api_request(method, endpoint, data, token):
    # Build request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    body = json.dumps(data) if data else None

    # Simulate response
    mock_response = {
        "status": 200,
        "data": {"success": True, "id": 123},
        "headers": headers,
    }
    return mock_response
""",
        function_name="simulated_api_request",
        test_cases=[
            (("POST", "/users", {"name": "Alice"}, "token123"), {"status": 200, "data": {"success": True, "id": 123}, "headers": {"Content-Type": "application/json", "Authorization": "Bearer token123"}}),
        ],
        concepts=["Complete API pattern", "Integration", "Full workflow"],
    ),
]
