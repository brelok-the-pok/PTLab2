from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('buy/<int:product_id>/', views.buy, name='buy'),
]
