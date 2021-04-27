# I have created this file - Anuj
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('''<h1>Home Page</h1>
    #  <a href="removepunc" > removepunc </a><br/>
    #  <a href="capitalizefirst"> capitalizefirst </a><br/>
    #  <a href="newlineremove"> newlineremove </a><br/>
    #  <a href="spaceremove"> spaceremove </a><br/>
    #  <a href="charcount"> charcount </a>''')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    
    #Removing Punctuation
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose':'Removed Punctuation', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', param)
    

    #Capitalization
    elif fullcaps == 'on':
        djtext = djtext.upper()
        param = {'purpose':'Capitalization', 'analyzed_text':djtext}
        return render(request, 'analyze.html', param)
    


    #Removing New Lines
    elif (newlineremove == "on"):
        # analyzed = ""
        # for char in djtext:
        #     if char != "\n":
        #         analyzed = analyzed + char
        djtext = djtext.replace('\r\n', "")
        param = {'purpose':'Removing New Lines', 'analyzed_text':djtext}
        return render(request, 'analyze.html', param)


    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        param = {'purpose':'Removing Extra Spaces', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', param)


    else:
        return HttpResponse('''Error <br/><a href="/"> Back  </a>''')
    
    # return HttpResponse('''Remove Punctuation <br/>
    # <a href="/"> Back  </a>''')

# def capitalizefirst(request):
#     return HttpResponse('''Capitalize First<br/>
#     <a href="/"> Back  </a>''')

# def newlineremove(request):
#     return HttpResponse('''New Line Remove<br/>
#     <a href="/"> Back  </a>''')

# def spaceremove(request):
#     return HttpResponse('''Space Remove<br/>
#     <a href="/"> Back  </a>''')

# def charcount(request):
#     return HttpResponse('''Character Count<br/>
#     <a href="/"> Back  </a>''')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')