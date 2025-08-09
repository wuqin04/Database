import json

# store single client information only, do not do any json file handling here
class Client(object):
    def __init__(self, name: str, gmail: str, source: str):
        self.name = name
        self.gmail = gmail
        self.source = source

# manage a collection of clients and handle reading/writing to storage 
class ClientManager():
    def __init__(self):
        pass

    # extract data from 'data_storage/data.json'
    def read_data():
        # open data.json file as read mode
        with open('data_storage/data.json', 'r') as file:
            data = json.load(file)
        
        for i in data['clients_data']:
            print(i)

    # this will replace everything previous had in the data.json 
    def add_data():
        client_name = input("Enter client's name: ")
        client_gmail = input("Enter client's gmail address: ")
        client_source = input("Enter client's source: ")

        data = dict(name = client_name, gmail = client_gmail, source = client_source)

        write_to_json = json.dumps(data, indent=4)
        with open('data_storage/data.json', 'w') as file:
            file.write(write_to_json)
    

def main():
    ClientManager.read_data()
    ClientManager.add_data()

if __name__ == "__main__":
    main()