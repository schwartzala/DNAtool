# help prompt that shows command usage.
def print_help():
    print "[L]oad: Import a DNA or RNA sequence from file"
    print "[H]elp: Prompt usage script"
    print "[E]xit: Exit the program\n"

# run flag is used to see if the user wishes to continue using the application.
run = True
# show help prompt at the beginning for new users
print_help()
while run:
    # Request user to input a command.
    command = str(raw_input("Please enter a command: [L]oad / [H]elp / [E]xit\n")).lower()
    # If "e" or "exit", exit the program.
    if command == "e" or command == "exit":
        print "See you later! o/"
        run = False
    else:
        # If "h" or "help", show help prompt.
        if command == "h" or command == "help":
            print_help()
        else:
            # If "l" or "load", prompt user to entire file location.
            if command == "l" or command == "load":
                fileLoc = str(raw_input("Please enter the location of your DNA / RNA sequence file: "))
            # If command is not valid, inform the user and request another input.
            else:
                print command, "not a valid command! Please use one of the following:"
                print_help()
