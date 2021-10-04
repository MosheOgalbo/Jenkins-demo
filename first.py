import pathlib 
file = pathlib.pathlib("file.txt")
if not file.exists():
    with open("file.txt","w") as file:
        file.write("first name :moshe\n")
        file.write("last name :ogalbo\n")
        file.write("city : tv \n")
else:
    exit(1)