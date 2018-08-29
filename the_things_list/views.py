from django.shortcuts import render
from django.views import generic
from .models import Thing

# Create your views here.
class HomeView(generic.ListView):
    template_name = 'the_things_list/index.html'
    context_object_name = 'all_things'

    def get_queryset(self):
        return Thing.objects.all()
