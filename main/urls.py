from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('video', views.video, name="video"),
    path('book', views.book, name="book"),
    path('feedback', views.feedback, name="feedback"),
    path('thanks', views.thanks, name="thanks"),
    path('vidos', views.vidos, name="vidos"),
]
