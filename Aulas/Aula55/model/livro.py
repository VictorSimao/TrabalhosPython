import sqlalchemy as db
from sqlalchemy.orm import relationship

from Aulas.Aula55.model.base import Base
from Aulas.Aula55.model.autor import Autor
from Aulas.Aula55.model.editora import Editora
from Aulas.Aula55.model.genero import Genero

class Livro(Base):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(lenght=100))
    sinopse = db.Column(db.String(lenght=100))
    data_primeira_publicacao = db.Column(db.DATE)
    autor_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_AUTOR.ID'))
    autor = relationship(Autor)
    editora_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_EDITORA.ID'))
    editora = relationship(Editora)
    genero_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_GENERO.ID'))
    genero = relationship(Genero)