from django.urls import path
from .views import home, chatbot_response

urlpatterns = [
    path('', home, name='home'),
    path('chat/', chatbot_response, name='chatbot_response'),
]
