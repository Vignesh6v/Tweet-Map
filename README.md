# Tweet-Map
Leveraged tweet data using the twitter API and displayed the same on a HeatMap using the Google Maps API while utilizing the ElasticSearch changefeed property to stream live data for a particular keyword thus reducing the overhead of polling the database constantly for new tweet data.


Dependencies:
=======
* Boto3
* Elasticsearch
* Flask
* requests_aws4auth
* Tweepy
* Google Map API


API Source:
=======
1) To get the Streaming Tweets from Twitter
```bash
http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
```

2) AWS - Elastic Search
```bash
https://search-tweettesting-mrejtfputdpvmqrkiay7um73yu.us-west-1.es.amazonaws.com/twitter/_search
```

3) AWS - Elastic BeanStalk
```bash
http://flask-env.pwfdjmpehv.us-west-2.elasticbeanstalk.com/
```


Screenshot:
=======

![Alt text](https://github.com/Vignesh6v/Tweet-Map/blob/master/static/Screenshot.png "Screen-shot")
