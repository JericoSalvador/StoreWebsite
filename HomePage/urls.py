from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShoppingView.as_view(), name='HomePage'),
    path('<slug:slug>/detail', views.ItemDetailView.as_view(), name='DetailPage'),
    path('<str:itemslug>/review', views.ReviewPage, name='ReviewPage'),
]
