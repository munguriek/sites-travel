from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "base.html", context)


def error_404(request, exception):
        data = {}
        return render(request,'400.html', status=404)

def error_500(request):
        data = {}
        return render(request,'500.html', status=500) 
