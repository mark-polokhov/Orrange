import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#34495E', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        close_img = Image.open('circle-cross.png')
        self.close_img_tk = ImageTk.PhotoImage(close_img)
        btn_close_window = tk.Button(toolbar, height=0, command=self.close, bg='#34495E', bd=0,
                                     compound=tk.TOP, image=self.close_img_tk)
        btn_close_window.pack(side=tk.RIGHT, anchor=tk.N)

        halfclose_img = Image.open('circle-minus.png')
        self.halfclose_img_tk = ImageTk.PhotoImage(halfclose_img)
        btn_halfclose_window = tk.Button(toolbar, height=0, command=self.half_cloce, bg='#34495E', bd=0,
                                     compound=tk.TOP, image=self.halfclose_img_tk)
        btn_halfclose_window.pack(side=tk.RIGHT, anchor=tk.N)

        add_img = Image.open('Add.ico')
        self.add_img_tk = ImageTk.PhotoImage(add_img)
        btn_open_dialog = tk.Button(toolbar, font="Georgia 8", command=self.open_dialog,
                                    bg='#34495E', bd=0, compound=tk.TOP, image=self.add_img_tk)
        btn_open_dialog.pack(side=tk.LEFT)

        edit_img = Image.open('Edit.ico')
        self.edit_img_tk = ImageTk.PhotoImage(edit_img)
        btn_edit_dialog = tk.Button(toolbar, font="Georgia 8", command=self.open_edit,
                                    bg='#34495E', bd=0, compound=tk.TOP, image=self.edit_img_tk)
        btn_edit_dialog.pack(side=tk.LEFT)

        delete_img = Image.open('Delete.ico')
        self.delete_img_tk = ImageTk.PhotoImage(delete_img)
        btn_delete = tk.Button(toolbar, font="Georgia 8", command=self.delete_records,
                               bg='#34495E', bd=0, compound=tk.TOP, image=self.delete_img_tk)
        btn_delete.pack(side=tk.LEFT)

        # checks_img = Image.open('Checks.png')
        # self.close_img_tk = ImageTk.PhotoImage(close_img)
        #btn_check_window = tk.Button(toolbar, text='Напоминания', command=self.open_checks, bg='#D9D9D9', bd=0,
                                     # compound=tk.TOP, font="Georgia 8")
        #btn_check_window.pack(side=tk.BOTTOM, anchor=tk.E)

        self.tree = ttk.Treeview(self, columns=('ID', 'Event', 'Science', 'Time', 'Date'), height=21, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('Event', width=410, anchor=tk.W)
        self.tree.column('Science', width=100, anchor=tk.CENTER)
        self.tree.column('Time', width=90, anchor=tk.CENTER)
        self.tree.column('Date', width=87, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('Event', text='Название события')
        self.tree.heading('Science', text='Направление')
        self.tree.heading('Time', text='Время')
        self.tree.heading('Date', text='Дата')

        self.tree.pack()
#
    def open_checks(self):
        Checks()
#
    def open_dialog(self):
        Child()

    def records(self, events, science, time, date):
        self.db.insert_data(events, science, time, date)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM Olymps''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def update_records(self, events, science, time, date):
        self.db.c.execute('''UPDATE Olymps SET events=?, science=?, time=?, date=? WHERE id=?''',
                          (events, science, time, date, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM Olymps WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def open_edit(self):
        Update()

    def close(self):
        root.destroy()

    def half_cloce(self):
        pass

#
class Checks(Main):

    def __init__(self):
        super().__init__(root)
        self.init_checks()

    def init_checks(self):
        self.check_tree = ttk.Treeview(self,  columns=('ID', 'Check', 'Time', 'Date'), height=21, show='headings')

        self.check_tree.column('ID', width=30, anchor=tk.CENTER)
        self.check_tree.column('Check', width=410, anchor=tk.W)
        self.check_tree.column('Time', width=90, anchor=tk.CENTER)
        self.check_tree.column('Date', width=87, anchor=tk.CENTER)

        self.check_tree.heading('ID', text='ID')
        self.check_tree.heading('Check', text='Напоминание')
        self.check_tree.heading('Time', text='Время')
        self.check_tree.heading('Date', text='Дата')

        self.check_tree.pack()
#

class Child(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить событие в список')
        self.geometry("550x130+380+150")
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        Label_Event = tk.Label(self, text='Название события:', font="Georgia 10")
        Label_Event.place(x=10, y=10)

        self.entry_event = ttk.Entry(self, width=50)
        self.entry_event.place(x=140, y=10)

        Label_Science = tk.Label(self, text='Направление:', font="Georgia 10")
        Label_Science.place(x=10, y=40)

        self.combobox = ttk.Combobox(self, values=[u'Математика', u'Информатика', u'Физика', u'Разное'])
        self.combobox.current(0)
        self.combobox.place(x=140, y=40)

        Label_Time = tk.Label(self, text='Время начала:', font="Georgia 10")
        Label_Time.place(x=10, y=70)

        self.entry_time = ttk.Entry(self)
        self.entry_time.place(x=140, y=70)

        Label_Date = tk.Label(self, text='Дата:', font="Georgia 10")
        Label_Date.place(x=10, y=100)

        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=140, y=100)

        self.btn_cancel = ttk.Button(self, text='Отменить', command=self.destroy)
        self.btn_cancel.place(x=460, y=40)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=460, y=10)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_event.get(), self.combobox.get(),
                                                                       self.entry_time.get(), self.entry_date.get()))


class Update(Child):

    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактирование события")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=365, y=100)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_records(self.entry_event.get(), self.combobox.get(),
                                                                           self.entry_time.get(), self.entry_date.get()))
        self.btn_ok.destroy()
        self.btn_cancel.destroy()

        self.btn_cancel_copy = ttk.Button(self, text='Отменить', command=self.destroy)
        self.btn_cancel_copy.place(x=460, y=100)


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('Olymps.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Olymps (id integer primary key, events text, 
            science text, time text, date text)'''
        )
        self.conn.commit()

    def insert_data(self, events, science, time, date):
        self.c.execute('''INSERT INTO Olymps(events, science, time, date) VALUES (?, ?, ?, ?)''',
                       (events, science, time, date))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.iconbitmap('Icon.ico')
    root.title("Olymps")
    root.geometry("720x500+320+110")
    root.resizable(False, False)
    root.update_idletasks()
    # root.overrideredirect(True)
    root.mainloop()

__version__ = '1.1'
__author__ = "Mark Polokhov <mark.polokhov@yandex.ru>"

# New version 1.1:
# Create update button (Done)
# Change design
# Create 3 tabs: Main, Registration and Check(Other)

# Temp
# text='Новое событие'
# text='Редактировать'
# text='Удалить событие'
