
# DocuMind - Document Analysis Module

DocuMind is a document analysis module that provides functionality to analyze text documents, including summarization and sentiment analysis.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The module consists of three main files:

- `main.py`: This file is the entry point of the DocuMind document analysis module. It provides a command-line interface for analyzing text documents. It uses the `doc_analyzer` module to perform document analysis and outputs the results to a file.

- `doc_analyzer.py`: This file contains the `Document`, `TextDocument`, and `WordDocument` classes that encapsulate the functionality for document summarization and sentiment analysis. It uses the Sumy library for text summarization and the TextBlob library for sentiment analysis.

- `cmd_utility.py`: This file contains the command-line utility functions for parsing command-line arguments, handling logging, and calling the `output` function in `main.py`.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repository
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To analyze a text document using DocuMind, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the `main.py` script:

   ```bash
   python main.py
   ```

3. You will be prompted to enter the path to the input document (.txt or .docx), the output path, and the number of sentences for the summary.

4. The script will analyze the document and generate an output file with the summarized text and sentiment analysis results.

## Contributing

Contributions to DocuMind are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature/bug fix:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your commit message"
   ```

4. Push your changes to your forked repository:

   ```bash
   git push origin feature/your-feature
   ```

5. Open a pull request on the original repository.

## License

This project is licensed under the [MIT License](LICENSE).
