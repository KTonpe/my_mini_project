import json
import string
import random

#globally stored the name of file
apperentice_file_path ='Apprentices.json'
#store the json data from file in DETAILS and retun deatils
def get_data():
    
    with open(apperentice_file_path, 'r') as f:
        details = json.load(f)
    # print(json.dumps(details, indent=4))
    return details

#globally stored the data , other functions can use it
data = get_data()


#1. to print all the data from a file having json file
def display_all_data():
    print('You have choosed to display all data \n')
    print(json.dumps(data, indent=4))
    

#2. print apprentice names of given location
def display_name_of_apperentice_of_location():
    print('You have choosed to display all members name working at specified location \n') 
    #hyd = data["Apprentices"]["Hyderabad"]

    location_user = input(f"Please enter location only from {list(data['Apprentices'].keys())} : ").lower()
    while location_user not in data["Apprentices"].keys():
        location_user =input(f'Enter a valid location from {data["Apprentices"].keys()} : ').lower()
        continue
    else:
        print(f'Members at the location :{location_user}')
        for members in data["Apprentices"][location_user]:
            print(members["name"])

# template to print the general details of the apprentice
def display_genral_details(member):
    print("Name:", member["name"])
    print("Employee ID:", member["employee_id"])
    print("Email:", member["email"])
    print("Contact:", member["contact"])
    print()

#get data of a specific apprentice by only specifying name
def details_by_only_name_from_data():
    name_by_user = input('Enter name of apprentice : ')
    # print(f'{name_by_user} works at {location_by_user}')
    while True:
        found = False
        for location, members in data["Apprentices"].items():
            for member in members:
                # print(type(member))
                if name_by_user == members[0]:
                    print(f'{name_by_user.upper()} works at {location}')
                    display_genral_details(member)
                    found = True
                    break  # Exit the inner loop once the member is found
            if found:
                break  # Exit the outer loop once the member is found
        if found:
            break  # Exit the while loop once the member is found


#get data of a specific apprentice by name and location
def details_of_name_from_data(name_by_user,location_by_user):
    # print(f'{name_by_user} works at {location_by_user}')

    for members in data["Apprentices"][location_by_user]:
        if name_by_user == members["name"]:
            display_genral_details(members)

#to create a employee ID  used in get_employee_detail function
def genereate_employee_id():
    random_digits = ''.join(random.choices(string.digits, k=7))
    new_employee_id = 'a'+ random_digits

    for locations,members in data["Apprentices"].items():
       for member in members:
         if new_employee_id != member['employee_id']:  
             return new_employee_id 
    else : genereate_employee_id()

    
# to create a new apprentice employee with name and contact information
def get_employee_details():
    new_member_name = input('Enter a name of new employee: ').lower()
    #to replace space by . Therefore used .replace builtin functon of CLASS STRING
    email = f'{new_member_name.replace(" ", ".")}@jda.com'
    employee_id = genereate_employee_id()
    contact = input('Enter a contact of new employee: ')
    while len(contact) != 10:
        contact = input('Enter a 10 digit contact number of new employee: ')
        continue
    else: 
        new_member_details = {
        "name": new_member_name,
        "employee_id": employee_id,
        "email": email,
        "contact": contact }
        return new_member_details

#to updat into a file 
def write_to_file(updated_json_data):
    with open('Apprentices.json', 'w') as file:
        file.write(updated_json_data)

def add_member_into_existing_data():
    print('You\'ve choosed to Add an employee: \n')
    #check location
    location_by_user = input(f'Enter a location: from {list(data["Apprentices"].keys())} : ')
    while location_by_user not in data["Apprentices"].keys():
        location_by_user =input(f'Enter a valid location from {list(data["Apprentices"].keys())} : ').lower()
        continue
    else: 
        # new_member = get_employee_details()
        data["Apprentices"][location_by_user].append(get_employee_details())
        updated_json_data = json.dumps(data, indent=2)
        write_to_file(updated_json_data)

