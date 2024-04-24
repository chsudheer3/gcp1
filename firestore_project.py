# -*- coding: utf-8 -*-
"""firestore_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DFkVuNyKyBjskNxZ9lx5U9HmMHSNg0vi
"""

import csv
import json
import pandas as pd
def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append(dict(rows))

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Typecast specific columns to integers
    columns_to_typecast = ['age', 'marks']
    df[columns_to_typecast] = df[columns_to_typecast].astype(int)

    # Write the modified DataFrame to a JSON file
    df.to_json(jsonFilePath, orient='records', indent=4)
csvFilePath = r'/content/StudentData.csv'  # Replace with your CSV file path
jsonFilePath = r'student3.json'  # Specify the desired JSON file path
make_json(csvFilePath, jsonFilePath)

!pip install google.auth

from google.colab import auth
auth.authenticate_user()
keyfile_path = "/content/project-sudheer-421110-35fc9ece22a6.json"
!gcloud auth activate-service-account --key-file="$keyfile_path"

from google.cloud import firestore
import json
#create a firestore client with the "student data" database
db = firestore.Client(project="project-sudheer-421110",database="students")
#function to add a student  record to firestore
def add_student_record(data,name):
    doc_ref=db.collection("students").document(name)
    doc_ref.set(data)
#function to read data from json and add it to firestore
def import_data_from_json(file_path):
    with open(file_path,"r") as json_file:
        data=json.load(json_file)
        for item in data:
            add_student_record(item,item['name'])
#path to your json file
json_file_path = "student3.json"
#import data from json to firestore
import_data_from_json(json_file_path)
print("data imported successsfully")

#update document
from google.colab import auth
auth.authenticate_user()
keyfile_path = "/content/project-sudheer-421110-35fc9ece22a6.json"
!gcloud auth activate-service-account --key-file="$keyfile_path"

from google.cloud import firestore

db = firestore.Client(project="project-sudheer-421110",database="students")

data={"name":"Abhishek Maradi"}

doc = db.collection("students").document("Abram Nagao").update(data)
print("Added Successfully")

#delete a field in document

from google.cloud import firestore
from google.colab import auth
auth.authenticate_user()
keyfile_path = "/content/project-sudheer-421110-35fc9ece22a6.json"
!gcloud auth activate-service-account --key-file="$keyfile_path"

db = firestore.Client(project="project-sudheer-421110",database="students")

data = db.collection("students").document("Abram Nagao")
data.update({"gender": firestore.DELETE_FIELD})
print("field deleted successfully for document")

#delete a document

from google.colab import auth
auth.authenticate_user()
keyfile_path = "/content/project-sudheer-421110-35fc9ece22a6.json"
!gcloud auth activate-service-account --key-file="$keyfile_path"

db = firestore.Client(project="project-sudheer-421110",database="students")
docid="Abram Nagao"
db.collection("students").document(docid).delete()
print("deleted",docid)

#delete a collection:

from google.cloud import firestore
from google.colab import auth
auth.authenticate_user()
keyfile_path = "/content/project-sudheer-421110-35fc9ece22a6.json"
!gcloud auth activate-service-account --key-file="$keyfile_path"

def delete_firestore_database(project_id, database_id):
    db = firestore.Client(project=project_id, database=database_id)

    # Get a reference to the root collection of the database
    database_ref = db.collections()

    # List all the collections in the database
    for collection_ref in database_ref:
        print(f'Deleting collection {collection_ref.id}')

        # List documents in the collection and delete them
        for doc_ref in collection_ref.list_documents():
            print(f'Deleting document {doc_ref.id}')
            doc_ref.delete()

#if there are more number of documents than batch_size
def delete_collection(coll_ref, batch_size):
    # Get the documents in the collection
    docs = coll_ref.limit(batch_size).stream()

    # Delete each document in the collection
    deleted = 0
    for doc in docs:
        print(f'Deleting doc {doc.id}')
        doc.reference.delete()
        deleted += 1

    # If there are more documents to delete, recursively call delete_collection
    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)

if __name__ == "__main__":
    delete_firestore_database('project-sudheer-421110', 'students')