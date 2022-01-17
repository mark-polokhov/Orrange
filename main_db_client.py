import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('db/events.db')
        self.curs = self.conn.cursor()
        self.curs.execute(
            '''CREATE TABLE IF NOT EXISTS Olymps (id integer primary key, name text, type text, 
                date text, time text, price integer, address text, coordinates text, is_open integer, about text, conditions text)'''
        )
        self.conn.commit()

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
        self.curs.execute('''INSERT INTO Olymps(name, type, date,
                            time, price, address, coordinates, is_open, about, conditions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (name, type, date, time, price, address, coordinates, is_open, about, conditions))
        self.conn.commit()

    def get_record(self, id: int):
        records = self.curs.execute('''SELECT * FROM Olymps''').fetchall()
        record = records[id - 1]
        return self.convert_data(record)

    def view_records_of(self, k):
        records = self.curs.execute('''SELECT * FROM Olymps''').fetchall()
        data_list = []
        for id in range(k):
            record = records[id - 1]
            data_list.append(self.convert_data(record))
        return data_list

    def view_records(self):
        records = self.curs.execute('''SELECT * FROM Olymps''').fetchall()
        data_list = []
        for record in records:
            data_list.append(self.convert_data(record))
        return data_list

    def delete_record(self, id):
        self.curs.execute('''DELETE FROM Olymps WHERE id=?''', id)
        self.conn.commit()

    def update_record(self, id, name, type, date, time, price, address, coordinates, is_open, about, conditions):
        self.curs.execute('''UPDATE Olymps SET name=?, type=?, date=?, time=?, price=?, address=?, coordinates=?, is_open=?, aboud=?, conditions=? WHERE id=?''',
                            (name, type, date, time, price, address, coordinates, is_open, about, conditions, id))
        self.conn.commit()
