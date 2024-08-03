#Single Responsibility Principle
from sqlalchemy.orm import Session
from app.models.personagem_model import PersonagemModel
from typing import Optional, List
import uuid

class PersonagemRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, personagem: PersonagemModel) -> PersonagemModel:
        self.session.add(personagem)
        self.session.commit()
        self.session.refresh(personagem)
        return personagem
    

    def get(self, personagem_id: uuid.UUID) -> Optional[PersonagemModel]:
        return self.session.query(PersonagemModel).filter_by(id=personagem_id).first()
    
    def get_all(self) -> List[PersonagemModel]:
        return self.session.query(PersonagemModel).all()
    
    # def update(self, personagem: PersonagemModel) -> PersonagemModel:
    #     self.session.commit()
    #     self.session.refresh(personagem)
    #     return personagem
    
    # def delete(self, personagem_id: uuid.UUID) -> None:
    #     personagem = self.session.query(PersonagemModel).filter_by(id=personagem_id).first()
    #     if personagem:
    #         self.session.delete(personagem)
    #         self.session.commit()