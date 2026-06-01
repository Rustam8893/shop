from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Create or update a Google SocialApp for django-allauth (development helper).'

    def add_arguments(self, parser):
        parser.add_argument('--client-id', required=True, help='Google OAuth client id')
        parser.add_argument('--secret', required=True, help='Google OAuth client secret')
        parser.add_argument('--name', default='Google', help='SocialApp name')
        parser.add_argument('--site-id', type=int, default=getattr(settings, 'SITE_ID', 1), help='Site ID to attach')

    def handle(self, *args, **options):
        client_id = options['client_id']
        secret = options['secret']
        name = options['name']
        site_id = options['site_id']

        try:
            from allauth.socialaccount.models import SocialApp
            from django.contrib.sites.models import Site
        except Exception as e:
            self.stderr.write('allauth not installed or Site model unavailable: %s' % e)
            return

        site = Site.objects.filter(id=site_id).first()
        if not site:
            self.stderr.write(f'Site with id={site_id} not found. Please create it in admin.')
            return

        app, created = SocialApp.objects.get_or_create(provider='google', defaults={'name': name, 'client_id': client_id, 'secret': secret})
        if not created:
            app.name = name
            app.client_id = client_id
            app.secret = secret
            app.save()
            self.stdout.write('Updated existing SocialApp for google.')
        else:
            self.stdout.write('Created new SocialApp for google.')

        if site not in app.sites.all():
            app.sites.add(site)
            self.stdout.write(f'Added site id={site_id} to SocialApp.')

        self.stdout.write('Done. Make sure the Google OAuth client has redirect URI: http://127.0.0.1:8000/accounts/google/login/callback/')
