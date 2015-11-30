from Task import Task
class SimpleTask(Task):
    
    def __init__(self, id, name, desc, date, duration,  pred, succ, resources, deliverables):
    	Task.__init__(self, id, name, desc, date, duration, pred, succ, resources, deliverables)
        pass 
        
    def setTaskInfo(self, info):
        pass
        
    def getTaskInfo(self):
        pass

    def newtask(self, taskInfo):
        pass

        