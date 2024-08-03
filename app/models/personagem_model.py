#Single Responsibility Principle

from app.shared.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String

class PersonagemModel(Base):
    __tablename__ = "personagens"
    id = Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column('nome', String, nullable=False)
    img = Column('img', String, nullable=False)
    descricao = Column('descricao', String, nullable=False)
    jogo = Column('jogo', String, nullable=False)