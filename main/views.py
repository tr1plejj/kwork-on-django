from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import OrderForm
from .models import Order, Profile


def index(request):
    orders = Order.objects.all()
    form = OrderForm()
    return render(request, 'main/index.html', {'orders': orders, 'form': form})


def order_detail(request, pk):
    if not request.user.is_authenticated:
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'main/order_detail.html', {'order': order})
    else:
        order = get_object_or_404(Order, pk=pk)
        user_offers = Profile.objects.get(user=request.user).offers.all()
        return render(request, 'main/order_detail.html', {'order': order, 'user_offers': user_offers})


def search_results(request):
    query = request.GET.get('orders')
    prof = request.GET.get('who_needs')
    form = OrderForm()
    orders = Order.objects.filter(title__contains=query, who_needs=prof)
    return render(request, 'main/index.html', {'orders': orders, 'form': form})


@login_required
def buyer_page(request):
    user_orders = Profile.objects.get(user=request.user).orders.all()
    return render(request, 'main/buyer_page.html', {'orders': user_orders})


@login_required
def seller_page(request):
    user_offers = Profile.objects.get(user=request.user).offers.all()
    return render(request, 'main/seller_page.html', {'offers': user_offers})


class OrderAction(LoginRequiredMixin, View):

    def get(self, request, pk):
        return redirect('order_detail', pk=pk)

    def post(self, request, pk):
        user_profile = Profile.objects.get(user=request.user)
        order = Order.objects.get(pk=pk)
        data = request.POST
        action = data.get('order')
        print(action)
        if action == 'delete':
            user_offers = user_profile.offers.all()
            if request.user != order.author:
                if order not in user_offers:
                    return redirect('index')
                else:
                    order.delete()
                    return redirect('buyer')
            order.delete()
            return redirect('buyer')
        elif action == 'add':
            if request.user == order.author:
                return redirect('buyer')
            else:
                user_profile.offers.add(order)
                return redirect('seller')
        elif action == 'cancel':
            user_profile.offers.remove(order)
            return redirect('seller')
        return redirect('order_detail', pk=pk)


class CreateOrder(LoginRequiredMixin, View):
    template_name = 'main/create_order.html'

    def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()
            author_profile = Profile.objects.get(user=order.author)
            author_profile.orders.add(order)
            return redirect('buyer')
        form = OrderForm()
        return render(request, self.template_name, {'form': form})


class OrderEdit(LoginRequiredMixin, View):
    template_name = 'main/order_edit.html'

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(instance=order)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()
            return redirect('order_detail', pk=pk)
        return render(request, self.template_name, {'form': form})




# @login_required
# def cancel_offer(request, order_pk):
#     if request.method == 'POST':
#         order = Order.objects.get(pk=order_pk)
#         user_profile = Profile.objects.get(user=request.user)
#         user_profile.offers.remove(order)
#         return redirect('seller')
#     return redirect('order_detail', pk=order_pk)
#
# @login_required
# def delete_order(request, order_pk):
#     if request.method == 'POST':
#         order = Order.objects.get(pk=order_pk)
#         user_offers = Profile.objects.get(user=request.user).offers.all()
#         if request.user != order.author:
#             if order not in user_offers:
#                 return redirect('index')
#             else:
#                 order.delete()
#                 return redirect('buyer')
#         else:
#             order.delete()
#             return redirect('buyer')
#     return redirect('order_detail', pk=order_pk)
#
# @login_required
# def add_offer(request, order_pk):
#     if request.method == 'POST':
#         order = Order.objects.get(pk=order_pk)
#         if request.user == order.author:
#             return redirect('buyer')
#         else:
#             Profile.objects.get(user=request.user).offers.add(order)
#             return redirect('seller')
#     return redirect('order_detail', pk=order_pk)
#
# class AddOffer(LoginRequiredMixin, View):
#
#     def get(self, request, order_pk):
#         return redirect('order_detail', pk=order_pk)
#
#     def post(self, request, order_pk):
#         order = Order.objects.get(pk=order_pk)
#         if request.user == order.author:
#             return redirect('buyer')
#         else:
#             Profile.objects.get(user=request.user).offers.add(order)
#             return redirect('seller')