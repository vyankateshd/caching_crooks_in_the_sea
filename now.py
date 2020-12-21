from flask import Flask, render_template, url_for, redirect, request
import pickle
model = pickle.load(open('rfrfinal_prediction.pickle', 'rb'))

app = Flask(__name__, template_folder='template')
import numpy as np

@app.route('/')
def hello_name():
    return render_template('index.html')


@app.route('/predicted', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        if output < 0.2:
            output = "Not_Fishing"
        else:
            output = "Fishing"
        return render_template('index.html', prediction_text=output)


if __name__ == '__main__':
    app.run(debug=True)
