from flask import Flask, request, render_template,jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    responce = jsonify({
        'locations': util.get_location_names()
    })
    responce.headers.add('Access-Control-Allow-Origin', '*')

    return responce


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    area_type = request.form['area_type']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    availability = request.form['availability']
    balcony = int(request.form['balcony'])

    price = str(util.get_estimated_price(location,area_type,availability,total_sqft,bath,balcony,bhk))

    return render_template("results.html",price=price)

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()