#!/usr/bin/env python3
"""
Script used to generate 1000 random applications.
"""
import os
import uuid

from lib.application_generator import sample_application

for _ in range(1000):
    application_id = uuid.uuid4()

    filename = f"./applications/application-{application_id}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        com = sample_application(application_id)
        file.write(sample_application(application_id))
