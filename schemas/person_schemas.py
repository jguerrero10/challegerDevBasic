from typing import Annotated, Optional

from pydantic import BaseModel, BeforeValidator, EmailStr, Field

PyObjectId = Annotated[str, BeforeValidator(str)]


class Person(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id", serialization_alias="id")
    name: str = Field(..., title="Name", description="Person's name")
    email: EmailStr = Field(..., title="Email", description="Person's email")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "23hsd6gas",
                "name": "John Poe",
                "email": "john.poe@email.com",
            }
        }
    }


class PersonCreate(BaseModel):
    name: str = Field(..., title="Name", description="Person's name")
    email: EmailStr = Field(..., title="Email", description="Person's email")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John Poe",
                "email": "john.poe@email.com",
            }
        }
    }


class PersonUpdate(BaseModel):
    name: Optional[str] = Field(..., title="Name", description="Person's name")
    email: Optional[EmailStr] = Field(..., title="Email", description="Person's email")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "John Poe",
                "email": "john.poe@email.com",
            }
        }
    }
