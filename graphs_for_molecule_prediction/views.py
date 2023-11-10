from django.shortcuts import render
from .matrix_creation import main
input_file_path = 'static/Python-Input.txt'

def home(requests):

    graph_of_identity=main()

    print(graph_of_identity)
    return render(requests, 'graph.html', {'formatted_data':graph_of_identity})
