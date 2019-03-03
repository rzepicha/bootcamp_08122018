from django.urls import path

from cars.views import car_list, car_details

urlpatterns = [

    path("",car_list),
    path('<int:id>/', car_details)
]
