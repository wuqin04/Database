import json

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

    def print_data(self):
        if not self.data:
            print("Error: Data is empty.")
            
        for client in self.data:
            print(f"Client's Name: {client.name}, Gmail: {client.gmail}, Source: {client.source}")

        
def main():
    manager = DataManager()
    manager.read_data()
    manager.print_data()

if __name__ == "__main__":
    main()