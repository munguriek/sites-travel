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


