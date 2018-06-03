import os

# Change to some directory
os.chdir("/Users/noorulainnoor/projects/Shell")
# print the current working directory
cwd = os.getcwd()
#print(cwd)
# List the contents of current working directoy
#print os.listdir(cwd)
status = os.system('echo hello')
print status
print type(status)
# print Environment
#print(os.environ['PATH'])

print("#######")
#print os.environ

# set some environment variable
os.environ['USMAN'] = cwd
#print(os.environ['USMAN'])