# delete a member from location and employee id
def delete_employee_by_id():
    print('You\'ve choosed Delete an employee: \n')
    #check location
    location_by_user = input(f'Enter a location: from {list(data["Apprentices"].keys())} : ')
    while location_by_user not in data["Apprentices"].keys():
        location_by_user =input(f'Enter a valid location from {list(data["Apprentices"].keys())} : ').lower()
        continue
    else:
    #check employee id
        apprentice_ID = {}
        for member in data["Apprentices"][location_by_user]:
            apprentice_ID.update({member["name"]:member["employee_id"]})
        employee_id_by_user = input(f'Enter an employee ID: from {list(apprentice_ID.items())} : ')
        while employee_id_by_user not in apprentice_ID.values():
            employee_id_by_user = input(f'Enter an employee ID: from {list(apprentice_ID.items())} : ')
            continue
        else:
            for member in data["Apprentices"][location_by_user]:
                if employee_id_by_user == member["employee_id"]:
                    data["Apprentices"][location_by_user].remove(member)
                    updated_json_data = json.dumps(data, indent=2)
                    write_to_file(updated_json_data)
                    break

# to check the location and name of the member present or not and called details function
def search_name_from_data():
    print('You\'ve choosed a name to search: \n')
    apprenitce_name_at =[]
    location_by_user = input(f'Enter location from {list(data["Apprentices"].keys())} : ').lower()
    while location_by_user not in data["Apprentices"].keys():
        location_by_user =input(f'Enter a valid location from {list(data["Apprentices"].keys())} : ').lower()
        continue
    else: 
        for members in data["Apprentices"][location_by_user]:
            apprenitce_name_at.append(members["name"]) 
        # print(apprenitce_name_at)
        name_by_user = input(f'Enter the name from the list {apprenitce_name_at}: ')
        while name_by_user not in apprenitce_name_at:
            name_by_user = input(f'Enter the name from the list {apprenitce_name_at}: ')
            continue
        else: 
            return details_of_name_from_data(name_by_user,location_by_user)

#to ask data from the user
def ask_data_to_change():
    dictionary_keys = ['name', 'employee_id', 'email', 'contact']
    user_data = { }
    for keys in dictionary_keys:
        user_data[keys] = input(f'Enter the value in {keys} : ').lower()
    return user_data

#to chanege details like name/contact/id/contact
def change_data():
    print('You\'ve choosed to change the details of a member \n')
    employee_id = input('Enter an Employee ID: ')
    for location, members in data['Apprentices'].items():
        for member in members:
            if member['employee_id'] == employee_id:
                new_data = ask_data_to_change()
                for key, value in new_data.items():
                    member[key] = value
                print(f"Data for employee with ID '{employee_id}' updated successfully.")
    
    else: print(f"No employee found with ID '{employee_id}'.")
    updated_json_data = json.dumps(data, indent=2)
    write_to_file(updated_json_data)

#to cahnge the location of a member by ID
def move_to_location():
    print('You\'ve choosed to cahnge the location of a member by ID')
    employee_id = input('Enter an employee ID: ').lower().strip()
    new_location = input('Enter a location to change: ').lower().strip()
    if new_location in data['Apprentices']:
        for location, employees in data['Apprentices'].items():
            for employee in employees:
                if employee['employee_id'] == employee_id:
                    data['Apprentices'][new_location].append(employee)
                    employees.remove(employee)
                    updated_json_data = json.dumps(data, indent=2)
                    write_to_file(updated_json_data)
                    print(f"Employee with ID '{employee_id}' moved to '{new_location}' successfully.")
                    return
        print(f"No employee found with ID '{employee_id}'.")
    else:
        print(f"Location '{new_location}' does not exist.")     

if __name__ == '__main__':

    menu = {
    '1': display_all_data,
    '2': display_name_of_apperentice_of_location,
    '3': details_by_only_name_from_data,
    '4': search_name_from_data,
    '5': add_member_into_existing_data,
    '6': change_data,
    '7': delete_employee_by_id,
    '8': move_to_location,
    '9': exit     #builtin function
    }

    while True:
        print('''
                Menu:
                       1. Display all details
                       2. Get names of working member by location 
                       3. get details of a specific member
                       4. get details only by name of the  member
                       5. Add member into a existing location
                       6. Update specific member's details 
                       7. Delete a member
                       8. Move a specific member to a specific location
                       9. exit
                    
                    ''')
        choice = input('Enter your choice: ')
        if choice in menu:
            menu[choice]()
        else:
            print('Invalid choice')