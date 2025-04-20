from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_post_view, name='post lost pet')
]