from flask import Flask, request,jsonify,send_file
import json
import apprentice_data_off

apprentice = Flask(__name__)

#read the data from the file
details_file_name = "Apprentices.json"
with open(details_file_name, 'r') as file:
    data = json.load(file)

#home page
@apprentice.route('/')
def home():
    # return "Hello World of Apprentices in BlueYonder"
    info = """
    <h1>Welcome to World of Apprentice in BlueYonder!</h1>
    <p>Here are the available routes:</p>
    <ul>
        <li><a href="/Blueyonderlogo">/Blueyonderlogo</a> - to display logo</li>
        <li><a href="/display_all_details/">/display_all_details/</a> - to display all the details of the apprentices</li>
        <li><a href="/display_specifc_details/?name=Username">/display_specifc_details/?name=UserNameHere</a> - to display details for a specific user</li>
        <li><a href="/membersinlocation/?location=UserLocation">/membersinlocation/?location=UserLocationHere</a> - to display members working in one location</li>
    </ul>
    """
    return info

@apprentice.route('/Blueyonderlogo', methods=['GET'])
def display_logo():
    image_path = "Blue_Yonder_logo.jpg"
    return send_file(image_path, mimetype='image/jpg')

@apprentice.route('/display_all_details/', methods=['GET'])
def display_all_details():
    return data

@apprentice.route('/display_specifc_details/', methods=['GET'])
def details_by_only_name_from_data():
    name_by_user = request.args.get('name')
    return_data = None
    for location, members in data["Apprentices"].items():
        for member in members:
            if member["name"] == name_by_user:
                # apprentice_data_off.display_genral_details(member)
                return_data = {
                    "Name": member["name"],
                    "Employee ID": member["employee_id"],
                    "Email": member["email"],
                    "Contact": member["contact"],
                    "Location": location
                }
                with open(f'{name_by_user}.txt','w')as writeinfile:
                    json.dump(return_data, writeinfile, indent=2)
                break
    if return_data is None:
        return_data = f'No information found for {name_by_user}'
    return {'Details': return_data}, 200

@apprentice.route('/membersinlocation/', methods=['GET'])
def details_of_name_from_location():
    names_list =[]
    location_by_user = request.args.get('location')
    for members in data["Apprentices"][location_by_user]:
        membsers_in_location_data = {
            "Name": members["name"],
            "employee_id": members["employee_id"]
        }
        names_list.append(membsers_in_location_data)
        with open(f'{location_by_user}.txt','w')as writeinfile:
            json.dump(names_list, writeinfile, indent=2)
    return {f'Member working in {location_by_user}': names_list},200

@apprentice.route('/addmember/', methods=['POST'])
def add_member():
    new_member_data = request.json  # Assuming the POST request contains JSON data with new member details
    # location = new_member_data.get('location')
    location ="hyderabad"
    if location not in data["Apprentices"]:
        data["Apprentices"][location] = []
    data["Apprentices"][location].append(new_member_data)
    
    with open(details_file_name, 'w') as file:
        json.dump(data, file, indent=4)
    
    return jsonify({"message": "New member added successfully"}), 201

if __name__ == "__main__":
    apprentice.run(debug=True)
