#Laila Kersh 
#1.19.2024
#To-DO Lists: Countries to Visit

myList = ["Mexico", "Japan", "France", "Brazil", "Morocco", "Australia"]


#Functions



def viewList(): 
    print("List name: Country Bucketlist")
    print(myList)
def exitList():
    print("Goodbye.")
def toDoList():
    print("Welcome to To-Do List!")
    print("Please pick an option: \nA. View List  \nB. Edit List  \nC. Exit")
    option = input(print("Option: "))
    if option == "A":
        viewList()
    elif option == "B": 
        print("List Name: Country Bucketlist")
        action = input(print("Pick Action: \ni. Add \nii. Remove \niii. Mark as Complete \niv. Sort Alphabetically \nv. Remove All Tasks \nvi. Number of Tasks"))
        if action == "i":
            myList.append(input("Add task to list: "))
            print(myList)
        elif action == "ii": 
            delete = input(print("What do you wish too remove?: "))
            if delete == "Mexico":
                myList.pop(0)
                print(myList)
            elif delete == "Japan":
                myList.pop(1)
                print(myList)
            elif delete == "France":
                myList.pop(2)
                print(myList)
            elif delete == "Brazil":
                myList.pop(3)
                print(myList)
            elif delete == "Morocco":
                myList.pop(4)    
                print(myList)
            elif delete == "Australia":
                myList.pop(5)
                print(myList)
        elif action == "iii":
           ans = int(input(print("Enter task to mark as complete(0-5): ")))
           x = myList.index(ans)
           myList[x] = ans + "X"
           print(myList)
        elif action == "iv": 
            myList.sort()
            print(myList)
        elif action == "v":
            myList.clear()
            print(myList)
        elif action == "vi":
            print(len(myList))
        else: 
            done = input(print("Would you like to exit this list?: \na. Exit \nb. View"))
            if done == "a":
                exitList()
            elif done == "b":
                viewList()
    elif option == "C":
        exitList()
    
#Main
toDoList()
