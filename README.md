# NYC-TAXI-TRIP

## Status
In progress

## Project Description
NYC-TAXI-TRIP is a data analysis and machine learning project focused on analyzing New York City taxi trip data. The project aims to extract insights from taxi trip patterns and develop predictive models for trip duration, fare amounts, or demand forecasting.

## Navigating this Repo

* `config` folder: Contains configuration files for the project, including database connections, model parameters, and environment settings in `config.py`.

* `utilities` folder: Contains utility modules used across the project:
  * `utils.py`: Helper functions for data processing, feature engineering, and common operations.

* `dev` folder: Contains all development phase code:
  * `eda` subfolder: Code for exploratory data analysis, including data visualization and statistical analysis.
  * `train_notebook.ipynb`: Jupyter notebook documenting the model training process.
  * `train.py`: Script for training machine learning models on taxi trip data.

* `prod` folder: Contains production-ready code for deployment.

## NOTES
* At the top of each file, there should be a purpose that states why that file exists / what it does. For details on what each file does, please open each file and refer to the purpose at the top.
* In each folder, review its README file to understand the purpose and additional details related to the files in that folder.

## Related Project Materials

* Links to decks:
  * 20240315: Project pitch deck [Google Drive](https://drive.google.com/file/d/1fY0-fxMRQ4klL2MA_02qV2CJo1JX9anu/view?usp=sharing)


## Getting Started

### Prerequisites
- Python 3.8+
- Required packages are listed in requirements.txt

### Installation
```bash
git clone https://github.com/username/NYC-TAXI-TRIP.git
cd NYC-TAXI-TRIP
pip install -r requirements.txt
```

### Usage
1. Configure the project by editing the files in the `config` folder
2. Run exploratory data analysis:
   ```bash
   python -m dev.eda.exploratory_analysis
   ```
3. Train models:
   ```bash
   python dev/train.py
   ```

## License
See the [LICENSE](LICENSE)  file for details.
