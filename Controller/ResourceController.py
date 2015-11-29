from EntityModel.CompositeTask import CompositeTask
from EntityModel.SimpleTask import SimpleTask
from EntityModel.Resource import Resource
from flask import Flask, jsonify, request
import main_func
import json

def addResource(json_request):
    name = json_request['name']
    type = json_request['type']
    taskId = json_request['taskId']
    
    resource = Resource(main_func.getId(), name, type)

    taskObject = main_func.project_objects[taskId]
    taskObject.addResource(resource)
    main_func.project_objects[resource.id] = resource
    
    #with open('project_objects.json', mode = 'w') as f:
	    #json.dump(taskObject, f, default=main_func.jdefault, indent = 2)
    
    resource_json = main_func.jdefault(resource)
    return json.dumps(resource_json, default=main_func.jdefault, indent = 2)