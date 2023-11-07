import importlib.util
import sys

# Define the module name and the path to the file.
module_name = 'dijkstra'
folder_path = 'dsacw/clrsPython/Chapter 22'  # Adjust this path if necessary

# For Python 2.7, use .format() or concatenation to construct file_path
file_path = '{}/{}.py'.format(folder_path, module_name)

# Create a module spec (Python 3 code, won't work in Python 2.7)
# spec = importlib.util.spec_from_file_location(module_name, file_path)

# For Python 2.7, we'll have to do this another way:
# Insert the folder path to the system path list
sys.path.insert(0, folder_path)

# Now you can import the module using the __import__ function
dijkstra = __import__(module_name)

# Remove the folder path from sys.path if you want to ensure it does not affect future imports
sys.path.pop(0)

# Now you can use the module's functions
# For example:
# result = dijkstra.some_function(arguments...)
wq