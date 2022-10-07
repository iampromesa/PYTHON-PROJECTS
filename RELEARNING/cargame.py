command = ""
started = False

while True: #command != "quit"
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Vroom!! Car Started!")
    elif command == "stop":
        if not started:
            print("Car had already been stopped")
        else:
            started = False
            print("Skrr!!! Car Stopped!")
    elif command == "help":
        print("""
start - to start the car 
stop - to stop the car
help - for help 
""")
    elif command == "quit":
        break
    else:
        print("Sorry i don't understand! you can type 'help' for more help")
