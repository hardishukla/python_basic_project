task=[] #adding empty list
while True: #choice loop
    choice =int(input("Enter your choice \n 1.Add task \n 2.Remove task \n 3. View task \n 4. Quit \n input: "))
    if choice==1: #newtask
        new_task=input("Enter task : ")
        task.append(new_task)
        print(f"{new_task} is added ;)")
    elif choice==2: #remove
        remove_task=input("Enter task : ")
        task.remove(remove_task)
        print(f"{remove_task} is removed successfully")
    elif choice==3:#view
        print(task)
    elif choice==4:#quit
        print("Quit")
        break 
    else:
        print("Invalid choice")
