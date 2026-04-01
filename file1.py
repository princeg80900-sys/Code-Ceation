#create a file and write data into it
file = open("demo_file.txt", "w")
file.write("hello! this is first line of the file.\n")
file.write("this is second line of the file.\n")
file.close()
print("file created successfully")
print("Data written successfully")


#open the file aand read the data from it
file = open("demo_file.txt", "r")
print(file.read())
file.close()
print("Data read successfully")

#open file and overwrite the data in the file
file = open("demo_file.txt","w")
file.write("this is new data in the file.\n")
file.close()
file = open("demo_file.txt", "r")
print(file.read())
file.close()
print("file overwritten successfully")

#open file and append data to the file
file = open("demo_file.txt", "a")                   
file.write("this is appended data in the file.\n")
file.close()

#open updated file and read the data from it
file = open("demo_file.txt", "r")
print(file.read())
file.close()
print("Data appended successfully")
