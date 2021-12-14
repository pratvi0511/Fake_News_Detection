import joblib
import pickle
import tensorflow as tf
from flask import Flask
from flask import Flask, redirect, render_template, request
from keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from wtforms import DecimalField, Form, IntegerField, SubmitField, TextField, validators

from utils import get_encoded_text, wordopt

app = Flask(__name__)


class ClickbaitedForm(Form):
	title = TextField("Enter the Article title", validators=[
		validators.InputRequired(), validators.Length(min=10)
	])
	submit = SubmitField("Submit")


class ReusableForm(Form):
	"""User entry form for entering specifics for generation"""
	title = TextField("Enter the Article title", validators=[
		validators.InputRequired(), validators.Length(min=10)
	])
	articletext = TextField("Enter the text of Article", validators=[
		validators.InputRequired(), validators.Length(min=20)
	])
	submit = SubmitField("Submit")


# Loading Models
global model
model = load_model('./trained_models/final_h5_model.h5')

global md_from_joblib
md_from_joblib = joblib.load('./trained_models/clickbait_model.pkl')

global tfidf_vectorizer
tfidf_vectorizer = joblib.load('./trained_models/vectorizer.pkl')


# Function for detection of FakeNews
@app.route("/", methods=['GET', 'POST'])
def indexpage():
	fakestring = ""
	form = ReusableForm(request.form)
	if request.method == "POST" and form.validate():
		rtitle = request.form['title']
		rarticletext = request.form['articletext']
		encoded_value = get_encoded_text(rarticletext)
		print(encoded_value)
		prediction = model.predict_classes(encoded_value)
		isfake = prediction[0][0]
		if (isfake == 0):
			fakestring = "You Are Reading a Fake News, Check you sources man."
		else:
			fakestring = "Nice, Your Sources of News are correct"
		return render_template("result.html", predict=fakestring)
	else:
		return render_template('index.html', form=form)


# Function to check Clickbait
@app.route('/clickbait', methods=['GET', 'POST'])
def checkClickbait():
	isclickbaited = ""
	form = ClickbaitedForm(request.form)
	if request.method == "POST" and form.validate():
		title = request.form['title']
		print("Title:" + title)
		clickbaited_title = md_from_joblib.predict(tfidf_vectorizer.transform([title]))
		clickbaited_title = clickbaited_title[0]
		if (clickbaited_title == 1):
			isclickbaited = "Yes, the title is clickbaited"
		else:
			isclickbaited = "No, the title is not clickbaited"
		return render_template('result.html', predict=isclickbaited)
	else:
		return render_template('clickbait.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)
