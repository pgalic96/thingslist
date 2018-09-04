from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import generic

from .forms import ContactForm
from .models import Thing

"""
Generic view which lists all Things on the front page
"""


class HomeView(generic.ListView):
    template_name = 'the_things_list/index.html'
    context_object_name = 'all_things'

    def get_queryset(self):
        # Getting all Thing objects in the home page ordered by the last edit
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
        # random 32 character long string is created
        r_str = get_random_string(length=32)
        # get a site domain
        current_domain = Site.objects.get_current().domain
        # generate a full editing url
        full_url = current_domain + "/edit/" + r_str
        # save random token to the Thing object for future mapping
        form.instance.random_str = r_str
        # send an email to the user with editing url
        send_mail('link for editing', full_url, 'from@example.com', [form.instance.author], fail_silently=False)
        return super(CreateView, self).form_valid(form)


"""
Generic view for deleting Things and going back to the index
"""


class DeleteThing(generic.edit.DeleteView):
    success_url = reverse_lazy('the_things_list:index')

    # override get_object method such that the object is not matched by pk and therefore deleted
    def get_object(self, queryset=None):
        return Thing.objects.get(random_str=self.kwargs.get('random_str'))


"""
Generic view for editing Thing
"""


class UpdateThing(generic.edit.UpdateView):
    fields = ['title', 'text']
    template_name = 'the_things_list/updatething_form.html'

    # Override get_object() method such that we can use random token instead of pk in link
    def get_object(self, queryset=None):
        return Thing.objects.get(random_str=self.kwargs.get('random_str'))


"""
Generic View with for contacting the author of Thing.
Uses get() method to get the Thing object for which the user wants to contact the author.
Uses post() method to send an e-mail to the author of the Thing.
"""


class ContactView(generic.View):
    template_name = 'the_things_list/contact_form_template.html'
    form_class = ContactForm

    def get(self, request, pk):
        thing = Thing.objects.get(pk=pk)
        return render(request, self.template_name, {'thing': thing})

    def post(self, request, pk):
        form = self.form_class(request.POST)
        thing = Thing.objects.get(pk=pk)
        if form.is_valid():
            message = form.cleaned_data['message']
            author = form.cleaned_data['author']
            send_mail('Contact message', 'Message regarding your Thing: ' + thing.title + '\n ' + message, author,
                      [thing.author], fail_silently=False)

        return redirect('the_things_list:thing-details', pk=pk)
