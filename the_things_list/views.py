from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .models import Thing

"""
Generic view which lists all Things on the front page
"""


class HomeView(generic.ListView):
    template_name = 'the_things_list/index.html'
    context_object_name = 'all_things'

    def get_queryset(self):
        return Thing.objects.all().order_by('lastEdit')


"""
Generic detailed view of each Thing
"""


class ThingView(generic.DetailView):
    model = Thing
    template_name = 'the_things_list/view.html'


"""
Generic view for creating new Things
"""


class CreateView(generic.edit.CreateView):
    model = Thing
    fields = ['title', 'text', 'author']

    def form_valid(self, form):
        return super(CreateView, self).form_valid(form)


"""
Generic view for deleting Things and going back to the index
"""


class DeleteThing(generic.edit.DeleteView):
    model = Thing
    success_url = reverse_lazy('the_things_list:index')
