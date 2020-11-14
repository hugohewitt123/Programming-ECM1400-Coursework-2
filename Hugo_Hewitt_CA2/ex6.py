"""A module to help organise a queue at a dental clinic"""
queue = ["David", "Matt"]
def arrival(name):
    '''A function to add a patient to the queue'''
    queue.append(name)
    return queue

def next_patient(position=1):
    '''A function to return the patient in a postition in the queue'''
    position -= 1
    patient = (queue.pop(position))
    return patient

print(next_patient(1))
print(arrival("Ronaldo"))
