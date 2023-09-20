from django.shortcuts import render
from finsync.decorators import custom_login_required

# Create your views here.


@custom_login_required
def get_page(request, data):
    """Get tax views"""
    return render(request, 'tax/index.html', data)
