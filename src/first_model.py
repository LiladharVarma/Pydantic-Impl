from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int



# Data Classes vs Pydantic
# Dataclasses give you a clean syntax for data containers, but they don't validate anything. The type hints are just documentation.

# Pydantic models look similar but actually enforce the types:
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age="not a number")
print(user.age)  # "not a number" - no validation!




class User(BaseModel):
    name: str
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age="not a number")
# ValidationError: Input should be a valid integer



# creatiung instances
# Pydantic validates the data when you create the instance. Invalid data raises an error immediately.


class User(BaseModel):
    name: str
    email: str
    age: int

# Create a user
user = User(name="Alice", email="alice@example.com", age=30)

print(user.name)   # Alice
print(user.email)  # alice@example.com
print(user.age)    # 30


# Required vs optional fields

# Fields without defaults are required:


class User(BaseModel):
    name: str              # Required
    email: str             # Required
    age: int | None = None # Optional (has default)

# Works - age is optional
user = User(name="Alice", email="alice@example.com")
print(user.age)  # None

# Also works - providing age
user = User(name="Bob", email="bob@example.com", age=25)
print(user.age)  # 25

# default values 


class APIConfig(BaseModel):
    api_key: str
    model: str = "gpt-4"
    max_tokens: int = 1000
    temperature: float = 0.7

# Only api_key is required
config = APIConfig(api_key="sk-abc123")

print(config.model)       # gpt-4
print(config.max_tokens)  # 1000



# Converting to a dictionary

# use model_dump to convert a model to dictionary



class User(BaseModel):
    name: str 
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age=30)

# Convert to dict
user_dict = user.model_dump()
print(user_dict)
# {'name': 'Alice', 'email': 'alice@example.com', 'age': 30}

# Converting to JSON


class User(BaseModel):
    name: str
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age=30)

# Convert to JSON string
json_string = user.model_dump_json()
print(json_string)
# {"name":"Alice","email":"alice@example.com","age":30}


# Creating from a dictionary

class User(BaseModel):
    name: str
    email: str
    age: int

# Data from an API response
data = {"name": "Alice", "email": "alice@example.com", "age": 30}

# Option 1: Unpack the dict (simple, common)
user = User(**data)

# Option 2: Use model_validate (explicit, more options)
user = User.model_validate(data)


# Models as type hints
class User(BaseModel):
    name: str
    email: str

def greet_user(user: User) -> str:
    return f"Hello, {user.name}!"

def load_user(data: dict) -> User:
    return User.model_validate(data)

# IDE knows 'user' is a User, autocomplete works
user = load_user({"name": "Alice", "email": "alice@example.com"})
message = greet_user(user)
print(message)  # Hello, Alice!


# Real-world example
class WeatherResponse(BaseModel):
    city: str
    temperature: float
    humidity: int
    description: str

# Simulating API response
api_data = {
    "city": "Amsterdam",
    "temperature": 18.5,
    "humidity": 75,
    "description": "Partly cloudy"
}

# Validate and parse
weather = WeatherResponse.model_validate(api_data)

print(f"Weather in {weather.city}: {weather.temperature}°C")
print(f"Humidity: {weather.humidity}%")
print(f"Conditions: {weather.description}")


# Strict Mode

# By default, Pydantic coerces compatible types (like "25" to 25). If you want to disable this and require exact types, use strict mode:

from pydantic import  ConfigDict

class StrictUser(BaseModel):
    model_config = ConfigDict(strict=True)
    
    name: str
    age: int

# This will fail - no coercion allowed
user = StrictUser(name="Alice", age="25")
# ValidationError: Input should be a valid integer