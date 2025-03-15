from django.shortcuts import render
from .models import project_variety
from django.shortcuts import get_object_or_404

# Create your views here.

def app(request):
    projects=project_variety.objects.all()
    return render(request,'app/app.html',{'projects':projects})

def app_detail(request,app_id):
    app=get_object_or_404(project_variety,pk=app_id)
    return render (request,'app/app_detail.html',{'app':app})


