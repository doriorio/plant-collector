from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from .models import Plant

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
  return render(request, 'plants/detail.html', {'plant': plant})

class PlantCreate(CreateView):
  model = Plant
  fields = '__all__'

class PlantUpdate(UpdateView):
  model = Plant
  fields = '__all__'