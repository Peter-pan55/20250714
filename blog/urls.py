from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('nuevo/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_edit'),
]
    
