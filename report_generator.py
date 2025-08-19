import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Step 1: Read data from CSV file
file_path = "sample_data.csv"  # Replace with your file name
data = pd.read_csv(file_path)

# Step 2: Analyze the data
summary = data.describe(include="all").transpose()

# Step 3: Generate PDF report
pdf_file = "data_report.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("Data Analysis Report", styles["Title"]))
story.append(Spacer(1, 12))

# Add summary statistics as a table
summary_table_data = [summary.columns.to_list()] + summary.reset_index().values.tolist()

table = Table(summary_table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

story.append(table)
doc.build(story)

print(f"PDF report generated successfully: {pdf_file}")