## Azure Blob storage

Azure Blob Storage is optimized to store massive amounts of semi-structured and unstructured data; in this repository:

- I have created a [script](https://github.com/MoeinT/Github-workflow/blob/feat/get_blobs/scripts/load_blobs.py) that would automatically transfer images from a local directory into a blob storage container on **Azure**.  
- Automated a workflow using CI/CD actions that would automatically load images to an Azure blob storage each time there's a push to the branch. See my script [script](https://github.com/MoeinT/Github-workflow/blob/feat/get_blobs/scripts/get_blobs.py)