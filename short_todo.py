tasks=[]
while True:
    print("\n To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("\n Options:")      
    print("1. Add Tasks")
    print("2. Remove Task")
    print("3. Exit")

    choice = input("Choosse an option:")

    if choice == "1":
        task = input("Enter task:")
        tasks.append(task)
    elif choice == "2":
       try:
           task_num = int(input("enter task number to remove:"))
           tasks.pop(task_num -1)
       except:
           print("Invalid number")
    elif choice =="3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")

