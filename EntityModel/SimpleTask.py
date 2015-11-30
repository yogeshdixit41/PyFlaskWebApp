from Task import Task
class SimpleTask(Task):
    
<<<<<<< HEAD
    def __init__(self, id, name, desc, date, duration, startTask, finalTasks, pred, succ, resources, deliverables):
    	Task.__init__(self, id, name, desc, date, duration, pred, succ, resources, deliverables)
=======
    def __init__(self, id, name, date, duration, startTask, finalTasks, pred, succ, resources, deliverables):
    	Task.__init__(self, id, name, date, duration, pred, succ, resources, deliverables)
>>>>>>> 9c3fda21d46de340bec3860c7ebd12809cc7709a
        pass 
        
    def setTaskInfo(self, info):
        pass
        
    def getTaskInfo(self):
        pass

    def newtask(self, taskInfo):
        pass

        