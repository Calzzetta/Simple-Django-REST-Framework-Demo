from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EmployeeList.as_view()),
    url(r'^(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.EmployeeDetail.as_view()),
]