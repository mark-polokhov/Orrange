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
    
    def convert_data(record):
        data = {
            "ID": [0],
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
                            time, price, address, coordinates, is_open, about, conditions) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (name, type, date, time, price, address, coordinates, is_open, about, conditions))
        self.conn.commit()
    
    def get_record(self, id):
        records = self.curs.fetchall()
        record = records[id]
        return self.convert_data(record)
    
    def view_records_of(self, k):
        records = self.curs.fetchall()
        data_list = []
        for id in range(k):
            record = records[id]
            data_list.append(self.convert_data(record))
        return data_list

    def delete_record(self, id):
        self.db.curs.execute('''DELETE FROM Olymps WHERE id=?''', id)
        self.db.conn.commit()
    
    def update_record(self, id, name, type, date, time, price, address, coordinates, is_open, about, conditions):
        self.db.curs.execute('''UPDATE Olymps SET name=?, type=?, date=?, time=?, price=?, address=?, coordinates=?, is_open=?, aboud=?, conditions=? WHERE id=?''',
                          (name, type, date, time, price, address, coordinates, is_open, about, conditions, id))
        self.db.conn.commit()
        self.view_records()
