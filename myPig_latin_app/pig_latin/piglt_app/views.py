from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def translate(request):
    #request.GET["untranslated_text"]
    #return render(request, "translate.html", )
    untranslated = request.GET['untranslated_text'].lower()
   
    translated = ""
   
    for word in untranslated.split():
        if word[0] in ["a", "e", "i", "o", "u"]:
        #vowel
            translated += word
            translated += "yay "
            

        else:
        #consonant
            translated += word[1:]
            translated += word[0]
            translated += "ay "
            


    
    #return HttpResponse(untranslated)
    #return HttpResponse(translated)
    return render(request, "translate.html",{"untranslated":untranslated, "translated":translated.title()})