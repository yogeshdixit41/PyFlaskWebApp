from EntityModel.CompositeTask import CompositeTask
from EntityModel.SimpleTask import SimpleTask
from EntityModel.Resource import Resource
from flask import Flask, jsonify, request
import main_func
import json
import os.path
import sys

def addResource(rname,rdailycost,rtype,rallocatedtasks):
    
    resource = Resource(main_func.getId(), rname, rdailycost, rtype, rallocatedtasks)
      
    resource_json = main_func.jdefault(resource)
    project_json = None
    with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'r') as inFile:
        project_json = json.load(inFile);

    project_json['resources'].append(resource_json)
    taskList = project_json['children']

    if rallocatedtasks is not None:
    	associateResource(taskList,resource,rallocatedtasks)
    project_json['children'] = taskList

    with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
        json.dump(project_json, outFile)
  
    return json.dumps(project_json, default=main_func.jdefault, indent = 2)
    

def editResource(rid,rname,rdailycost,rtype,rallocatedtasks):

    project_json = None
	
    resource = Resource(rid, rname, rdailycost, rtype, rallocatedtasks)
    resource_json = main_func.jdefault(resource)

    with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'r') as inFile:
        project_json = json.load(inFile);

    resources = project_json['resources']
    taskList = project_json['children']
    
    for eachResource in resources:
        if rid == eachResource['id']:
			project_json['resources'].remove(eachResource)

    project_json['resources'].append(resource_json)
    associateResource(taskList, resource, rallocatedtasks )
    project_json['children'] = taskList

    with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
        json.dump(project_json, outFile)

    return json.dumps(project_json, default=main_func.jdefault, indent = 2)
	        

def associateResource(taskList,resource,rallocatedtasks):
	for task in taskList:
		if task['id'] in rallocatedtasks and resource in task['resources']:
			pass
		elif task['id'] in rallocatedtasks and resource not in task['resources']:
			task['resources'].append(resource.id)
		elif task['id'] not in rallocatedtasks and resource in task['resources']:
			task['resources'].remove(resource.id)

		if task.has_key('children'):
			children = task['children']
			if children:
				associateResource(children,resource,rallocatedtasks)

def removeResource(id):
    project_json = None
    with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'r') as inFile:
        project_json = json.load(inFile);

    taskList = project_json['children']
    project_json['resources'] = [resource for resource in project_json['resources'] if resource['id'] != id ]
    removeResourceFromTasks(taskList,id)
    project_json['children'] = taskList
    with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
        json.dump(project_json, outFile)

    return json.dumps(project_json, default=main_func.jdefault, indent = 2)

def removeResourceFromTasks(taskList,id):
    for task in taskList:
        if id in task['resources']:
            task['resources'].remove(id)
        if task.has_key('children'):
            children = task['children']
            if children:
                removeResourceFromTasks(children,id)