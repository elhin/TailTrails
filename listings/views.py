from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Imageform

# Create your views here.
#image view / maybe just post view?
def listing_post_view(request):
    if request.method == "POST":
        form = Imageform(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = Imageform()
    return render(request, 'listing_post_view.html', {'form': form})

def success(request):
    return HttpResponse('successfully posted')