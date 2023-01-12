<p align="center">
    <a href="https://github.com/EDJINEDJA/pilot">
        <img src="https://github.com/EDJINEDJA/pilot/blob/main/hands.png" alt="Pilot">
    </a> 
<br>


<p align="center">
    <a href="https://www.python.org/doc/" alt="Python 3.7">
        <img src="https://img.shields.io/badge/python-v3.7+-blue.svg" />
    </a>
    <a href="https://github.com/mhaythornthwaite/Football_Prediction_Project/blob/main/LICENSE" alt="Licence">
        <img src="https://img.shields.io/badge/license-MIT-yellow.svg" />
    </a>
    <a href="https://github.com/mhaythornthwaite/Football_Prediction_Project/commits/main" alt="Commits">
        <img src="https://img.shields.io/github/last-commit/mhaythornthwaite/Football_Prediction_Project/master" />
    </a>
    <a href="https://github.com/EDJINEDJA/pilot" alt="Activity">
        <img src="https://img.shields.io/badge/contributions-welcome-orange.svg" />
    </a>
    <a href="http://matthaythornthwaite.pythonanywhere.com/" alt="Web Status">
        <img src="https://img.shields.io/website?down_color=red&down_message=down&up_color=success&up_message=up&url=http%3A%2F%2Fmatthaythornthwaite.pythonanywhere.com%2F" />
    </a>
</p>


## Table of Contents

<!--ts-->
* [Aims and Objectives](#Aims-and-Objectives)
* [What is Feature engineering](#Feature-engineering)
* [Usage](#Usage)
* [Handle missing values](#Handle-missing-values)
* [Handle outliers](#Handle-outliers)
* [Remove unnecessary variables](#Remove-unnecessary-variables)
* [Encoding categorical variables](#Encoding-categorical-variables)
* [Numerical transformation](#Numerical-transformation)
* [Scaling numerical features](#Scaling-numerical-features)
* [Extracting of date](#Extracting-of-date)
<!--te-->

## Aims and Objectives

pilot is a package that aims to perform feature engineering.

## What is Feature engineering
An optimal machine learning using python can't be build without feature engineering.
<br>
What is exactlly Features Engineering? 
<br>
In order to select prominent variables for avoid issues such as overfitting, underfitting etc
When we build machine learning models, it is suitable to consuming little bit time on feature engineering.
Features engineering contains numerous types of technologies:

- Handle missing values 
- Handle outliers
- Remove unnecessary variables 
- Delete low-variance variables 
- Show Numerical and categorical variables
- Encoding categorical variables
- Numerical transformation 
- Scaling numerical features 
- Extracting of date
              
This technology will help you to have you hand on feature engineering and perform well the choice of prominent variables.


# Usage

#### Install

- git clone 

Clone this repository in the main folder of your project to use pilot. 

```bash
$ git clone https://github.com/EDJINEDJA/pilot
```
- requirements

The toolkit support Python 3.10.6 

To install required packages use:

```bash
$ pip3 install -r requirements.txt
```

#### pilot  usage

```python
$ import pilot
or  
$ from pilot import pilot 
```
## Handle missing values
<strong>Hadling missing values </strong> is an essential in feature engineering because all data in real life comes with some missing values.
In general there is not an optimal way to handle missing values. because there is different types and charactiristics of the dataset.
Indeed, there are several ways to handle missing values in a dataset, including:

Deleting rows or columns with missing data:

This approach is simple and can work well if the amount of missing data is small. However, it can lead to a loss of information if a large portion of the data is removed.

To do that use strategy default


```python
$ from pilot import pilot 
$ pilot.HandlMissingValues(data=data,scalar = None strategy = "default")
```

Imputing missing values:

This method involves replacing missing values with estimates, such as the mean or median of the non-missing values. This approach can help to preserve the size of the dataset, but the imputed values are not always accurate.

Using a predictive model:

A machine learning model can be trained to predict missing values based on the other features in the dataset. This approach can be more accurate than imputation, but it requires a sufficient amount of non-missing data to train the model.

Using a flag:

Creating a new column which indicates whether a value is missing or not.


Using interpolation technique:

replacing the missing value with the average of the value before and after the missing value.

The best approach depends on the specific situation and the amount of missing data. It's also best to use multiple techniques and compare the results.
## Handle outliers

## Remove unnecessary variables

## Delete low-variance variables

## Show Numerical and categorical variables

## Encoding categorical variables

## Numerical transformation 

## Scaling numerical features 

## Extracting of date

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


