# i hve created this file - Nish
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')

def analyze(request):
    text = request.POST.get('textarea', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcapss = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    param = {'purpose': text, 'analyze_text': text}
    punctuation = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''

    if removepunc == "on":
        analyzed = ""
        for char in text:
            if char not in punctuation:
                analyzed += char
        text = analyzed
        param = {'purpose': text, 'analyze_text': analyzed}

    if fullcapss == "on":
        analyzed = ""
        for char in text:
            if char not in punctuation.upper():
                analyzed += char.upper()
        text = analyzed
        param = {'purpose': text, 'analyze_text': analyzed}

    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != "\n":
                analyzed += char
        text = analyzed
        param = {'purpose': text, 'analyze_text': analyzed}

    if spaceremover == "on":
        analyzed = ""
        for index,char in enumerate(text):
            if not (text[index] == " " and text[index+1] == " "):
                analyzed += char
        text = analyzed
        param = {'purpose': text, 'analyze_text': analyzed}

    if charcount == "on":
        analyzed = 0
        for char in text:
            analyzed += 1
        text = analyzed
        param = {'purpose': text, 'analyze_text': analyzed}



    return render(request,'analyze.html',param)



