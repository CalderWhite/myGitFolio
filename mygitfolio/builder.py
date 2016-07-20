from mygitfolio import builder
import sys, os
def gitfolio(cmds,dash,ddash):
    """main file\n--help for help"""
    if len(ddash) > 0:
        if ddash[0] == "--help":
            funcs.pop(funcs.index("check_commands"))
            for i in funcs:
                if i[0:2] != "__" and i != "builder" and i != "os" and i != "sys":
                    print(i + ":")
                    print(" " + funcCalls.__getattribute__(i).__doc__)
                    print("----------")
        else:
            try:
                eval(cmds[0] + "(" + str(cmds[1:]) + "," + str(dash) + "," + str(ddash) + ")")
            except NameError:
                raise Exception("No such command as " + cmds[0])
    else:
        try:
            eval(cmds[0] + "(" + str(cmds[1:]) + "," + str(dash) + "," + str(ddash) + ")")
        except NameError:
            raise Exception("No such command as " + cmds[0])     
def build_package(cmds,dash,ddash):
    """by default, this will build for the current user's oauth_token only\n
    options:\n
    --name : custom group build is activated, and build wil build a gitfolio for all the PUBLIC repos to the input name
    --private : custom build activated, custom build requires a full api url and oauth token (when --private)
    """
    if len(ddash) > 0:
        for i in ddash:
            if i == "--name":
                if len(cmds) < 1:
                    print("not enough arguments given!")
                else:
                    print("building...")
                    print(builder.custom_group_build(cmds[0]))
    pass
def authenticate(cmds,dash,ddash):
    """this will retrive your oauth_token, so you may run gitfolio commands"""
    if os.path.exists(os.getcwd() + "\\mygitfolio"):
        os.chdir(os.getcwd() + "\\mygitfolio")
    # this is just so when the program is compiled we don't run into any errors
    builder.build_auth(useWebBrowser=True)
    pass
def check_commands(args):
    commands = []
    options1 = []
    options2 = []
    for i in args:
        if i.find("--") > -1:
            options2.append(i)
        elif i.find("-") > -1:
            options1.append(i)
        else:
            commands.append(i)
    try:
        eval(commands[0] + "(" + str(commands[1:]) + "," + str(options1) + "," + str(options2) + ")")
    except NameError:
        raise Exception("No such command as " + commands[0])
if __name__ == '__main__':
    sys.path.append(os.getcwd() + "gitfolio.py")
    import gitfolio as funcs
    import gitfolio as funcCalls
    funcs = dir(funcs)
    args = [sys.argv[0].split(".")[0]]
    for i in sys.argv[1:]:
        args.append(i)
    check_commands(args)
    
