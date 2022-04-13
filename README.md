# DS_Salary_Project
Predation of Data Science salaries. Following Ken Jee create a data science project from scratch series.

# Data Science Salary Estimator: Project Overview
* Created a tool that estimates data science salaries(MAE ~ $11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Optimized Linear, Lasso and Random Forest Regressors using GridsearchCV to reach the best model.

## Code and Resources Used
**Python Version:** 3.7
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
**For Web Framework Requirements:** '''pip install -r requirments.txt'''
**Scraper Github:**  https://github.com/arapfaik/scraping-glassdoor-selenium
**Scraper Article:** https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
**Flask Productionization:** https://towardsdatascience.com/machine-learning-model-deployment-on-heroku-using-flask-467acb4a34da

## YouTube Project Walk-Through
 Ken Jee - Data Science Project from Scratch series
 https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Heaquarters
* Company size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
* Parsed numeric data out of salary
* Made columns for employer provided salary and hourly wages
* Removed rows without salary
* Parsed rating out of company text
* Made a newe column for company state
* Added a column for if the job was at the company's headquarters
* Transformed founded date into age of company

## Exploritory Data Analysis (EDA)
I looked at the distributions fo teh data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

## Model Building


 
