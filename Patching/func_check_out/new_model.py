from subprocess import check_output

def checking():
    return check_output(["dir"]).split()

# print(checking())