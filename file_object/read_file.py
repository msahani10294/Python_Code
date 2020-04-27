with open("text.txt", "r") as f:
    f_content = f.read(10)
    print(f_content)
    f.seek(0)

    f_content = f.read(10)
    print(f_content)