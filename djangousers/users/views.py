from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.forms import CreateUserForm
from users.models import User


class UserListView(ListView):
    model = User
    context_object_name = "users"


class UserDetailView(DetailView):
    model = User
    context_object_name = "user"


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user-list')
    context_object_name = "user"


class UserUpdateView(UpdateView):
    model = User
    fields = ['birthday', 'random_number']
    template_name_suffix = '_update_form'


class UserCreateView(CreateView):
    model = User
    template_name_suffix = '_create_form'
    form_class = CreateUserForm
    success_url = reverse_lazy('user-list')
