#010 How do you add extra body parameters using Body()?

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items")
def create(
    item: Item,                                  # main request body (Pydantic model)
    importance: int = Body(..., ge=1, le=5)       # extra body parameter with validation
):
    """
    Body() is used to:
        ✔ Add additional fields to request body
        ✔ Apply validation (range, default, metadata)
        ✔ Control how FastAPI reads the data
    """

    return {
        "item": item,
        "importance": importance
    }


# Example Request JSON:
"""
{
    "item": {
        "name": "Laptop",
        "price": 1200
    },
    "importance": 3
}
"""


# Professional Comment:
# ✔ Body() is powerful for validation without creating separate models
# ✔ Use it for small extra fields (flags, priority, metadata)
# ✔ For complex structures, prefer separate Pydantic models for clarity
# ✔ Always validate ranges (ge, le) to prevent invalid data in production

#---------------------
