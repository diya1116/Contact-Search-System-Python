import contacts as contacts 


def get_contact(contact):

    target = contact.lower()
    found = False

    for var_name, var_value in vars(contacts).items():
        
       
        if not var_name.startswith("__") and isinstance(var_value, list):
            
            lowercase_list = [c.lower() for c in var_value]
            
            if target in lowercase_list:
                print(f"Found '{contact}' in the list named: {var_name}")
                found = True

    if not found:
        print(f"The contact '{contact}' is not in any list.")


def find_contact(contact, list_name):
   
    target = contact.lower()
    
    
    specific_list = getattr(contacts, list_name, None)

    
    if specific_list is None or not isinstance(specific_list, list):
        print(f"Error: Could not find a list named '{list_name}'. Check your spelling!")
        return 

    
    lowercase_list = [c.lower() for c in specific_list]

    if target in lowercase_list:
        print(f" '{contact}' is in the '{list_name}' list.")

    else:
        print(f" '{contact}' is NOT in the '{list_name}' list.")

def get_list(list_name):

    target = list_name.lower()

    found_list = getattr(contacts,target,None)

    if isinstance(found_list, list):
        print(f"Here is the list : \n{list_name} : {found_list}")

    else : 
        print(list_name, "is not in the file")        


    
def main_menu():

    while True :
        print("Contact Search")
        print("\n")
        print("1. find contact")
        print("2. find contact in specific list")
        print("3. find list")
        print("4. exit")

        choice = input("\nEnter your choice: ")
        
        if choice == "1" :
            contact = input("Enter a contact that you want to find : ")
            get_contact(contact)

        if choice == "2":
            contact = input("Enter a contact that you want to find : ")
            list_name = input("Enter a list you want to find that contact : ")
            find_contact(contact,list_name)
            
        if choice == "3":
            list_name = input("Enter a list that you want to find : ")
            get_list(list_name)

        if choice == "4":
            print("Exit the menu")
            break

main_menu()