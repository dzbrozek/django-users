# urls.py
from django.urls import path
from users.views import UserCreateView, UserDeleteView, UserDetailView, UserExportView, UserListView, UserUpdateView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-details'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('export/', UserExportView.as_view(), name='user-export'),
]
