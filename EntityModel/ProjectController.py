from EntityModel.CompositeTask import CompositeTask
from EntityModel.SimpleTask import SimpleTask
from EntityModel.Deliverable import Deliverable
from flask import Flask, jsonify, request
import main_func
import json



def createProject(json_request):
	name = json_request['name']
	date = json_request['date']
	duration = None
	if('duration' in json_request):
	    duration = json_request['duration']
	
	project = CompositeTask(main_func.getId(), name, "main_project", date, duration, None, [], [], [], [], [], [])
	
	main_func.project_objects[project.id] = project
	#project = main_func.project_objects[project.id]
	main_func.mainProject = project
	#with open('project_objects.json', mode = 'w') as f:
	    #json.dump(main_func.project_objects, f, default=main_func.jdefault, indent = 2)
	    
	#with open('project_objects.json', mode = 'r') as f:
	    #data = json.load(f)
	    
	    
	
	project_json = main_func.jdefault(project)
	return json.dumps(project_json, indent = 2)
	
	
    
    
def createDeliverable(json_request):
    name = json_request['name']
    type = json_request['type']
    taskId = json_request['taskId']
    
    deliverable = Deliverable(main_func.getId(), name, type)
    taskObject = main_func.project_objects[taskId]
    taskObject.addDeliverable(deliverable)
    main_func.project_objects[deliverable.id] = deliverable
    
    deliverable_json = main_func.jdefault(deliverable)
    return json.dumps(deliverable_json, default=main_func.jdefault, indent = 2)
    
    
def saveProject(json_request):
    projectId = json_request['projectId']
    project = main_func.project_objects[projectId]
    
    project_json = main_func.jdefault(project)
    
    with open('project.json', mode = 'w') as f:
	    json.dump(project_json, f, default=main_func.jdefault, indent = 2)
	    
    return json.dumps(project_json, default=main_func.jdefault, indent = 2)
    