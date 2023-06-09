from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', head_page, name='home'),
    path('hi/', hi, name='hi'),
    path('categories/', details_list),
    path('about/', about, name='about'),
    path('categories/displays/', displays),
    path('categories/displays/IPhone/', displays),
    re_path(r'^displays/IPhone/(?P<IPhone_model>[0-1]{1}[0-3]{1}|[0-1]{1}[0-3]{1}Pro|6sPlus|[0-1]{1}[0-3]{1}ProMax|XSMax|[0-1]{1}[0-3]{1}Max|[5-6]{1}s|[5-8]|[6-8]{1}Plus|XS|X|XR)/', displays_exect)
]