# Task 3: Task Scheduler Simulation 


tasks_definitions = [  
("T1", "Compile Code", 1, []),  
("T2", "Run Unit Tests", 2, ["T1"]),  
("T3", "Generate Report", 3, ["T2"]),  
("T4", "Deploy Artifacts", 2, ["T1"]), # Another task dependent on T1  
("T5", "Urgent Patch", 0, []), # Highest priority  
]

# 1. Initialize Task Queue: Create a list task_queue from tasks_definitions. 

task_queue = tasks_definitions.copy()


# 2. Sort Task Queue: Sort the task_queue based on priority (lowest number first).

task_queue = sorted(task_queue, key=lambda x: x[2])

# 3. Process Tasks

completed_tasks = []

print("\nTask Processing")

for task in task_queue:
    task_id, description, priority, dependencies = task

    if all(dep in completed_tasks for dep in dependencies):
        print(f"Processing {task_id} - {description}")
        completed_tasks.append(task_id)
    else:
        print(
            f"Skipping {task_id}. Dependencies not met: {dependencies}"
        )

print("\nCompleted:", completed_tasks)

# 4. Add High Priority Task

new_task = ("T6", "Emergency DB Backup", 0, [])
task_queue.insert(0, new_task)

print("\nQueue After Adding T6:")
for task in task_queue:
    print(task)


    # 5. Reverse Processing


reverse_queue = sorted(tasks_definitions, key=lambda x: x[2])
reverse_queue.reverse()

print("\nReverse Order Processing")

while reverse_queue:
    task = reverse_queue.pop()
    print(task[0], "-", task[1])


    # 6. Analyze Priorities


priorities = [task[2] for task in tasks_definitions]

print("\nPriority Analysis")
print("Min:", min(priorities))
print("Max:", max(priorities))
print("Sum:", sum(priorities))
