from django import views
from django.views.generic import View
from django.shortcuts import render

class IndexView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'index.html')
