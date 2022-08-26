# Data to register_archive_format
# 1. Total number of votes cast
# 2. A list of candiates
# 3. % of votes each candidate won 
# 4. Total number of votes each candidate won 
# 5. Winner of the election base on popular 

import os 
import csv




file_to_load = os.path.join("resources", "election_results.csv")

# with open(file_to_load) as election_data:
#     print(election_data)

 #with open(file_to_load) as election_data
#     print(election_data)
   
   # Read and print csv file 
    
# with open(file_to_load, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(types(lines))

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the Election results and read the file 
with open(file_to_load) as election_data:

# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")


    file_reader = csv.reader(election_data)

    #for row in file_reader:
     #   print(row)
    headers = next(file_reader)
    print (headers)