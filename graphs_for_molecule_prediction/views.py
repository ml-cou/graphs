from django.shortcuts import render

input_file_path = 'static/Python-Input.txt'


# Create your views here.
def main_graph(requests):
    # Define the input file path

    # Read data from the input file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Initialize variables to store the formatted data
    formatted_data = []
    identity = None
    beads = None

    # Process the lines from the input file
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            if parts[0] == 'Identity':
                # Save the current data (if any)
                if identity:
                    formatted_data.append({'name': identity, 'children': beads})
                # Start processing a new identity
                identity = parts[1]
                beads = []
            elif parts[0] == 'BEADS':
                beads = [{'name': part, 'value': 10} for part in parts[1:]]

    # Save the last identity
    if identity:
        formatted_data.append({'name': identity, 'children': beads})

    # Create a JavaScript string with the formatted data
    # js_data = 'var data = ' + str(formatted_data) + ';'


    return render(requests,'graph.html',{'js_data':str(formatted_data)})

    # Define a function to parse the text data
import json
def parse_text_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {
        "nodes": [],
        "links": []
    }

    identity = None
    atoms = None

    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            if parts[0] == 'Identity':
                # Save the current data (if any)
                if identity and atoms:
                    # Add atoms as nodes
                    data["nodes"].extend(atoms)
                    # Create links between consecutive atoms
                    for i in range(len(atoms) - 1):
                        data["links"].append({"source": atoms[i]["id"], "target": atoms[i + 1]["id"]})
                # Start processing a new identity
                identity = parts[1]
                atoms = []
            elif parts[0] == 'BEADS':
                # Create atoms from BEADS line
                atoms = [{"id": part, "name": f"{part}"} for part in parts[1:]]

    # Add the last set of atoms and links
    if identity and atoms:
        data["nodes"].extend(atoms)
        for i in range(len(atoms) - 1):
            data["links"].append({"source": atoms[i]["id"], "target": atoms[i + 1]["id"]})
    data['nodes'] = [{'id': i, 'name': i} for i in set(node['name'] for node in data['nodes'])]

    return data

def inter_graph(requests):
    result_data = parse_text_data(input_file_path)


    return render(requests,'bonds.html',{'inter_data':result_data})
