from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


# Create your views here.

def index(request):
    """pizzas = Pizza.objects.all()
    pizzas_names_prices = [pizza.nom + ": " + str(pizza.prix)  + "$" for pizza in pizzas]
    pizzas_names_prices_str = '- '.join(pizzas_names_prices)
    return HttpResponse(" Yes Les Pizza : " + pizzas_names_prices_str)"""

    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas': pizzas})
