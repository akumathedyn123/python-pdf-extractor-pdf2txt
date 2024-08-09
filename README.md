## pdf_extractor-pdf2txt

This Python script efficiently extracts text content from multiple PDF files within a designated folder and saves the extracted text as separate TXT files with the same name as the original PDFs (excluding the ".pdf" extension).

### Features

* Processes multiple PDFs in a single run.
* Preserves the original file structure for easy identification.
* Utilizes the well-established PyPDF2 library for robust PDF handling.

### Prerequisites

* Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* PyPDF2 library (installation: `pip install PyPDF2`)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/akumathedyn123/python-pdf-extractor-pdf2txt.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd pdf_extractor-pdf2txt
   ```

### Usage

1. **Set the PDF Folder Path:**

   - Open the `main.py` file in a text editor.
   - Locate the line that defines the `pdf_folder` variable (usually near the beginning).
   - Replace `"path/to/folder"` with the absolute path to the directory containing your PDF files.

   **Example:** If your PDFs are in a folder named `my_pdfs` on your desktop, you would change the line to:

   ```python
   pdf_folder = os.path.join(os.path.expanduser('~'), 'Desktop', 'my_pdfs')
   ```

2. **Run the Script:**

   - From the project directory (where `main.py` is located), execute the script using the following command:

   ```bash
   python main.py
   ```

   **Note:** If you're using Python 3, you might need to replace `python` with `python3` depending on your system setup.

### License

This project is licensed under the MIT License (see LICENSE file for details).

### Contributing

We encourage contributions to this project. Feel free to submit pull requests for bug fixes, enhancements, or new features.

### Contact

For any questions or feedback, please feel free to create an issue on the project's GitHub repository.
