from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.utils.crypto import get_random_string
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
        r_str = get_random_string(length=32)
        # current_domain = Site.objects.get_current().domain
        full_url = "127.0.0.1:8000/edit/" + r_str
        #while Thing.objects.filter(random_str=r_str) is not 0:
         #   r_str = get_random_string(length=32)
        form.instance.random_str = r_str
        send_mail('link for editing', full_url, 'from@example.com', [form.instance.author], fail_silently=False)
        return super(CreateView, self).form_valid(form)


"""
Generic view for deleting Things and going back to the index
"""


class DeleteThing(generic.edit.DeleteView):
    model = Thing
    success_url = reverse_lazy('the_things_list:index')


class UpdateThing(generic.edit.UpdateView):
    #model = Thing
    fields = ['title', 'text']
    template_name = 'the_things_list/thing_form.html'

    def get_object(self, queryset=None):
        return Thing.objects.get(random_str=self.kwargs.get('random_str'))
