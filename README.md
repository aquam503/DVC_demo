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
   dvc run -n preprocess \
        -d data.csv -d preprocess.py \
        -o processed_data.csv \
        python preprocess.py
   
   # Stage 2: Training
   dvc run -n train \
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