from typing import List
from fastapi import APIRouter
from pydantic import BaseModel


pet_router = APIRouter(prefix='/pets', tags=['pets'])


class Pet(BaseModel):
    id: int
    name: str
    age: int
    species: str


class PetStore(BaseModel):
    id: int
    name: str


pets: List[Pet] = [
    Pet(id=1, name='Fido', age=3, species='dog'),
    Pet(id=2, name='Whiskers', age=5, species='cat'),
]


@pet_router.get('/', response_model=List[Pet])
async def get_pets() -> List[Pet]:
    return pets
