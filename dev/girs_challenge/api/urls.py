# from typing_extensions import Self
from django.urls import path
from .views import PipeView, pipe_list, pipe_detail, pipe_threshold_gt, pipe_threshold_lt

urlpatterns = [
    path('view/', PipeView.as_view()),
    path('list/', pipe_list),
    path('detail/<int:pk>', pipe_detail),
    path('red/<str:risk>', pipe_threshold_gt),
    path('green/<str:risk>', pipe_threshold_lt)
]