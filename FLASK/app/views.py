from flask import render_template
from app import app
from flask import request
from flask import Flask

from twython import TwythonStreamer
from twython import Twython
from pattern.en import sentiment,positive
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

@app.route('/')
@app.route('/index')

def index():
    latlang = [('North-East','43,-73.5,330mi'),('Mid-West','43.24,-91.25,610mi'),('South','29.22,-89.58,500mi'),('West','40.55,-110.3,650mi')] 
    query = 'republican'
    
    res_1 = get_regional_average(query,latlang[0][1])
    res_2 = get_regional_average(query,latlang[1][1])
    res_3 = get_regional_average(query,latlang[2][1])
    res_4 = get_regional_average(query,latlang[3][1])
    
    return render_template("map.html",
        title = 'Home',
        user_ne = res_1,
        user_mw = res_2,
        user_s = res_3,
        user_w = res_4 )



def get_regional_average(query,position):
    APP_KEY = 'kK38G4kaJ96PjsTVeLydA'
    APP_SECRET = 'yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY'
    twitter = Twython(APP_KEY, APP_SECRET)
    n_sum = 0
    n_tweets = 0
    for each_item in twitter.search(q=query,geocode=position)['statuses']:
        tweet = each_item['text']
        polarity = sentiment(tweet)
        n_sum += polarity[0]
        n_tweets += 1
    if n_tweets == 0:
        return 'No tweets for this topic'
    return str(n_sum/n_tweets)
