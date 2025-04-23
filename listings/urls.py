from django.urls import path
from .views import (
    PetPostListView, PetPostDetailView, PetPostCreateView,
    PetPostUpdateView, LostPetListView, FoundPetListView,
    HomePageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('pets/', PetPostListView.as_view(), name='pet_list'),
    path('post/<int:pk>/', PetPostDetailView.as_view(), name='pet_detail'),
    path('post/new/', PetPostCreateView.as_view(), name='pet_create'),
    path('post/<int:pk>/edit/', PetPostUpdateView.as_view(), name='pet_update'),
    path('lost/', LostPetListView.as_view(), name='lost_pets'),
    path('found/', FoundPetListView.as_view(), name='found_pets'),
]
