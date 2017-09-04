import mysql.connector

config = {'user':'root', 'password':'root', 'host':'127.0.0.1', 'database':'event_signup'}

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(**config)
        self.cursor = self.db.cursor()

    def add(self, firstname, lastname, email, event, password):
        query = "INSERT INTO members (firstName, lastName, email, event) VALUES ('%s', '%s', '%s', '%s')"%(firstname, lastname, email, event)
        query1 = "INSERT INTO users (email, password) VALUES ('%s', '%s')"%(email, password)
        self.cursor.execute(query)
        self.cursor.execute(query1)
        self.db.commit()
        print('Done!')  # for debug

    def remove(self, email):
        query = "DELETE FROM members WHERE email='%s'"%email
        query1 = "DELETE FROM users WHERE email='%s'"%email
        self.cursor.execute(query)
        self.cursor.execute(query1)
        self.db.commit()
        print('Done!')  # for debug

    def all_members(self):
        query = "SELECT firstName, lastName, event from members"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_member(self, email, password):
        query = "SELECT email from users where email='%s' and password='%s'"%(email, password)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result == []:
            return None
        else:
            user_email = result[0][0]
            query = "SELECT firstName, lastName, email, event from members WHERE email='%s'"%(user_email)
            self.cursor.execute(query)
            user_details = self.cursor.fetchall()
            return user_details

    def change_name(self, email, first_name, last_name):
        query = "UPDATE members SET firstName='%s' WHERE email='%s'"%(first_name, email)
        self.cursor.execute(query)
        query = "UPDATE members SET lastName='%s' WHERE email='%s'" % (first_name, email)
        self.cursor.execute(query)
        self.db.commit()
        print("Done")  # for debug

    def edit_activity(self, email, activity):
        query = "UPDATE members SET event='%s' WHERE email='%s'"%(activity, email)
        self.cursor.execute(query)
        self.db.commit()
        print("Done")  # for debug

    def __del__(self):
        self.db.close()
