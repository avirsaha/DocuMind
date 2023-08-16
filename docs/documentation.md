
# Document Analyzer Module

The **doc_analyzer** module provides functionality to analyze text documents, including summarization and sentiment analysis.

**Author**: Aviraj Saha  
**Copyright**: ©Aviraj Saha 2023

## Installation

To use the **doc_analyzer** module, you need to install the following dependencies:

- [sumy](https://github.com/miso-belica/sumy): A library for automatic text summarization.
- [textblob](https://textblob.readthedocs.io/en/dev/): A library for processing textual data.
- [docx2txt](https://pypi.org/project/docx2txt/): A library for extracting text from Word documents.

You can install these dependencies using **pip**:

```
pip install sumy
pip install textblob
pip install docx2txt
```

## Usage

To use the **doc_analyzer** module, follow these steps:

1. Import the necessary classes and functions:

   ```python
   from doc_analyzer import Document, TextDocument, WordDocument
   ```

2. Create an instance of the `Document` class by providing the path to the text file:

   ```python
   document = Document("path/to/text/file.txt")
   ```

   Alternatively, you can create an instance of the `TextDocument` class if the document is a plain text file:

   ```python
   text_document = TextDocument("path/to/text/file.txt")
   ```

   Or create an instance of the `WordDocument` class if the document is a Word file:

   ```python
   word_document = WordDocument("path/to/word/file.docx")
   ```

   Possible Errors:
   - **FileNotFoundError**: If the file path provided does not exist or is incorrect. Make sure to provide the correct path to the text file.

3. Summarize the content of the document using the `summarize` method:

   ```python
   try:
       summary = document.summarize(sentences_count=5)
       print("Summary:")
       print(summary)
   except ValueError as e:
       print("Error:", str(e))
   ```

   The `sentences_count` parameter specifies the number of sentences in the summary. If the document contains fewer sentences than the requested summary length, a `ValueError` is raised. You can catch the exception and handle the error accordingly.

4. Perform sentiment analysis on the document using the `analyze_sentiment` method:

   ```python
   sentiment = document.analyze_sentiment()
   print("Sentiment:", sentiment)
   ```

   The `analyze_sentiment` method returns the sentiment polarity of the document, which can be 'positive', 'negative', or 'neutral'.

## Example

Here's an example that demonstrates the usage of the **doc_analyzer** module:

```python
from doc_analyzer import Document, TextDocument

try:
    # Create a TextDocument instance
    document = TextDocument("path/to/text/file.txt")

    # Summarize the document
    summary = document.summarize(sentences_count=5)
    print("Summary:")
    print(summary)

    # Perform sentiment analysis
    sentiment = document.analyze_sentiment()
    print("Sentiment:", sentiment)
except FileNotFoundError:
    print("Error: File not found.")
except ValueError as e:
    print("Error:", str(e))
```

Make sure to handle the possible errors that may occur, such as `FileNotFoundError` when the file path is incorrect or `ValueError` when the document contains fewer sentences than the requested summary length.

## License



This module is licensed under the [MIT License](LICENSE).