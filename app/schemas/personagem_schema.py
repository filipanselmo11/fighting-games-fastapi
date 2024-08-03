from pydantic import BaseModel
import uuid

class PersonagemRequest(BaseModel):
    nome: str
    img: str
    descricao: str
    jogo: str

class PersonagemResponse(BaseModel):
    id: uuid.UUID
    nome: str
    img: str
    descricao: str
    jogo: str

    class Config:
        from_attributes = True