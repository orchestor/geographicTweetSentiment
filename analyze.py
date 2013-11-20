from twython import TwythonStreamer
from twython import Twython
from pattern.en import sentiment,positive
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_introspection_functions()

def get_results():
    APP_KEY = 'kK38G4kaJ96PjsTVeLydA'
    APP_SECRET = 'yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY'
    twitter = Twython(APP_KEY, APP_SECRET)
    res = []
    avg = 0
    for each_item in twitter.search(q='tesla')['statuses']:
        tweet = each_item['text']
        polarity = sentiment(tweet)
        avg += polarity[0]
        res.append(polarity[0])
    return avg

server.register_function(get_results)
server.serve_forever()


