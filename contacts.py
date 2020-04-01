import sqlite3


class contac(object):
    def connect(self):
        try:
            self.connection = sqlite3.connect('database.db')
            self.c = self.connection.cursor()
            self.c.execute('''Create Table Contacts
                         (Name text,Phone_Number integer,Email text,Linkdin text)''')
            self.connection.commit()
        except:
            self.connection = sqlite3.connect('database.db')
            self.c = self.connection.cursor()

    def insert_row(self, name, age, email, linkdin):
        self.name = name
        self.c.execute("Insert into Contacts values(?,?,?,?)",(name,age,email,linkdin))
        self.connection.commit()
    def get_row(self,name):

        self.c.execute("SELECT * from Contacts where name = ?",(str(name),))
        row = self.c.fetchone()
        return row
con = contac()
