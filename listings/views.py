from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import PetPost
from .forms import PetPostForm

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

class PetPostCreateView(CreateView):
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

