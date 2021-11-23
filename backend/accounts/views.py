from django.shortcuts import render

# Create your views here.
def error_404(request, exception):
        data = {}
        return render(request,'400.html', status=404)

def error_500(request):
        data = {}
        return render(request,'500.html', status=500) 


def index(request):
    context = {}
    return render(request, "index.html", context)


def group_packages(request):
    context = {}
    return render(request, "packages-group.html", context)


def custom_packages(request):
    context = {}
    return render(request, "packages-custom.html", context)


def ticketing(request):
    context = {}
    return render(request, "ticketing.html", context)


def cars(request):
    context = {}
    return render(request, "cars.html", context)


def gallery(request):
    context = {}
    return render(request, "gallery.html", context)


def blog_list(request):
    context = {}
    return render(request, "blog_list.html", context)

def blog_detail(request):
    context = {}
    return render(request, "blog_detail.html", context)


def contacts(request):
    context = {}
    return render(request, "contacts.html", context)