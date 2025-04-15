import os
import csv
from graphviz import Digraph

# Folder containing the header files
folder_path = '../data/NPPES_Data_Dissemination_April_2025_V2'

# Find all *_fileheader.csv files
header_files = [f for f in os.listdir(folder_path) if f.endswith('_fileheader.csv')]

entities = {}
relationships = []

# Parse each header file to extract entity (table) and attributes
for header_file in header_files:
    entity_name = header_file.replace('_fileheader.csv', '')
    with open(os.path.join(folder_path, header_file), newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        entities[entity_name] = headers

# Identify relationships (NPI is the foreign key in all but the main table)
for entity, fields in entities.items():
    if entity != 'npidata_pfile_20050523-20250413' and 'NPI' in fields:
        relationships.append((entity, 'npidata_pfile_20050523-20250413', 'NPI'))

# Create ERD using graphviz
erd = Digraph('NPPES_ERD', format='png')

# Add entities
for entity, fields in entities.items():
    label = f"{entity}|" + "\\l".join(fields) + "\\l"
    erd.node(entity, label=label, shape='record')

# Add relationships
for src, dst, key in relationships:
    erd.edge(src, dst, label=key)

# Output ERD to file
erd.render('nppes_erd', view=False)
print('ERD generated as nppes_erd.png')
