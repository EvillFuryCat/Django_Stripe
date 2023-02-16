from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.conf import settings
from django.shortcuts import redirect

import stripe

from .models.item import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemViewList(ListView):
    model = Item
    template_name = 'payment_system/item_list.html'
    context_object_name = "items"


class ItemDetailView(DetailView):
    model = Item
    template_name = 'payment_system/item_detail.html'
    context_object_name = 'item'


class StripeCheckoutSessionView(View):
    
    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "rub",
                        "unit_amount_decimal": int(item.price * 100),
                        "product_data": {
                            "name": item.name,
                            "description": item.description,
                        },
                    },
                    "quantity": item.quantity,
                }
            ],
            metadata={"product_id": item.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "payment_system/success.html"


class CancelView(TemplateView):
    template_name = "payment_system/cancel.html"
