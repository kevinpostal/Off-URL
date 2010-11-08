from django import forms
from url.models import URL

class UploadForm(forms.ModelForm):

    #trick for giving custom attributes to forms using widgets
    da_widget = forms.widgets.TextInput(attrs={'class':"txtWatermark",'value':"enter your url"})
    link = forms.URLField(widget=da_widget)  
    
    class Meta:
        model = URL
        fields = ('link',)

