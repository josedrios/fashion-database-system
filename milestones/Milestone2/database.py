# In this file you must implement your main query methods 
# so they can be used by your database models to interact with your bot.

import os
import pymysql.cursors

# note that your remote host where your database is hosted
# must support user permissions to run stored triggers, procedures and functions.
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


class Database:

    @staticmethod
    def connect(bot_name=None):
        """
        This method creates a connection with your database
        IMPORTANT: all the environment variables must be set correctly
                   before attempting to run this method. Otherwise, it
                   will throw an error message stating that the attempt
                   to connect to your database failed.
        """
        try:
            conn = pymysql.connect(host=db_host,
                                   port=3306,
                                   user=db_username,
                                   password=db_password,
                                   db=db_name,
                                   charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
            print("Bot connected to database {}".format(db_name))
            return conn
        except ConnectionError as err:
            print(f"An error has occurred: {err.args[1]}")
            print("\n")

    #TODO: needs to implement the internal logic of all the main query operations
    def get_response(self, query, values=None, fetch=False, many_entities=False):
      con = Database.connect()
      cur = con.cursor()
      if values: 
         if many_entities: 
            cur.executemany(query, values)
         else: 
            cur.execute(query, values)
      else:  
         cur.execute(query)

      con.commit()
      con.close()
      if fetch: 
        return cur.fetchall()
      return None

    @staticmethod
    def select(query, values=None, fetch=True):
        database = Database()
        return database.get_response(query, values=values, fetch=fetch)

    @staticmethod
    def insert(query, values=None, many_entities=False):
        database = Database()
        return database.get_response(query, values=values, many_entities=many_entities)

    @staticmethod
    def update(query, values=None):
        database = Database()
        return database.get_response(query, values=values)

    @staticmethod
    def delete(query, values=None):
        database = Database()
        return database.get_response(query, values=values)

class Query: 
  GET_EMPLOYER = """SELECT full_name FROM FashionDesignDB.Employer WHERE employer_id = %s"""
  GET_GENDER = """SELECT gender FROM FashionDesignDB.Employer WHERE employer_id = %s"""
  GET_BIOGRAPHY = """SELECT biography FROM FashionDesignDB.Employer WHERE employer_id = %s"""
  GET_TEAMID = """SELECT team_id FROM FashionDesignDB.Employer WHERE employer_id = %s"""
  GET_ALL_EMPLOYERS = """SELECT * FROM FashionDesignDB.Employer"""
  ADD_EMPLOYER = """INSERT INTO FashionDesignDB.Employer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
  UPDATE_EMPLOYER = """UPDATE Employer SET full_name = %s WHERE employer_id = %s"""