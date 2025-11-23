from faker import Faker
import json

fake = Faker()
Faker.seed(42) # Reproducible results

profiles = []
for _ in range(3):
    profiles.append(fake.profile(fields=['username', 'mail', 'company']))

with open("/output/fake_data.json", "w") as f:
    json.dump(profiles, f, indent=2)
