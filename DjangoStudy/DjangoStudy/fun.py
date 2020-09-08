
from  django.shortcuts import HttpResponse,redirect, render
# def home(request):
#     return HttpResponse("你好")
def home(request):
    return render(request,"home.html")

def count(request):
    text=request.GET['text']
    num=len(request.GET['text'])

    word_dict={}
    for word in text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word] += 1
    sort_word=sorted(word_dict.items(),key=lambda key:key[1],reverse=True)
    return render(request,"count.html",{'num':num,"text":text,'sort_word':sort_word})
