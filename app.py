from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from flask_cors import CORS, cross_origin

from utils import text_cleaner, links_generator, quiz
from summa import summarizer

app = Flask(__name__)
CORS(app)

api = Api(app)
parser = reqparse.RequestParser()

class Summary(Resource):
  def get(self):
    return {'hello': 'world'}

  def post(self):
    parser.add_argument('data')
    args = parser.parse_args()
    html = args["data"]

    raw_data = text_cleaner.get_article_from_html(html).text

    smry = summarizer.summarize(raw_data, words=250)
    related_links = links_generator.get_links_for_article(raw_data)
    return {'summary': smry, 'related_links': related_links}

class Quiz(Resource):
	def get(self):
		return {'hello': 'world'}

	def post(self):
	    parser.add_argument('data')
	    args = parser.parse_args()
	    html = args["data"]

	    raw_data = text_cleaner.get_article_from_html(html).text

	    qz = quiz.generate_quiz(raw_data)
	    return {'data': qz}


api.add_resource(Summary, '/summary')
api.add_resource(Quiz, '/quiz')

if __name__ == '__main__':
	app.run(debug=True)
