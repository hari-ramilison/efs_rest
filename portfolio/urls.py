from django.conf.urls import url
from . import views, admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'portfolio'
urlpatterns = [

    path('', views.customer_list),
    url(r'^api/customers/$', views.customer_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.getCustomer),
    path('investments/', views.investment_list),
    url(r'^api/investments/$', views.investment_list),
    url(r'^api/investments/(?P<pk>[0-9]+)$', views.getInvestment),
    path('stocks/', views.stock_list),
    url(r'^api/stocks/$', views.stock_list),
    url(r'^api/stocks/(?P<pk>[0-9]+)$', views.getStock)
]

urlpatterns = format_suffix_patterns(urlpatterns)