# Notebooks for Data Mining and Text Mining

## Installation
Note: that this repository requires Python 3.8

First we suggest you create an environment for this project using conda. We have tested the installation procedures
on Linux 64-bits (Ubuntu 18.04), macOS Catalina 10.15, and Windows 10. 

First, install *miniconda*, instructions on how to install miniconda are found in 
[Their docs](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

Second, clone this repository, checkout, and install the environment with the following:
```console
git clone https://github.com/fernandobperezm/2020-data-mining-and-text-mining.git
cd 2020-data-mining-and-text-mining
conda env create -f environment.yml
conda activate data-mining-and-text-mining
```

## Using the repo.
You'll have four different notebooks.

* `introduction`: It's a presentation notebook with some very good memes.
* `data_preparation`: It's the first (of two) notebook that tells you how to use numpy, pandas, and scipy to prepare data for recommender systems.
* `creating_a_recommender_from_scratch`: This is the notebook where we use the data that we prepared before and use it to create two basic recommender systems.
