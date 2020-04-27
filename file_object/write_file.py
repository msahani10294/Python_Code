with open("text.txt", "r") as f:
    f_content = f.read()

    with open("new_text.txt", "w") as new_f:
        new_f.write(f_content)