from django.shortcuts import render
from django.http import HttpResponse
from twython import TwythonStreamer
from twython import Twython
from pattern.en import sentiment,positive
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

APP_KEY = 'kK38G4kaJ96PjsTVeLydA'
APP_SECRET = 'yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY'
twitter = Twython(APP_KEY, APP_SECRET)

def index(request,query):
    latlang = [('North-East','43,-73.5,330mi'),('Mid-West','43.24,-91.25,610mi'),('South','29.22,-89.58,500mi'),('West','40.55,-110.3,650mi')] #NE,MW,S,W co-ordinates
    res = []
    for place in latlang:
        res.append('People in the ' + place[0] + ' say ' + get_regional_average(query,place[1]))

    #return HttpResponse('</br>'.join(res))


def get_regional_average(query,position):
    global twitter #Eek, but we are at a hackathon
    sum = 0
    n_tweets = 0
    for each_item in twitter.search(q=query,geocode=position)['statuses']:
        tweet = each_item['text']
        polarity = sentiment(tweet)
        sum += polarity[0]
        n_tweets += 1
    if n_tweets == 0:
        return 'No tweets for this topic'
    return str(sum/n_tweets)

def search_form(request):
    return render(request, '/index.html')    

    
