from pandas import read_csv
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os
import csv
import json

APPNAME='Video_Player'

# Create your views here.
def page1(request):
    return render(request, 'index.html')
#----------------------------------------------------------------
# DEFAULT_LIST= '''{
# "columns": [0, 1, 2, 3],
# "values" : [
#     ["id1", "Matrix Multip", "", "https://www.youtube.com/embed/LXKku-IbSak", "Math"],
#     ["id2", "Life goes on ", "", "https://www.youtube.com/embed/Hg7BGS7ap3I", "Philosophy"],
#     ["id3", "Mistake/Mystique", "", "https://www.youtube.com/embed/VQrhl7KJ0m4", "Philosophy"]
# ]
# }'''

def getlist():
    urls_list = {"columns": [], "values": []}  
    with open("./static/data/sci_video_url_data.txt", 'r') as f:
        reader = csv.reader(f, delimiter=',', skipinitialspace=True)
        next(reader)
        for row in reader:
            urls_list["values"].append(row)
            urls_list["columns"] = [c for c in range(len(urls_list["values"][0]))]   
    return urls_list

def getmenu(request, topic=None, **kwargs):
    print(f"Getting menu for topic: {topic}")
    
    default_list = json.dumps(getlist())  
    
    # return HttpResponse( DEFAULT_LIST )
    return HttpResponse( default_list )





