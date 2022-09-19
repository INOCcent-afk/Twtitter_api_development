from django.urls import path
from .views import AllTweetsView

urlpatterns = [
    path('tweets/', AllTweetsView)
]
