# Finding EOL CloudSQL Instances in Your GCP Org

### Introduction

This repository contains the code to identify end-of-life (EOL) CloudSQL instances within your GCP organization. It aims to assist security practitioners and developers by identifying outdated versions that need upgrading before extended support runs out. More details on how to use this repository can be found in the article:

[**Finding EOL CloudSQL Instances in Your GCP Org**](https://thecloudstead.medium.com/finding-eol-cloudsql-instances-in-your-gcp-org)

### Prerequisites

- Google Cloud Platform account with permissions to access Cloud SQL instances.
- APIs that must be enabled in your project:
  - Cloud SQL Admin API
  - Google Cloud Firestore API
  - Cloud Resource Manager API
- Python installed on your local machine.
- `gcloud` CLI configured to interact with your GCP account.

### Getting Started

Clone the repository and move into the appropriate directory:

```bash
git clone https://github.com/TheCloudStead/eol-cloudsql-checker
cd eol-cloudsql-checker/src/
```

### Setting Up Environment

To run this script, install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Running the Script

Make sure you are authenticated to your GCP account before running the script. You can use the following commands to re-authenticate if necessary:

```bash
gcloud config set project <project_id>
gcloud config set account <email>
gcloud auth login
gcloud auth application-default login
```

After authenticating, run the script to identify EOL CloudSQL instances:

```bash
python main.py
```

### Files Overview

- **main.py**: The core Python script for fetching EOL CloudSQL instance information from your GCP organization.
- **requirements.txt**: Lists Python dependencies needed for the script (e.g., google-cloud-firestore, google-api-python-client, rich).
- **firestore_setup.py**: Script to set up Firestore collections if they don't already exist.

### How the Script Works

1. The script queries a Firestore collection in a specific GCP project to get the current list of GCP projects.
2. It then loops through these projects, lists any SQL instances, and checks if their versions are end-of-life based on the defined `eol_versions`.
3. Results are displayed in a stylized table with version counts using the **Rich** library.

### Updating the Project List

To update the list of GCP projects that this script checks, modify the `FIRESTORE_COLLECTION` and `FIRESTORE_DOCUMENT` variables in `main.py`. You may also need to add new projects to the Firestore collection if necessary.

### Tips

- Ensure you have the correct permissions for accessing Cloud SQL instances and Firestore collections.
- Regularly update your Firestore project list to ensure new projects are scanned for EOL instances.
- If you need a more detailed output (e.g., instance size or specific configurations), consider modifying the script or using Jupyter Notebook for a more interactive experience.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Acknowledgments

Thank you to the readers of my Medium articles!

