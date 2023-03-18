import boto3
import pandas as pd
from faker import Faker
from io import StringIO

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

# Create a CSV from the DataFrame
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# Upload the CSV to the S3 bucket
s3 = boto3.client('s3')
bucket_name = 'fakenews-data'
folder_name = 'rawdata'
file_name = 'fake_data.csv'
s3.put_object(Bucket=bucket_name, Key=f'{folder_name}/{file_name}', Body=csv_buffer.getvalue())

print(f'Fake data uploaded to s3://{bucket_name}/{folder_name}/{file_name}')
