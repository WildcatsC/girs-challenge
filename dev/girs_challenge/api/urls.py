from django.urls import path
from .views import PipeView

urlpatterns = [
    path('', PipeView.as_view())
]