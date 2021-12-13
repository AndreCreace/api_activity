# Let´s import Flask
from flask import Flask, request

# Let´s import Resource and Api
from flask_restful import Resource, Api

# Let´s import our Models
from models import Persons, Activities

# Let´s create our app
app = Flask(__name__)

# Let´s create api
api = Api(app)

# *******************************************************************************************
# *********************************** Class Person ******************************************
# *******************************************************************************************
class Person(Resource):

    # ******************************** SMethod GET *********************************
    def get(self, name):

        # Let´s do a query on Persons Table using the name attribute. Let´s returning an object of type Persons
        person = Persons.query.filter_by(name=name).first()

        try:
            # Let´s build JSON response
            response = {
                'name': person.name,
                'age': person.age,
                'id': person.id
            }

        # let´s check if any error type of AttributeError happened
        except AttributeError:
            # Let´s build JSON response
            response = {
                "status": "error",
                "message": "Person not found!"
            }

        # Any other exception
        except Exception as e:
            # Let´s build JSON response
            response = {
                "status": "error",
                "message": str(e)
            }

        # Method return
        return response

    # ******************************** Method PUT *********************************
    def put(self, name):

        # Let´s do a query on persons table, to research any people by name.
        # let´s return an object of type Persons
        person = Persons.query.filter_by(name=name).first()

        # Let´s recive the data of requisition in JSON format, to update a specific person
        data = request.json

        try:

            # Let´s check if name exists in request
            if "name" in data:
                person.name = data["name"]

            # Let´s check if age exists in request
            if "age" in data:
                person.age = data["age"]

            # Let´s update and commit
            person.save()

            # Let´s return JSON
            response = {
                "id": person.id,
                "name": person.name,
                "age": person.age
            }

        # let´s check if any error type of AttributeError happened
        except AttributeError:
            # Let´s build JSON response
            response = {
                "status": "error",
                "message": "Person not found!"
            }

        # Any other exception
        except Exception as e:
            # Let´s build JSON response
            response = {
                "status": "error",
                "message": str(e)
            }

        # Method Return
        return response

    # ******************************** Method DELETE *********************************
    def delete(self, name):

        # Local variables
        response = ""
        status = ""
        message = ""

        # Let´s do a query to search a the person in table persons
        person = Persons.query.filter_by(name=name).first()

        try:
            # Let´s try to delete the person
            person.delete()
            # Let´s create a return message
            status = "success"
            message = "Person {} was deleted!".format(person.name)

        # let´s check if any error type of AttributeError happened
        except AttributeError:
            # Let´s create a return message
            status = "error"
            message = "Person {} not found!".format(person.name)

        # Any other exception
        except Exception as e:
            # Let´s create a return message
            status = "error"
            message = str(e)

        # Let´s create the JSON message return
        finally:
            # JSON message return
            response = {
                "status":status,
                "message":message
            }

        # method return
        return response

# *******************************************************************************************
# ********************Let´s create a class to list the Peoples objects **********************
# *******************************************************************************************
class ListPeoples(Resource):

    # ******************************** Method GET *********************************
    def get(self):

        # Let´s do a query to return all registered people
        people = Persons.query.all()

        # Let´s create the response
        response = [{"id":person.id, "name":person.name, "age":person.age} for person in people]

        # Method return
        return response

    # ******************************** Method POST *********************************
    def post(self):

        # Local variables
        status = ""
        message = ""

        try:
            # Let´s recive the data in format JSON, of request
            data = request.json

            # Let´s instantiate a new Person object, informing the attribute values
            person = Persons(name=data["name"], age=data["age"])

            # Let´s commit
            person.save()

            # Let´s define the status and message
            status = "success"
            message = "Successfully created person!"

        except Exception as e:
            # Let´s define the status and message
            status = "error"
            message = str(e)

        finally:

            # Let´s create the response message
            response = {
                "status":status,
                "message":message
            }

        # Method return
        return response

# *******************************************************************************************
# ******************************** List All/Create Activity *********************************
# *******************************************************************************************
class ListActivity(Resource):

    # ******************************** Method GET (List all registered Activities) *********************************
    def get(self):
        activities = Activities.query.all()
        response = [{"id":activity.id, "description":activity.description, "person":activity.person.name} for activity in activities]
        return response

    # ******************************** Method POST (Create) *********************************
    def post(self):

        try:

            # Let´s recive the data request
            data = request.json

            # Let´s check if person_id passedby parameter, exists in persons table
            person = Persons.query.filter_by(name=data["person_name"]).first()

            # let´s check if person id was found
            if person:

                # Let´s create the activity for the person
                activity = Activities(description=data["description"], person=person)

                # Let´s commit
                activity.save()

                # Let´s create the response message
                response = {
                    "id": activity.id,
                    "description": activity.description,
                    "person_id": activity.person_id,
                    "personame": activity.person.name
                }

            else:

                # Let´s create the response message
                response = {
                    "status":"error",
                    "message":"Activity not found! "
                }

        except Exception as e:
            response = {
                "status":"error",
                "message":str(e)
            }

        return response

# *********************************************************************************
# ******************************** Class Activity *********************************
# *********************************************************************************
class Activity(Resource):

    # ******************************** Method GET *********************************
    def get(self, description):
        activity = Activities.query.filter_by(description=description).first()
        try:
            response = {
                "id":activity.id,
                "description": activity.description,
                "person_id": activity.person_id
            }

        except AttributeError:
            response = {
                "status":"error",
                "message":"Activity {} not found!".format(description)
            }

        except Exception as e:
            response = {
                "status":"error",
                "message":str(e)
            }

        # Method return
        return response

    # ******************************** Method DELETE *********************************
    def delete(self, id):
        activity = Activities.query.filter_by(id=id).first()
        activity.delete()
        response = {"status":"success",
                    "message":"Activity was deleted!"}
        return response

# *****************************************************************************************************
# *********************************************** ROUTES **********************************************
# *****************************************************************************************************
"""
    Let´s register our routes (the first parameter is the our classe to create objects of type 
    person not a class to create the model.
"""
# Route to List, Update and Delete a specific person: GET (return a specific person), PUT (update a specific person) and DELETE (delete a specific person)
api.add_resource(Person, "/person/<string:name>")

# Route to list all registered people in the persons table and create a new person
api.add_resource(ListPeoples, "/person")

# Route to List, Update and Delete a specific activity: GET (return a specific activity), PUT (update a specific activity) and DELETE (delete a specific activity)
api.add_resource(Activity, "/activity/<int:id>")

# Route to list all registered people in the persons table and create a new person
api.add_resource(ListActivity, "/activity")

# *********************************************** EXECUTE APP **********************************************
# Let´s check who´s trying to execute our app
if __name__ == '__main__':
    app.run(debug=True) # Let´s execute the app



