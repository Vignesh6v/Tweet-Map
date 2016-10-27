from flask import Flask, request, jsonify, session, render_template,session

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

from datetime import datetime
import logging

import json
import config


application = Flask(__name__)
def __int__():
	pass

@application.route('/')
def index():
	logger= logging.getLogger('application')
	logger.setLevel(logging.INFO)
	fh = logging.FileHandler('spam.log')
	fh.setLevel(logging.INFO)
	logger.addHandler(fh)
	logger.info('content')
	return render_template('TweetMap.html', name="TweetMap")


@application.route('/search')
def search():

	search_key = request.args.get('search_key')
	search_key = search_key.lower()
	result_list = []
	awsauth = AWS4Auth(config.access_token, config.access_token_secret, "us-west-1", 'es')
	es = Elasticsearch(
		hosts=[{'host': config.host, 'port': 443}],
		http_auth=awsauth,
		use_ssl=True,
		verify_certs=True,
		connection_class=RequestsHttpConnection
	)
	res = es.search(index="twitter", body={"query": {"wildcard": {"text":'*'+search_key+'*'}}},size=400)
	hits = res['hits']['hits']
	if hits:
		for hit in hits:
			latitude = hit['_source']['latitude']
			longitude = hit['_source']['longitude']
			sentiment_response = hit['_source']['name']
			tweet_text = hit['_source']['text']
			result_list.append(dict(latitude=latitude, longitude=longitude, sentiment_response=sentiment_response, tweet_text=tweet_text))

	result_json = json.dumps(result_list)
	return result_json


if __name__ == '__main__':
	application.debug = True
	application.run()
