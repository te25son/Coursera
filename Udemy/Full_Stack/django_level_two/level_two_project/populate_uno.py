import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level_two_project.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from uno.models import AccessRecord, Webpage, Topic
from faker import Faker


fake = Faker()

topics = [
    'Search',
    'Social',
    'Marketplace',
    'News',
    'Games',
]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        # get the topic to enter
        top = add_topic()

        # create the fake data to enter
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        # create new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create fake access record for webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == "__main__":
    print('Populating script...')
    populate(20)
    print('Populating complete.')
