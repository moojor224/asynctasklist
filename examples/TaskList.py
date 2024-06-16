# this file was copid from the readme example

from asynctasklist import TaskList, Task
import time

tasks = TaskList()

# template function to return a new instance of a function
def makeTask(timeout, callback):
    startTime = 0 # initialize startTime variable

    def init():
        nonlocal startTime
        startTime = round(time.time() * 1000) # set the start time to the time when this task is first run

    def task():
        if round(time.time() * 1000) - startTime >= timeout: # check if timeout duration has passed
            callback() # run some code
            return True # return True since to task is done
        return False # return False since to task is not done
    return Task(init=init, task=task) # return a new task

# define callback function
def run():
    print("timeout is done")
    pass

# add a new task to the list
tasks.add(makeTask(1000, run)) # print message after 1 second
tasks.add(makeTask(2000, run)) # print message after 2 seconds

# if you want to run the tasklist truly asynchronously, run a new thread before the main program loop
import threading
def task_worker():
    while True:
        tasks.execute()

t = threading.Thread(target=task_worker, daemon=True) # set daemon to true to stop thread when program ends
t.start()
# main program loop
while True:
    # run main app code
    # app.run() # example
    # update gui
    # gui.update() # example

    # run the tasklist
    # tasks.execute() # this is for verifying the tasklist works without getting the main program loop stuck in an infinite loop
    if tasks.isDone():
        print("all tasks are done")
        break
    pass


