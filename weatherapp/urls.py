from django.urls import path
from weatherapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'weatherapp'

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("delete/<int:id>",views.delete_weather,name='delete')
]

urlpatterns +=staticfiles_urlpatterns()