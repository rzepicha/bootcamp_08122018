from django.urls import path

from mathematics.views import do_math

urlpatterns = [
    path('<operation>/<a>/<b>', do_math)
]