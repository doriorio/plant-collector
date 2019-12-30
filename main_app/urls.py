from django.urls import path
from . import views



urlpatterns = [
    path('', views.plants_index, name='index'),
    path('about/', views.about),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plant_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('pollinators/create/', views.PollinatorsCreate.as_view(), name='pollinators_create'),
    path('pollinators/pollinators_list/', views.PollinatorList.as_view(), name='pollinators_list'),
    path('pollinators/<int:pk>/', views.PollinatorsDetail.as_view(), name='pollinators_detail'),
    path('plants/<int:plant_id>/add_use/', views.add_use, name='add_use'),
    path('accounts/signup/', views.signup, name='signup'),

]