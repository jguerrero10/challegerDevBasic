from pydantic import BaseModel, Field

from schemas.person_schemas import Person


class Vehicle(BaseModel):
    person: Person
    patent_plate: str = Field(..., title="Patent Plate Name", description="Patent Plate Name of the Vehicle")
    brand: str = Field(..., title="Brand Name", description="Brand Name of Vehicle")
    color: str = Field(..., title="Color Name", description="Color's vehicle")

    model_config = {
        "json_schema_extra": {
            "example": {
                "person": {
                    "name": "John Poe",
                    "email": "john.poe@email.com",
                },
                "patent_plate": "KXR243",
                "brand": "Sandero",
                "color": "Blue",
            }
        }
    }
