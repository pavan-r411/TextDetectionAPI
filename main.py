from flask import *
import json, time

from Models.detection import identify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page':'home', 'Message':'Hello World','TimeStamp':time.time(),'result':"Hello World!"}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/detect', methods=['POST','GET'])
def request_page():
    # n1 = int(request.args.get('num1'))  #/user/?num1=7&num2=6
    # n2 = int(request.args.get('num2')) 
    res = identify('C:\\Users\\I569380\\Documents\\VSProj\\DecisionAPI\\Models\\card1.jpg')
    data_set = {'Page':'Request', 'Message':f'Aadhar Numer: {res}','TimeStamp':time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(port=7777)
