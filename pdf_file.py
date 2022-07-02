#!/usr/bin/env python3

import datetime
import os, sys
from reportlab.platypus import Paragraph, Spacer, Table, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def pdf_body(raw_data):
    """This function takes a file/path to a file in .txt format and returns the content in string"""
    if os.path.isfile(raw_data):
        with open(raw_data, "r") as rd:
            result_data = rd.read()
    return result_data
    


def generate_report(file_name, title, add_info):
    """This function takes a file_name or path, a title for the file and a string data and builds a pdf file."""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file_name)
    report_title = Paragraph (title, styles['h1'])
    report_info = Paragraph(add_info, styles["BodyText"])
    empty_line = Spacer(1, 20)

    report.build([report_title, empty_line, report_info, empty_line])

if __name__ == "__main__":
    pdf_template = sys.argv
    pdf_data = pdf_body(pdf_template[1])
    generate_report(
        file_name=pdf_template[2],
        title = "Report Date: {}".format(datetime.date.today().strftime("%B %d, %Y")),
        add_info=pdf_data
    )
