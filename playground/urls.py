from django.urls import path
from . import views

#urlConfig
# mapping for the endpoints to the function which will return data
urlpatterns = [
    path('hello/', views.say_hello),
    path('html/', views.say_helloHtml)
]

