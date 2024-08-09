#Interface Segregation Principle
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.personagem_service import PersonagemService
from app.models.personagem_model import PersonagemModel
from app.shared.dependencies import get_db
from app.repositories.presonagem_repository import PersonagemRepository
from typing import List
import uuid
from app.schemas.personagem_schema import PersonagemRequest, PersonagemResponse

router = APIRouter()

def get_personagem_service(db: Session = Depends(get_db)) -> PersonagemService:
    repository = PersonagemRepository(db)
    return PersonagemService(repository=repository)

@router.post("/api/v1/personagens", response_model=PersonagemResponse)
def create_personagem(personagemRequest: PersonagemRequest, service: PersonagemService = Depends(get_personagem_service)):
    return service.create_personagem(personagemRequest)

@router.get("/api/v1/personagens/{personagem_id}", response_model=PersonagemResponse)
def get_personagem(personagem_id: uuid.UUID, service: PersonagemService = Depends(get_personagem_service)):
    personagem = service.get(personagem_id)
    if not personagem:
        raise HTTPException(status_code=404, detail='Personagem com o id informado não foi encontrado')
    return personagem

# @router.get("/api/v1/personagens", response_model=List[PersonagemResponse])
# def list_personagens(service: PersonagemService = Depends(get_personagem_service)):
#     return service.list_personagens()

'''
@router.put("/personagens/{personagem_id}", response_model=PersonagemResponse)
def update_personagem(personagem_id: uuid.UUID, personagem: PersonagemUpdate, service: PersonagemService = Depends(get_personagem_service)):
    personagem_atualizado = service.update_personagem(personagem_id, personagem)
    if not personagem_atualizado:
        raise HTTPException(status_code=404, detail="Personagem not found")
    return personagem_atualizade

@router.delete("/personagens/{personagem_id}")
def delete_personagem(personagem_id: uuid.UUID, service: PersonagemService = Depends(get_personagem_service)):
    service.delete_personagem(personagem_id)
    return {"detail": "Personagem deleted"}

'''