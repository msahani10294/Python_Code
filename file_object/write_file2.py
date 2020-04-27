with open("file.txt", "w")as f:

    for i in range(10):
        f.write("this is line no {}\n".format(i))