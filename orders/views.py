from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal

        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            total_price=total,
            payment_status='pending',
        )

        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['product'].price,
            )

        request.session['cart'] = {}

        return redirect('order_success', order_number=order.order_number)

    return render(request, 'checkout.html', {
        'items': items,
        'total': total,
    })


@login_required
def order_success(request, order_number):
    order = get_object_or_404(
        Order,
        order_number=order_number,
        user=request.user
    )

    return render(request, 'order_success.html', {
        'order': order,
    })


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'my_orders.html', {
        'orders': orders
    })