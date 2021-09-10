from flask import Flask
from flask_restful import Api, Resource
import time
import random

app = Flask(__name__)
api = Api(app)

class demo(Resource):
	def get(self):
		delay = random.randint(1,10)/10
		time.sleep(delay)
		return {"delay":delay}

api.add_resource(demo, "/demo")

if __name__ == "__main__":
	app.run()