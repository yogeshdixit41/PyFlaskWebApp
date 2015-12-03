from EntityModel.CompositeTask import CompositeTask
from EntityModel.SimpleTask import SimpleTask
from EntityModel.Deliverable import Deliverable
from flask import Flask, jsonify, request
import main_func
import json
import os.path
import sys



def createProject(name, date):
	#name = json_request['pname']
	#date = json_request['date']	
	project = CompositeTask(main_func.getId(), name, "main_project", date, 0, None, [], [], [], [], [], [])
	
	main_func.project_objects[project.id] = project
	#project = main_func.project_objects[project.id]
	main_func.mainProject = project
	#with open('project_objects.json', mode = 'w') as f:
	    #json.dump(main_func.project_objects, f, default=main_func.jdefault, indent = 2)
	
	project_json = main_func.jdefault(project)
	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
		json.dump(project_json, outFile)
	return json.dumps(project_json, indent = 2)
	
	
    
    
def createDeliverable(name, type, pId):

	deliverable = Deliverable(main_func.getId(), name, type)
	#parseJSON and get taskObject against the pId
	deliverable_json = main_func.jdefault(deliverable)
	project_json = None
	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'r') as inFile:
		project_json = json.load(inFile);
		project_json['deliverables'].append(deliverable_json);

	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
		json.dump(project_json, outFile)
  
	return json.dumps(project_json, default=main_func.jdefault, indent = 2)
    
    
def saveProject(projectId):
    #projectId = json_request['projectId']

	#parse project file and fetch json object corresponsing to projectId
    project = main_func.project_objects[projectId]
    
    project_json = main_func.jdefault(project)
    
    with open('project.json', mode = 'w') as f:
	    json.dump(project_json, f, default=main_func.jdefault, indent = 2)
	    
    return json.dumps(project_json, default=main_func.jdefault, indent = 2)
    
def importProject(project):
	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
		json.dump(project, outFile)
  
	return json.dumps(project, default=main_func.jdefault, indent = 2)

