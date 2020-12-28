# This is a sample Python script.
import csv

def update_users(first, last, newf, newl):
   counter = 0
   with open("users.csv", "w+") as mycsv :
       csvreader = csv.reader(mycsv)

       for(index, row) in enumerate(csvreader):
            print(row[0])
        #   csvwriter = csv.writer(mycsv)
            csvwriter = csv.writer(mycsv, delimiter=',')
            if first == row[0] and last == row[1] :
               row[0] = newf
               row[1] = newl
            #   csvwriter.writerow(row)
               counter+= 1

   return "Users updated: " +str(counter) +"."






print(update_users("Grace", "Hopper", "Hello", "World"))

print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
print("updates : " + str(update_users("Not", "Here", "Still not", "Here"))) # Users updated: 0.
