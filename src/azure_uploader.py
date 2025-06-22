from azure.storage.blob import BlobServiceClient
import os

AZURE_CONN_STRING = os.getenv('AZURE_BLOB_CONNECTION')
CONTAINER_NAME = "fraud-data"

def upload_to_azure(file_path, blob_name):
    try:
        service = BlobServiceClient.from_connection_string(AZURE_CONN_STRING)
        container = service.get_container_client(CONTAINER_NAME)

        with open(file_path, "rb") as data:
            container.upload_blob(name=blob_name, data=data, overwrite=True)

        print(f"✅ Uploaded {blob_name} to Azure Blob Storage.")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

