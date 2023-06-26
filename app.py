from flask import Flask, request, json
from .bard import bard
from flask_cors import CORS
from serpapi import GoogleSearch

app = Flask(__name__)
CORS(app)

gugu = 'c93c14079ef1e4900d7279cbb18d3db7d03c822b091e9a031651ea01b9427723'

def get_img(location):
    params = {
  f"api_key": {gugu},
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
  f"api_key": {gugu},
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


@app.route("/setapikey",methods=['POST'])
def set_api_key():
    query = request.get_json()
    if (query['secret_key'] == '8075850847'):
     api_key = query['api_key']
     return f"current api key set to {api_key}"
    else:
        return "Invalid secret_key"