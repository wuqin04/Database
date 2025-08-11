import string
import json
from email_validator import validate_email, EmailNotValidError

# store single client information only, do not do any json file handling here
class Client(object):
    def __init__(self, name: str, gmail: str, source: str):
        self.name = name
        self.gmail = gmail
        self.source = source

    @classmethod
    def from_dict(cls, data_dict):
        return cls(data_dict['name'], data_dict['gmail'], data_dict['source'])
    
    def to_dict(self):
        return {
            'name':   self.name,
            'gmail':  self.gmail,
            'source': self.source
        }

# manage a collection of clients and handle reading/writing to storage 
class DataManager():
    def __init__(self):
        # store Clients objects
        self.data = []

    # extract data from 'data_storage/data.json'
    def read_data(self):
        # open data.json file as read mode
        try:
            with open('data_storage/data.json', 'r') as file:
                json_data = json.load(file)
            
            for i in json_data['clients_data']:
                client = Client.from_dict(i)
                self.data.append(client)

        except FileNotFoundError:
            print("Error: File cannot be found.")

    # add the data and store in run-time, this do not save into 'data.json' file
    def add_data(self):
        while True:
            name = input("Enter Client's name: ")
            if checkName(name):
                break

        while True:
            gmail = input("Enter Gmail Address: ").lower()
            if checkGmail(gmail):
                break

        while True:        
            source = input("Enter source: ").lower()
            if checkSource(source):
                break

        new_client = Client(name, gmail, source)
        self.data.append(new_client)

    def save_data(self):
        # create a list to store data
        new_data = []
        for client in self.data:
            new_data.append(Client.to_dict(client))

        # store the new data in json format
        data_to_save = {'clients_data': new_data}

        # write it into 'data.json' file
        json_data = json.dumps(data_to_save, indent=4)

        # Todo: check if 'data_storage' dir and 'data_json' exists or not
        with open("data_storage/data.json", "w") as file:
            file.write(json_data)        

    def print_data(self):
        if not self.data:
            print("Error: Data is empty.")

        for client in self.data:
            print(f"Client's Name: {client.name}, Gmail: {client.gmail}, Source: {client.source}")

# email-validator module needed to check whether the gmail is valid or not
def checkGmail(gmail):
    try:
        validate_email(gmail)
        return True
    
    except EmailNotValidError as error:
        print(str(error))
        return False

# check whether the name contains special characters or it is empty
def checkName(name):
    if not name:
        print("Client's name cannot be empty.")
        return False
    
    for char in name:
        if char in string.punctuation:
            print("Client's name cannot have special characters.")
            return False
    return True  

# check if the source is meet with currently sources available
def checkSource(source):
    if not source == "course" and not source == "c++ course" and not source == "c++" \
        and not source == "website":
        print("Source can only be course or website.")
        return False
    return True

def main():
    manager = DataManager()
    manager.read_data()
    manager.print_data()
    manager.add_data()
    manager.print_data()
    manager.save_data()

if __name__ == "__main__":
    main()