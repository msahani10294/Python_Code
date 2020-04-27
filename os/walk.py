import os

os.chdir(r"C:\Users\msaha\PycharmProjects\python_practice\os")
for folder, subfolder, files in os.walk(os.getcwd()):
    print("=========printing folder==========")
    print(folder)

    print("-----subfolder----")
    for sub_folder in subfolder:
        print(subfolder)
    print(".........files......")
    for file in files:
        print(file)