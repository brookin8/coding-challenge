from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     url(
        r'^api/referrals/(?P<pk>[0-9]+)$',
        views.get_delete_update_referral,
        name='get_delete_update_referral'
    ),
    url(
        r'^api/referrals/$',
        views.get_post_referrals,
        name='get_post_referrals'
    ),
     url(
        r'^api/referrals/click/(?P<pk>[0-9]+)$',
        views.increment_referral_click,
        name='increment_referral_click'
    ),
]