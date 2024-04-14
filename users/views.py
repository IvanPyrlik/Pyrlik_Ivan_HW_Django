import random

from django.conf import settings
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserForm, ResetPasswordForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(subject='Поздравляем с регистрацией',
                  message='Вы зарегистрировались, добро пожаловать!',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[new_user.email])
        return super().form_valid(form)


class ResetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'users/reset_password.html'

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        send_mail(subject='Пароль восстановлен',
                  message=f'Ваш новый пароль {new_password}',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[user.email])
        user.set_password(new_password)
        user.save()
        return super().form_valid(form)
