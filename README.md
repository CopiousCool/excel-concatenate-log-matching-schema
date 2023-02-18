# excel-concatenate-log-matching-schema
This looks inside it's CWD for excel files and concatenates those with matching schema adding the filename to a log file, if it discovers a any with an alternate schema it adds that filename to a separate log file and concatenates the matching alternate files and continues to create new concatenated xlsx files and .txt log files for new schemas

This code looks at all the Excel files in a certain directory and groups together the files that have the same column headers (or "schema"). It then concatenates all the data from the files in each group into a single file, and saves that file in a new folder called "output".

To do this, the code first uses the Python modules os, pandas, and defaultdict. os allows us to interact with the file system, pandas allows us to read and manipulate Excel files, and defaultdict is a special kind of dictionary that allows us to group values by keys.

The code then sets a few variables and starts iterating through all the files in the current directory. For each file that ends in ".xlsx", the code tries to read the file using pd.read_excel() and get the column headers as a tuple. If this succeeds, the code adds the filename to a list of files that have the same schema. If it fails, the code adds the filename to a list of files with errors.

Next, the code creates a new directory called "output" if it doesn't already exist. For each group of files with the same schema, the code concatenates the data using pd.concat() and saves the resulting DataFrame to a new Excel file. The code also writes a text file that lists the filenames of the concatenated files.

Finally, if there were any errors while reading or concatenating files, the code writes those errors to a text file called "error_log.txt".

Overall, this code takes a group of Excel files with the same schema and combines them into a single file, saving that file and some metadata about it to a new directory.
