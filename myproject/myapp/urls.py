
from django.urls import path
from . import views
# localhost:8000/myapp
# localhost:8000/myapp/insta
urlpatterns = [
   
    path('', views.myapp,name='myapp'),
    path('<int:app_id>/', views.app_detail,name='app_detail'),
    path('app_store/', views.app_store_view,name='app_store'),
    # path('insta/', views.insta,name='insta'),
   
]