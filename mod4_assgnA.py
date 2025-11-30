
#first import pickle and create database list
import pickle 
def main():
    database = {}
    #open database in reading bytes mode&set restrictions
    try: 
        src_file = open("database.pickle", "rb")
        database = pickle.load(src_file)
    except:
        print("File does not exist.")

    #Create menu & print
    print(database)
    menu = {}
    menu['1']="Add Name." 
    menu['2']="=Delete Name."
    menu['3']="Lookup Name"
    menu['4']="Exit"
    menu['5']="Change Name"
    while True: 
        options=menu.keys()

        print("Select 1 for Adding Name")
    
        print("Select 2 for Deleting Name.")

        print("Select 3 for Looking Up Name.")

        print("Select 4 for Changing Name.")

        print("Select 5 for Exiting Program.")

        selection= input("Please Select:") 
    #Use if else statement & add restrictions to go through list of options for user
        if selection =='1': 
            name = input("Enter Users Name to add: ")
            email = input("Enter Users email to add: ")
            database[name]=email 
        elif selection == '2': 
            name = input("Enter Name for Deletion : ")
            database.pop(name)
        elif selection == '3':
            name = input("Lookup Users Name : ")
            print(database[name])
        elif selection == '4':
            name = input("Change Users Name : ")
            keepEmail = database[name]
            new_name = input("Enter New Name : ")
            database.pop(name)
            database[new_name]= keepEmail
        elif selection == '5': 
            break
    else: 
        print ("Unknown Option Selected!")
    #use print function so user is able to see list of options
    print(database)
    #use try, except statement to open destined file and pickle it.
    try: 
        dest_file = open("database.pickle", "wb")
        pickle.dump(database, dest_file)
    except:
        print("File does not exist.")

    
if __name__ == "__main__":
    main()