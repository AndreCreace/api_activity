# Let´s import the sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

# Let´s import the dependencies to make a session with Data Base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

# Let´s import the declarative_base
from sqlalchemy.ext.declarative import declarative_base

# Let´s create a SQLite
engine = create_engine("sqlite:///activities", convert_unicode=True)

# Let´s create a session with the Data Base
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

# Let´s create the base
Base = declarative_base()
Base.query = db_session.query_property()

##### Let´s create our tables


# ********************************** Table People ********************************
class Persons(Base):

    # Here, we can chance the table´s name for the environment production
    __tablename__ = "persons"

    # Attributes (Table´s fields)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), index=True)
    age = Column(Integer)

    # method to add a new person
    def save(self):
        db_session.add(self) # Let´s add the new person
        db_session.commit() # Let´s commit

    # method to delete a person
    def delete(self):
        db_session.delete(self) # Let´s delete the person
        db_session.commit() # Let´s commit

    # Method to print (repr means representação in Portuguese)
    def __repr__(self):
        return "Person: {}".format(self.name)

# *********************************** Table Activities **************************************
class Activities(Base):

    # Here, we can ro chance the table´s name for the environment production
    __tablename__ = "activities"

    # Attributes (Table´s fields)
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(80), index=True) # The index is used in tunning queries
    person_id = Column(Integer, ForeignKey("persons.id")) # Foreign Key
    person = relationship("Persons")

    # Method to print (repr means representação in Portuguese)
    def __repr__(self):
        return "Activity: {}".format(self.description)

    # method to add a new person
    def save(self):
        db_session.add(self) # Let´s add the new activity
        db_session.commit() # Let´s commit

    # method to delete a person
    def delete(self):
        db_session.delete(self) # Let´s delete the activity
        db_session.commit() # Let´s commit

# *********************************** Table Users **************************************
class Users(Base):

    # Here, we can ro chance the table´s name for the environment production
    __tablename__ = "users"

    # Attributes (Table´s fields)
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), index=True, unique=True) # The index is used in tunning queries, and the unique means unique indice
    password = Column(String(50))

    # Method to print (repr means representação in Portuguese)
    def __repr__(self):
        return "Username: {}".format(self.username)

    # method to add a new person
    def save(self):
        db_session.add(self) # Let´s add the new activity
        db_session.commit() # Let´s commit

    # method to delete a person
    def delete(self):
        db_session.delete(self) # Let´s delete the activity
        db_session.commit() # Let´s commit

# ******************* Function to create our Data Base
def init_db():
    Base.metadata.create_all(bind=engine)

# ******************** Let´s check who´s calling the main
if __name__ == "__main__":
    init_db()