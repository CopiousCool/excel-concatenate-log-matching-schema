import os
import pandas as pd
from collections import defaultdict

# get current directory
current_dir = os.getcwd()

# dictionary to store dataframes grouped by schema
schema_dict = defaultdict(list)

# list to store file names with incompatible schemas
incompatible_files = []

#list to store file names with error
error_files = []

# iterate through files in directory
for filename in os.listdir(current_dir):
    if filename.endswith('.xlsx'):
        try:
            # read excel file
            df = pd.read_excel(filename)
            # get column names as tuple to use as key
            key = tuple(df.columns)
            # add dataframe to dictionary with column names as key
            schema_dict[key].append(filename)
        except Exception as e:
            # add file name to list of incompatible files
            error_files.append(filename)
            #save the error to a text file
            with open("error_log.txt", "a") as file:
                file.write(f"{filename} raised an error: {e}\n")
            print(f'Error reading {filename}: {e}')

# create new directory for output
if not os.path.exists('output'):
    os.makedirs('output')

# create excel files for each group of schemas
for i, (key, file_list) in enumerate(schema_dict.items()):
    # concatenate dataframes
    try:
        concatenated_df = pd.concat([pd.read_excel(file) for file in file_list])
        # save concatenated dataframe to new file
        concatenated_df.to_excel(f'output/schema_{i+1}.xlsx', index=False)
        print(f'Successfully concatenated {len(file_list)} files with schema {key}.')
        # write file names of concatenated files to text file
        with open(f'output/schema_{i+1}_files.txt', 'w') as f:
            f.write(f'Concatenated files: {", ".join(file_list)}')
    except Exception as e:
        print(f'Error concatenating dataframes: {e}')
        with open("error_log.txt", "a") as file:
            file.write(f"{', '.join(file_list)} raised an error: {e}\n")
