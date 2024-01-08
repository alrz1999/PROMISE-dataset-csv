# PROMISE Dataset CSV Generator

This repository contains a Python script (`csv_generator.py`) that generates CSV files using the data from the [PROMISE backup](https://github.com/feiwww/PROMISE-backup) repository. The generated CSV files serve as a dataset derived from the PROMISE dataset, specifically formatted for ease of use and analysis.

## Dataset Information

- The original data source: [PROMISE backup](https://github.com/feiwww/PROMISE-backup)

## Files

- `csv_generator.py`: Python script used to generate CSV files from the PROMISE backup data.
- `promise.zip`: Compressed file containing all generated CSV files.
- `ant-1.3_ground-truth-files_dataset.csv`: Sample CSV file created using `csv_generator.py`.

## Generated CSV Format

The generated CSV files contain the following three columns:

1. `File`: Represents the file names from the PROMISE dataset.
2. `Bug`: Indicates the bug-related information associated with each file.
3. `SRC`: Contains specific source-related details corresponding to the files.
