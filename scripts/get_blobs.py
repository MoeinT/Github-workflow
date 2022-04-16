from azure.storage.blob import BlobServiceClient
import os
#Running the following scripts outputs the number of images within a blob storage container

connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "rootsac22container"

def get_list_blobs(connection_string = connection_string, container_name = container_name):

    """
    This function return a blob list of type ItemPaged

    keyworkd arguments:

    connection_string -- connection string associated with a storage account in which the blob container is located
    container_name -- The name of the blob storage container (default "rootsac22container")

    """

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_list = container_client.list_blobs()

    return blob_list


def main():
    blob_list = get_list_blobs()
    print(f"There are {len(list(blob_list))} images in this containers")

if __name__ == "__main__":
    main()











