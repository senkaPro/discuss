from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.LinkCreateView.as_view(), name='link-create'),
    path('submitted/<int:pk>/',views.LinkDetail.as_view(),name='link-detail'),
    path('delete/<int:pk>/', views.LinkDelete.as_view(), name='link-delete'),
    path('',views.LinkList.as_view(),name='user-links'),
]
