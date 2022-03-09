import os
os.chdir("/home/parallels/Desktop/")
os.mkdir("/home/parallels/Desktop/created_folder")
with open("/home/parallels/Desktop/created_folder/created_file.txt", mode="w+") as file:
    mytext = file.write("Hello, we found vulnerability in your computer \n That is why we're here")
    file.close()

