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

    return render(requests, 'graph.html', {'js_data': str(formatted_data)})

    # Define a function to parse the text data


import json


def parse_text_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {
        "name": "Ross",
        "value": 216,
        "linkWith": [
            "Joey",
            "Phoebe",
            "Mrs Geller",
            "Aunt Lilian",
            "Mrs Bing",
            "Ben",
            "Mrs Green",
            "Emily"
        ],
        "children": []
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
                    # Add the atoms as children to the current identity
                    identity_data = {
                        "name": identity,
                        "value": 216,
                        "linkWith": [atom["name"] for atom in atoms]
                    }
                    data["children"].append(identity_data)
                # Start processing a new identity
                identity = parts[1]
                atoms = []
            elif parts[0] == 'BEADS':
                # Create atoms from BEADS line
                atoms = [{"name": part, "value": 1} for part in parts[1:]]

    # Add the last set of atoms
    if identity and atoms:
        identity_data = {
            "name": identity,
            "value": 216,
            "linkWith": [atom["name"] for atom in atoms]
        }
        data["children"].append(identity_data)

    print(data)


def inter_graph(requests):
    result_data = parse_text_data(input_file_path)

    return render(requests, 'bonds.html', {'inter_data': result_data})


def home(requests):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Initialize variables to store the formatted data
    formatted_data = []
    identity = ''
    beads = {}
    links={}

    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            if parts[0] == 'Identity':

                if identity:
                    formatted_data.append({'name': identity,
                                           'value': 21,
                                           'children': beads})
                identity = parts[1]
                beads =[]
            elif parts[0] == 'BEADS':
                for part in parts[1:]:
                    beads.append({'name': str(part), 'value': 10})
            else:
                for part in parts[1:]:
                    node1,node2=part.split('-')
                    if node1 not in links:
                        links[node1] = []
                    if node2 not in links:
                        links[node2] = []
                    links[node1].append([identity,node2])
                    links[node2].append([identity,node1])


    if identity:
        formatted_data.append({'name': identity,
                               'value': 21,
                               'children': beads})

    for k,v in links.items():
        print(k)
        print(v)
    # print(formatted_data)


    return render(requests, 'graph.html', {'formatted_data': formatted_data,'links':links})
