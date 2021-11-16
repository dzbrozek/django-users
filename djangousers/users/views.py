import csv

from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.forms import CreateUserForm
from users.models import User
from users.templatetags.user_extras import bizz_fuzz, is_allowed


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


class UserExportView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        users = User.objects.all()
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="users.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
        for user in users:
            writer.writerow(
                [
                    user.username,
                    user.birthday.strftime('%d/%m/%Y'),
                    is_allowed(user.birthday),
                    user.random_number,
                    bizz_fuzz(user.random_number),
                ]
            )

        return response
