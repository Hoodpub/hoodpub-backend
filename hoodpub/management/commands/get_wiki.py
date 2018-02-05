from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('keyword', nargs='+', type=str)

    def handle(self, *args, **options):
        for keyword in (options['keyword']):
            User.objects.new_from_wiki(keyword)
