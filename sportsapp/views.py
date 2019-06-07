from django.shortcuts import render, get_object_or_404, redirect
import feedparser
from .models import PostModel
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


from django.core.paginator import Paginator

def index(request):

    form = PostForm(request.POST or None)
    queryset = PostModel.objects.all().order_by('dateCreated')[:5]
    feeds = feedparser.parse('http://www.nba.com/rss/nba_rss.xml')

    context = {
        "object_list":  queryset,
        'feeds': feeds,
        'Postform': form,
    }
    if request.method == 'POST':
        print(request.method)
        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            print(form.errors)
        context = {
    'errors': form.errors,
    'Postform': form,
            'feeds': feeds,
}

    # latest_post_list = Post.objects.all()
    # context = {'latest_post_list':latest_post_list}
    # return render(request, 'posts/index.html', context)

    return render(request, 'sportsapp/index.html', context)

# def createpost(request):
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         instance= form.save(commit=False)
#         instance.save()
#         messages.success(request, 'Successfully Created')
#         return HttpResponseRedirect(instance.get_absolute_())
#     else:
#         messages.error(request, 'Not Successfully Created')
#     context={
#         'form': form,
#     }
#     return render(request, "sportsapp/post_form.html", context)

def createpost(request):
    form = PostForm(request.POST or None)


    context = {'Postform': form}

    if request.method == 'POST':
        print(request.method)

        if form.is_valid():

            form.save()

            return redirect('index')

        else:
            print(form.errors)
            context = {
                'errors': form.errors,
                'Postform': form
            }

    return render(request, "sportsapp/post_form.html", context)



def post_list(request):
    queryset = PostModel.objects.all()
    context = {
        "object_list":  queryset,
        'title': 'List'
    }
    return  render(request,'sportsapp/index.html',context)