from flask import Flask, request, json
from .bard import bard
from flask_cors import CORS
from serpapi import GoogleSearch

app = Flask(__name__)
CORS(app)

def get_img(location):
    params = {
  f"api_key": "89897174d76777754aa3c1718aa2066832fe17e965b61e765e92702fbf573650",
  "engine": "google",
  "q": {location},
  "location": "Kerala, India",
  "google_domain": "google.co.in",
  "gl": "in",
  "hl": "hi",
  "tbm": "isch"
    }

    search = GoogleSearch(params)
    results = search.get_dict()['images_results'][0]['original']
    return results

@app.route("/chat", methods=['POST'])
def send_reply():
    query = request.get_json()
    from_des = query['from_des']
    to_des = query['to_des']
    start_date = query['start_date']
    end_date = query['end_date']

    prompt = f"""
Generate an itinerary from {from_des} to {to_des},  from {start_date} to {end_date} with the  following properties as an array within attribute *itinerary :
* day:
* date:
* accommodation:(Only suggest real places)
* events:[* location: *description: *time: ]
* transport:
response_format:json
Always use the same format. The places and hotels must be real and not made up.
"""
   

    reply = bard(prompt)    
    code =  '{'+reply['code']
    data = json.loads(code)
    

    for item in data['itinerary']:
        for event in item['events']:
            event['link'] = get_img(event['location'])


    code = json.dumps(data)
    return code


@app.route("/getimg",methods=['POST'])
def send_img():
    query = request.get_json()
    params = {
  f"api_key": "89897174d76777754aa3c1718aa2066832fe17e965b61e765e92702fbf573650",
  "engine": "google",
  "q": {query['location']},
  "location": "Kerala, India",
  "google_domain": "google.co.in",
  "gl": "in",
  "hl": "hi",
  "tbm": "isch"
    }

    search = GoogleSearch(params)
    results = search.get_dict()['images_results'][0]
    return results