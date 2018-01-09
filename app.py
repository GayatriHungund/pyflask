from flask import Flask
import couchdb

app = Flask(__name__)

@app.route("/home")
def hello():
	print "Hello World!"
	server = couchdb.Server("http://0.0.0.0:5984/")
	server.create('python')
	return "Created"

if (__name__ == "__main__"):
	app.run(port = 5004)
	

