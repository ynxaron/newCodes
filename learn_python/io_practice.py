import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("The file does not exist")
