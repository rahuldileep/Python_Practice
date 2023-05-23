#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import glob
import os

table = []
styles = getSampleStyleSheet()
report = SimpleDocTemplate("/Users/rahjadha/Documents/2020/practice/Python/Coursera_Python_course/report.pdf")
for infile in glob.glob('00*.txt'):
    with open(os.path.abspath(infile)) as fp:
        reader = fp.read().splitlines()
        table.append("")
        table.append('name: '+reader[0].strip())
        table.append('weight: '+reader[1].strip())
print(table)
table = "<br/>".join(table)
empty_line = Spacer(1,20)
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report_info = Paragraph(table, styles["BodyText"])
report.build([report_title, empty_line,report_info, empty_line])