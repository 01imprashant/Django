from django.shortcuts import render
from .models import myapp_variety,store
from django.shortcuts import get_object_or_404
from .forms import myapp_variety_form

# Create your views here.

def myapp(request):
    passes=myapp_variety.objects.all()
    return render(request,'myapp/myapp.html',{'passes':passes})

def app_detail(request,app_id):
    apps=get_object_or_404(myapp_variety,pk=app_id)
    return render(request,'myapp/app_detail.html',{'apps':apps})

def app_store_view(request):
    stores=None
    if request.method=='POST':
        form=myapp_variety_form(request.POST)
        if form.is_valid():
            app_variety=form.cleaned_data['app_variety']
            stores=store.objects.filter(app_varieties=app_variety)
    else:
        form=myapp_variety_form()                
    return render(request,'myapp/app_store.html',{'stores':stores,'form':form})

