from google.cloud import firestore

db = firestore.Client(project="glossy-ally-420106",database="supermarket")

users_ref = db.collection("products")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
