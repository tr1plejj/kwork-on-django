# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import CustomUser
from .forms import RegisterForm, ChangeProfileForm
# from .forms import LoginForm


class Register(View):
    template_name = 'users/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})

# сначала сделал логин сам, но потом нашел встроенный класс представлений в django

# class Login(View):
#     template_name = 'users/login.html'
#
#     def get(self, request):
#         form = LoginForm()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user:
#                 login(request, user)
#                 return redirect('profile')
#         return render(request, self.template_name, {'form': form})


def profile(request, username):
    if not request.user.is_authenticated and username != 'AnonymousUser' or request.user.is_authenticated:
        user = CustomUser.objects.get(username=username)
        return render(request, 'users/profile.html', {'user_info': user})
    else:
        return redirect('login')


def find_workers(request):
    form = RegisterForm()
    profession = request.GET.get('profession')
    if profession is None or profession == '':
        workers = CustomUser.objects.all()
        return render(request, 'users/find_workers.html', {'workers': workers, 'form': form})
    workers = CustomUser.objects.filter(profession=profession)
    return render(request, 'users/find_workers.html', {'workers': workers, 'form': form})


class ProfileEdit(LoginRequiredMixin, View):
    template_name = 'users/edit_profile.html'

    def get(self, request):
        profile = get_object_or_404(CustomUser, id=request.user.id)
        form = ChangeProfileForm(instance=profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        profile = get_object_or_404(CustomUser, id=request.user.id)
        form = ChangeProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
        return render(request, self.template_name, {'form': form})
