from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^process-edit/', views.process_edit, name='process-edit'),
    url(r'^add-photo/', views.add_photo, name='add-photo'),
]
