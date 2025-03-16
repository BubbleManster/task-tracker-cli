import getopt, sys, json

with open("tasks.json", "r")  as tasks:
    tasks = json.load(tasks)['tasks']

argumentList = sys.argv[1:]

# Long options
long_options = ["add=", "update=", "delete=", "mark-in-progress=", "mark-done=", "list="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, "", long_options)
    
    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument == "--add":
            print ("Added: " + currentValue)
            
        elif currentArgument == "--update":
            print ("Displaying file_name:", sys.argv[0])
            
        elif currentArgument == "--delete":
            print (("Enabling special output mode (% s)") % (currentValue))
            
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
