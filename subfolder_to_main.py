import shutil
import os
 
 
dest_dir = input("Input file directory: ")


walker = os.walk(dest_dir)
 
 
for data in walker:
    for files in data[2]:
        try:
            shutil.move(data[0] + os.sep + files, dest_dir)
            print("Moving files to ", dest_dir, "...")
            
        except shutil.Error:
            print("Transfer failed")
            continue

print("Done!")
 
