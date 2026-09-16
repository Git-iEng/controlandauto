from django.urls import path
from . import views

app_name = 'cmmsApp'

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Demo form submit
    path('request-demo/', views.request_demo_view, name='request_demo'),

    # =========================================================
    # CHANGE BY diptee - 10-Sep-2026
    # EMAIL OTP VERIFICATION - START
    # =========================================================
    path(
        'api/contact/send-email-otp/',
        views.send_email_otp,
        name='send_email_otp'
    ),
    path(
        'api/contact/verify-email-otp/',
        views.verify_email_otp,
        name='verify_email_otp'
    ),
    # =========================================================
    # CHANGE BY diptee - EMAIL OTP VERIFICATION - END
    # =========================================================

    # Main pages
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),

    # Contact form
    path('contact/thanks/', views.contact_thanks, name='contact_thanks'),
    path('contact/submit/', views.contact_block_submit, name='contact_submit'),
    path('contact/phone-info/', views.phone_info, name='phone_info'),
    path('contact/country-list/', views.country_list, name='country_list'),

    # Control and Automation pages
    path('plc/', views.gsa, name='gsa'),
    path('hmi/', views.gsafd, name='gsafd'),
    path('scada/', views.xgsfd, name='xgsfd'),
    path('vsd/', views.nets, name='nets'),
    path('dcs/', views.xgsatd, name='xgsatd'),
    path('iot/', views.sheild, name='sheild'),
    path('project/', views.sheilda, name='sheilda'),

    # Product / NEPLAN pages
    # Updated by Diptee on 16-Sep-2026: START
    # Disabled because views.py currently has no neplan_electricity() view.
    # path(
    #     'product/neplan-electricity/',
    #     views.neplan_electricity,
    #     name='neplan-electricity'
    # ),
    # Updated by Diptee on 16-Sep-2026: END

    path('product/gsafd/', views.gsafd, name='gsafd'),
    path('product/xgsfd/', views.xgsfd, name='xgsfd'),
    path(
        'neplan-asset-management/',
        views.neplan_asset_management,
        name='neplan_asset_management'
    ),

    # Existing NEPLAN contact aliases
    path(
        'neplan-gas-water-heating/contact/',
        views.contact,
        name='neplan_gas_water_heating_contact'
    ),
    path(
        'neplan-anywhere/contact/',
        views.contact,
        name='neplan_anywhere_contact'
    ),

    # Sitemap
    path('sitemap.xml', views.sitemap, name='sitemap'),
]
