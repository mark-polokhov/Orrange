import sqlite3

conn = sqlite3.connect('events.db')
curs = conn.cursor()
curs.execute(
    '''CREATE TABLE IF NOT EXISTS Olymps (id integer primary key, name text, type text, 
        date text, time text, price integer, address text, coordinates text, is_open integer, about text, conditions text)'''
)
conn.commit()

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

def insert_data(name, type, date, time, price, address, coordinates, is_open, about, conditions):
    curs.execute('''INSERT INTO Olymps(name, type, date,
                        time, price, address, coordinates, is_open, about, conditions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (name, type, date, time, price, address, coordinates, is_open, about, conditions))
    conn.commit()

def get_record(id):
    records = curs.fetchall()
    record = records[id]
    return convert_data(record)

def view_records_of(k):
    records = curs.fetchall()
    data_list = []
    for id in range(k):
        record = records[id]
        data_list.append(convert_data(record))
    return data_list

def view_records():
    records = curs.execute('''SELECT * FROM Olymps''')
    data_list = []
    for record in records:
        data_list.append(convert_data(record))
    return data_list

def delete_record(id):
    curs.execute('''DELETE FROM Olymps WHERE id=?''', id)
    conn.commit()

def update_record(id, name, type, date, time, price, address, coordinates, is_open, about, conditions):
    curs.execute('''UPDATE Olymps SET name=?, type=?, date=?, time=?, price=?, address=?, coordinates=?, is_open=?, aboud=?, conditions=? WHERE id=?''',
                        (name, type, date, time, price, address, coordinates, is_open, about, conditions, id))
    conn.commit()
