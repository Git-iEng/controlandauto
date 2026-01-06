# In iEngApp/urls.py
from django.urls import path
from . import views
from .views import contact_section
app_name = 'cmmsApp'
from .views import request_demo_view

urlpatterns = [
      path("request-demo/", views.request_demo_view, name="request_demo"),
    # path("contact-thanks/", views.thanks_view, name="contact_thanks"),  # if you add a separate thanks view for demo
    path('', views.home, name='home'),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
   

    # path('contact/', views.contact, name='contact'),
    # path("contacts/", views.contact_section, name="contact_section"),
path("product/", views.product, name="product"),
   path("contact/", views.contact, name="contact"),
    path('about/', views.about, name='about'),
    # path('contacts/', views.contact_section, name='contact_section'),
    path('contact/thanks/', views.contact_thanks, name='contact_thanks'),
    
    # More URLs
     # --- NEW: consulting block form + helper ---
    path("contact/submit/", views.contact_block_submit, name="contact_submit"),
    path("contact/phone-info/", views.phone_info, name="phone_info"),
    path('plc/', views.gsa, name='gsa'),


     path('hmi/', views.gsafd, name='gsafd'),

     path('product/neplan-electricity/', views.neplan_electricity, name='neplan-electricity'),
     path('product/gsafd/', views.gsafd, name='gsafd'),
    path("contact/country-list/", views.country_list, name="country_list"),
path('scada/', views.xgsfd, name='xgsfd'),
path('services/', views.services, name='services'),
# path('neplan-additional-solutions/', views.neplan_additional_solutions, name='neplan_additional_solutions'),

path('vsd/', views.nets, name='nets'),
path('dcs/', views.xgsatd, name='xgsatd'),
path('iot/', views.sheild, name='sheild'),
path("sitemap.xml", views.sitemap, name="sitemap"),

path('product/xgsfd/', views.xgsfd, name='xgsfd'),
path('neplan-asset-management/', views.neplan_asset_management, name='neplan_asset_management'),

path('product/sheilda/', views.sheilda, name='sheilda'),
    # contact section
    path('contact/', views.contact, name='contact'),
    path('neplan-gas-water-heating/contact/', views.contact, name='contact'),
    path('neplan-anywhere/contact/', views.contact, name='contact'),
      # path('neplan-additional-solutions/contact/', views.contact, name='contact'),

]
