from flask import Flask, render_template, request
import blob

server = Flask(__name__)


@server.route('/')
def home_page():
	return render_template('index.html')

@server.route('/result', methods=['GET','POST'] )
def result():
	text = request.form['text_input']
	result = blob.input(text)
	return render_template('index.html', result=result)


if __name__ == "__main__":
	server.run(debug=True)