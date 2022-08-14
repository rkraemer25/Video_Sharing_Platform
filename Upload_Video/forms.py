from django import forms 

class upload_video_form(forms.Form):
    vname = forms.CharField(required=True)
    vurl = forms.CharField(required=True)
    vtag = forms.CharField(required=True)
    