"""
In this file you must implement all your database models.
If you need to use the methods from your database.py call them
statically. For instance:
       # opens a new connection to your database
       connection = Database.connect()
       # closes the previous connection to avoid memory leaks
       connection.close()
"""

from database import Database, Query


class TestModel:
    """
    This is an object model example. Note that
    this model doesn't implement a DB connection.
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.author = ctx.message.author.name

    def response(self):
        return f'Hi, {self.author}. I am alive'



class Employer: 

  def __init__(self, employer_id): 
      self._id = employer_id
      self._name = Database.select(Query.GET_EMPLOYER, (self._id))
      self._gender = Database.select(Query.GET_GENDER, (self._id))
      self._biography = Database.select(Query.GET_BIOGRAPHY, (self._id)) 
      self._account = None 
      self._team = Database.select(Query.GET_TEAMID, (self._id))  
      self._region = None
      self._language = None
      self._fashiongenre = None
      self._load()
  
  def _load(self): 
      employers_data = Database.select(Query.GET_EMPLOYER, (self._id))
      #if employers_data:
      #    first_element = employers_data[0]
      #    self._name = first_element
      name = employers_data
      
  
  @staticmethod
  def get(employer_id):
      return Employer(employer_id)

  
  @staticmethod
  def all(): 
      employers = [] # this is an array
      employers_data = Database.select(Query.GET_ALL_EMPLOYERS)
      for tmp_employer in employers_data: 
          employer_id = tmp_employer['employer_id']
          employer = Employer.get(employer_id)
          employers.append(employer)
      return employers
  
  @staticmethod
  def add(employer_id, name, gender, biography, account, team, region, language, fashiongenre):
      employer = Employer.get(employer_id)
      employer._name = name
      employer._gender = gender 
      employer._biography = biography
      employer._account = account
      employer._team = team
      employer._region = region
      employer._language = language
      employer._fashiongenre = fashiongenre
      Database.insert(Query.ADD_EMPLOYER, (employer_id, name, gender, biography, account, team, region, language, fashiongenre))

  @staticmethod
  def update(employer_id, name):
      employer = Employer.get(employer_id)
      employer._name = name
      Database.update(Query.UPDATE_EMPLOYER, (name, employer_id))

