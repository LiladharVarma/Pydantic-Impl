age = 26

valid_age = 2026 -age 

# -------------------------------------------

from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    age: int

# Valid data - works fine
user = User(id=1, email="dave@example.com", age=25)

# Invalid data - fails immediately with clear error
user = User(id=1, email=None, age="unknown")


# ---------------------------------
# Type Hints

name: str = "Dave"
# name : int = "Dave"  #This also works as the type hints are not enforced by python as it is in java or any other statically typed language
age: int = 30
price: float = 19.99
is_active: bool = True


def create_user(name, email, age):
    # What types are these supposed to be?
    pass


def create_user(name: str, email: str, age: int) -> dict:
    # Crystal clear
    pass

# this shows that the fucntion returns the dict 
# same fcuntion can be written in java like 
# private static Map<String , String> createUser(String name , String email , int age ){...}

# Container types 

tages : list[str] = ["python" , "java" , "javascript"] 

# List of integers
quantities: list[int] = [1, 5, 3, 2]

# Dictionary with string keys and integer values
word_counts: dict[str, int] = {"error": 12, "warning": 5}

# Dictionary with string keys and string values
settings: dict[str, str] = {"theme": "dark", "language": "en" }
# settings: dict[str, str] = {"theme": "dark", "language": "en" , "number" : 12}


# Optional values
# Use Optional values when a value might be None:

from typing import Optional

# These mean the same thing
middle_name: Optional[str] = None
middle_name: str | None = None



# Literal types

# we use literals when value must be one specific type options 
# This is similar to enums in JAVA. 

from typing import Literal 

status : Literal["draft" , "published" , "archived" , "inactive"] = "draft"

# Only these three values are valid
status = "draft"      # OK
status = "published"  # OK
status = "pending"    # Type checkers will warn about this but that will still work as typhints are only for documentation and is not enforced

# few more examples 
from typing import Literal

log_level: Literal["debug", "info", "warning", "error"] = "info"
priority: Literal["low", "medium", "high"] = "medium"
status: Literal["pending", "approved", "rejected"] = "pending"


# common patterns 
from typing import Optional, Literal

# Required string
name: str

# Optional string (can be None)
nickname: str | None = None

# String with default
country: str = "USA"

# List of items
items: list[str] = []

# Dictionary
metadata: dict[str, str] = {}

# Specific allowed values
role: Literal["admin", "user", "guest"] = "user"



# Type hints don't validate
# Remember: Python ignores type hints. This code runs without error:

age: int = "not a number"
prices: list[float] = "definitely not a list"
# Type hints are just hints. They don't enforce anything.

# This is where Pydantic comes in. Pydantic reads your type hints and actually validates data against them.