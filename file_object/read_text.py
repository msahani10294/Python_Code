with open("text.txt", 'r') as read_file:
    f_content = read_file.readlines()

    for lines in f_content:
        print(lines, end="")