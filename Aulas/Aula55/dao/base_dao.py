import sqlalchemy as db

from sqlalchemy.orm.session import sessionmaker

class BaseDao:
    def __init__(self, table):
        self.table = table
        engine = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
        session_mk = sessionmaker()
        session_mk.configure(bind=engine)
        self.session = session_mk()

    def list_all(self):
        return [obj.json() for obj in self.session.query(self.table).all()]

    def get_by_id(self, id):
        return self.session.query(self.table).filter_by(id=id).one()

    def insert(self, model):
        self.session.add(model)
        self.session.commit()
        return f"Objeto inserido com sucesso! id = {model.id}"

    def update(self, model):
        self.session.merge(model)
        self.session.commit()
        return f"Objeto inserido com sucesso! {model}"

    def delete(self, id):
        self.session.delete(self.get_by_id(id))
        self.session.commit()
        return f"Objeto deletado com sucesso!"