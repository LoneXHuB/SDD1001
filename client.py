import requests
import json 
api_url = 'http://localhost:5000/get_clients'
add_url = 'http://localhost:5000/add_client'

def request_clients():    
    response = requests.post(api_url, json={'table_name' : 'clients'})

    if response.status_code == 200:
        data = response.json()
        table_data = json.loads(data['table_data'])
        
        print("Liste Clients : \n")

        for row in table_data:
            print(f"ID: {row['id']} ,  Name : {row['name']} , Age: {row['age']}")

    else:
        print(f"Error: {response.status_code} = {response.json()['error']}")

def request_add_client():
    client_row = {'id':5 , 'name': 'Doe' , 'age' : 33} 

    response = requests.post(add_url, json={"new_row": client_row})

    if response.status_code == 200:
        print(response.json()['message'])
    else:
        print(f"Error! : {response.status_code} = {response.json()['error']}")

if __name__ == "__main__":
    request_clients()
    request_add_client()
    request_clients()
    
