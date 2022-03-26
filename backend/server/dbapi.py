from typing import Dict, Optional
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy import MetaData, create_engine, Table
from sqlalchemy.engine import Engine

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
        self.tables: Dict[str, Table] = {table.name: table for table in self.metadata.sorted_tables}

    def _update_tables(self):
        self.metadata.reflect(self.db)
        self.tables = {table.name: table for table in self.metadata.sorted_tables}
        
    @staticmethod
    def _make_output(cols, vals):
        return [dict(zip(cols, val)) for val in vals]

    def get_web_user(self, phone_num):

        table = self.tables["Users"]
        q:Query = self.session.query(table)
        q = q.filter(table.c.Phone_Number == phone_num)
        if q.count() == 1:
            user = q.all()[0]
            user_type = "Users"
        else: 
            if q.count == 0:
                table = self.tables["Volunteers"]
                q = self.session.query(table)
                q = q.filter(table.c.Phone_Number == phone_num)
                if q.count() == 1:
                    user = q.all()[0]
                    user_type="Volunteers"
                else:
                    raise KeyError("User Not Found") 
            else:
                raise KeyError("User Not Found")
        
        cols = [col.name for col in table.c]
        dict_usr = dict(zip(cols, user))
        return_val = {key: dict_usr[key] for key in ["Name", "Phone_Number", "Language"]}
        return_val['user_type'] = user_type

        return return_val

    def get_volunteer(self, id=None):
        self._update_tables()
        table = self.tables['Volunteers']
        q:Query = self.session.query(table)
        
        if id is not None:
            q = q.filter(table.c.Vol_ID == id)
        
        cols = [col.name for col in table.c]
        result = q.all()

        return self._make_output(cols, result)

    def get_user(self, id=None):
        self._update_tables()
        table = self.tables['Users']
        q:Query = self.session.query(table)

        if id is not None:
            q = q.filter(table.c.UserID == id)
        
        cols = [col.name for col in table.c]
        result = q.all()

        return self._make_output(cols, result)


    def get_appointment(self, id):
        self._update_tables()
        appt_table = self.tables['Appointment']
        users_table = self.tables['Users']
       
        # q: Query = self.session.query(appt_table)
        # q = q.join(users_table.c.User_ID)
        cols = ["Appointment_Key",
                "Start_Time",
                "End_Time",
                "Volunteer",
                "User",
                "PhoneNumber",
                "Issue"]
        query_text = 'Select distinct "Appointment"."Appointment_Key", "Appointment"."Start_Time","Appointment"."End_Time","Volunteers"."Name" as Volunteer_Name,"Users"."Name" as User,"Users"."Phone_Number" as PhoneNumber,"Users"."Issue" from "Appointment","Users", "Volunteers" where "Users"."UserID" = "Appointment"."User_ID" and "Appointment"."Volunteer_ID" =  "Volunteers"."Vol_ID"'
        if id is not None:
            query_text = query_text + ' and "Appointment"."Appointment_Key" = {}'.format(id)
        result = self.db.execute(query_text)

        return self._make_output(cols, result)

    def create_user(self, 
                    Name: str, 
                    Phone_Number: str, 
                    Language: str, 
                    Issue: str, 
                    Issue_Desc: str, 
                    Availability: int):
        '''
        Creates a new user in the database.

        returns the id of the newly created record
        on fail, returns -1
        '''

        self._update_tables()
        table = self.tables['Users']

        record = dict(
            Name=Name,
            Phone_Number=Phone_Number,
            Language=Language,
            Issue=Issue,
            Issue_Desc=Issue_Desc,
            Availability=Availability,
            Appointment=None
        )

        try:
            with self.db.begin() as conn:
                res = conn.execute(table.insert(), record)
        except:
            return -1

        return res.inserted_primary_key[-1]
        
    def create_volunteer(self, 
                         Name: str, 
                         Language: str, 
                         Phone_Number: str,
                         Start_Time: int,
                         Stop_Time: int):
        '''
        Creates a new volunteer in the database.

        returns the id of the newly created record
        on fail, returns -1
        '''

        self._update_tables()
        table = self.tables['Volunteers']

        record = dict(
            Name=Name,
            Language=Language,
            Phone_Number=Phone_Number,
            Start_Time=Start_Time,
            Stop_Time=Stop_Time
        )

        try:
            with self.db.begin() as conn:
                res = conn.execute(table.insert(), record)
        except Exception as e:
            print(e)
            return -1

        return res.inserted_primary_key[-1]


    def create_appointment(self,
                            Start_Time: int,
                            End_Time: int,
                            User_ID: int,
                            Volunteer_ID: int,
                            Issue: str):

        self._update_tables()
        table = self.tables['Appointment']

        record = dict(
            Start_Time=Start_Time,
            End_Time=End_Time,
            User_ID=User_ID,
            Volunteer_ID=Volunteer_ID,
            Issue=Issue
        )

        try:
            with self.db.begin() as conn:
                res = conn.execute(table.insert(), record)
        except:
            return -1

        return res.inserted_primary_key[-1]



    def update_appointment(self,
                           Start_Time: int,
                           End_Time: int,
                           Name: str,
                           Volunteer_Name: str,
                           Issue: str):

        self._update_tables()
        table = self.tables['Appointment']

        record = dict(
            Start_Time=Start_Time,
            End_Time=End_Time,
            Name=Name,
            Volunteer=Name,
            Issue=Issue
        )
        try:
            with self.db.begin() as conn:
                res = conn.execute(table.update(), record)
        except:
            return -1

        return res.inserted_primary_key[-1]

        return res.inserted_primary_key[-1]



    def update_volunteer(self,
                           Name: str,
                           Start_Time: int,
                           Endtime: str,
                           Language: str,
                           UserID: int
                          ):

        self._update_tables()
        table = self.tables['Volunteer']

        record = dict(
                Name=Name,
                Start_Time=Start_Time,
                End_time=Endtime,
                Language=Language,
        )
        try:
            with self.db.begin() as conn:
                res = conn.execute(table.update(), record)
        except:
            return -1

        return res.inserted_primary_key[-1]


    def update_User(self,
                        Name: str,
                        Start_Time: int,
                        Endtime: str,
                        Language: str,
                        UserID: int
                          ):

        self._update_tables()
        table = self.tables['Users']

        record = dict(
                Name=Name,
                Start_Time=Start_Time,
                End_time=Endtime,
                Language=Language,
        )
        try:
            with self.db.begin() as conn:
                res = conn.execute(table.update(), record)
        except:
            return -1