import firebase_admin
from firebase_admin import credentials, storage

class FirebaseStorageHandler:
    def __init__(self, service_account_key_path, storage_bucket_name):
        # Path to your service account key file
        cred = credentials.Certificate(service_account_key_path)
        
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'storageBucket': storage_bucket_name
        })
        print("Firebase has been initialized successfully")
    
    def upload_file(self, local_file_path, storage_file_path):
        bucket = storage.bucket()
        blob = bucket.blob(storage_file_path)
        blob.upload_from_filename(local_file_path)
        print(f"File {local_file_path} uploaded to {storage_file_path}.")
    
    def download_file(self, storage_file_path, local_file_path):
        bucket = storage.bucket()
        blob = bucket.blob(storage_file_path)
        blob.download_to_filename(local_file_path)
        print(f"File {storage_file_path} downloaded to {local_file_path}.")

if __name__ == "__main__":
    # Initialize FirebaseStorageHandler
    service_account_key_path = r'D:\Sriman\Ai\NLP\End_to_End_Nlp\listener-d2eb5-firebase-adminsdk-k3wzn-4dc755d8c9.json'
    storage_bucket_name = 'listener-d2eb5.appspot.com'
    
    firebase_handler = FirebaseStorageHandler(service_account_key_path, storage_bucket_name)
    
    # Example file paths
    local_file_path = r'D:\Sriman\Ai\NLP\End_to_End_Nlp\imbalanced_data.csv'
    storage_file_path = 'demo/imbalanced_data.csv'
    download_destination_path = r'D:\Sriman\Ai\NLP\End_to_End_Nlp\downloaded_imbalanced_data.csv'
    
    # Upload a file to Firebase Storage
    firebase_handler.upload_file(local_file_path, storage_file_path)
    
    # Download a file from Firebase Storage
    firebase_handler.download_file(storage_file_path, download_destination_path)
 