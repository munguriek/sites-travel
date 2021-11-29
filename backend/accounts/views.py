from django.shortcuts import render
from myapp.models import Accomadation, Trip
from django.contrib import messages
from myapp.models import Gallery

# Create your views here.
def error_404(request, exception):
        data = {}
        return render(request,'400.html', status=404)

def error_500(request):
        data = {}
        return render(request,'500.html', status=500) 


def index(request):
    pictures = Gallery.objects.all()
    partners = pictures.filter(category="partner")
    banners = pictures.filter(category="gallery")
    context = {
            "partners": partners,
            "banners": banners,
    }
    return render(request, "index.html", context)








