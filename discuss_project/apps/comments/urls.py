from django.urls import path
from . import views
urlpatterns = [
    path('new-comment/', views.CommentCreateView.as_view(), name='new-comment'),
]
