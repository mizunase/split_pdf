import os
import sys
import pypdf

def split_pdf_file(input_file, output_dir, page_range=20):
    """
    Split a PDF file into multiple files with the specified number of pages
    and save them in the specified directory.

    Args:
        input_file (str): The name of the input PDF file.
        output_dir (str): The name of the output directory.
        page_range (int): The number of pages to include in each output file.

    Returns:
        int: The number of output files created.
    """
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the input file
    with open(input_file, 'rb') as f:
        pdf_reader = pypdf.PdfReader(f)
        num_pages = len(pdf_reader.pages)

        # Calculate the number of output files
        num_files = (num_pages + page_range - 1) // page_range

        # Save the output files
        for i, page_start in enumerate(range(0, num_pages, page_range)):
            page_end = min(page_start + page_range, num_pages)

            # Create the output file name
            output_filename = os.path.splitext(os.path.basename(input_file))[0] + f'_{i+1:03}.pdf'
            output_file = os.path.join(output_dir, output_filename)

            # Create the output PDF file
            with open(output_file, 'wb') as f:
                pdf_writer = pypdf.PdfWriter()
                for j in range(page_start, page_end):
                    pdf_writer.add_page(pdf_reader.pages[j])
                pdf_writer.write(f)

            print(f'Output file: {os.path.abspath(output_file)}')

    return num_files

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python split_pdf.py <input_file> <output_dir> [page_range]')
        sys.exit(1)
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    page_range = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    split_pdf_file(input_file, output_dir, page_range)