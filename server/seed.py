#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    fake = Faker()

    # Delete all rows in the pets table
    Pet.query.delete()

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    pets = []

    # Generate 10 random pets
    for _ in range(10):
        pet = Pet(
            name=fake.first_name(),
            species=rc(species)
        )
        pets.append(pet)

    db.session.add_all(pets)
    db.session.commit()
