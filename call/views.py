from django.shortcuts import render
import requests

def show(request):
    response=requests.get('http://127.0.0.1:8000/api/basic/')
    todos=response.json()
    return render(request,'index.html',{'user':todos})
