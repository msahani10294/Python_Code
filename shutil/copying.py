import os, shutil

# this function helps to copy one file from one location to another
shutil.copy("demo1/sample1.py", "demo2")


# this function helps to copy one folder from one location to another
shutil.copytree("demo1", "demo3")