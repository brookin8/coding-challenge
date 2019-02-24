from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     url(
        r'^api/v1/referrals/(?P<pk>[0-9]+)$',
        views.get_delete_update_referral,
        name='get_delete_update_referral'
    ),
    url(
        r'^api/v1/referrals/$',
        views.get_post_referrals,
        name='get_post_referral'
    )
]