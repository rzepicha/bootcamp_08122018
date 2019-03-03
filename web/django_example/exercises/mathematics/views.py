from django.shortcuts import render
from django.http import HttpResponse


def do_math(request,operation, a, b):
    result=None
    a,b=int(a), int(b)
    if operation=="add":
        result =a+b
    elif operation=="sub":
        result =a-b
    elif operation=="mul":
        result =a*b
    elif operation=="div":
        if b==0:
            result="nie dziel przez 0"
        else:
            result =a/b

    return HttpResponse(result)


# Create your views here.
