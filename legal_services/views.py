import os

from django.core.mail import send_mail

from django.urls import reverse_lazy

from django.views.generic import ListView, TemplateView, DetailView, FormView
from dotenv import load_dotenv
import logging

from legal_services.forms import AppointmentForm
from legal_services.models import Legislation

load_dotenv(override=True)


logger = logging.getLogger(__name__)



class IndexView(ListView):
    model = Legislation
    template_name = 'legal_services/home.html'
    context_object_name = 'objects'


class IndividualsView(FormView):
    template_name = 'legal_services/individuals.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('legal_services:thank_you')  # страница благодарности

    def form_valid(self, form):
        # Получаем данные из формы
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone_number']
        subject = form.cleaned_data['msg_subject']
        message = form.cleaned_data['message']

        # Собираем текст письма
        body = f"""
                Новое сообщение от клиента:

                Имя: {name}
                Email: {email}
                Телефон: {phone}
                Тема: {subject}
            """
        # Отправляем письмо
        send_mail(
            subject='Новое сообщение с сайта',
            message=body,
            from_email=os.getenv("FROM_EMAIL"),  # от кого
            recipient_list=[os.getenv("RECIPIENT")],  # куда
            fail_silently=False,
        )

        return super().form_valid(form)

class ConsultationDetailsView(FormView):
    template_name = 'legal_services/consultation.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('legal_services:thank_you')  # страница благодарности

    def form_valid(self, form):
        # Получаем данные из формы
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone_number']
        subject = form.cleaned_data['msg_subject']
        message = form.cleaned_data['message']

        # Собираем текст письма
        body = f"""
        Новое сообщение от клиента:

        Имя: {name}
        Email: {email}
        Телефон: {phone}
        Тема: {subject}
        Сообщение: {message}
        """

        # Отправляем письмо
        send_mail(
            subject='Новое сообщение с сайта',
            message=body,
            from_email=os.getenv("FROM_EMAIL"),  # от кого
            recipient_list=[os.getenv("RECIPIENT")],  # куда
            fail_silently=False,
        )

        return super().form_valid(form)


class AboutView(FormView):
    template_name = 'legal_services/about.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('legal_services:thank_you')  # страница благодарности

    def form_valid(self, form):
        # Получаем данные из формы
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone_number']
        subject = form.cleaned_data['msg_subject']
        message = form.cleaned_data['message']

        # Собираем текст письма
        body = f"""
        Новое сообщение от клиента:

        Имя: {name}
        Email: {email}
        Телефон: {phone}
        Тема: {subject}
        Сообщение: {message}
        """

        # Отправляем письмо
        send_mail(
            subject='Новое сообщение с сайта',
            message=body,
            from_email=os.getenv("FROM_EMAIL"),  # от кого
            recipient_list=[os.getenv("RECIPIENT")],  # куда
            fail_silently=False,
        )

        return super().form_valid(form)

class LegislationView(ListView):
    model = Legislation
    template_name = 'legal_services/legislation.html'
    context_object_name = 'objects'

class BlogDetailsView(DetailView):
    model = Legislation
    template_name = 'legal_services/blog-details.html'
    context_object_name = 'legislation'


class LegalView(TemplateView):
    template_name = 'legal_services/legal.html'

class ContactView(FormView):
    template_name = 'legal_services/contact.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('legal_services:thank_you')  # страница благодарности

    def form_valid(self, form):
        # Получаем данные из формы
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone_number']
        subject = form.cleaned_data['msg_subject']
        message = form.cleaned_data['message']

        # Собираем текст письма
        body = f"""
            Новое сообщение от клиента:

            Имя: {name}
            Email: {email}
            Телефон: {phone}
            Тема: {subject}
            Сообщение: {message}
            """

        # Отправляем письмо
        send_mail(
            subject='Новое сообщение с сайта',
            message=body,
            from_email=os.getenv("FROM_EMAIL"),  # от кого
            recipient_list=[os.getenv("RECIPIENT")],  # куда
            fail_silently=False,
        )

        return super().form_valid(form)


class PrivacyPolicyView(TemplateView):
    template_name = 'legal_services/privacy-policy.html'


class ThankYouView(TemplateView):
    template_name = 'legal_services/thank_you.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({}, status=404)