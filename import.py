from google.cloud import firestore
import json
#create a firestore client with the "student data" database
db = firestore.Client(project="project-sudheer-a5abf",database="final28")
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
