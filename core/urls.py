
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views

app_name = 'core'
urlpatterns = [
    path('', core_views.home, name='home'),
    path('about-me/', core_views.about, name='about'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', core_views.contact, name='contact'),
]