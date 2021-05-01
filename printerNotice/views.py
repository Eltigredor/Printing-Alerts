from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime
import cv2
import numpy as np
from django.http import StreamingHttpResponse

def home(request):
    return render(request, "printerNotice/home.html")

def Email_Signup(request):
    return render(request, "printerNotice/Email-Signup.html")

def hello_there(request, name):
    return render(
        request,
        'printerNotice/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

