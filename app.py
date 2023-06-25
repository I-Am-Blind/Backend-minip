from flask import Flask, request, json,json
from .bard import bard
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=['POST'])
def send_reply():
    query = request.get_json()
    from_des = query['from_des']
    to_des = query['to_des']
    start_date = query['start_date']
    end_date = query['end_date']

    prompt = f"Generate an itinerary from {from_des} to {to_des},  from {start_date} to {end_date} with the  following properties as an array within attribute *itinerary : * day: * date: *Accomodation: *Events:[*name: *time:] *Mode_of_transport: .  response_format:json.Always use the same format. The places and hotels must be real and not made up. "
   

    reply = bard(prompt)    
    code =  '{'+reply['code']
    print(code)
    msg = {"message" :reply['content'] , "c_id" : reply['conversation_id'] , "links" : reply['links']}
    return code
