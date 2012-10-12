from django.core.management.base import BaseCommand, CommandError

from main.models import Country

import csv

class Command(BaseCommand):
  args = ''
  help = 'Import country data from geonames'

  def handle(self, *args, **options):

    # TODO: need to load from csv

    for c in Country.objects.all():
      c.delete()

    with open("data/countryInfo.txt", "r") as country_file:
      reader = csv.DictReader(country_file, delimiter='\t')
      for row in reader:
        country = Country(name=row['Country'], iso_code=row['ISO'])
        country.save()

    print "{country_count} countries saved ".format(country_count=Country.objects.all().count())
