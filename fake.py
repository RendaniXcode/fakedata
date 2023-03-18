from faker import Faker
import pandas as pd

# Initialize the Faker library
fake = Faker()

# Define the number of records to generate
num_records = 100

# Generate fake data
data = []
for _ in range(num_records):
    record = {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'birthdate': fake.date_of_birth(),
        'company': fake.company(),
        'job_title': fake.job(),
        'phone_number': fake.phone_number(),
    }
    data.append(record)

# Create a DataFrame from the fake data
df = pd.DataFrame(data)

# Print the first 10 rows of the DataFrame
print(df.head(10))
