from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy import MetaData, create_engine

class DbApi:
    def __init__(self):
        db_user = "postgres"
        db_pwd = "hackattack"
        db_server = "eclectic-sheep.com"
        db_port = 5433

        db_string = f'postgresql://{db_user}:{db_pwd}@{db_server}:{db_port}'
        self.db = create_engine(db_string)

        self.metadata = MetaData()
        self.metadata.reflect(self.db)
        self.session = sessionmaker(bind=self.db)()
        self.tables = {table.name: table for table in self.metadata.sorted_tables}

    def _update_tables(self):
        self.metadata.reflect(self.db)
        self.tables = {table.name: table for table in self.metadata.sorted_tables}
        
    def _make_output(cols, vals):
        return [dict(zip(cols, val) for val in vals)]

    def get_volunteer(self, id=None):
        self._update_tables()
        table = self.tables['Volunteers']
        q:Query = self.session.query(table)
        
        if id is not None:
            q = q.filter(table.c.Vol_ID == id)
        
        cols = [col.name for col in table.c]
        result = q.all()

        return self._make_output(cols, result)

    def get_user(self, name=None):
        self._update_tables()
        table = self.tables['Users']
        q:Query = self.session.query(table)

        if id is not None:
            q = q.filter(table.c.Name == name)
        
        cols = [col.name for col in table.c]
        result = q.all()

        return self._make_output(cols, result)


    def get_appointment(self, name):
        self._update_tables()
        table = self.tables['Appointment']
        q:Query = self.session.query(table)

        if id is not None:
            q = q.filter(table.c.Name == name)

        cols = [col.name for col in table.c]
        result = q.all()

        return self._make_output(cols, result)

        