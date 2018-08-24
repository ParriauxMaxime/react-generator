class AST:
    """AST contains tree definition"""
    imports = list()
    definition = ""
    statics = list()
    properties = list()
    methods = list()
    fileScopeValue = list()

    def __init__(self):
        pass

    def addImport(self, name, fromFile):
        self.imports.append("import " + name + " from \"" + fromFile + "\";" )

    def addDefinition(self, name):
        self.definition = "class " + name + " extends Component"

    def addProperty(self, property, value):
        self.properties.append(f"\t{property} = {value};")

    def addStaticProperty(self, static, value):
        self.statics.append(f"\tstatic {static} = {value};") 
    
    def addMethod(self, method): 
        self.methods.append(f"\t{method}")

    def toString(self):
        return str("\n").join(self.imports) + "\n\n" + \
            str(self.definition) + " {\n" + \
            ((str("\n").join(self.statics) + "\n") if len(self.statics) > 0 else "") + \
            str("\n").join(self.properties) + "\n" + \
            str("\n").join(self.methods) + "}"