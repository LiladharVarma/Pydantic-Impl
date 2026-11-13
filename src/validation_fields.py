# This whole thing is simlar to validation in JAVA , we use annotations to validate fields in java similar to that in python this is how we validate 


from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0, le=120)
    email: str

user = User(name="Alice", age=30, email="alice@example.com")

# String Constraints

class UserProfile(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    bio: str = Field(max_length=500)
    website: str = Field(pattern=r"^https?://.*")

# Valid
profile = UserProfile(
    username="alice_dev",
    bio="Python developer",
    website="https://example.com"
)

# Invalid - username too short
profile = UserProfile(username="ab", bio="Hi", website="https://x.com")
# ValidationError: username must be at least 3 characters


# Numeric Constraints


class Product(BaseModel):
    name: str
    price: float = Field(gt=0)           # Greater than 0
    quantity: int = Field(ge=0)          # Greater than or equal to 0
    discount: float = Field(ge=0, le=1)  # Between 0 and 1

product = Product(
    name="Widget",
    price=29.99,
    quantity=100,
    discount=0.15
)



# Default values with Fields

class APIConfig(BaseModel):
    api_key: str
    model: str = Field(default="gpt-4")
    max_tokens: int = Field(default=1000, ge=1, le=4096)
    temperature: float = Field(default=0.7, ge=0, le=2)

# Only api_key required
config = APIConfig(api_key="sk-abc123")

print(config.model)        # gpt-4
print(config.max_tokens)   # 1000
print(config.temperature)  # 0.7

# Field Description 
#  we can also dd descripition to fields 
# Descriptions appear in generated JSON schemas and API documentation.


class Order(BaseModel):
    order_id: str = Field(description="Unique order identifier")
    total: float = Field(gt=0, description="Order total in USD")
    items: int = Field(ge=1, description="Number of items in order")


# Custom Validator 
# when we need custom validation on field we use these custom validations 

from pydantic import field_validator

class User(BaseModel):
    username: str
    
    @field_validator("username")
    def validate_username(cls, v):
        if " " in v:
            raise ValueError("Username cannot contain spaces")
        return v.lower()  # Normalize to lowercase

user = User(username="AliceSmith")
print(user.username)  # alicesmith


# Common patterns 

# Email Validation 
from pydantic import EmailStr

class User(BaseModel):
    email: EmailStr  # Built-in email validation

# URL validation 
from pydantic import HttpUrl

class Link(BaseModel):
    url: HttpUrl  # Must be valid HTTP/HTTPS URL

# List
from pydantic import Field

class Order(BaseModel):
    items: list[str] = Field(min_length=1)  # At least one item



# JSON schema generation 
# this we use to convert model to json 
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=1, description="User's full name")
    age: int = Field(ge=0, description="User's age in years")

print(User.model_json_schema())