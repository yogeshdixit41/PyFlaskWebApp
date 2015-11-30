from EntityModel.CompositeTask import CompositeTask
from EntityModel.SimpleTask import SimpleTask
from EntityModel.Deliverable import Deliverable
from flask import Flask, jsonify, request
import main_func
import json
import os.path
import sys

def createTask(name, duration, tsktype, children, pred, succ, resources, desc, parentId, deliverables):
	

	if(tsktype == "SimpleTask"):
	    newTask = SimpleTask(main_func.getId(), name, desc, None, duration, pred, succ, resources, deliverables)
	else:
	    startTask = None
	    finalTasks = []
	    newTask = CompositeTask(main_func.getId(), name, desc, None, duration, startTask, finalTasks, pred, succ, [], resources, deliverables)
	
	if(parentId in main_func.project_objects):
	    parentTask = main_func.project_objects[parentId]
	    parentTask.addChildTask(newTask)

	newTask_json = main_func.jdefault(newTask)
	project_json = None
 	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'r') as inFile:
		project_json = json.load(inFile);
		project_json['children'].append(newTask_json);

	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
		json.dump(project_json, outFile)

	#main_func.project_objects[newTask.id] = newTask	
	return json.dumps(project_json, default=main_func.jdefault, indent = 2)