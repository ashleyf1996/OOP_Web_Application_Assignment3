import os

from django.conf import settings
from django.contrib import messages
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from .forms import CreateEventForm
from .models import *
from django.views.generic import View
from django.views import generic
from .forms import UserForm
from django.http import HttpResponse
from django.core.exceptions import *


# the index page

class index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


# Shows whats on
class EventView(View):
    def get(self, request):
        context = {
            'types': Type.objects.all(),
            'cities': Cities.objects.all()
        }

        return render(request, 'event.html', context)

    def post(self, request):
        type = request.POST['type']
        location = request.POST['location']

        # Now we gotta do a little do do do do dooooo search

        events = Event.objects.all().filter(event_type=type, event_location=location)

        if events:
            context = {
                'search_events': events
            }

            return render(request, 'event.html', context)


        else:
            messages.warning(request, "Cannot find any events")
            return redirect('event')





def city(request):
    all_cities = Cities.objects.all()
    html = ''

    for city in all_cities:
        html += '<a href=">' + city.town_name + '</a><br>'
    return HttpResponse(html)


class CreateEvent(View):
    def get(self, request):

        # this filters out who can make an event
        if request.user.is_authenticated():
            form = CreateEventForm()
            context = {
                "form": form,
                "cities": Cities.objects.all(),
                "types": Type.objects.all()
            }
            print(context)
            return render(request, 'event_form.html', context)
        else:
            messages.warning(request, "sorry! you must be logged in to do that")
            # this redirects the user back to login
            return redirect('login')

    def post(self, request):
        event_name = request.POST['event_name']
        event_location = request.POST['event_location']
        event_type = request.POST['event_type']
        event_address = request.POST['event_address']
        event_creator = request.POST['event_creator']


        full_filename = os.path.join(settings.MEDIA_ROOT, settings.MEDIA_ROOT, request.FILES['upload_photo'].name)

        fout = open(full_filename, 'wb+')

        file_content = ContentFile(request.FILES['upload_photo'].read())

        # Iterate through the chunks.
        for chunk in file_content.chunks():
            fout.write(chunk)
        fout.close()
        user = request.user
        # Make sure the user is logged in properly
        if request.user.is_authenticated():
            event = Event(event_name=event_name, event_location=event_location,event_address=event_address,event_creator=event_creator,
                       event_type=event_type, upload_photo=request.FILES['upload_photo'].name)



            event.save()

            if event is not None:
                messages.success(request, "Thank you %s! Event added successfully!"% request.user)

                return redirect('event')
            else:
                messages.warning(request, "Please add an event")


class Logout(View):
    def get(self, request):
        # Log the user out. If they are logged in
        if request.user.is_authenticated:
            # Log them out
            user = request.user
            logout(request)

            messages.success(request, "Bye %s You have now been logged out, Danke :)!" % user)
            return redirect('index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # display blank form new user coming to site
    def get(self, request, ):
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
                    messages.success(request, "You have registered successfully and are now logged in.")

                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # If the user is authenticated
        if user is not None:
            login(request, user)
            messages.success(request, '%s you are now logged in.' % username)
            return redirect('index')
        else:
            messages.warning(request, 'Invalid username or password. Please make sure you are registered!')
            return redirect('login')
