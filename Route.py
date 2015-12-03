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
	rname = request.args.get('resourceName')
	rdailycost = request.args.get('dailycost')
	rtype = request.args.get('resourceType')
	allocatedTasks = request.args.getlist('allocTask[]')
	return Controller.ResourceController.addResource(rname,rdailycost,rtype,allocatedTasks)

@app.route('/deliverable/addDeliverable')
def createDeliverable():
	dname = request.args.get('deliverableName')
	dtype = request.args.get('deliverableType')
	pid = request.args.get('pId')
	return Controller.ProjectController.createDeliverable(dname, dtype, pid)

@app.route('/task/addTask')
def createTask():
	name = request.args.get('taskName')
	duration = request.args.get('duration')
	tsktype = request.args.get('optTaskType')
	children = request.args.getlist('selChild[]')
	pred = request.args.getlist('selPred[]')
	succ = request.args.getlist('selSucc[]')
	resources = request.args.getlist('selRes[]')
	desc = request.args.get('taskDescription')
	parentId = request.args.get('parentId')
	deliverables = request.args.getlist('deliverables')
	return Controller.TaskController.createTask(name, duration, tsktype, children, pred, succ, resources, desc, parentId, deliverables)

@app.route('/resource/editResource')
def editResource():
	rid = request.args.get('resourceId')
	rname = request.args.get('resourceName')
	rdailycost = request.args.get('dailycost')
	rtype = request.args.get('resourceType')
	allocatedTasks = request.args.getlist('allocTask[]')
	return Controller.ResourceController.editResource(rid,rname,rdailycost,rtype,allocatedTasks)

@app.route('/task/editTask')
def editTask():
	id = request.args.get('taskId')
	name = request.args.get('taskName')
	duration = request.args.get('duration')
	tsktype = request.args.get('optTaskType')
	children = request.args.getlist('selChild[]')
	pred = request.args.getlist('selPred[]')
	succ = request.args.getlist('selSucc[]')
	resources = request.args.getlist('selRes[]')
	desc = request.args.get('taskDescription')
	parentId = request.args.get('parentId')
	deliverables = request.args.getlist('deliverables')
	return Controller.TaskController.editTask(id, name, duration, tsktype, children, pred, succ, resources, desc, parentId, deliverables)


if __name__ == '__main__':
    app.debug=True
    app.run()
