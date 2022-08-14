
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import upload_video_form
import os
import csv



APPNAME='Upload_Video'

# Create your views here.
def page1(request):
    return render(request, 'index.html')

#########

def write_to_file(array):
    
    print("This is passed to write file: ", array)
    
    with open("../static/data/video_url_test_data.txt", 'a') as f:
        writer = csv.writer(f) 
#         if "watch?v=" in url:
#             url = url.replace("watch?v=", "embed/" convert url to embed
        writer.writerow(array)

def upload_video(request, arr):
    print("made it to upload video function")
    write_to_file(arr)
    return
    
    

