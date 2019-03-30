from flask import Flask, jsonify, request


app = Flask(__name__)

stores = [
  {
    'name': 'store1',
    'items': [
      {
        'name': 'pen',
        'price': 15.99
      }
    ]
  }
]

@app.route('/stores', methods=['POST'])
def create_store():
  req_data = request.get_json()
  new_store = {
    'name': req_data['name'],
    'items': req_data['items']
  }

  stores.append(new_store)

  return jsonify(new_store)


@app.route('/stores/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify(store)
  
  return 'no store found'

@app.route('/stores')
def get_stores():
  return jsonify(stores)

@app.route('/stores/<string:name>/items', methods=['POST'])
def create_item_in_store(name):
  data = request.get_json()

  for store in stores:
    if store['name'] == name:
      new_item = {
        'name': data['name'],
        'price': data['price'],
      }
      
      store['items'].append(new_item)
      return jsonify(store['items'])
  
  return 'no store found'


@app.route('/stores/<string:name>/items')
def get_items_in_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify(store['items'])
  
  return 'no store found'



app.run(port=5500)