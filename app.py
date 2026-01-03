from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("car_price_prediction.joblib")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        Year = int(request.form.get("Year"))
        Present_Price = float(request.form.get("Present_Price"))
        Kms_Driven = int(request.form.get("Kms_Driven"))
        Fuel_Type = int(request.form.get("Fuel_Type"))
        Seller_Type = int(request.form.get("Seller_Type"))
        Transmission = int(request.form.get("Transmission"))
        Owner = int(request.form.get("Owner"))

        input_data = np.array([[Year, Present_Price, Kms_Driven,
                                Fuel_Type, Seller_Type, Transmission, Owner]])

        prediction = model.predict(input_data)[0]

        return render_template(
            "index.html",
            prediction=round(prediction, 2)
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=str(e)
        )

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
