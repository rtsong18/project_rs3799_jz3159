from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def GET(request):
    return render(request, 'index.html')
def POST(request):
    return render(request, 'index.html')
