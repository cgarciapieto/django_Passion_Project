from django.shortcuts import render
import feedparser

def index(request):



    feeds = feedparser.parse('http://www.nba.com/rss/nba_rss.xml')

    context = {

        'feeds': feeds
    }

    return render(request, 'sportsapp/index.html', context)

