import sys

def parseBoolInput(input):
    return True if input == "Y" or input == "y" else False

def listCommand(): 
    print("Command: ")
    print("\tcomponent: ")

def commandNotFound(arg):
    return "Error, command \"" + str(arg[1]) + "\" not found"

def createComponent(arg):
    pbi = parseBoolInput
    name = input("Name :")
    proptypes = pbi(input("proptypes [Y/n]:") or "Y")
    styles = pbi(input("styles [Y/n]:") or "Y")
    withTracker = pbi(input("Name [y/N]:") or "N")     
    return ({
        "name": name,
        "proptypes": proptypes,
        "styles": styles,
        "withTracker": withTracker
    })

def main():
    arg = sys.argv
    if len(arg) >= 2:
        firstArg = arg[1]
        switcher = {
            "component": createComponent,  
        }
        answer = switcher.get(str(firstArg), commandNotFound)(arg)
        print(answer)
    else:
        listCommand()

if __name__ == "__main__":
    main()