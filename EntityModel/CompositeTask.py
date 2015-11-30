
from Task import Task
from Schedule import Schedule
class CompositeTask(Task):
    
<<<<<<< HEAD
    def __init__(self, id, name, desc, date, duration, startTask, finalTasks, pred, succ, children, resources, deliverables):
    	Task.__init__(self, id, name, desc, date, duration, pred, succ, resources, deliverables)
=======
    def __init__(self, id, name, date, duration, startTask, finalTasks, pred, succ, children, resources, deliverables):
    	Task.__init__(self, id, name, date, duration, pred, succ, resources, deliverables)
>>>>>>> 9c3fda21d46de340bec3860c7ebd12809cc7709a
    	self.children = children
        self.startTask = startTask
        self.finalTasks = finalTasks
        
        
    def setTaskInfo(self, info):
        pass
        
    def getTaskInfo(self):
        pass

    def newtask(self, taskInfo):
        pass
        
    def setFinalTask(self, taskInfo):
        pass
        
    def testing(self):
        return "Testing pass"
    
    def addChildTask(self, task):
        self.children.append(task)
        
    def generateSchedule(self):
        self.schedule = Schedule.entry
        
<<<<<<< HEAD
    def addResource(self, resource):
        self.resources.append(resource)
        
    def addDeliverable(self, deliverable):
        self.deliverables.append(deliverable)
        
=======
>>>>>>> 9c3fda21d46de340bec3860c7ebd12809cc7709a
#test = CompositeTask(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
#test.testing()
        
         
