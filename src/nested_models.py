# models inside models 
from pydantic import BaseModel

class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    order_id: str
    item: OrderItem  # Nested model

# Create with nested data
order = Order(
    order_id="ORD-001",
    item=OrderItem(
        product_id="P1",
        name="Widget",
        quantity=2,
        price=29.99
    )
)

print(order.item.name)  # Widget



# Creating from dictionaries


class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    order_id: str
    item: OrderItem

# Data from an API response
data = {
    "order_id": "ORD-001",
    "item": {
        "product_id": "P1",
        "name": "Widget",
        "quantity": 2,
        "price": 29.99
    }
}

# Pydantic validates everything, including nested data
order = Order.model_validate(data)

print(order.order_id)     # ORD-001
print(order.item.name)    # Widget




# List of models


class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    order_id: str
    customer_email: str
    items: list[OrderItem]  # List of models

# From API response
order_data = {
    "order_id": "ORD-001",
    "customer_email": "customer@example.com",
    "items": [
        {"product_id": "P1", "name": "Widget", "quantity": 2, "price": 29.99},
        {"product_id": "P2", "name": "Gadget", "quantity": 1, "price": 49.99}
    ]
}

order = Order(**order_data)

print(f"Order {order.order_id}")
for item in order.items:
    print(f"  - {item.name}: {item.quantity} x ${item.price}")




# Optional Nested models

class Discount(BaseModel):
    code: str
    percent: float

class Order(BaseModel):
    order_id: str
    total: float
    discount: Discount | None = None  # Optional nested model

# Works without discount
order = Order(order_id="ORD-001", total=99.99)
print(order.discount)  # None

# Works with discount
order = Order(
    order_id="ORD-002",
    total=99.99,
    discount={"code": "SAVE20", "percent": 20.0}
)
print(order.discount.code)  # SAVE20



# Deep nested model example 


class Address(BaseModel):
    street: str
    city: str
    country: str

class Customer(BaseModel):
    name: str
    email: str
    billing_address: Address
    shipping_address: Address | None = None

class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    order_id: str
    customer: Customer
    items: list[OrderItem]
    notes: str | None = None

# Complex nested data
data = {
    "order_id": "ORD-123",
    "customer": {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "billing_address": {
            "street": "123 Main St",
            "city": "Amsterdam",
            "country": "Netherlands"
        }
    },
    "items": [
        {"product_id": "SKU-001", "name": "Widget", "quantity": 3, "price": 19.99}
    ]
}

order = Order.model_validate(data)
print(order.customer.billing_address.city)  # Amsterdam


# Converting nested models 


class OrderItem(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    order_id: str
    item: OrderItem

order = Order(
    order_id="ORD-001",
    item=OrderItem(name="Widget", price=29.99)
)

# Converts everything to dict
data = order.model_dump()
print(data)
# {'order_id': 'ORD-001', 'item': {'name': 'Widget', 'price': 29.99}}


# Common patterns
# Reusing models across your codebase
class Money(BaseModel):
    amount: float
    currency: str = "USD"

class Product(BaseModel):
    name: str
    price: Money

class Invoice(BaseModel):
    items: list[Product]
    subtotal: Money
    tax: Money
    total: Money



# Self-referencing models (trees)

from __future__ import annotations


class Comment(BaseModel):
    text: str
    author: str
    replies: list[Comment] = []

comment = Comment(
    text="Great article!",
    author="Alice",
    replies=[
        Comment(text="Thanks!", author="Bob")
    ]
)