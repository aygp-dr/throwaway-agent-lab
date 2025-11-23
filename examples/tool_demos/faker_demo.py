# The agent "tool use" for generating synthetic user data
from faker import Faker
import json
import random

fake = Faker()
print("Generating 5 mock users...")

users = []
for _ in range(5):
    user = {
        "id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "job": fake.job(),
        "company": fake.company(),
        "created_at": fake.iso8601()
    }
    users.append(user)

# Output to JSON
output_path = "/output/users.json"
with open(output_path, "w") as f:
    json.dump(users, f, indent=2)

print(f"Success! Mock data saved to {output_path}")
print("Preview of first user:")
print(json.dumps(users[0], indent=2))
