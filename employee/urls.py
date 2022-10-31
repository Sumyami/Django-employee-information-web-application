from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('display/',views.display,name='display'),
    path('insert/',views.insert,name='insert'),
    path('<int:id>/update/',views.update,name='update'),
    path('<int:id>/delete/',views.delete,name='delete')
]