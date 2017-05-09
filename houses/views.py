from django.shortcuts import render
from django.views.generic import ListView, DetailView
from houses.models import House

class MajorHouseListView(ListView):
    model = House

    queryset = House.objects.filter(major=True)
    context_object_name = 'houses'


class HouseDetailView(DetailView):
    model = House

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        target = House.objects.get(id=self.kwargs['pk'])
        context['minor'] = House.objects.filter(major=False,region=target.region)
        context['house'] = target
        print(target.major)
        return context
