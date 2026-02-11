from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'main/index.html')  


def home(request):
    return render(request, 'main/index2.html')