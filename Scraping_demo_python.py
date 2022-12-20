# -*- coding: utf-8 -*-
"""ScrapingDemo_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a1wwm3FYj6vs1iSi4UsU03claf0RgOnG

# Please don't edit directly in this document. Create your own copy first.

# This is a demo for [Canadian Archive of Women in STEM](https://biblio.uottawa.ca/en/women-in-stem) with [requests](https://github.com/psf/requests) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python libraries.

---

# Extract

First, let's run the cell below to import neccesary libraries. Although most of the commonly used Python libraries are pre-installed, new libraries can be installed as *!pip install [package name]* or *!apt-get install [package name]*.

##1. Libraries
*   [requests](https://github.com/psf/requests): an elegant and simple HTTP library for Python.
*   [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): Python library for pulling data out of HTML and XML files
"""

# install
#!pip install requests
#!pip install beautifulsoup4

# import
import requests
from bs4 import BeautifulSoup

"""Second, set the url of the website from which we'd like to extract data using the requests library that we imported in the first step. If the access was successful, you should see the output as <Response [200]>.

## 2. Set the URL
"""

# Set the URL you want to scrape from
url='https://biblio.uottawa.ca/en/women-in-stem'

# Connect to the URL and download document
response = requests.get(url)
response

"""Third, parse the html with BeautifulSoup.

## 3. Parse HTML file
"""

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")
soup

"""Fourth, find an element with its attribute name. 

###Syntax: find_all(name, attrs)
Find all elements following the same syntax rules.
###Syntax: find(name, attrs)
Find a specific element only.

## 4. Extract fonds title, hosting institution, description and STEM fields.
"""

#First element only
soup.find('div', attrs={'class': 'field field-name-title-field field-type-text field-label-hidden'}).text

# Find fonds_title: save as list

title = [fonds_title.text for fonds_title in soup.find_all('div', attrs={'class': 'field field-name-title-field field-type-text field-label-hidden'})]
title

# Hosting institutions: save as list

hosting = [hosting_institutions.text for hosting_institutions in soup.find_all('div', attrs={'class': 'field field-name-uottawa-women-organization field-type-text field-label-hidden'})]
hosting

# Description: save as list

description = [description.text for description in soup.find_all('div', attrs={'class': 'field field-name-uottawa-women-scope field-type-text-long field-label-hidden'})]
description

# STEM Fields: save as list

stem = [stem_fields.text for stem_fields in soup.find_all('div', attrs={'class': 'field field-name-uottawa-women-category field-type-entityreference field-label-hidden'})]
stem

"""# Export to CSV
Import neccesary libraries. The file will be saved in the virtual machine, so in order to download a csv file to your local computer, you need to import *files* from google.colab. 

## 1. Libraries

*   [pandas](https://pandas.pydata.org/): open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools.



"""

# import
import pandas as pd
from google.colab import files

"""You need to combine multiple lists (title, hosting institution, description, and STEM fields) per row to the one data frame. The easiest approach is to create an empty data frame and then add each list to the data frame.

## 2. DataFrame
"""

# Create an empty data frame
df = pd.DataFrame()

# Add a title to df
df['Title'] = title

# Add a hosting institution to df
df['Hosting'] = hosting

# Add description to df
df['Description'] = description

# Add STEM fields to df
df['STEM'] = stem

df

"""You can save df (Data frame) to csv format using df.to_csv().

## 3. Save as CSV
"""

# Save df as csv in the virtual machine provided by Google
df.to_csv('women_stem.csv', sep='\t', encoding='utf-8')

# Download the file to your computer
files.download("women_stem.csv")