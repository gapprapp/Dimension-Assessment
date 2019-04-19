from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('input')

# Index
class Index(Resource):
	def get(self):
		return {
			"Title": "Dimension Assessment",
			"Name" : "Perakit Sakulsaithongkum",
			"Function & Path":{ 
					"FirstFactorial": "api/firstfactorial/",
					"FirstReverse": "api/firstreverse/",
					"AlphabetSoup": "api/alphabetsoup/",
				}
			}
		
def recursion(num):
	if num > 1:
		return num * recursion(num-1)
	else:
		return num

# FirstFactorial
class FirstFactorial(Resource):
	def post(self):
		args = parser.parse_args()

		try:
			num = int(args['input'])
			if num >= 1 and num <= 18:
				return {'Input':{'input': int(args['input'])}, 'Output': {'output': recursion(num)}}
			else:
				return {'Input':{'input': int(args['input'])}, 'Output': {'output': "Invalid input..."}}
		except Exception as e:
			return {'Input':{'input': int(args['input'])}, 'Output': {'output': "Invalid input..."}}

			## ## ## ## ##

# FirstReverse
class FirstReverse(Resource):
	def post(self):
		args = parser.parse_args()
		string = args['input']

		return {'Input':{'input': string}, 'Output': {'output': string[::-1]}}

		## ## ## ## ##

#AlphabetSoup
class AlphabetSoup(Resource):
	def post(self):
		args = parser.parse_args()
		string = args['input']

		return {'Input':{'input': string}, 'Output': {'output': "" .join(sorted(string))}}

		## ## ## ## ##

api.add_resource(Index, '/')

api.add_resource(FirstFactorial, '/api/firstfactorial/')
api.add_resource(FirstReverse, '/api/firstreverse/')
api.add_resource(AlphabetSoup, '/api/alphabetsoup/')


if __name__ == '__main__':
    app.run(debug=True)