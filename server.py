from flask import Flask, jsonify, request
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()


app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    model = joblib.load('model/cc_model.pkl')
    df = pd.DataFrame(json, index=[0])

    for col in df.columns.values:
    # Compare if the dtype is object
        if df[col].dtypes=='object':
    # Use LabelEncoder to do the numeric transformation
            df[col]=le.fit_transform(df[col])

    scaler = MinMaxScaler(feature_range=(0, 1))
    df_scaled = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
    y_predict = model.predict(df_scaled)
    approval=""
    if y_predict=='+':
        approval = "Yes"
    else:
        approval = "No"

    result = {"Predicted credit card application: " : approval}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)  