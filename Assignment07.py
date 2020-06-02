# ------------------------------------------------- #
# Title: Assignment 07
# Description: Loads an ID and Name from file,
# and gives you the option to overwrite the content of the file with a new ID and Name
# ChangeLog: (Who, When, What)
# mkoj,6.1.2020,Created processing functions
# mkoj,6.1.2020,Created presentation functions
# mkoj,6.1.2020,Created main body of script
# ------------------------------------------------- #

import pickle  # This imports code from another code file

# Data -------------------------------------------- #
# Declare variables and constants
strFileName = "AppData.dat"
lstCustomer = []
strChoice = ""

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    pickle_out = open(file_name, "wb")
    pickle.dump(list_of_data, pickle_out)
    pickle_out.close()

def read_data_from_file(file_name):
    pickle_in = open(file_name, "rb+")
    data_from_file = pickle.load(pickle_in)
    pickle_in.close()
    return data_from_file

# Presentation ------------------------------------ #
def print_menu():
    print('''
            Options:
            1) See current data
            2) Overwrite with new data and save to file
            3) Exit
            ''')
    print()  # Add an extra line for looks

def collect_user_data():
    id = input("ID: ").strip()
    name = input("Name: ").strip()  # adds inputs to task and priority key
    id_name_lst = [id, name] # saves local variables to a list
    return id_name_lst  # return data as a list object

def input_menu_choice():
    choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
    print()  # Add an extra line for looks
    return choice

# Main body of script ----------------------------- #
# Read data from file, and if the file doesn't exist, print a message
try:
    lstCustomer = read_data_from_file(strFileName)
except:
    print("No existing data in file \"AppData.dat\"")

# Print menu until option 3 is selected
while(True):
    print_menu()
    strChoice = input_menu_choice()
    if strChoice.strip() == '1': # Option 1: See current data
        print("ID: " + lstCustomer[0]) # Prints information from lstCustomer cleanly
        print("Name: " + lstCustomer[1]) # Prints information from lstCustomer cleanly
    elif strChoice.strip() == '2': # Option 2: Overwrite with new data and save to file
        lstCustomer = collect_user_data() # Get ID and NAME From user, then store it in a list object
        save_data_to_file(strFileName, lstCustomer) # Stores the list object in a binary file
    elif strChoice.strip() == '3': # Option 3: Exit
        input("Press [ENTER] to exit.")
        break
    else: # Catches invalid menu responses
        print("Invalid selection, press [ENTER] to continue.")






