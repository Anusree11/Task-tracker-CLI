import sys
import json
import os
from datetime import datetime

FILE_NAME= "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def add_task(description):
    
    tasks= load_tasks()
    task = { "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%M-%D %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%M-%D %H:%M:%S")}
    
    tasks.append(task)
    save_tasks(tasks)
    print("Task added succesfully")
    print("Task saved succesfully")




    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def update_tasks(task_id, new_description):
    tasks = load_tasks()
    for task in tasks :
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().strftime("%y-%m-%D %h:%m:%S")
            save_tasks(tasks)
            print("Updated succesfully")
            return
    
    print("Id not found")



def delete_tasks(task_id):
    tasks= load_tasks()
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted succesfully")
            return
        
    print("Id not found")

def mark_in_progress(task_id):
    tasks= load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "In progress"
            task["updatedAt"] = datetime.now().strftime("%y-%m-%D %H:%M:%S")
            print("Status updated to In progress")
            save_tasks(tasks)
            return
        
    print("Id not found")

def list_all():
    tasks= load_tasks()

    for task in tasks:
        print(task)
        return
    print("No data found")

def list_status(status):
    tasks =load_tasks()
    for task in tasks:
        if task["status"] == status:
            print(task)
            return
    print("No data found")


            
        

    
    
def main():
    
    print("Welcome to the task tracker")
    print("Arguments received", sys.argv)

    command = sys.argv[1]
    
    

    if command == "add":

        if len(sys.argv) < 3:
            print("Add proper task/description")
        else:
            description = sys.argv[2]
            add_task(description)

    if command == "update":
        task_id = int(sys.argv[2])
        new_description = sys.argv[3]

        update_tasks(task_id, new_description)


    if command == "delete":
        task_id = int(sys.argv[2])

        delete_tasks(task_id)

    if command == "mark-in-progress":
        task_id = int(sys.argv[2])
        
        mark_in_progress(task_id)

    if command == "list" and len(sys.argv) == 2:
            list_all()
    
    elif command == "list" and len(sys.argv) > 2:
            
            status = sys.argv[2]
            list_status(status)
        

        

    



if __name__ =="__main__":
    main()
