from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Plant
from .forms import UseForm

from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  use_form = UseForm()
  return render(request, 'plants/detail.html', {
    'plant': plant,
    'use_form': use_form
  })

class PlantCreate(CreateView):
  model = Plant
  fields = '__all__'

class PlantUpdate(UpdateView):
  model = Plant
  fields = '__all__'

class PlantDelete(DeleteView):
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
  return redirect('detail', plant_id=plan_id)