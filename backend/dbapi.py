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

    def get_volunteers(self):
        out = self.db.execute('SELECT * FROM "Volunteers"')
        return out
        