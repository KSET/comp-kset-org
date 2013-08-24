from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class Minutes(models.Model):
    date = models.DateTimeField('Meeting date')
    slug = models.SlugField()
    content = models.TextField('Minutes content')
    members_present = models.TextField('Present members')
    mail_notification = models.BooleanField(default=False)

    def __unicode__(self):
        return self.content[:64]

    class Meta:
        verbose_name_plural = "minutes"


@receiver(post_save, sender=Minutes)
def send_email(sender, instance, created, **kwargs):
    if created and instance.mail_notification:
        context = { 'date' : instance.date,
            'members_present' : instance.members_present,
            'content' : instance.content}
        subject = 'Zapisnik sastanka {}'.format(instance.date.strftime('%x'))
        from_email = settings.EMAIL_HOST_USER
        to = settings.EMAIL_TO_ADDRESS 
        text = render_to_string('email.txt', context)
        html = render_to_string('email.html', context)
        msg = EmailMultiAlternatives(subject, text, from_email, [to])
        msg.attach_alternative(html, "text/html")
        msg.send()


