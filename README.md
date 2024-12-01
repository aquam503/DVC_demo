# DVC Demo

This is a demo project showcasing how to use [DVC](https://dvc.org/) for data version control and pipelines, entirely locally without remote storage.

## Project Structure

```
dvc-demo/
├── data.csv             # Raw dataset
├── preprocess.py        # Script for preprocessing
├── train.py             # Script for training
├── processed_data.csv   # Output of preprocessing (tracked by DVC)
├── model.txt            # Output of training (tracked by DVC)
├── dvc.yaml             # DVC pipeline configuration
├── dvc.lock             # Snapshot of pipeline state
└── README.md            # Documentation
```
for example data.csv
```
name,age
Radouane,23
Ahmed,26
Alice,30
Bob,25
Charlie,35
```
## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone <repo_url>
   cd dvc-demo
   ```

2. **Install Dependencies**:
   Make sure you have Python and DVC installed:
   ```bash
   pip install dvc pandas
   ```

4. **Define the DVC Pipeline**:
   Run the following commands to define the pipeline:
   ```bash
   # Stage 1: Preprocessing
   dvc stage add -n preprocess \
        -d data.csv -d preprocess.py \
        -o processed_data.csv \
        python preprocess.py
   
   # Stage 2: Training
   dvc stage add -n train \
        -d processed_data.csv -d train.py \
        -o model.txt \
        python train.py
   ```

4. **Reproduce the Pipeline**:

   Run the entire pipeline:
   ```bash
   dvc repro
   ```

5. **View Results**:
   - Preprocessed data: `processed_data.csv`
   - Trained model summary: `model.txt`


## Switching Between Versions
You can easily switch between different versions of your pipeline using git and dvc:
   ```bash
   git checkout <commit_hash>
   ```
   Run dvc checkout to sync the data files to the version of the pipeline at that commit:
   
   ```bash
   dvc checkout
   ```

If you have modified data.csv and need to revert to the version in the commit, DVC will prompt with an error that you are trying to overwrite unsaved files. In such cases, use the --force flag to confirm that you want to discard your local changes:

   ```bash
   dvc checkout --force
   ```
Important: When you return to a previous version of data.csv, DVC will also ensure that all downstream outputs (like processed_data.csv and model.txt) match the state of the pipeline at that commit. This means:

The version of data.csv you checkout will correspond to a specific state of processed_data.csv and model.txt.
So, by checking out a previous version of data.csv, you are also reverting the processed data and model to the versions generated from that specific dataset.

Return to the main branch (or any other branch you're working on):

   ```bash
   git checkout main
   ```
Update your local data and models to the latest version:
   ```bash
   dvc checkout
   ```
This will bring your local environment back to the latest version of the pipeline and its outputs.

## How It Works

- `data.csv` is tracked by DVC to manage dataset versions.
- `preprocess.py` processes the dataset and creates `processed_data.csv`.
- `train.py` reads the processed data and outputs `model.txt`.

## Features

- Demonstrates local DVC setup without remote storage.
- Simple pipeline with two stages: preprocessing and training.

## Next Steps

- Add remote storage for collaborative workflows.
- Experiment with more complex pipelines.

## Read : https://medium.com/@elmahfoudradwane/dvc-for-everyone-a-friendly-guide-to-data-and-model-versioning-a37a30b70999
