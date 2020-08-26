from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')
def analyse(request):
    djText=request.GET.get('textarea','No text is entered')
    djPunc=request.GET.get('removepunc','off')
    djUppercase=request.GET.get('uppercase','off')
    djSpaceremover=request.GET.get('extraspaceremover','off')
    analyze=djText
    newText=""
    
    if djPunc=='on':
        analyze=""
        for char in djText:
            if char not in string.punctuation:
                analyze=analyze+char
        newText=analyze            
    if djUppercase=='on':
        analyze=analyze.upper()
        newText=analyze    
    if djSpaceremover=='on':
        analyze=""
        for index,char in enumerate(newText):
            if not(newText[index]==' ' and newText[index+1]==' '):
                analyze=analyze+newText[index]
        djText=newText   
    if djText=='':
        analyze='No text entered' 
    paramater={'analyzeText':analyze,'removepunch':djPunc}
    return render(request,'analyse.html',paramater)
