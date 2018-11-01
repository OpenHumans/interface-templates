from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Starting page for app.
    """
    return render(request, 'templating/index.html')


def index_logged_in(request):
    """
    Starting page for app.
    """
    return render(request, 'templating/index_logged_in.html')


def about(request):
    """
    Starting page for app.
    """
    return render(request, 'templating/about.html')
