import os

from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient

conn_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
connection_name = "rootsac22container"
local_path = os.path.join("..", "images")


def load_images_container(local_path, connection_string, con_name):
    """
    This function will automatically trasnfer images from a local directory into a blob storage account.

    Keyword arguments:
    local_path -- The path to the local diectory where the images are stored (default ../images)
    connection_string -- The connection string associated with the storage account on Azure
    con_name -- The name of the blob storage container (default "rootsac22container")
    """
    try:
        # Connect to the resource group
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

        # Connect to a container within that group
        container_client = blob_service_client.get_container_client(con_name)

        if os.path.exists(local_path):

            images = os.listdir(os.path.join(local_path))

            print("\nUploading the images to Azure Storage as blob\n")

            for im_name in images:

                blob_client = blob_service_client.get_blob_client(
                    container=con_name, blob=im_name
                )

                upload_file_path = os.path.join(local_path, im_name)

                with open(upload_file_path, "rb") as data:
                    blob_client.upload_blob(data)

        else:
            print("Directory not found!")

    except Exception as ex:
        print("Exception:\nThe images already exist in the blob storage container")


def main():
    load_images_container(
        local_path=local_path, connection_string=conn_string, con_name=connection_name
    )


if __name__ == "__main__":
    main()
