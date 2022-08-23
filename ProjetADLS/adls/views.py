from django.shortcuts import render

# Create your views here.
def whoweare(request):
    return render(request, 'who-we-are.html')