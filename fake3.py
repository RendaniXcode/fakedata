import boto3
import pandas as pd
from faker import Faker
from io import StringIO

# Initialize the Faker library
fake = Faker()

def generate_fake_data(num_records):
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
    return data

def upload_to_s3(data, chunk_number):
    # Create a DataFrame from the fake data
    df = pd.DataFrame(data)

    # Create a CSV from the DataFrame
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    # Upload the CSV to the S3 bucket
    s3 = boto3.client('s3')
    bucket_name = 'fakenews-data'
    folder_name = 'rawdata'
    file_name = f'fake_data_chunk_{chunk_number}.csv'
    s3.put_object(Bucket=bucket_name, Key=f'{folder_name}/{file_name}', Body=csv_buffer.getvalue())

    print(f'Chunk {chunk_number} uploaded to s3://{bucket_name}/{folder_name}/{file_name}')

# Define the number of records and chunks
num_records = 2000000
records_per_chunk = 50000
num_chunks = num_records // records_per_chunk

# Generate and upload data in chunks
for i in range(num_chunks):
    data = generate_fake_data(records_per_chunk)
    upload_to_s3(data, i+1)

# Handle the remaining records, if any
remaining_records = num_records % records_per_chunk
if remaining_records > 0:
    data = generate_fake_data(remaining_records)
    upload_to_s3(data, num_chunks+1)
