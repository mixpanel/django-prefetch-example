import os
import django
import json
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from boards.models import Board, Report  # Replace 'boards' with your actual app name

fake = Faker()

# Create 20 Board rows with random names
for _ in range(2000):
    name = fake.word().capitalize()
    board = Board.objects.create(name=f"{name}'s Board")

    # Create 10 Report rows for each Board with random names and data
    for i in range(10):
        report_name = fake.word()
        Report.objects.create(name=f"{name}'s Report {str(i+1)}", board=board)

print("Database populated successfully!")
