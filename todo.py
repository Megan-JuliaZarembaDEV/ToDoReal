# todo.py

# Step 1: Start with an empty list to hold tasks
task = []

# Step 2: Add a task
def add_task(task):
    task.append(task)

# Step 3: View tasks
def view_tasks():
    for i in task in enumerate(task,start=1):
        print(f"{i}. {task}")

# Step 4: Delete a task
def delete_task(index):
    task = task.pop(index)
    print(f"Deleted:{task}")    
    
    #   for i in task in enumerate(task,start=1):
    #     if i=="done":
    #         tasks=tasks.pop(task)


# Step 5: Mark task complete





# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    view_tasks()
    delete_task(0)
    # mark_complete(0)
    # view_tasks()
    # save_t