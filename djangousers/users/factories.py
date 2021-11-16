import datetime

import factory.fuzzy
from users.models import User

USER_PASSWORD = 'password'  # nosec


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f'user-{n}')
    email = factory.Sequence(lambda n: f'user-{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', USER_PASSWORD)
    is_active = factory.Faker('pybool')
    birthday = factory.fuzzy.FuzzyDate(datetime.date(1900, 1, 1))

    class Meta:
        model = User
        django_get_or_create = ('username',)
