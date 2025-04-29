from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import PetPost, Author
from .forms import PetPostForm, RegisterForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

## used this to try and get user https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-editing/#models-and-request-user

class PetPostListView(ListView):
    model = PetPost
    template_name = 'listings/pet_list.html'
    context_object_name = 'pets'
    
    def get_queryset(self):
        return PetPost.objects.filter(is_resolved=False).order_by('-created_date')

class PetPostDetailView(DetailView):
    model = PetPost
    template_name = 'listings/pet_detail.html'
    context_object_name = 'pet'

### ADD NEW PET LISTING
class PetPostCreateView(CreateView, LoginRequiredMixin):
    model = PetPost
    form_class = PetPostForm
    template_name = 'listings/pet_form.html'
    success_url = reverse_lazy('pet-list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user        
        return super().form_valid(form)

class PetPostUpdateView(UpdateView):
    model = PetPost
    form_class = PetPostForm
    template_name = 'listings/pet_form.html'
    success_url = reverse_lazy('pet-list')


class LostPetListView(ListView):
    model = PetPost
    template_name = 'listings/lost_pets.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return PetPost.objects.filter(status='lost', is_resolved=False).order_by('-created_date')

class FoundPetListView(ListView):
    model = PetPost
    template_name = 'listings/found_pets.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return PetPost.objects.filter(status='found', is_resolved=False).order_by('-created_date')
    
    from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'listings/home.html'

## user/account management stuff
def logout_view(request):
    logout(request)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/pets")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form":form})

