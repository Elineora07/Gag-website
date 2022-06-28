from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class RegistrationView(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Ro'yhatdan o'tish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistrationForm
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, _("Siz muvaffaqiyatli ro'yhatdan o'tdingiz"))
            return redirect('main:index')
        return render(request, 'layouts/form.html', {
            'form': form
        })


class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Tizimga kirish")

    def get(self, request):
        form = LoginForm()
        return render(request, 'layouts/form.html', {
            'form': form
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                messages.success(request, _("Xush kelibsiz"))
                return redirect('main:index')

            form.add_error('password', _("Login va/yoki parol noto'g'ri"))

        return render(request, 'layouts/form.html', {
            'form': form
        })

@login_required()
def client_logout(request):
    messages.success(request, _("Xayr"))
    logout(request)

    return redirect('main:index')
