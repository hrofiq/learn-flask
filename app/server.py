from flask import Flask, jsonify, json, request

app = Flask(__name__)

@app.route('/')
def hello():
    print('***', request)
    return 'Welcome'

@app.route('/read_json')
def read_json():
    data_json = open('app/data.json')
    stored_json = json.load(data_json)
    print('*** read json ***')
    return jsonify(stored_json)

@app.route('/add_json', methods=['POST'])
def add_json():
    data_json = open('app/data.json', mode='r')
    stored_json = json.load(data_json)
    data_json.close()
    stored_json.append(request.json)
    data_json = open('app/data.json', mode='w')
    json.dump(stored_json, data_json)
    data_json.close()
    print('*** insert *** %s' % (request.json))
    return 'successfuly inserted:\n\n' + str(request.json)

@app.route('/remove_json', methods=['POST'])
def remove_json():
    data_json = open('app/data.json', mode='r')
    stored_json = json.load(data_json)
    data_json.close()
    stored_json.remove(request.json)
    data_json = open('app/data.json', mode='w')
    json.dump(stored_json, data_json)
    data_json.close()
    print('*** remove *** %s' % (request.json))
    return 'successfuly removed:\n\n' + str(request.json)