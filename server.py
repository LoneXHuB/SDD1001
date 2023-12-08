from flask import Flask, request, jsonify
import pandas as pd
import os

file_directory = os.path.dirname(os.path.abspath(__file__))

os.chdir(file_directory)

print("directory : ", os.getcwd())

app = Flask(__name__)

csv_data = {
    "clients" : pd.read_csv("clients.csv"),
    "prices": pd.read_csv("prices.csv")
}
print("TYPE : " , type(csv_data['clients']))

@app.route('/get_clients', methods= ['POST'])
def get_clients():
    data = request.get_json()

    if 'table_name' not in data:
        return jsonify({'error' : 'Table name not provided!'}) , 400

    table_name = data['table_name']

    if table_name not in csv_data:
        return jsonify({'error':'table not found!'}), 404
    
    table_df = csv_data[table_name]
    table_json = table_df.to_json(orient='records') 

    return jsonify({'table_data' : table_json})


@app.route('/add_client', methods= ['POST'])
def add_client():
    #get client info 
    data = request.get_json()

    if 'new_row' not in data:
        return jsonify({'error' : 'No row provided'})
    
    new_client = data['new_row']

    #lire le fichier csv et y ajouter le nouveau client
    csv_data['clients'] = csv_data['clients'].append(new_client, ignore_index=True)

    csv_data['clients'].to_csv('clients.csv', index=False)

    return jsonify({'message': "Row added successfully!"})

app.run(port=5000)