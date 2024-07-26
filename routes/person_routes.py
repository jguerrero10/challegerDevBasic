from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from database.crud import (
    add_object,
    delete_object,
    get_all_objects,
    get_object,
    update_object,
)
from schemas.person_schemas import Person, PersonCreate, PersonUpdate

person_router = APIRouter()


@person_router.get("/", response_model=List[Person])
async def get_persons() -> List[Any]:
    return await get_all_objects("persons")


@person_router.get("/{person_id}", response_model=Person)
async def get_person(person_id: str) -> Any:
    return await get_object("persons", person_id)


@person_router.post("/", response_model=Person)
async def create_person(person: PersonCreate) -> Any:
    return await add_object("persons", dict(person))


@person_router.patch("/{person_id}", response_model=Person)
async def update_person(person_id: str, person: PersonUpdate) -> Any:
    return await update_object("persons", person_id, dict(person))


@person_router.delete("/{person_id}", response_model=Person)
async def delete_person(person_id: str) -> Dict[str, str]:
    person_deleted = await delete_object("persons", person_id)
    if person_deleted == 1:
        return {"message": "Person deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error deleting person")
