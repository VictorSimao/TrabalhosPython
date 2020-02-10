import sqlalchemy as db
from sqlalchemy.orm import relationship

from Aulas.Aula55.model.pessoa import Pessoa


class Autor:
    __tablename__ = 'LIVRARIA_AUTOR'
    id = db.Column(db.Integer, primary_key=True)
    pseudonimo = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=100))
    pessoa_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_PESSOA.ID'))
    pessoa = relationship(Pessoa)