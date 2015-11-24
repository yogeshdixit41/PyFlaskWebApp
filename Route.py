import os
from flask import Flask, jsonify, render_template, request
import flask

app = Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template('main_page.html', method=['POST'])

@app.route('/project/newProject')    
def createProject():
	pname = request.args.get('pname')
	pdate = request.args.get('date')
	return jsonify(project_name=pname,project_date=pdate)

@app.route('/resource/addResource')
def createResource():
	rname = request.args.get('resourceName')
	rdailycost = request.args.get('dailycost')
	rtype = request.args.get('resourceType')
	rallocatedtasks = request.args.get('allocTask')
	return jsonify(resource_name=rname,resource_dailycost=rdailycost,resource_type=rtype,resource_allocated_tasks=rallocatedtasks)

@app.route('/deliverable/addDeliverable')
def createDeliverable():
	dname = request.args.get('deliverableName')
	dtype = request.args.get('deliverableType')
	return jsonify(deliverable_name=dname,deliverable_type=dtype)

@app.route('/task/addTask')
def createTask():
	tname = request.args.get('taskName')
	tduration = request.args.get('duration')
	ttype = request.args.get('optTaskType')
	tpredecsr = request.args.get('selPred')
	tsucesr = request.args.get('selSucc')
	tres = request.args.get('selRes')
	tdesc = request.args.get('taskDescription')
	return jsonify(task_name=tname,task_dur=tduration,task_type=ttype,task_pred=tpredecsr,task_succ=tsucesr,task_res=tres,task_desc=tdesc)

if __name__ == '__main__':
    app.debug=True
    app.run()
