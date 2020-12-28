

file = open("story.txt")
#print(file.read())
#cursor goes to the end
file.seek(0)
#print(file.read())
file.seek(50)
#print(file.read())
file.readline()
print(file.readline())

print(file.closed)
file.close()
print(file.closed)


with open("story.txt") as f:
    data = f.read()

print(f.closed) #True
print(data)

f.__exit__()


with open("haiku.txt", "w") as f2 :
    f2.write("hello\n")
    f2.write("you\n")

# file modes default r, "w" for write, will overwrite
f.close()

with ("story.txt") as f1:
    data = f1.read()
with ("story_copy.txt", "w") as f3 :
    f3.write(data)
