# kwargs is keyboard length argument
# type of kwargs is dictionary

def students(**kwargs):

    for key, val in kwargs.items():
        # print ("%s == %s" %(key, val))
        print("{} {}".format(key, val))


students(first_name="manoj", last_name = "sahani", age=5)
students(first_name="Rohit", last_name = "kumar", age=5)
students(first_name="Abhishek", last_name = "yadav", age=5)
