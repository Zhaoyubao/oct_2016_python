from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maps/directions', methods=['POST'])
def get_directions():
    print "Request Form:", request.form
    data = {
            'origin' : request.form['origin'],
            'destination' : request.form['destination'],
            'sensor' : 'false',
            'key' : 'AIzaSyAhMCk1vqD_DKO1L3UH_Z_gJnK5-MUz6Yo'
        }
    url = "https://maps.googleapis.com/maps/api/directions/json?"
    res = requests.get(url, data).json()
    # print "Res:", res
    if res['status'] == 'OK':
        result = {
                'from': res['routes'][0]['legs'][0]['start_address'],
                'to': res['routes'][0]['legs'][0]['end_address'],
                'distance': res['routes'][0]['legs'][0]['distance']['text'],
                'time': res['routes'][0]['legs'][0]['duration']['text'],
                'steps': res['routes'][0]['legs'][0]['steps']
        }
    else:
        result = { 'error': "Driving directions from {} to {} are not available...".format(request.form['origin'].upper(), request.form['destination'].upper()) }
    return render_template('partials/directions.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
