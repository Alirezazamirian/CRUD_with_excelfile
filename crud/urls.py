from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_excel, name='excel_upload'),
    path('people/', views.PostListView.as_view(), name='post_list'),
    path('people/create/', views.PostCreateView.as_view(), name='post_create'),
    path('people/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('people/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('invalid-url/', views.invalid_url, name='invalid_url'),
]
