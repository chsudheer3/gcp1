from google.cloud import firestore_admin_v1
from google.cloud.firestore_admin_v1.types import firestore_admin

def delete_firestore_database(project_id: str, database_id: str):
    client = firestore_admin_v1.FirestoreAdminClient()
    parent = f'projects/{project_id}/databases/{database_id}'

    operation = client.delete_database(request={"name": parent})
    operation.result()

if __name__ == "__main__":
    delete_firestore_database('glossy-ally-420106', 'univ')
#here in univ replace your databaseid
