from abc import ABCMeta, abstractmethod
class Task(object):
    __metaclass__ = ABCMeta

<<<<<<< HEAD
    def __init__(self, id, name, desc, date, duration, pred, succ, resources, deliverables):
    	self.id = id
        self.name = name
        self.desc = desc
=======
    def __init__(self, id, name, date, duration, pred, succ, resources, deliverables):
    	self.id = id
        self.name = name
>>>>>>> 9c3fda21d46de340bec3860c7ebd12809cc7709a
        self.date = date
        self.duration = duration
        self.pred = pred
        self.succ = succ
        self.resources = resources
        self.deliverables = deliverables
    
    @abstractmethod    
    def setTaskInfo(self, info):
        pass
        
    @abstractmethod    
    def getTaskInfo(self):
        pass
        
    @staticmethod 
    def removeTask(task):
        pass
        
    def setDuration(self):
        pass
        
    def removeResource(self, resource):
        pass
        
    def addResource(self, resource):
        pass

    @abstractmethod
    def newtask(self, taskInfo):
        pass
        
    def generateSchedule(self):
        pass
        
    
        

        

  
        
    