# PDF Splitter

This is a Python script that splits a PDF file into multiple files with a specified number of pages and saves them in a specified directory.

## Requirements

- Python 3.x
- pypdf library

You can install the pypdf library using pip:

```
pip install pypdf
```

## Usage

```
python split_pdf.py <input_file> <output_dir> [page_range]
```

- `input_file`: The name of the input PDF file.
- `output_dir`: The name of the output directory.
- `page_range`: (Optional) The number of pages to include in each output file. Default is 20.

Example usage:

```
python split_pdf.py input.pdf output_folder 10
```

This will split the `input.pdf` file into multiple files with 10 pages each and save them in the `output_folder`.

## Functionality

The `split_pdf_file()` function takes three arguments:

- `input_file`: The name of the input PDF file.
- `output_dir`: The name of the output directory.
- `page_range`: The number of pages to include in each output file. Default is 20.

The function returns the number of output files created.

The script uses the pypdf library to read the input PDF file, calculate the number of output files, and save the output files. The output files are named using the input file name and a numerical suffix.

If the output directory does not exist, it is created.

## License

This script is licensed under the MIT License.