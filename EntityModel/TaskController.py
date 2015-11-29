from EntityModel.CompositeTask import CompositeTask
from EntityModel.SimpleTask import SimpleTask
from EntityModel.Deliverable import Deliverable
from flask import Flask, jsonify, request
import main_func
import json

def createTask(json_request):
	name = json_request['name']
	desc = json_request['desc']
	date = json_request['date']
	duration = json_request['duration']
	type = json_request['type']
	parentId = json_request['parentId']
	pred = json_request['pred']
	succ = json_request['succ']
	resources = json_request['resources']
	deliverables = json_request['deliverables']
	
	

	if(type == "simple"):
	    newTask = SimpleTask(main_func.getId(), name, desc, date, duration, pred, succ, resources,deliverables)
	else:
	    startTask = json_request['startTask']
	    finalTasks = json_request['finalTasks']
	    newTask = CompositeTask(main_func.getId(), name, desc, date, duration, startTask, finalTasks, pred, succ, [], resources, deliverables)
	
	if(parentId in main_func.project_objects):
	    parentTask = main_func.project_objects[parentId]
	    parentTask.addChildTask(newTask)
	
    
	main_func.project_objects[newTask.id] = newTask
	
	newTask_json = main_func.jdefault(newTask)
	return json.dumps(newTask_json, default=main_func.jdefault, indent = 2)