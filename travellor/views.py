from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = "Nairobi"
    dest1.desc = "The city that never sleeps"
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Mombasa"
    dest2.desc = "The veauty of sea and beaches"
    dest2.img = 'destination_2.jpg'
    dest2.price = 1500

    dest3 = Destination()
    dest3.name = "Kisumu"
    dest3.desc = "Enjoy the fish and cast culture"
    dest3.img = 'destination_3.jpg'
    dest3.price = 1000

    dests = [dest1, dest2 , dest3]

    return render (request, 'index.html',   {'dests' : dests})
