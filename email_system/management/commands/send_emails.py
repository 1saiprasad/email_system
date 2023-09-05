import datetime
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from email_system.models import Event, EmailTemplate, EmailLog

class Command(BaseCommand):
    help = 'Send event-related emails'

    def handle(self, *args, **options):
        current_date = datetime.date.today()
        events = Event.objects.filter(event_date=current_date)
        
        for event in events:
            try:
                template = EmailTemplate.objects.get(event_type=event.event_type)
                subject = template.subject
                content = template.content.format(employee_name=event.employee.name)
                recipient_email = event.employee.email

                send_mail(
                    subject,
                    content,
                    'your_email@example.com',  # Set your sender email here
                    [recipient_email],
                    fail_silently=False,
                )

                EmailLog.objects.create(
                    employee=event.employee,
                    event_type=event.event_type,
                    status='Success',
                )

            except EmailTemplate.DoesNotExist:
                EmailLog.objects.create(
                    employee=event.employee,
                    event_type=event.event_type,
                    status='Failed',
                    error_message='Email template not found',
                )
            except Exception as e:
                EmailLog.objects.create(
                    employee=event.employee,
                    event_type=event.event_type,
                    status='Failed',
                    error_message=str(e),
                )

        self.stdout.write(self.style.SUCCESS('Emails sent successfully'))
