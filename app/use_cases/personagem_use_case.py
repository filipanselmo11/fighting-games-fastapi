from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.exceptions import HTTPException
from app.schemas.personagem_schema import PersonagemRequest
from app.models.personagem_model import PersonagemModel
import uuid

class PersonagemUseCase:
    def __init__(self, db: Session):
        self.db = db
    
    def create_personagem(self, personagem: PersonagemRequest):
        personagem_model = PersonagemModel(
            nome=personagem.nome,
            img=personagem.img,
            descricao=personagem.descricao,
            jogo=personagem.jogo
        )
        try:
            self.db.add(personagem_model)
            self.db.commit()
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Personagem já existe')
        
    
    def get_personagem_id(self, personagem_id: uuid):
        personagem_db = self.db.query(PersonagemModel).filter(PersonagemModel.id == personagem_id).first()
        if personagem_db is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Personagem com o id informado, não foi encontrado')
        return personagem_db
    
    def get_personagens(self, skip: int = 0, limit: int = 10):
        return self.db.query(PersonagemModel).offset(skip).limit(limit).all()