from url.forms import UploadForm
from url.models import URL
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from url.models import URL

def upload_view(request):

    if request.method == 'POST': # If the form has been submitted...
        form = UploadForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            url = form.save()
            url.generate_url()
            return HttpResponseRedirect("/url/" + url.key) # Redirect after POST
    else:
        form = UploadForm()

    
    return render_to_response('upload.html', {
        'form': form,
    })

def direct_view(request, key):
    
    url = get_object_or_404(URL, pk = key )

    return HttpResponseRedirect(url.link) # Redirect after POST
    
def show_view(request, key):

    link = get_object_or_404(URL, pk = key )
    
    context = {'link': link.short_link}
    
    return render_to_response('show.html',context)