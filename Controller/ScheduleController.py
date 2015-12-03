from EntityModel.CompositeTask import CompositeTask
from EntityModel.SimpleTask import SimpleTask
from EntityModel.Schedule import Schedule
from flask import Flask, jsonify, request
import main_func
import json
import os.path
import sys
import datetime
import Queue

schedule = []
taskList = {}

def generateSchedule(project_start_date):
	
	project_json = None
	#taskList = None
	taskResourceDict = {}
	global schedule
	global taskList

 	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'r') as inFile:
		project_json = json.load(inFile);
	
	if project_json.has_key('schedule'):
		project_json['schedule'] = None
	project_json['date'] = project_start_date
	taskList = project_json['children']
	projectStartDate = project_json['date']
	dateFormat = "%d-%m-%Y"
	startDate = getDateFromString(projectStartDate, dateFormat)
	projectStartDate2 = getStringFromDate2(startDate)
	taskQueue = Queue.Queue()

	for task in taskList:
		
		if not task['pred']:
			taskQueue.enqueue(task)
			#print 'inside first if...................'
			if not taskResourceDict: #first task with no pred
				#print 'inside second if...................'
				task['date'] = projectStartDate
				task['date2'] = projectStartDate2
				endDate = startDate + datetime.timedelta(days=int(task['duration']))
				task['end_date1'] = getStringFromDate1(endDate, dateFormat)
				taskResourceDict[task['id']] = {'Resources':task['resources'], 'Duration':task['duration'], 'Start_date':task['date'], 'End_date':task['end_date1']}
				#print taskResourceDict[task['id']]['Resources']
				task['end_date2'] = getStringFromDate2(endDate)
				schedule.append({"title":task['name'], "start":task['date2'], "end":task['end_date2']})
			else: #following tasks with no pred
				tempPredTask = ''
				maxDate = datetime.datetime(1900, 01, 01)
				for taskId in taskResourceDict:
					if(commonResourceExist(task['resources'], taskResourceDict[taskId]['Resources'])):
						#print "!!!!!!!!!!!!!!Hello !!!!!!!!!!!!!!"
						taskDate = getDateFromString(taskResourceDict[taskId]['End_date'], dateFormat)
						#print taskDate
						if taskDate > maxDate:
							maxDate = taskDate
							tempPredTask = taskId
				
				if(maxDate == datetime.datetime(1900, 01, 01)):
					maxDate = getDateFromString(projectStartDate, dateFormat) - datetime.timedelta(days=1)

				#print maxDate
				task['date'] = getStringFromDate1(maxDate + datetime.timedelta(days=1), dateFormat)
				task['date2'] = getStringFromDate2(maxDate + datetime.timedelta(days=1))
				endDate = maxDate + datetime.timedelta(days=1) + datetime.timedelta(days=int(task['duration']))
				task['end_date1'] = getStringFromDate1(endDate, dateFormat)
				taskResourceDict[task['id']] = {'Resources':task['resources'], 'Duration':task['duration'], 'Start_date':task['date'], 'End_date':task['end_date1']}
				task['end_date2'] = getStringFromDate2(endDate)
				schedule.append({"title":task['name'], "start":task['date2'], "end":task['end_date2']})
		else:
			pass

	getSchedule(taskQueue)
	project_json['schedule'] = schedule
	with open(os.path.join(sys.path[0]+'/static/data', 'Project.json'), 'w') as outFile:
		json.dump(project_json, outFile)
				
	return json.dumps(schedule)


