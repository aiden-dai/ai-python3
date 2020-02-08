import os

#pwd = os.path.abspath(".")
#fname = os.path.join(pwd, "test.txt")
fname = "test.txt"
with open(fname, "w") as file:
    file.write('Hello\n')
    file.write('World')


with open(fname, 'r') as file:

    """
    # Note that it’s already possible to iterate on file objects using for line in file: ... without calling file.readlines().
    lines = file.readlines()
    for l in lines:
        print(l)
    """

    for l in file:
        print(l.rstrip('\n'))
    
    

