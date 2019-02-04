from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'hithere':'whatsupp'})

def flowers(request):
    return HttpResponse('Flowers are good')

def count(request):
    fulltext=request.GET['fulltext']
    wlist = fulltext.split()
    return render(request, 'count.html', {'fulltext' : fulltext, 'count': len(wlist)})
