start_count = 0
stop_count = 0
user_input = "Kay"
print("(You may ask for help if you don't know what to do by typing 'help')")
while True:
    user_input = input("> ")

    if user_input.lower() == "help":
        print("""
        start - to start the car 
        stop - to stop the car 
        quit - to quit 
        """)

    elif user_input.lower() == "start":
        stop_count = 0
        while True:
            if start_count == 0:
                print("Car started... ")

            elif start_count > 0:
                print("Car has already started")
                break
            break
        start_count += 1

    elif user_input.lower() == "stop":
        start_count = 0
        while True:
            if stop_count == 0:
                print("Car stopped ")
            elif stop_count > 0:
                print("Car has already stopped!!!!!")
                break
            break
        stop_count += 1

    elif user_input.lower() == "quit":
        print("Operation Ended")
        break

    else:
        print("I don't understand ")