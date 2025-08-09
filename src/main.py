import json

# extract data from 'data_storage/data.json'
def read_data():
    # open data.json file as read mode
    with open('data_storage/data.json', 'r') as file:
        data = json.load(file)
    
    for i in data['clients_data']:
        print(i)

def add_data():
    client_name = input("Enter client's name: ")
    client_gmail = input("Enter client's gmail address: ")
    client_source = input("Enter client's source: ")

    data = dict(name = client_name, gmail = client_gmail, source = client_source)

    write_to_json = json.dumps(data, indent=4)
    with open('data_storage/data.json', 'w') as file:
        file.write(write_to_json)

def main():
    read_data()
    add_data()

if __name__ == "__main__":
    main()