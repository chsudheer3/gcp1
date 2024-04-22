from google.cloud import firestore

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
    delete_firestore_database('projectname', 'databasename')
