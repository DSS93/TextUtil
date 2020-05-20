# I have created
from django.http import HttpResponse
from  django.shortcuts import render

data = {'name':'Hello dhruv'}


def index(request):
    return render(request, 'index.html', data)


def aboutus(request):
    return render(request, 'about.html')


def analyze(request):
    a = request.POST.get('text', 'default')
    b = request.POST.get('remove', 'off')
    fullcaps = request.POST.get('caps', 'off')
    if b != "off":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in a:
            if char not in punctuations:
                analyzed = analyzed + char
        data = {'purpose': 'Remove Punctuations','analyzed_text': analyzed}
        return render(request, 'analyze.html', data)
    elif fullcaps != 'off':
        analyzed = ""
        for char in a:
                analyzed = analyzed + char.upper()
        data = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', data)
    else:
        return HttpResponse('Error')


