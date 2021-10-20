from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import BeerModel
from django.urls import reverse_lazy

# Create your views here.
class BeerList(ListView):
    model=BeerModel

class BeerDetail(DetailView):
    model=BeerModel

class BeerCreate(CreateView):
    model=BeerModel
    fields='__all__'

class UpdateBeer(UpdateView):
    model=BeerModel
    fields='__all__'

class DeleteBeer(DeleteView):
    model=BeerModel
    success_url=reverse_lazy('beermodels')
