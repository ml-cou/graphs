import pandas as pd
import os

# Create a Lipid object
class Lipids:
    def __init__(self, name):
        self.name = name
        self.node = {}
        self.inter_connections = {}  # An adjacency list where links are node to node
# Create a Lipid object for 'APC'

def process_nodes(lipid_name):

    lipid = Lipids(lipid_name)


    # Define the path to your node feature matrix data file
    node_feature_file_path = os.path.join(node_feature_dir, lipid_name+'.txt')

    # Read the node feature matrix data into a DataFrame
    node_feature_df = pd.read_csv(node_feature_file_path, sep='\t', index_col=0)

    # Define the path to your adjacency matrix data file
    adjacency_matrix_file_path = os.path.join(adjacency_matrix_dir, f"{lipid_name} .txt")

    # Read the adjacency matrix data into a DataFrame
    adjacency_df = pd.read_csv(adjacency_matrix_file_path, sep='\t', index_col=0)

    # Process the node feature DataFrame
    for index, row in node_feature_df.iterrows():
        features = [column for column in node_feature_df.columns if row[column] > 0.0]
        if features:
            lipid.node[index] = features

    # Process the adjacency matrix to populate the 'inter_connections' attribute
    for source_node, row in adjacency_df.iterrows():

        for target_node, value in row.items():
            if value > 0.0:
                if source_node in lipid.inter_connections:
                    lipid.inter_connections[source_node].append(target_node)
                else:
                    lipid.inter_connections[source_node] = [target_node]

    # Printing the result
    # print(f"Lipid Name: {lipid.name}")
    lipid_dic = {'name': lipid_name, 'value':50, 'children': []}
    node_dic={}
    for node, features in lipid.node.items():
        node_dic.update({node:{'name':node, 'value': 17,'children':[]}})
        for feature in features:
            node_dic[node]['children'].append({'name':feature,'value':4})
        # print(f"Node: {node}, Features: {', '.join(features)}")
    # print("Interconnections:")
    for source_node, targets in lipid.inter_connections.items():
        node_dic[source_node]['linkWith']=targets
        # print(f"Source Node: {source_node}, Target Nodes: {', '.join(targets)}")

    for key,val in node_dic.items():
        lipid_dic['children'].append(val)

    return lipid_dic

# Define the directories containing node feature and adjacency matrix files
node_feature_dir = './Nodes_Data/Node_Features/'  # Replace with the actual directory path
adjacency_matrix_dir = './Nodes_Data/Adjacency_Matrix/'  # Replace with the actual directory path

def main():
    all_lipids={}
    for node_feature_file in os.listdir(node_feature_dir):
        if node_feature_file.endswith(".txt"):
            lipid_name = os.path.splitext(node_feature_file)[0]  # Extract name from the filename
            graph_for_lipid=process_nodes(lipid_name)
            all_lipids.update({lipid_name:graph_for_lipid})

    return all_lipids







