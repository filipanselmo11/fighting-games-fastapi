# Open/Closed Principle, Dependency Inversion Principle
from app.repositories.presonagem_repository import PersonagemRepository
from app.models.personagem_model import PersonagemModel
from typing import Optional, List
import uuid
from app.schemas.personagem_schema import PersonagemRequest, PersonagemResponse

class PersonagemService:
    def __init__(self, repository: PersonagemRepository):
        self.repository = repository

    def create_personagem(self, personagem_request: PersonagemRequest) -> PersonagemResponse:
        personagem = PersonagemModel(**personagem_request.model_dump())
        personagem = self.repository.add(personagem)
        return PersonagemResponse.model_validate(personagem)
    
    def get_personagem(self, personagem_id: uuid.UUID) -> Optional[PersonagemResponse]:
        personagem = self.repository.get(personagem_id)
        return PersonagemResponse.model_validate(personagem) if personagem else None
    
    def list_personagens(self) -> List[PersonagemResponse]:
        personagens = self.repository.get_all()
        return [PersonagemResponse.model_validate(personagem) for personagem in personagens]
    
    '''
    def update_personagem(self, personagem_id: uuid.UUID, personagem_data: PersonagemUpdate) -> Optional[PersonagemResponse]:
        personagem = self.repository.get(personagem_id)
        if personagem:
            for key, value in personagem_data.dict().items():
                setattr(personagem, key, value)
            personagem = self.repository.update(personagem)
            return PersonagemResponse.from_orm(personagem)
        return None

    def delete_personagem(self, personagem_id: uuid.UUID) -> None:
        self.repository.delete(personagem_id)
    '''
