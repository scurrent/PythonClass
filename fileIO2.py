with open("story.txt") as f1:
    data = f1.read()

with open("story_copy.txt", "w") as f3:
    f3.write(data)

with open("story.txt") as f1:
    data = f1.read()
    with open("story_reverse.txt", "w") as back_file :
        for line in reversed(data) :
            back_file.write(line)




def find_and_replace(file, name1, name2):
#    with open(file, "r+") as file1 :
#        data2 = file1.read()
#        data2.replace(name1, name2)
#        file1.write(data2)

# Read in the file
    with open(file, 'r') as file1:
        filedata = file1.read()

    # Replace the target string
    filedata = filedata.replace(name1, name2)

    print(type(filedata))
    # Write the file out again
    with open(file, 'w') as file1:
        file1.write(filedata)





find_and_replace("story1.txt", "Shane", "MikeD")