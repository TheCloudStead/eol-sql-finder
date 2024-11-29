from google.cloud import firestore
from googleapiclient import discovery

from rich.table import Table
from rich.console import Console

FIRESTORE_COLLECTION = "<collection>"
FIRESTORE_DOCUMENT = "<document>"

projects = firestore.Client(project="<project_id>").collection(FIRESTORE_COLLECTION).document(FIRESTORE_DOCUMENT).get().to_dict()
project_ids = [project for folder, project_list in projects.items() for project in project_list]
print(len(project_ids))

eol_versions = [
  "MYSQL_5_6",
  "MYSQL_5_7",
  "POSTGRES_9_6",
  "POSTGRES_10",
  "POSTGRES_11",
  "POSTGRES_12"
]

sql_client= discovery.build('sqladmin', 'v1beta4')

sql_instances = {}
for project_id in project_ids:
    req = sql_client.instances().list(project=project_id)
    instances = req.execute()
    
    if instances and 'items' in instances:
        for instance in instances['items']:
            db_version = instance['databaseVersion']
            project = instance['project']
            
            if db_version in eol_versions:
                if project not in sql_instances:
                    sql_instances[project] = {}

                if db_version not in sql_instances[project]:
                    sql_instances[project][db_version] = 1
                else:
                    sql_instances[project][db_version] += 1

console = Console()

table = Table(title="EOL SQL Instances by Version", title_style="bold magenta", title_justify="center")

table.add_column("Project", justify="left", style="cyan", no_wrap=True)
table.add_column("Version", justify="left", style="green")
table.add_column("Count", justify="center", style="red bold")
for project, versions in sql_instances.items():
    for version, count in versions.items():
        table.add_row(project, version, str(count))

# Display the table
console.print(table)