
python_folder = "D:\\Programs\\Python\\Python38-32"
python_executable = "python3.exe"


import os
try:
    from PIL import ImageGrab
except ImportError:
    os.system(python_folder+"\\"+python_executable+" -m pip install PIL")
    try:
        from PIL import ImageGrab
    except ImportError:
        input("Could not install PIL. Please install in manually for your version of python.")
        exit("")


import win32gui # ???