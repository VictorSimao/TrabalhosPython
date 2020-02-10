import sqlalchemy as db

from Aulas.Aula55.model.base import Base

class Genero(Base):
    __tablename__ = 'LIVRARIA_GENERO'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(lenght=100))