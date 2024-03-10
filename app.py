from flask import Flask, render_template, jsonify, request
from helper import get_access_token
import requests
import constants
from random import randint

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10
app.config[
    "SECRET_KEY"] = "Capstone projects are challenging."

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/animals')
def animals():
    get_access_token()
    base_response = requests.get(constants.BASE_URL_PET+'/animals', headers={'Authorization' : 'Bearer '+constants.ACCESS_TOKEN_PET}).json()
    animals = base_response["animals"]
    return jsonify(animals)

@app.route('/animal')
def animal():
    get_access_token()
    animal_response = requests.get(constants.BASE_URL_PET+"animals/70270817", headers={'Authorization' : 'Bearer '+constants.ACCESS_TOKEN_PET}).json()
    return jsonify(animal_response) 

@app.route('/number')
def get_number():
    res = requests.get(constants.BASE_URL_NUMBER, headers={'Content-Type':'application/json'}).json()
    return jsonify(res)

@app.route('/news')
def news():
    #res = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2023-12-07&sortBy=publishedAt&apiKey={constants.API_KEY_NEWS}").json()
    params = (
    ('q', 'Christmas'),
    ('from', '2023-12-21'),
    ('sortBy', 'popularity'),
    ('apiKey', constants.API_KEY_NEWS),
)
    res = requests.get(constants.URL_NEWS, params=params).json()
    return jsonify(res)


@app.route('/youtubeinfo')
def info():
    searchterm = "Glute bridge"
    limit = 25
    res = requests.get(f"{constants.BASE_URL_YT}{searchterm}&maxResults={limit}&key={constants.API_KEY_YT}", headers={'Content-Type': 'application/json'}).json()
    return jsonify(res)


@app.route('youtube/<searchterm>')
def show_youtube(searchterm):
    limit = 5
    res = requests.get(f"{constants.BASE_URL_YT}{searchterm}&maxResults={limit}&key={constants.API_KEY_YT}", headers={'Content-Type': 'application/json'}).json()
    return jsonify(res)


@app.route('/exercisestart')
def exercise():
    muscle = 'abdominals'
    offset = 0
    res = requests.get(f"{constants.BASE_URL_EXERCISE}{muscle}&offset={offset}", headers={'X-Api-Key': constants.API_KEY_NINJAS}).json()
    names = [res[i]['name'] for i in range(len(res))]
    #return jsonify(res)
    return render_template('exercise.html', names=names, muscle=muscle)


@app.route('/exercise', methods=['GET', 'POST'])
def exercise_offset():
    muscle = request.form['muscle']
    offset = request.form['offset']
    if not muscle:
        print("no muscle group")
        muscle = 'traps'
    print("muscle", muscle)
    if not offset:
        offset = 0
    res = requests.get(f"{constants.BASE_URL_EXERCISE}{muscle}&offset={offset}", headers={'X-Api-Key': constants.API_KEY_NINJAS}).json()
    names = [res[i]['name'] for i in range(len(res))]
    return render_template('exercise.html', names=names, muscle=muscle)

