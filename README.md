Introduction

This is a academic project developed under the guidance of Dr. Jon Pearce in class CS-251 (Object Oriented Analysis) .

This is a Project management application (web application) which Project Managers can use to manage 

projects, task, resources and generate schedule online. The application has been developed 

using the Python Flask framework and uses RESTful API's. Application is deployed on Heroku server.
---------------------------------------------------------------------------------------------------

Project Structure:

EntityModel

All the entity classes reside here. Our EntityModel contains following entity 

classes:

 Task.py

 CompositeTask.py

 SimpleTask.py

 Resource.py

 Schedule.py

 Deliverable.py

Controller

The controller contains controller modules. The purpose of the controller is to 

communicate to EntityModel. We have different controller to communicate with 

different entity class. The Controller contains following controller module

 Project Controller

 Task Controller

 Resource Controller

 Schedule Controller

Templates

Templates contains the user interface modules. It contains all the files related to 

frontend.

Route.py

Route.py plays a very important role. The purpose of route.py is to route the 

request to the appropriate module. It also lets the developer define the custom 

URL for requests. These URLs are easy to use and remember, and also hides the 

actual file names from the outside world.

Static

This folder contains all the JavaScript files that front-end is using. 