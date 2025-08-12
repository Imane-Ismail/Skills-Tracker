# check_users_module.py
import importlib, pprint, sys, traceback

try:
    m = importlib.import_module('app.routes.users')
    print("MODULE FILE:", getattr(m, '__file__', None))
    print("MODULE ATTRS:")
    pprint.pprint([n for n in dir(m) if not n.startswith('__')])
except Exception:
    print("IMPORT ERROR:")
    traceback.print_exc()
print("\nFirst entries of sys.path:")
pprint.pprint(sys.path[:6])
