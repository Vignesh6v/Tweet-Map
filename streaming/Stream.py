import collections,json,time
from elasticsearch import Elasticsearch, RequestsHttpConnection

from requests_aws4auth import AWS4Auth
from datetime import datetime
import logging
import json
import boto3
import config
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import boto3



consumer_key=config.consumer_key
consumer_secret= config.consumer_secret
access_token= config.access_token
access_token_secret	= config.access_token_secret


tweet = {}
temp={}


class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            decoded = json.loads(data)
            if decoded['coordinates']:
                #print "ID:%s Username:%s Tweet:%s"%(decoded['id'],decoded['user']['screen_name'],decoded['text'])
                temp["text"]= decoded['text']
                temp["id"]= str(decoded['id'])
                temp["name"]= decoded['user']['screen_name']
                temp["latitude"]= str(decoded['coordinates']['coordinates'][1])
                temp["longitude"]= str(decoded['coordinates']['coordinates'][0])
                final = json.dumps(temp)

                host = config.host
                awsauth = AWS4Auth(config.aws_access_token, config.aws_access_token_secret, "us-west-2", 'es')
                es = Elasticsearch(
                    hosts=[{'host': host, 'port': 443}],
                    http_auth=awsauth,
                    use_ssl=True,
                    verify_certs=True,
                    connection_class=RequestsHttpConnection
                )
                res = es.index(index="twitter", doc_type='tweet', id=temp["id"], body=final)
                #print res
                return True
        except Exception, e:
            print "***"+str(e)+"****"
            return True


    def on_error(self, status):
        print status


if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(track=['love','job','you','good','happy','hate','india'])
