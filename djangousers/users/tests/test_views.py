import datetime

from django.test import Client, TestCase
from django.urls import reverse
from users.factories import UserFactory
from users.models import User


class UserListViewTest(TestCase):
    def test_user_list(self):
        UserFactory.create_batch(3)

        response = self.client.get(reverse('user-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_list.html')
        self.assertEqual(response.context['users'].count(), 3)


class UserDetailViewTest(TestCase):
    def test_missing_user_details(self):
        response = self.client.get(reverse('user-details', kwargs=dict(pk=1)))

        self.assertEqual(response.status_code, 404)

    def test_user_details(self):
        user = UserFactory()

        response = self.client.get(reverse('user-details', kwargs=dict(pk=user.pk)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_detail.html')
        self.assertEqual(response.context['user'], user)


class UserDeleteViewTest(TestCase):
    def test_render_delete_page_for_missing_user(self):
        response = self.client.get(reverse('user-delete', kwargs=dict(pk=1)))

        self.assertEqual(response.status_code, 404)

    def test_delete_missing_user(self):
        client = Client(enforce_csrf_checks=False)

        response = client.post(reverse('user-delete', kwargs=dict(pk=1)))

        self.assertEqual(response.status_code, 404)

    def test_render_delete_page(self):
        user = UserFactory()

        response = self.client.get(reverse('user-delete', kwargs=dict(pk=user.pk)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_confirm_delete.html')
        self.assertEqual(response.context['user'], user)

    def test_delete_user(self):
        client = Client(enforce_csrf_checks=False)
        user = UserFactory()

        response = client.post(reverse('user-delete', kwargs=dict(pk=user.pk)))

        self.assertRedirects(response, reverse('user-list'))

        with self.assertRaises(User.DoesNotExist):
            user.refresh_from_db()


class UserUpdateViewTest(TestCase):
    def test_render_update_page_for_missing_user(self):
        response = self.client.get(reverse('user-update', kwargs=dict(pk=1)))

        self.assertEqual(response.status_code, 404)

    def test_update_missing_user(self):
        client = Client(enforce_csrf_checks=False)
        data = dict(birthday='1993-09-04', random_number='33')

        response = client.post(reverse('user-update', kwargs=dict(pk=1)), data=data)

        self.assertEqual(response.status_code, 404)

    def test_render_update_page(self):
        user = UserFactory()

        response = self.client.get(reverse('user-update', kwargs=dict(pk=user.pk)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_update_form.html')
        self.assertEqual(response.context['user'], user)

    def test_update_user(self):
        client = Client(enforce_csrf_checks=False)
        user = UserFactory()
        data = dict(birthday='1993-09-04', random_number='33')

        response = client.post(reverse('user-update', kwargs=dict(pk=user.pk)), data=data)

        self.assertRedirects(response, reverse('user-details', kwargs=dict(pk=user.pk)))

        user.refresh_from_db()

        self.assertEqual(user.birthday, datetime.date(1993, 9, 4))
        self.assertEqual(user.random_number, 33)


class UserCreateViewTest(TestCase):
    def test_render_create_page(self):
        response = self.client.get(reverse('user-create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_create_form.html')

    def test_create_user(self):
        client = Client(enforce_csrf_checks=False)
        data = dict(username='test', password='testpassword', birthday='1993-09-04')  # nosec

        response = client.post(reverse('user-create'), data=data)

        self.assertRedirects(response, reverse('user-list'))

        user = User.objects.get()

        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.birthday, datetime.date(1993, 9, 4))
        self.assertTrue(user.is_active)
        self.assertTrue(user.check_password(data['password']))


class UserExportViewTest(TestCase):
    def test_export_users(self):
        UserFactory(username='demo', birthday=datetime.date(2000, 1, 15), random_number=10)

        response = self.client.get(reverse('user-export'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            b'Username,Birthday,Eligible,Random Number,BizzFuzz\r\ndemo,15/01/2000,allowed,10,Fuzz\r\n',
        )
