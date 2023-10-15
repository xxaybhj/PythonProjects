import sys,shelve


try:
    shelfFile = shelve.open('toDo')
    if sys.argv[1].lower() == 'add':
        while True:
            taskname = input("Task name : ")
            if taskname.strip() != '':
                break
        taskDescription = input("Description : ")

        shelfFile[taskname] = taskDescription
    elif sys.argv[1].lower() == 'list':
        for todo in shelfFile.keys():
            print(f"{todo} : {shelfFile[todo]}")
    elif sys.argv[1].lower() in ['delete','complete']:
        while True:
            taskname = input("Task name : ")
            if taskname.strip() != '':
                break
        if taskname not in shelfFile.keys():
            print("Task doesn't exist")
        else:
            del shelfFile[taskname]
            print("Task Completed !")
    shelfFile.close()
except:
    raise Exception("py toDo.py <keyword> ex:add | list | delete/complete")
