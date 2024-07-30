# asynctasklist

[![PyPI](https://img.shields.io/pypi/v/asynctasklist.svg)](https://pypi.org/project/asynctasklist/)
[![Tests](https://github.com/moojor224/asynctasklist/actions/workflows/test.yml/badge.svg)](https://github.com/moojor224/asynctasklist/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/moojor224/asynctasklist?include_prereleases&label=changelog)](https://github.com/moojor224/asynctasklist/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/moojor224/asynctasklist/blob/main/LICENSE)

a simple tasklist library for running tasks asynchronously or synchronously

## Installation

Install this library using `pip`:
```bash
pip install asynctasklist
```

## Basic TaskList Usage

```python
from asynctasklist import TaskList, Task
import time

# initialize the tasklist variable
tasks = TaskList()

# template function to return a new task
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
def message():
    print("timeout is done")
    pass

# add a new task to the list
tasks.add(makeTask(1000, message)) # print message after 1 second
tasks.add(makeTask(2000, message)) # print message 2 seconds after the first message
pt = ParallelTask()
pt.add(makeTask(1000, message))
pt.add(makeTask(2000, message))
tasks.add(pt) # print message 1 second and 2 seconds after second message

# the timeline for the above tasklist would be as follows:
# wait 1sec --> message1 --> wait 2sec --> message2 --> wait 1sec --> message3 --> wait 1sec --> message3

# if you want to run the tasklist asynchronously, call the start_async method
tasks.start_async()

# alternatively, you can run the tasklist in a thread if you want more control
task_thread = tasks.start_async_thread()


# if you want to run the tasklist alongside your main program, simply put `tasks.execute()` in the main program loop
# main program loop
while True:
    # run main app code
    app.run() # example code
    # update gui
    gui.update() # example code

    # run the tasklist
    tasks.execute()
    if tasks.isDone():
        print("all tasks are done")

```

 - notes:
   - lambdas can be used in place of functions for inline task initialization
 - ParallelTasks function the same as TaskLists, but instead of running the task one at a time in the order they were added, it runs all tasks at the same time.
   - it is recommended to have a check at the beginning of each task in a ParallelTask to make sure work needs to be done before running the task in case some tasks take longer to finish than the others


## how to build locally
```bash
git clone https://github.com/moojor224/asynctasklist.git
cd asynctasklist
python3 -m pip wheel ./
```