import getopt, sys, json, datetime, re

with open("tasks.json", "r")  as tasklist:
    tasks = json.load(tasklist)

argumentList = sys.argv[1:]

# Long options
long_options = ["add=", "update=", "delete=", "mark-in-progress=", "mark-done=", "list="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, "", long_options)
    
    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument == "--add":
            id = len(tasks["tasks"])+1
            tasks["tasks"].append({
                "id": id,
                "desc": currentValue,
                "status": "todo",
                "createdAt": datetime.datetime.now().isoformat(),
                "updatedAt": datetime.datetime.now().isoformat()
            })
            print ("Added:", currentValue, f"(I.D. {id})")
            
        elif currentArgument == "--update":
            exp = re.split("(?<=\\d)(?=\\D)", currentValue)
            if len(exp) == 2:
                id, val = exp
                id = int(id)
                val = val.strip()
            else:
                print("Invalid use. Check the README.")
                exit()
            index_of_id = next((i for i, item in enumerate(tasks["tasks"]) if item["id"] == id), None)
            try:
                tasks["tasks"][index_of_id]["desc"] = val
                tasks["tasks"][index_of_id]["updatedAt"] = datetime.datetime.now().isoformat()
                print ("Updated:", val, f"(I.D. {id})")
            except TypeError:
                print("An item with that I.D. does not exist.")
                exit()
            
        elif currentArgument == "--delete":
            id = int(currentValue)
            index_of_id = next((i for i, item in enumerate(tasks["tasks"]) if item["id"] == id), None)
            try:
                tasks["tasks"].pop(index_of_id)
                print ("Deleted:", f"I.D. {id}")
            except TypeError:
                print("An item with that I.D. does not exist.")
                exit()
        
        elif currentArgument == "--mark-done":
            id = int(currentValue)
            index_of_id = next((i for i, item in enumerate(tasks["tasks"]) if item["id"] == id), None)
            try:
                tasks["tasks"][index_of_id]["status"] = "done"
                print ("Marked:", f"I.D. {id}", "as done.")
            except TypeError:
                print("An item with that I.D. does not exist.")
                exit()
        
        elif currentArgument == "--mark-in-progress":
            id = int(currentValue)
            index_of_id = next((i for i, item in enumerate(tasks["tasks"]) if item["id"] == id), None)
            try:
                tasks["tasks"][index_of_id]["status"] = "in-progress"
                print ("Marked:", f"I.D. {id}", "as in progress.")
            except TypeError:
                print("An item with that I.D. does not exist.")
                exit()

        elif currentArgument == "--list":
            if currentValue == "all":
                for item in tasks["tasks"]:
                    print(f'{item["desc"]}: {item["status"]}')
            elif currentValue == "todo":
                for item in tasks["tasks"]:
                    if item["status"] == "todo":
                        print(f'{item["desc"]}: {item["status"]}')
            elif currentValue == "done":
                for item in tasks["tasks"]:
                    if item["status"] == "done":
                        print(f'{item["desc"]}: {item["status"]}')
            elif currentValue == "in-progress":
                for item in tasks["tasks"]:
                    if item["status"] == "in-progress":
                        print(f'{item["desc"]}: {item["status"]}')
            else:
                print("Not a valid flag.")
                exit()
            
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

with open("tasks.json", "w")  as tasklist:
    json.dump(tasks, tasklist, indent=4) 