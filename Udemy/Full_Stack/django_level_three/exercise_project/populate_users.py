import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise_project.settings')

import django
django.setup()


# populate fake users as test
import random
from users.models import User
from faker import Faker

fake = Faker()

def add_user():
    user = User.objects.get_or_create(
        first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email()
    )[0]
    return user


def populate(n=5):

    for entry in range(n):
        add_user()



if __name__ == "__main__":
    print("Populating users...")
    populate()
    print("Populating finished.")
