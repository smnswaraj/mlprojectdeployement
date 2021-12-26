from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/",methods=['GET'])
def HomePage():
    return render_template("index.html")


@app.route("/", methods=['POST','GET'])
def index():
    if  request.method == 'POST':
        age= (request.form['age'])
        prediction = model.bmi_prediction(age)
        output = prediction[0]

    return render_template('index.html', pred = output )

if __name__ == "__main__":
    app.run(debug=True)