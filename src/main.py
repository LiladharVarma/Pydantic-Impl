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

