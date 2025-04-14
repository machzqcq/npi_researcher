from tabula.io import read_pdf
import pandas as pd

def parse_pdf_to_table(pdf_path, output_csv_path):
    """
    Parses a PDF file and extracts tables into a CSV file.

    Args:
        pdf_path (str): Path to the PDF file.
        output_csv_path (str): Path to save the extracted table as a CSV file.
    """
    try:
        # Extract tables from the PDF
        tables = read_pdf(pdf_path, pages="all", multiple_tables=True, lattice=True, stream=True)

        # Combine all tables into a single DataFrame
        combined_df = pd.concat(tables, ignore_index=True)

        # Save the combined DataFrame to a CSV file
        combined_df.to_csv(output_csv_path, index=False)

        print(f"Tables extracted and saved to {output_csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_path = "../data/MUP_DPR_RY22_20220715_DD_PRV_Drug.pdf"
    output_csv_path = "../data/extracted_table.csv"

    parse_pdf_to_table(pdf_path, output_csv_path)

