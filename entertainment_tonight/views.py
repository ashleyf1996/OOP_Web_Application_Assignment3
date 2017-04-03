
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import CreateEventForm
from .models import Event
from django.views.generic import View
from django.views import generic
from .forms import UserForm
from django.http import HttpResponse

def index(request):
    all_events = Event.objects.all()
    return render(request, 'index.html', {'all_events': all_events})


class DetailView(generic.DeleteView):
    model = Event
    template_name = 'detail.html'


class EventCreate(CreateView):
    model = Event
    fields = ['event_name', 'event_type', 'event_location']


def home(request):
    form = CreateEventForm()
    context = {
        "form": form
    }
    return render(request, 'event_form.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'


    # display blank form new user coming to site
    def get(self, request,):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    # whenthe user hits submit
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # creates an object from a form
            user = form.save(commit=False)

            # cleaned(normalised data)
            # data that is formatted properly

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # change users password
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct - nboston
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    html = "<html><body>hi</body></html>"
                    return HttpResponse(html)

        return render(request, self.template_name, {'form': form})















