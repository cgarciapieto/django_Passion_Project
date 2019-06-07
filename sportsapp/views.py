from django.shortcuts import render, get_object_or_404, redirect
import feedparser
from .models import PostModel
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


from django.core.paginator import Paginator

def index(request):

    form = PostForm(request.POST or None)
    # grabs all objects from datbase and orders by date 5 at a time
    queryset = PostModel.objects.all().order_by('-id')[:5]

    # imports feedparser to parse the data from the xml url and puts it into context
    feeds = feedparser.parse('http://www.nba.com/rss/nba_rss.xml')

    context = {
        "object_list":  queryset,
        'feeds': feeds,
        'Postform': form,
    }
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('index')

        else:

            context = {
    'errors': form.errors,
    'Postform': form,
            'feeds': feeds,
}



    return render(request, 'sportsapp/index.html', context)



def createpost(request):
    form = PostForm(request.POST or None)


    context = {'Postform': form}

    if request.method == 'POST':


        if form.is_valid():

            form.save()

            return redirect('index')

        else:

            context = {
                'errors': form.errors,
                'Postform': form
            }

    return render(request, "sportsapp/post_form.html", context)

# grabs all objects from datbase and orders by date10 at a time

def post_list(request):
    queryset = PostModel.objects.all().order_by('dateCreated')[:10]
    context = {
        "object_list":  queryset,
        'title': 'List'
    }
    return  render(request,'sportsapp/index.html',context)