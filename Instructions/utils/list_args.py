import inspect, importlib, os, pkgutil

if __name__=="__main__":
    print(os.getcwd())

    commands = pkgutil.iter_modules(["./Instructions/commands"])

    

    module = importlib.import_module("./Instructions/commands/insert.py")
    print(module)