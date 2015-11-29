import uuid

mainProject = ""
project_objects = {}

def getId():
    return str(uuid.uuid4().fields[-1])[:5]
    
def jdefault(o):
    return o.__dict__