from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Finch
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
# Create your views here


class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

# class Finch:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio

# finches = [
#     Finch("Lebron James", "https://cdn.nba.com/headshots/nba/latest/1040x760/2544.png", "4x NBA Champion"),
#     Finch("Stephen Curry", "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/3975.png&w=350&h=254", "3x NBA Champion"),
#     Finch("Giannis Antetokounmpo", "https://cdn.nba.com/headshots/nba/latest/1040x760/203507.png", "1x NBA Champion")
# ]

class FinchList(TemplateView):
    template_name = "finch_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finches'] = Finch.objects.all()
        return context


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'bio']
    template_name = "finch_create.html"
    success_url = "/finches/"

class FinchDetail(DetailView):
    model = Finch
    template_name = 'finch_detail.html'