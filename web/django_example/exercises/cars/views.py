from django.shortcuts import render
from cars.models import Car

def car_list(request):
    cars=Car.objects.all()# Car.objects.filter(is_ready=True) #jesli chce filtr
    return render(
        request=request,
        template_name="cars_list.html",
        context={'cars':cars},

    )
# Create your views here.
def car_details(request, id):
    car=Car.objects.get(pk=id)


    return render (
        request=request,
        template_name="car_details.html",
        context={'car':car}
    )