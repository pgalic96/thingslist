import datetime

from django.utils import timezone

from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import Thing


# Create your views here.
class HomeView(generic.ListView):
    template_name = 'the_things_list/index.html'
    context_object_name = 'all_things'

    def get_queryset(self):
        return Thing.objects.all()


class ThingView(generic.DetailView):
    model = Thing
    template_name = 'the_things_list/view.html'


class CreateView(generic.edit.CreateView):
    model = Thing
    fields = ['title', 'text', 'author']

    def form_valid(self, form):
        return super(CreateView, self).form_valid(form)


class DeleteThing(generic.edit.DeleteView):
    model = Thing
    success_url = reverse_lazy('the_things_list:index')