from django.shortcuts import render

# Create your views here.


def get_page(request):
    """Homepage views"""
    return render(request, 'index/index.html')
