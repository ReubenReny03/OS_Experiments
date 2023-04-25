import os
while True:
    print("1.add new dir    2. Create File  3. Remove   4.Search    5.Display   6.Exit")
    user = int(input("What u want buddy: "))
    path = "Ex_9_folder/" # need to change depending on the system 
    if user == 1:
        new_dir = input("Dir name: ")
        os.mkdir(path + new_dir) # make a new dir
        print("Made a new folder named "+new_dir)
    if user == 2:
        dir = input("Dir name: ")
        if os.path.exists(path + dir): # check if folder exist 
            print("dir varified")
            file = input("File name: ")
            content = input("Content: ")
            with open(path + f"{dir}/" + file, 'w') as file: # make a file and add content
                file.write(f"{content}")
    if user == 3:
        dir = input("Dir name: ")
        if os.path.exists(path + dir): # check if folder exist 
            print("dir verified")
            file = input("file name: ")
            if os.path.exists(path + dir + f"/{file}" ):
                print("file found")
                os.remove(path + dir + f"/{file}" )
                print("file removed")
    if user == 4:
        dir = input("Dir name: ")
        if os.path.exists(path + dir): # check if folder exist 
            print("dir verified")
            file = input("file name: ")
            if os.path.exists(path + dir + f"/{file}" ):
                print("file found")
    if user == 5:
        files = os.listdir(path) # show the list of things in the dir
        for x in files:
            print(x)
    if user == 6:
        break


    
    







