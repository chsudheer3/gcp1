from google.cloud import storage
import json
from google.cloud import firestore
 
# Initialize Firestore client with specific credentials and database
db = firestore.Client(project="glossy-ally-420106", database="supermarket")
 
# Initialize Google Cloud Storage client
storage_client = storage.Client()
 
# Define your bucket and JSON file name
bucket_name = "fs-bucket-1234"
json_file_name = "super_db.json"
 
# Download the JSON file from the Google Cloud Storage bucket
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(json_file_name)
json_data = blob.download_as_string()

data = json.loads(json_data)
 
# Add each document from JSON data to the appropriate collection in the specified database
for collection_name, documents in data.items():
    collection_ref = db.collection(collection_name)
    for document_data in documents:
        doc_ref = collection_ref.document()
        doc_ref.set(document_data)