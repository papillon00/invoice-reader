import numpy as np
import pandas as pd
import glob ##merge multiple csv files into one dataframe    
import re #re.search('Toter.+' , variable)
import os
import pdfplumber
import re
from collections import namedtuple
import tkinter as tk
from tkinter import filedialog

def export_folder_path():
    """Prompt the user to select a folder to save the export"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(
        title="Select a Folder to export the data"
    )

    root.destroy()  # Close the Tkinter window

    os.chdir(folder_path)
    os.getcwd()
    print("The file has been exported to {}".format(os.getcwd()))
    
    
def get_folder_path():
    """Prompts the user to select a folder and returns its path."""

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(
        title="Select a Folder"
    )

    root.destroy()  # Close the Tkinter window

    os.chdir(folder_path)
    os.getcwd()
    extension = 'pdf'
    import_list = [ i for i in glob.glob('*.{}'.format(extension), recursive=True)]
    print(f"There are {len(import_list)} invoices in {folder_path}")
    return import_list
    
def main(import_list):
    
    # Keyword input (instruct user to enter only one colon)
    keyword1 = input("Enter the keyword before the invoice number (no colon): ")
    num_chars = int(input("Enter the number of characters in the invoice number: "))

    # Dynamically build the regular expression pattern (without extra backslashes)
    pattern = r"{keyword1}:\s+?(\w{{{num_chars}}})".format(keyword1=keyword1, num_chars=num_chars)
    inv_line_re = re.compile(pattern)

    # Keyword input for date
    keyword2 = input("Enter the keyword before the invoice Date (no colon) ")
    pattern2 = rf"{keyword2}:\s+?(?P<date>\w+\s+\d{{2}},\s+\d{{4}})"
    Stmt_date_re = re.compile(pattern2)

    # Keyword input for Customer
    keyword3 = input("Enter the keyword before the Customer name (no colon) ")
    pattern3 = rf"{keyword3}:\s+(?P<id>\d{{6}} - \d{{5}})"
    cust_no_re = re.compile(pattern3)
    # Keyword input for Grand Total
    keyword4 = input("Enter the keyword before the Grand Total (no colon) ")
    pattern4 = rf"(?<={keyword4}:)\s+\$\s*(?P<amount>[\d,]+\.\d{{2}})"
    grand_total_re = re.compile(pattern4)

    #Keyword Input for Tax
    keyword5 = input("Enter the keyword before the Tax (no colon) ")
    pattern5 = rf"{keyword5}+\s*\$?\s*(?P<amount>[\d,]+\.\d{{2}})"
    Tax_re = re.compile(pattern5)

    #inv_line_re= re.compile(r"Invoice / Facture:\s+?(\w{6})")
    #Stmt_date_re = re.compile(r"Date:\s+(?P<date>\w+\s+\d{2},\s+\d{4})") 
    #cust_no_re = re.compile(r"Customer / Client:\s+(?P<id>\d{6} - \d{5})") 
    #grand_total_re= re.compile (r"(?<=Montant de facture:)\s+\$\s*(?P<amount>[\d,]+\.\d{2})")
    #Tax_re = re.compile(r"GST 5.0000 %+\s*\$?\s*(?P<amount>[\d,]+\.\d{2})")

    line_items = []
    inv_read = namedtuple('inv','Inv_no, Date, Customer, Grand_total, Tax, File_name')

    for invoice in import_list: 
    # Open the PDF document
        File_name = invoice
        pages = pdfplumber.open(invoice).pages

        # Initialize an empty list to store all lines
        all_lines = []

        # Iterate through each page
        for page in pages:
            # Extract the text from the current page
            page_text = page.extract_text()

            # Split the text into lines
            lines = page_text.splitlines()

            # Add each line to the `all_lines` list
            all_lines.extend(lines)

        # Combine all lines into a single string
        text_for_search = "\n".join(all_lines)

        # Now you can use `text_for_search` for your text search operations

        #print(f"Total lines extracted: {len(all_lines)}")
        #print(f"Example line: {text_for_search[:100]}")  # Print the first 100 characters as an example

        inv_no = find_match(text_for_search, inv_line_re)
        stmt_date = find_match(text_for_search, Stmt_date_re)
        customer =  find_match(text_for_search, cust_no_re)
        subtotal = find_match(text_for_search, subtotal_re)
        grand_total = find_match(text_for_search, grand_total_re)
        Tax = find_match(text_for_search, Tax_re)

        line_items.append(inv_read(inv_no, stmt_date, customer, grand_total, Tax, File_name))

    #line_items = []
    df = pd.DataFrame(line_items)  
    export_folder_path()
    df.to_csv(datetime.date.today().strftime("%Y%m%d")+'_invoice_export.csv')
    return print(f"Invoice data exported to {datetime.date.today().strftime('%Y%m%d')+'_invoice_export.csv'}")

if __name__ == '__main__':
    import_list = get_folder_path()
    main(import_list)