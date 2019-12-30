from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Plant, Pollinator
from .forms import UseForm

from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')

@login_required
def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  use_form = UseForm()
  return render(request, 'plants/detail.html', {
    'plant': plant,
    'use_form': use_form
  })


class PlantCreate(LoginRequiredMixin, CreateView):
  model = Plant
  fields = '__all__'

class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  fields = '__all__'

class PlantDelete(LoginRequiredMixin,DeleteView):
  model = Plant
  success_url = '/plants/'

def add_use(request, plant_id):
	# create the ModelForm using the data in request.POST
  form = UseForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_use = form.save(commit=False)
    new_use.plant_id = plant_id
    new_use.save()
  return redirect('detail', plant_id=plant_id)

class PollinatorsCreate(CreateView):
  model = Pollinator
  fields = '__all__'

class PollinatorsDetail(DetailView):
  model = Pollinator

class PollinatorList(ListView):
  model = Pollinator

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)