import os,ctypes,sys
import subprocess
from shutil import copyfile
import time

#if run on windows adminsitrator privilages are needed
if sys.platform.startswith("win"):
    if not ctypes.windll.shell32.IsUserAnAdmin():
        os.system('powershell -Command "Start-Process python {} -Verb RunAs"'.format(os.path.basename(__file__)))
        sys.exit(0)

#check python version
py_version = sys.version.split(" ")[0].split(".")
if py_version[0] == "3":
    if int(py_version[1]) < 8:
        print("python version: {}, ok".format(".".join(py_version)))
    else:
        print("Error: python version: {}, not compatible. Try a python version between 3.5.x - 3.7.x".format(".".join(py_version)))
        x = input("press key to exit")
        sys.exit(0)

else:
    print("Error: python version: {}, not compatible. Try a python version between 3.5.x - 3.7.x".format(".".join(py_version)))
    x = raw_input("press key to exit")
    sys.exit(0)

#make notebook output folder
subprocess.run("mkdir output", cwd = os.path.join(os.getcwd(),"Notebooks"))

#cmake commands
#platform dependend commands
subprocess.run("mkdir build",shell=True,cwd=os.path.join(os.getcwd(), "cmake_program"),stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
pip_command = "-m pip install"
cmake_command1 = os.path.join(os.getcwd(), "cmake_program","build")
cmake_command2 = '-DCMAKE_CXX_COMPILER=g++ -DCMAKE_C_COMPILER=gcc -DCMAKE_BUILD_TYPE=Release ../'
if sys.platform.startswith("win"):
    pip_command = "python " + pip_command
    cmake_command = 'cmake -G "MinGW Makefiles" ' + cmake_command2
    make_command = "mingw32-make"
elif sys.platform.startswith("linux"):
    pip_command = "python3 " + pip_command
    cmake_command =  'cmake ' + cmake_command2
    make_command = "make install"
else:
    print("Error: Only available on windows and linux")
    x = input("press key to exit")
    sys.exit(0)

#__________________________________________________
if sys.platform.startswith("win"):
    subprocess.run(cmake_command,shell=True,cwd=cmake_command1,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
subprocess.run(cmake_command,shell=True,cwd = cmake_command1)
subprocess.run(make_command,shell=True,cwd=cmake_command1)

try:
    copyfile(os.path.join(os.getcwd(),"cmake_program","build","lib","libNuclF1F2.so"),
    os.path.join(os.getcwd(),"cmake_program","build","bin","libNuclF1F2.so"))
except:
    print("Error: libNuclF1F2.so could not be copied")
    x = input("press key to exit")
    sys.exit(0)

#__________________________________________________
os.system(pip_command + " --upgrade pip")
os.system(pip_command + " jupyterlab")
os.system(pip_command + " numpy")
os.system(pip_command + " scipy")
os.system(pip_command + " -U matplotlib")
os.system(pip_command + " ipywidgets")
os.system(pip_command + " ipython")
os.system(pip_command + " ipywidgets")
os.system(" ".join(pip_command.split(" ")[:2]) + " jupyter nbextension enable --py widgetsnbextension")

x = input("press key to exit")
