import factory
from django.contrib.auth.models import User
from Blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

        password = "test"
        usernamr = "test"
        is_superuser = True
        is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

        title = "x"
        subtitle = "x"
        slug = "x"
        author = factory.SubFactory(User)
        content = "x"
        status = "published"
