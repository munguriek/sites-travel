from django.shortcuts import render
from myapp.models import Accomadation, Package, Transport, Ticket
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
    partners = Gallery.objects.filter(category="partner")
    context = {"partners": partners}
    return render(request, "index.html", context)








