# from typing_extensions import Self
from django.urls import path
from .views import PipeView, pipe_list, pipe_detail, pipe_threshold

urlpatterns = [
    path('view/', PipeView.as_view()),
    path('list/', pipe_list),
    path('detail/<int:pk>', pipe_detail),
    # path(r'threshold/(?P<value>\d+\.\d{2})/$', pipe_threshold),
    # path('/', )
]