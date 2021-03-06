# Let´s import the dependencies
from models import Persons, Users

# Function to make a query and return a specific person
def getPersonsAll():

    try:
        person = Persons.query.all()

        # Let´s check if the pepople was located
        if person:
            print(person)

        # The person was not locted
        else:
            print("Person not located!")

    except Exception as e:
        print(str(e))

# Function to make a query and return a specific person
def getPersonsByName():

    try:
        person = Persons.query.filter_by(name="Gabi").first() # Let´s make a query

        # Let´s check if the pepople was located
        if person:
            print(person.age)

        # The person was not locted
        else:
            print("Person not located!")

    except Exception as e:
        print(str(e))

# Function to add new person
def addPerson():
    person = Persons(name="Andre", age=46) # Let´s instantiate a new Person object
    person.save() # Let´s add the new person and commit

# Function to update persons
def updatePerson():
    person = Persons.query.filter_by(name="Gabi").first()  # Let´s make a query
    person.age = 37 # Let´s do the update
    person.save() # Let´s do the commit

# Function to update persons
def deletePerson():
    person = Persons.query.filter_by(name="Andre").first()  # Let´s make a query
    person.delete() # Let´s do the commit

# ************************ USER ***************************
def addUser():
    user = Users(username="gabi", password="321")
    user.save()

def deleteUser():
    user = Users.query.filter_by(username="andre").first()
    user.delete()

def getUserAll():

    try:
        user = Users.query.all()

        # Let´s check if the pepople was located
        if user:
            print(user)

        # The person was not locted
        else:
            print("User not located!")

    except Exception as e:
        print(str(e))

# Let´s check who´s calling the main
if __name__ == "__main__":
    #addPerson()
    #updatePerson()
    #deletePerson()
    #getPersonsAll()
    #getPersonsByName()
    addUser()
    getUserAll()