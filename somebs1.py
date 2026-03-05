

user_command =""
while user_command != "quit":
    user_command = input("enter command: ")
    if user_command.lower()=="help":
        print("start- to start the car\nstop- to stop the car\nquit- to quit the program ")
    elif user_command.lower()=="start":
        print("car started-ready to go")
    elif user_command.lower()=="stop":
        print("car stopped")
    else:
        print("command not recognized")