'''
Definition for all the successor nodes
'''
def getSchedule(taskQueue):
	print taskQueue
	global schedule
	global taskList
	while (taskQueue.size() > 0):
		print "In Task Queue 1......."
		currTask = taskQueue.dequeue()
		#print currTask['succ']
		taskResourceDict = {}
		currTaskSTartDateString = currTask['end_date1']
		print currTaskSTartDateString
		dateFormat = "%d-%m-%Y"
		print dateFormat
		currTaskSTartDate = getDateFromString(currTaskSTartDateString, dateFormat)       
		myList = currTask['succ']
		print myList
		for taskId in myList:
			print taskId
			task = findTask(taskId, taskList)
			print task
			taskQueue.enqueue(task)

			if not taskResourceDict: #first task with no pred
				print 'inside second if...................'
				taskStartDate = currTaskSTartDate + datetime.timedelta(days=1)
				task['date'] = getStringFromDate1(taskStartDate, dateFormat)
				task['date2'] = getStringFromDate2(taskStartDate)
				endDate = taskStartDate + datetime.timedelta(days=int(task['duration']))
				task['end_date1'] = getStringFromDate1(endDate, dateFormat)
		
				taskResourceDict[task['id']] = {'Resources':task['resources'], 'Duration':task['duration'], 'Start_date':task['date'], 'End_date':task['end_date1']}
				#print taskResourceDict[task['id']]['Resources']
				task['end_date2'] = getStringFromDate2(endDate)
				schedule.append({"title":task['name'], "start":task['date2'], "end":task['end_date2']})
		
			else: #following tasks with no pred
				tempPredTask = ''
				maxDate = datetime.datetime(1900, 01, 01)
				for taskId in taskResourceDict:
					if(commonResourceExist(task['resources'], taskResourceDict[taskId]['Resources'])):
						#print "!!!!!!!!!!!!!!Hello !!!!!!!!!!!!!!"
						taskDate = getDateFromString(taskResourceDict[taskId]['End_date1'], dateFormat)
						#print taskDate
						if taskDate > maxDate:
						    maxDate = taskDate
						    tempPredTask = taskId

				if(maxDate == datetime.datetime(1900, 01, 01)):
					maxDate = currTaskSTartDate

				#print maxDate
				task['date'] = getStringFromDate1(maxDate + datetime.timedelta(days=1), dateFormat)
				task['date2'] = getStringFromDate2(maxDate + datetime.timedelta(days=1))
				endDate = maxDate + datetime.timedelta(days=1) + datetime.timedelta(days=int(task['duration']))
				task['end_date1'] = getStringFromDate1(endDate, dateFormat)
				taskResourceDict[task['id']] = {'Resources':task['resources'], 'Duration':task['duration'], 'Start_date':task['date1'], 'End_date':task['end_date']}
				task['end_date2'] = getStringFromDate2(endDate, dateFormat)
				schedule.append({"title":task['name'], "start":task['date2	'], "end":task['end_date2']})
		'''
        for each in myList:
            print "Inside for loop"
            print taskId
            task = findTask(taskId, taskList)
            print task
            taskQueue.enqueue(task)
            
            if not taskResourceDict: #first task with no pred
                #print 'inside second if...................'
                taskStartDate = currTaskSTartDate + datetime.timedelta(days=1)
                task['date'] = getStringFromDate(taskStartDate, dateFormat)
                endDate = taskStartDate + datetime.timedelta(days=int(task['duration']))
                task['end_date'] = getStringFromDate(endDate, dateFormat)
                
                taskResourceDict[task['id']] = {'Resources':task['resources'], 'Duration':task['duration'], 'Start_date':task['date'], 'End_date':task['end_date']}
                #print taskResourceDict[task['id']]['Resources']
                schedule.append({"title":task['name'], "start":task['date'], "end":task['end_date']})
                
            else: #following tasks with no pred
                tempPredTask = ''
                maxDate = datetime.datetime(1900, 01, 01)
                for taskId in taskResourceDict:
                    if(commonResourceExist(task['resources'], taskResourceDict[taskId]['Resources'])):
                        #print "!!!!!!!!!!!!!!Hello !!!!!!!!!!!!!!"
                        taskDate = getDateFromString(taskResourceDict[taskId]['End_date'], dateFormat)
                        #print taskDate
                        if taskDate > maxDate:
                            maxDate = taskDate
                            tempPredTask = taskId

                if(maxDate == datetime.datetime(1900, 01, 01)):
                    maxDate = currTaskSTartDate

                #print maxDate
                task['date'] = getStringFromDate(maxDate + datetime.timedelta(days=1), dateFormat)
                endDate = maxDate + datetime.timedelta(days=1) + datetime.timedelta(days=int(task['duration']))
                task['end_date'] = getStringFromDate(endDate, dateFormat)
                taskResourceDict[task['id']] = {'Resources':task['resources'], 'Duration':task['duration'], 'Start_date':task['date'], 'End_date':task['end_date']}
                schedule.append({"title":task['name'], "start":task['date'], "end":task['end_date']})
	'''
				
	return json.dumps(schedule)




def commonResourceExist(list1, list2):
	
	for eachElement in list1:
		if eachElement in list2:
			return True
		else:
			pass
	return False

def getDateFromString(strDate, dateFormat):
	return datetime.datetime.strptime(strDate, dateFormat)
	
	
def getStringFromDate1(date, dateFormat):
	return date.strftime(dateFormat)

def getStringFromDate2(date):
	return date.strftime('%Y-%m-%d')

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





			

	

	
