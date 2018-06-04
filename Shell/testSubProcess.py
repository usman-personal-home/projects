import subprocess
import os

# Actually changes the current working directory
cwd = os.getcwd()
#print(cwd)

# Changes the directory and issues ls inside the directory and returns the command status
#status = subprocess.call('cd ~;ls -al', shell=True)


# execute shell script with stdout
subprocess.call('sh echo.sh',shell=True)

# execute shell script with stdout
subprocess.call('sh echo.sh  > /dev/null 2>&1',shell=True)

subprocess.Popen()