from django.shortcuts import render
from django.http import JsonResponse
from .models import * 

# Create your views here.
def get_technologies_by_category(request, category):
    technologies = Technology.objects.filter(category=category)
    technology_data = [{'name': tech.name} for tech in technologies]
    return JsonResponse(
        technology_data,
        safe=False
    )

def home(request):
    context = {
      'projects': Project.objects.all()
    }
    return render(request, 'main/index.html', context)
