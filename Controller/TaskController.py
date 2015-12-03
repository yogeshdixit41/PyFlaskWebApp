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

	if children:
		taskList = project_json['children']
		newTask_json['children'] = [task for task in taskList if task['id'] in children]
		project_json['children'] = [task for task in taskList if task['id'] not in children]

	project_json['children'].append(newTask_json);

	if resources:
		resList = project_json['resources']
		for resource in resList:
			if resource['id'] in resources:
				resource['allocTasks'].append(newTask.id)

	if pred:
		taskList = project_json['children']
		for task in taskList:
			if task['id'] in pred:
				task['succ'].append(newTask.id)

	if succ:
		taskList = project_json['children']
		for task in taskList:
			if task['id'] in succ:
				task['pred'].append(newTask.id)

	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
		json.dump(project_json, outFile)

	return json.dumps(project_json, default=main_func.jdefault, indent = 2)

def editTask(id, name, duration, tsktype, children, pred, succ, resources, desc, parentId, deliverables):

	project_json = None
 	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'r') as inFile:
		project_json = json.load(inFile);

	taskList = project_json['children']
	old_task = findTask(id,taskList)

	if(tsktype == "SimpleTask"):
	    newTask = SimpleTask(id, name, desc, old_task['date'], duration, pred, succ, resources, deliverables)
	else:
	    startTask = None
	    finalTasks = []
	    if old_task.has_key('startTask'):
	    	startTask = old_task['startTask']
	    if old_task.has_key('finalTasks'):
	    	finalTasks = old_task['finalTasks']
	    newTask = CompositeTask(id, name, desc, old_task['date'], duration, startTask, finalTasks, pred, succ, [], resources, deliverables)
	
	newTask_json = main_func.jdefault(newTask)
	if old_task.has_key('children'):
		if (tsktype == "CompositeTask"):
			newTask_json['children'] = [task for task in old_task['children'] if task['id'] in children]
			taskList.extend([task for task in old_task['children'] if task['id'] not in children])

		else:
			taskList.extend([task for task in old_task['children']])

	if children:
		newTask_json['children'].extend([task for task in taskList if task['id'] in children])
		taskList = [task for task in taskList if task['id'] not in children]

	resList = project_json['resources']
	for resource in resList:
		if resource['id'] in resources and id not in resource['allocTasks']:
			resource['allocTasks'].append(id)
		elif resource['id'] not in resources and id in resource['allocTasks']:
			resource['allocTasks'].remove(id)

	for task in taskList:
		if task['id'] in pred and id not in task['succ']:
			task['succ'].append(id)
		elif task['id'] not in pred and id in task['succ']:
			task['succ'].remove(id) 

	for task in taskList:
		if task['id'] in succ and id not in task['pred']:
			task['pred'].append(id)
		elif task['id'] not in succ and id in task['pred']:
			task['pred'].remove(id)

	replaceTask(id,taskList,newTask_json)

	project_json['children'] = taskList
	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
		json.dump(project_json, outFile)

	return json.dumps(project_json, default=main_func.jdefault, indent = 2)	

def findTask(id,taskList):
	for task in taskList:
		if task['id'] == id:
			return task
		if task.has_key('children'):
			children = task['children']
			if children:
				tsk = findTask(id,children)
				if tsk is not None:
					return tsk
	return None

def replaceTask(id,taskList,newTask):
	for task in taskList:
		if task['id'] == id:
			taskList.remove(task)
			taskList.append(newTask)
			print newTask
			return
		if task.has_key('children'):
			children = task['children']
			if children:
				replaceTask(id,children,newTask)

def removeTask(tid):

    project_json = None
    with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'r') as inFile:
		project_json = json.load(inFile)
					
    predSuccList = None
    removeAllocTasks(project_json, tid)
    
    predSuccList = getPredSucc(project_json, tid )
    	
    if(predSuccList != None):
        successors = predSuccList['successors'] 
        predecessors = predSuccList['predecessors']
        for successor in successors:
            setPred(project_json, successor,predecessors, tid)
        for pred in predecessors:
        	setSucc(project_json, pred, successors, tid)


    with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
        json.dump(project_json, outFile, indent = 2)

    return json.dumps(project_json, default=main_func.jdefault, indent = 2)
    

#this function removes the task from the resource's allocated task list
def removeAllocTasks(json_data, taskId):
    
    for resource in json_data['resources']:

        if(resource['allocTasks'] != None):
            if(taskId in resource['allocTasks']):
                resource['allocTasks'].remove(taskId)
                
    

#this function get the predecessors and successors of the task to be removed and also remove the task from project_json
def getPredSucc(json_data, taskId):
    predSuccList = None

    for task in json_data['children']:
        if(taskId == task['id']):
        	predSuccList = {"predecessors" : [], "successors" : []}
         	if(task['succ'] != None):
        		predSuccList['successors'] = task['succ']
         	if(task['pred'] != None):
        		predSuccList['predecessors'] = task['pred']
         	json_data['children'].remove(task)
         	return predSuccList
               
        if task.has_key('children'):
        	children = task['children']
        	if children:
        		predSuccList = getPredSucc(task,taskId)
        		if predSuccList != None:
        			return predSuccList
        print taskId
    return None
                
                

#This function set the predecessors  of deleted task as the predecessors of the deleted task's successors
def setPred(json_data, successor, predecessors, oldId):
    found = None
    if(json_data['id'] == successor):
        
        for predecessor in predecessors:
            json_data['pred'].append(predecessor)
            json_data['pred'].remove(oldId)
        found = 1
        return found
        
            	
    else:
        if(json_data.has_key('children')):
            for child in json_data['children']:
        	    found = setPred(child, successor, predecessors, oldId)
        	    if(found != None):
        	        return found

def setSucc(json_data, pred, successors, oldId):
    found = None
    if(json_data['id'] == pred):
        
        for successor in successors:
            json_data['succ'].append(successor)
            json_data['succ'].remove(oldId)
        found = 1
        return found
        
            	
    else:
        if(json_data.has_key('children')):
            for child in json_data['children']:
        	    found = setSucc(child, pred, successors, oldId)
        	    if(found != None):
        	        return found