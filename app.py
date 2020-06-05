from flask import Flask, jsonify

app = Flask(__name__)

services = [
    {
        'request_services':[
            {
                'active_service':[
                    {
                        'name':'child_care',
                        'benefits':[
                            'free child care'
                        ]
                            
                    }
                ],
                'inactive_service':[
                    {
                        'name':'employment_service',
                        'benefits':[
                            'employment benefits'
                        ]
                    }
                ]
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/services', methods=['POST'])
def create_store():
    pass

@app.route('/services')
def get_services():
    return jsonify({'services': services})


@app.route('/services/<string:name>/')
def get_acpt_in_activeServices(name):
    pass

'''
app.run(port=5001)

app.run(host="0.0.0.0", port=8998)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8998)

'''
app.run(port=5001)
