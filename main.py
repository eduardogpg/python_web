from flask import Flask, jsonify, abort, request
from flask import make_response
from flask import render_template

from models import initialize, Task

DEBUG = True

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder='./dist')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Element not found'}), 404)

@app.route('/codigofacilito/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify( {'tasks': Task.get_all() })

@app.route('/codigofacilito/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.get_element(task_id)
    if task is not None:
        return jsonify({'task': task.serialize})

    abort(404)

@app.route('/codigofacilito/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json or not 'description' in request.json:
        abort(400)

    task = Task.create_element(request.json['title'],
                               request.json['description'],
                               request.json['active'])

    return jsonify({'task': task.serialize}), 201

@app.route('/codigofacilito/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.get_element(task_id)

    if task is None:
        abort(404)

    if not request.json or not 'title' in request.json or not 'description' in request.json:
        abort(400)

    task.update_element(request.json['title'],
                request.json['description'],
                request.json['active'])


    return jsonify({'task': task.serialize})

@app.route('/codigofacilito/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.get_element(task_id)
    if task is None:
        abort(404)

    task.delete_element()
    return jsonify({'result': True})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def test_demo():
    return jsonify('Eduardo Ismael!')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    initialize()
    app.run(debug=DEBUG)
