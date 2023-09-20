from django.shortcuts import render

# Create your views here.


def error_404(request):
    """Error page not found"""
    return render(request, 'error/404.html', status=404)


def error_403(request):
    """Error page"""
    return render(request, 'errors/csrf.html', status=403)


def custom_error_404(request, data):
    """Custom error page not found"""
    return render(request, 'errors/404.html', data, status=404)
