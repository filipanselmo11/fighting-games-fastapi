from pydantic import BaseModel
import uuid

class PersonagemResponse(BaseModel):
    id: uuid
    nome: str
    img: str
    descricao: str
    jogo: str

    class Config:
        from_attributes = True


class PersonagemRequest(BaseModel):
    nome: str
    img: str
    descricao: str
    jogo: str