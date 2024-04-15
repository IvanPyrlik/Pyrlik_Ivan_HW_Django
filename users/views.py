import random

from django.conf import settings
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from users.forms import UserForm, ResetPasswordForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:product_list ')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        current_site = self.request.get_host()
        subject = 'Подтверждение с регистрации'
        verification_code = ''.join(str(random.randint(0, 9)) for _ in range(8))
        user.verification_code = verification_code
        message = (f'Вы зарегистрировались, чтобы продолжить перейдите по ссылке'
                   f' http://{current_site}/users/conform/ и введите код верификации {verification_code}')
        user.save()
        send_mail(subject=subject,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[user.email])
        user.save()
        return super().form_valid(form)


class ConfirmRegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/confirm.html')

    def post(self, request, *args, **kwargs):
        verification_code = request.POST.get('verification_code')
        user = get_object_or_404(User, verification_code=verification_code)
        if user:
            user.is_active = True
            user.save()
            return redirect('users:login')
        return redirect('catalog:product_list')



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
