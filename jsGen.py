from AST import AST

def componentGen(arg):
    ast = AST()
    name = arg.get("name", "componentName")
    ast.addImport("React, { Component }", "react")
    ast.addDefinition(name)
    ast.addProperty("state", "{}")
    ast.addMethod("constructor(props) {\n\t\tsuper(props);\n\t}\n")
    ast.addMethod("render() {\n\t\treturn (\n\t\t\t<div>\n\t\t\t\tdefault generation\n\t\t\t</div>\n\t\t);\n\t}\n")
    if (arg.get("proptypes") == True):
        ast.addImport("PropTypes", "prop-types")
        ast.addStaticProperty("propTypes", "{}")
    print("_______________________")
    print(ast.toString())
    print("_______________________")
    return ast