from flask import Flask, request, jsonify

app = Flask(__name__)
todos = [
    {"label": "Sample Todo 1", "done": True},
    {"label": "Sample Todo 2", "done": False}
]
@app.route('/todos',methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This isthe position to delete", position)
    todos.pop(position)
    return jsonify(todos)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3245,debug=True)