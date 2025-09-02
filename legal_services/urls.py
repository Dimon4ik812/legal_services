from django.urls import path


from legal_services.views import LegislationView, ThankYouView, ConsultationDetailsView, AboutView, LegalView, \
    IndividualsView

from legal_services.apps import LegalServicesConfig


from .views import (
    IndexView,
    BlogDetailsView,
    ContactView,
    PrivacyPolicyView,
)


app_name = LegalServicesConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="home"),

    # О нас
    path('about/', AboutView.as_view(), name='about'),

    # Физическим лицам
    path('individuals/', IndividualsView.as_view(), name='individuals'),

    #Онлайн консультация
    path('consultation/', ConsultationDetailsView.as_view(), name='consultation'),

    # Поговорим о законодательстве
    path('legislation/', LegislationView.as_view(), name='legislation'),
    path('blog-details/<int:pk>/', BlogDetailsView.as_view(), name='blog_details'),

    #Юридическим лицам
    path('legal/', LegalView.as_view(), name='legal'),

    # Контакты
    path('contact/', ContactView.as_view(), name='contact'),

    # Политика конфиденциальности
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),

    # Страница благодарности
    path('thank-you/', ThankYouView.as_view(), name='thank_you'),
]

