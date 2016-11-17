from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'enterance', views.enterance, name='enterance'),
    url(r'^escape', views.escape, name='escape'),
    url(r'^FAQs.html', views.faq),
    url(r'^fjc', views.fjc, name='fjc'),
    url(r'^home', views.home, name='home'),
    url(r'^incident-log.html',views.index,name='incident'),
    url(r'^index', views.index, name='index'),
    url(r'^log-in.html', views.login),
    url(r'^phone-safe.html', views.phoneSafe),
    url(r'^portal', views.portal, name='portal'),
    url(r'^prepare-visit.html', views.prepare),
    url(r'^registration.html', views.reg),
    url(r'^secret', views.secret, name='secret'),
    url(r'^testimonial.html', views.testimonial, name='testimonial'),
    url(r'^tip-remove.html', views.tipR),
    url(r'^', views.index),
]