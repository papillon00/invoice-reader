# Pdf Invoice Reader
This repository contains a Python script that extracts key information from PDF invoices and exports it to a CSV file.
User will be prompt to select a folder where it may contain one or more pdf files. 
The program will scrape the following key fields:
* Invoice No ( can be digits or characters)
* Invoice Date
* Customer Name/ Customer ID
* Grand Total
* Tax

# How it works

The user will be prompted to provide specific keywords. For example in the sample invoice below,

![Screenshot 2024-02-21 at 8 42 39 PM](https://github.com/papillon00/invoice-reader/blob/main/Sample_invoice)


user can enter the following keywords:

* Invoice No  = Invoice / Facture
* No. of characters / digits in Invoice No = 6
* Invoice Date = Date
* Customer Name/ Customer ID = Customer / Client
* Grand Total = Montant de facture
* Tax = GST 5.0000 %

The program will scrape each pdf in selected folder based on information above and save any findings into a named tuple. 
If no matches are found, empty string will be returned.

At the end of the scrape, the programm will prompt user to select a folder to export the csv file.
A file titled 'yyyymmdd_invoice_export.csv' will be saved to the selected folder.

# How to use:

Install the required libraries: numpy, pandas, glob, re, os, pdfplumber, collections, tkinter.
Clone this repository or download the script (invoice_reader.py).
Run the script using python invoice_reader.py or pdf_reader.ipynb (Jupyter Notebook).
Follow the prompts to select the invoice folder and provide keyword information for each data point.
The extracted data will be saved as a CSV file in the same location as the script.

Example:

When prompted, enter the keywords that appear before each data point in the PDF invoices without the colon. For example, if the invoice number appears before a colon like this: "Invoice Number: 123456", then enter "Invoice Number" as the keyword.

# Customization:

You can modify the regular expressions in the main function to match the specific format of your invoices.
You can adjust the output filename format by changing the code in the export_folder_path function.
Dependencies:

This script requires the following Python libraries/Modules:

- numpy
- pandas
- glob
- re
- os
- pdfplumber
- collections
- tkinter
- datetime

# Contributing:

We welcome contributions to this project. Please submit pull requests with any improvements or bug fixes.

# Additional Notes:

This script provides a basic framework for extracting invoice data. You may need to adjust it based on the specific format and content of your invoices.
Make sure you have the necessary permissions to access and read the PDF invoices you want to process.
