#!/usr/bin/env python3
"""
All functions used to generate random applications.
"""
import random
from datetime import datetime, timedelta

START = datetime.strptime("2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
END = datetime.strptime("2023-06-01 00:00:00", "%Y-%m-%d %H:%M:%S")


def random_date(start, end):
    """
    This function return a random datetime between two datetime objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def sample_application(uuid):
    """
    This function return a random application.
    """
    therapeutic_area = random.choice(["oncology", "pulmonology", "infectious diseases"])

    site = random.choice(
        [
            {"site_name": "New York University Hospital", "site_category": "academic"},
            {"site_name": "Lyon Medical Center", "site_category": "community"},
            {"site_name": "Miami Health Institute", "site_category": "network"},
            {"site_name": "Lisbon University Hospital", "site_category": "academic"},
            {"site_name": "Los Angeles", "site_category": "network"},
        ]
    )

    return "|".join(
        [
            f"id={uuid}",
            f"therapeutic_area={therapeutic_area}",
            f'created_at={random_date(START, END).strftime("%Y-%m-%d %H:%M:%S")}',
            f"site={site}",
        ]
    )
