from django.shortcuts import render

def index(request):
    '''a view to display an index page'''
    return render(request, "index.html")