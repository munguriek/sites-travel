from django.shortcuts import render
from myapp.models import Accomadation, Package, Transport, Ticket

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


def login(request):
        return render(request, "admin/login.html")





def main(request):
    """Index page for admin panel."""
    group_packages = Package.objects.filter(type="group").count()
    custom_packages = Package.objects.filter(type="custom").count()

    accom_budget = Accomadation.objects.filter(budget="budget").count()
    accom_mid_range = Accomadation.objects.filter(budget="mid range").count()
    accom_up_market = Accomadation.objects.filter(budget="up market").count()

    trans_budget = Transport.objects.filter(budget="budget").count()
    trans_mid_range = Transport.objects.filter(budget="mid range").count()
    trans_up_market = Transport.objects.filter(budget="up market").count()

    trans_driver = Transport.objects.filter(driver="driver").count()
    trans_self = Transport.objects.filter(driver="self").count()

    trans_town = Transport.objects.filter(driver="town service").count()
    trans_upcountry = Transport.objects.filter(driver="upcountry").count()

    one_way_tickets = Ticket.objects.filter(type="town service").count()
    return_tickets = Ticket.objects.filter(type="upcountry").count()

    context = {
            "group_packages": group_packages,
            "custom_packages": custom_packages,
            "accom_budget" : accom_budget,
            "accom_mid_range": accom_mid_range,
            "accom_up_market": accom_up_market,
            "trans_budget" : trans_budget,
            "trans_mid_range": trans_mid_range,
            "trans_up_market": trans_up_market,
            "trans_driver": trans_driver,
            "trans_self": trans_self,
            "trans_town": trans_town,
            "trans_upcountry": trans_upcountry,
            "one_way_tickets": one_way_tickets,
            "return_tickets": return_tickets,
    }
    return render(request, "admin/main.html", context) 
