import os
from flask import Flask, jsonify, render_template, request
import flask
import Controller.ProjectController
import Controller.ResourceController
import Controller.TaskController


app = Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template('main_page.html', method=['POST'])

@app.route('/project/newProject')    
def createProject():
	#request = {'pname':'Naman Ojha', 'date':4}
	pname = request.args.get('pname')
	pdate = request.args.get('date')
	return Controller.ProjectController.createProject(pname, pdate)
	#return jsonify(project_name=pname,project_date=pdate)

@app.route('/resource/addResource')
def createResource():
    return Controller.ResourceController.addResource(request.json)
	#rname = request.args.get('resourceName')
	#rdailycost = request.args.get('dailycost')
	#rtype = request.args.get('resourceType')
	#rallocatedtasks = request.args.get('allocTask')
	#return jsonify(resource_name=rname,resource_dailycost=rdailycost,resource_type=rtype,resource_allocated_tasks=rallocatedtasks)

@app.route('/deliverable/addDeliverable')
def createDeliverable():
	dname = request.args.get('deliverableName')
	dtype = request.args.get('deliverableType')
	pid = request.args.get('pId')
	Controller.ProjectController.createDeliverable(dname, dtype, pid)
	return jsonify(deliverable_name=dname,deliverable_type=dtype, project_id=pid)

@app.route('/task/addTask')
def createTask():
	name = request.args.get('taskName')
	duration = request.args.get('duration')
	tsktype = request.args.get('optTaskType')
	children = request.args.get('selChild')
	pred = request.args.get('selPred')
	succ = request.args.get('selSucc')
	resources = request.args.get('selRes')
	desc = request.args.get('taskDescription')
	parentId = request.args.get('parentId')
	deliverables = request.args.get('deliverables')
	return Controller.TaskController.createTask(name, duration, tsktype, children, pred, succ, resources, desc, parentId, deliverables)
	#tname = request.args.get('taskName')
	#tduration = request.args.get('duration')
	#ttype = request.args.get('optTaskType')
	#tpredecsr = request.args.get('selPred')
	#tsucesr = request.args.get('selSucc')
	#tres = request.args.get('selRes')
	#tdesc = request.args.get('taskDescription')
	#return jsonify(task_name=tname,task_dur=tduration,task_type=ttype,task_pred=tpredecsr,task_succ=tsucesr,task_res=tres,task_desc=tdesc)
	

if __name__ == '__main__':
    app.debug=True
    app.run()
