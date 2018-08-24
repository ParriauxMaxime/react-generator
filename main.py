import sys
import jsGen

def parseBoolInput(input):
    return True if input == "Y" or input == "y" else False

def listCommand(): 
    print("Command: ")
    print("\tcomponent [name]")

def commandNotFound(arg):
    return "Error, command \"" + str(arg[1]) + "\" not found"

def createComponent(arg):
    pbi = parseBoolInput
    argName = "componentName"
    if (len(arg) > 2):
        argName = arg[2]
    name = input("Name [" + argName + "]:") or argName
    proptypes = pbi(input("proptypes [Y/n]:") or "Y")
    #styles = pbi(input("styles [Y/n]:") or "Y")
    #withTracker = pbi(input("Name [y/N]:") or "N")
    component = jsGen.componentGen({
        "name": name,
        "proptypes": proptypes,
     #   "styles": styles,
      #  "withTracker": withTracker
    })
    return ''     

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