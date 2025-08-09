import json

# extract data from 'data_storage/data.json'
def read_data():
    # open data.json file as read mode
    with open('data_storage/data.json', 'r') as file:
        data = json.load(file)
    
    for i in data['clients_data']:
        print(i)

def main():
    read_data()

if __name__ == "__main__":
    main()