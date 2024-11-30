# -*- coding: utf-8 -*-
import random
import string
import json
from faker import Faker

fake = Faker()

def print_banner():
    banner = """
    ========================================
         MOCK DATA GENERATOR
         Created by Python 2.7
    ========================================
    """
    print(banner)

def generate_mock_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "company": fake.company(),
            "job": fake.job(),
            "text": fake.text(max_nb_chars=100)
        }
        data.append(record)
    return data

def save_to_file(data, filename="mock_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("Mock data saved to '{}'".format(filename))

def main():
    print_banner()
    try:
        num_records = int(raw_input("Enter the number of mock data records to generate: "))
        if num_records <= 0:
            print("Number of records must be greater than 0.")
            return
        data = generate_mock_data(num_records)
        
        print(json.dumps(data, indent=4, ensure_ascii=False))
        
        save_to_file(data)
        print("Mock data generation complete!")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
