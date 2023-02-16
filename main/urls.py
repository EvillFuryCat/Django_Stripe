from django.urls import path
from main.admin import payment_system_site
from main.views import ItemDetailView, ItemViewList, StripeCheckoutSessionView, SuccessView, CancelView


app_name = 'main'

urlpatterns = [
    path('', ItemViewList.as_view(), name='item-list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path(
        'create-checkout-session/<int:pk>/',
        StripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]
