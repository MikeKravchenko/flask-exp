 
from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

workflows = [{
    'name': 'Current Workflow',
    'items': [
            {
                'active_workflows':[
                    {
                        'name':'child_care',
                        'benefits':[
                            'free child care'
                        ]
                            
                    }
                ],
                'inactive_workflows':[
                    {
                        'name':'employment_service',
                        'benefits':[
                            'employment benefits'
                        ]
                    }
                ]
            }

        ]
}]


@app.route('/')
def home():
  print('FlaskAPI Demo')

#post /workflow data: {name :}
@app.route('/workflow' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_workflow = {
    'name':request_data['name'],
    'items':[]
  }
  workflows.append(new_workflow)
  return jsonify(new_workflow)

#get /workflow/<name> data: {name :}
@app.route('/workflow/<string:name>')
def get_workflow(name):
  for workflow in workflows:
    if workflow['name'] == name:
          return jsonify(workflow)
  return jsonify ({'message': 'Workflow not found'})

#get /workflow
@app.route('/workflow')
def get_workflows():
  return jsonify({'workflows': workflows})

#post /workflow/<name> data: {name :}
@app.route('/workflow/<string:name>/item' , methods=['POST'])
def create_item_in_workflow(name):
  request_data = request.get_json()
  for workflow in workflows:
    if workflow['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        workflow['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'Workflow not found'})

#get /workflow/<name>/item data: {name :}
@app.route('/workflow/<string:name>/item')
def get_item_in_workflow(name):
  for workflow in workflows:
    if workflow['name'] == name:
        return jsonify( {'items':workflow['items'] } )
  return jsonify ({'message':'store not found'})

app.run(port=5000)
