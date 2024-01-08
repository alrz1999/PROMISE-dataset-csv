import pandas as pd
import os
import javalang

# Function to extract source code from Java files
def extract_source_code(filename):
    try:
        with open(filename, 'r') as file:
            source_code = file.read()
            tree = javalang.parse.parse(source_code)
        return source_code

    except:
        return None
 
project_versions = {
    'ant': ['1.3', '1.4', '1.5', '1.6', '1.7'],
    'camel': ['1.0', '1.2', '1.4', '1.6'],
    'ivy': ['1.0', '1.1', '1.2'],
    'jedit': ['3.2', '4.0', '4.1', '4.2', '4.3'],
    'log4j': ['1.0', '1.1', '1.2'],
    'lucene': ['2.0', '2.2', '2.4'],
    'poi': ['1.5', '2.0', '2.5', '3.0'],
    'synapse': ['1.0', '1.1', '1.2'],
    'velocity': ['1.4', '1.5', '1.6'],
    'xalan': ['2.4', '2.5', '2.6', '2.7'],
    'xerces': ['1.1', '1.2', '1.3', '1.4.4']   
}

source_dir_path = './PROMISE-backup/source code'
bug_data_dir_path = './PROMISE-backup/bug-data'
for project, versions in project_versions.items():
    for version in versions:
        # Read the CSV file containing filenames and bug counts
        bug_data = pd.read_csv(os.path.join(bug_data_dir_path, project, f'{project}-{version}.csv'))

        # Directory containing Java files
        java_files_directory = os.path.join(source_dir_path, project, f'{project}-{version}')
        bug_data['File'] = bug_data['name'].apply(lambda x: str.replace(x, '.', '/') + '.java')
        bug_data['SRC'] = bug_data['File'].apply(lambda x: extract_source_code(os.path.join(java_files_directory, x)))

        # Create a new column indicating buggy or not based on the bug counts
        bug_data['Bug'] = bug_data['bug'].apply(lambda x: 'true' if x > 0 else 'false')

        bug_data = bug_data.dropna(subset=['SRC'])
        # Create a new CSV file with filename, source code, and buggy indicator columns
        bug_data[['File', 'Bug', 'SRC']].to_csv(f'{project}-{version}_ground-truth-files_dataset.csv', index=False)
