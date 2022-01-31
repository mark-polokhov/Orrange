import sqlalchemy as sa

class DB:
    def __init__(self):
        meta = sa.MetaData()
        self.table = sa.Table('Event', meta,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String, nullable=False),
            sa.Column('name', sa.String),
            sa.Column('email', sa.String),
            sa.Column('password_hash', sa.String),
            sa.Column('price', sa.Integer),
            sa.Column('address', sa.String),
            sa.Column('coordinates', sa.String),
            sa.Column('is_open', sa.Integer),
            sa.Column('about', sa.String),
            sa.Column('conditions', sa.String))
        
        self.engine = sa.create_engine('sqlite:///db/events.db', echo=True)
        self.table.create(self.engine)
        self.conn = self.engine.connect()


    def convert_data(self, record):
        data = {
            "ID": record[0],
            "Name": record[1],
            "Type": record[2],
            "Date": record[3],
            "Time": record[4],
            "Price": record[5],
            "Address": record[6],
            "Coordinates": record[7],
            "IsOpen": record[8],
            "About": record[9],
            "Conditions": record[10],
        }
        return data

    def insert_data(self, name, type, date, time, price, address, coordinates, is_open, about, conditions):
        self.conn.execute(self.table.insert().values(name, type, date, time, price, address, coordinates, is_open, about, conditions))

    def get_record(self, id: int):
        record = self.conn.execute(self.table.select().where(sa.table.c.id == id))
        return self.convert_data(record)

    def view_records_of(self, k):
        records = self.conn.execute(self.table.select().where(sa.table.c.id < k))
        data_list = []
        for id in range(k):
            record = records[id - 1]
            data_list.append(self.convert_data(record))
        return data_list

    def view_records(self):
        records = self.conn.execute(self.table.select())
        data_list = []
        for record in records:
            data_list.append(self.convert_data(record))
        return data_list

    def delete_record(self, id):
        self.conn.execute(self.table.delete().where(sa.table.c.id == id))

    def update_record(self, id, name, type, date, time, price, address, coordinates, is_open, about, conditions):
        self.conn.execute(self.table.update().values(name, type, date, time, price, address, coordinates, is_open, about, conditions))
