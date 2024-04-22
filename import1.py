from google.cloud import firestore
from google.cloud import storage
import json

# Initialize Firestore client
db = firestore.Client(database="supermarket")

# Function to import data from a JSON file into Firestore
def import_data_from_json(bucket_name, json_file_path):
    # Download the JSON file from Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(json_file_path)
    temp_json_file_path = "/tmp/temp.json"
    blob.download_to_filename(temp_json_file_path)
    
    # Read data from the JSON file
    with open(temp_json_file_path, "r") as json_file:
        data = json.load(json_file)
    
    # Import data into Firestore
    for collection_name, collection_data in data.items():
        collection_ref = db.collection(collection_name)
        import_collection_data(collection_ref, collection_data)
    
    print("Data imported successfully!")

# Function to import collection data into Firestore
def import_collection_data(collection_ref, data):
    for item in data:
        # Add document to Firestore collection
        doc_ref = collection_ref.document()
        doc_ref.set(item)

# Replace 'superbucket123' and 'supermarket_data.json' with your actual bucket name and JSON file path
bucket_name = 'superbucket123'
json_file_path = 'supermarket_data.json'

# Call the function to import data from the JSON file into Firestore
import_data_from_json(bucket_name, json_file_path)
