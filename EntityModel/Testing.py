from Task import Task
from CompositeTask import CompositeTask
from SimpleTask import SimpleTask
from Resource import Resource
from Schedule import Schedule
from Deliverable import Deliverable
import gn_fun

from datetime import datetime
import json


now = datetime.now()
date = "/".join([str(now.month), str(now.day), str(now.year)])
    
resource = Resource(gn_fun.getId(), "Anumeha", "labor")
deliverable = Deliverable(gn_fun.getId(), "deliverable", "file")

    
project = CompositeTask(gn_fun.getId(), 'myProject', date, 10, None, [], [], [], [], [resource],[deliverable])

childTask1 = CompositeTask(gn_fun.getId(), 'task1', date, 2, None, [], [], [], [], resource.id,None)
project.addChildTask(childTask1);

childTask2 = CompositeTask(gn_fun.getId(), 'task2', date, 2, None, [], [], [], [], resource.id,None)
project.addChildTask(childTask2);

project.generateSchedule()


with open('test.json', mode='w') as f:
    json.dump(project, f, default=gn_fun.jdefault, indent = 2)




