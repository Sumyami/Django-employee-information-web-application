from django.contrib import admin
from django.urls import include,path
urlpatterns = [ 
    path('books/', include('books.urls')),
    path('poll/',include('poll.urls')),
    path('polls/',include('polls.urls')),
    path('sam/',include('sam.urls')),
    path('store/',include('store.urls')),
    path('blogapp/',include('blogapp.urls')),
    path('BookOnline/',include('BookOnline.urls')),
    path('item/',include('item.urls')),
    path('employee/',include('employee.urls')),
    path('bus/',include('bus.urls')),
    path('admin/', admin.site.urls)
]