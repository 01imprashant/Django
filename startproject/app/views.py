from django.shortcuts import render
from . models import project_variety,store
from . forms import project_variety_form
from django.shortcuts import get_object_or_404

# Create your views here.

def app(request):
    projects=project_variety.objects.all()
    return render(request,'app/app.html',{'projects':projects})

def app_detail(request,app_id):
    app=get_object_or_404(project_variety,pk=app_id)
    return render (request,'app/app_detail.html',{'app':app})

def app_store(request):
    stores=None
    if request.method == 'POST':
        form=project_variety_form(request.POST)
        if form.is_valid():
            project_variety=form.cleaned_data['project_variety']
            stores=store.object.filter(project_varities=project_variety)

    else:
        form=project_variety_form()    
    return render(request,'app/app_stores.html',{ 'stores': stores , 'form':form })


