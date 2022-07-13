import importlib.util
import sys, subprocess

libraries = ['pandas', 'opencv-python', 'pillow', 'tk', 'matplotlib']
names = ['pandas', 'cv2', 'PIL', 'tk', 'matplotlib',]

for i, name in enumerate(names) :

    if name in sys.modules:
        print(f"{name!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(name)) is not None:
        # If you choose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        print(f"{name!r} has been imported")
    else:
        #index.append(i)
        print(f"can't find the {name!r} module")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', libraries[i]])

print("All packages and libraries needed are imported/installed !")