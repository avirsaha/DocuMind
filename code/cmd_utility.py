import os
import logging
import argparse
from doc_analyzer import TextDocument, WordDocument
from tqdm import tqdm

FOOTER = "\n©Aviraj Saha 2023"
START_UP_MESSAGE = """
\033[1m\033[94mDocuMind - A document analysis module.\033[0m

\033[92mThis module provides functionality to analyze text documents, including summarization and sentiment analysis.\033[0m

\033[93mAuthor:\033[0m \033[1mAviraj Saha\033[0m
\033[93mCopyright:\033[0m \033[1;35m©Aviraj Saha 2023\033[0m
"""

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Create console handler and set level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Create file handler and set level to DEBUG
file_handler = logging.FileHandler("documind.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def output(
    file_path: str, output_path: str, no_of_sentences: int, file_type: str
) -> None:
    """
    Analyzes the document and writes the summary and sentiment to the output file.

    Args:
        file_path (str): The path to the input document.
        output_path (str): The path to the output file.
        no_of_sentences (int): The number of sentences for the summary.
        file_type (str): The type of the input document ('.txt' or '.docx').
    Raises:
        ValueError: If an invalid file type is provided.
    """
    if file_type not in [".txt", ".docx"]:
        raise ValueError("Invalid file type. Please provide a .txt or .docx file.")

    try:
        if file_type == ".txt":
            document = TextDocument(file_path)
        else:
            document = WordDocument(file_path)

        output_file_path = os.path.join(output_path, "output_documind.txt")
        with open(output_file_path, "w") as file:
            summary = document.summarize(no_of_sentences)
            sentiment = document.analyze_sentiment()
            file.write(
                f"{summary}sentiment as analyzed by the model: {sentiment}{FOOTER}"
            )

        logger.info(f"Output saved successfully at: {output_file_path}")

    except Exception as e:
        logger.error(f"An error occurred during document analysis: {str(e)}")
        raise


@lambda _: _()
def main() -> None:
    """
    Main function to run the DocuMind document analysis module.
    """
    logger.info(START_UP_MESSAGE)

    parser = argparse.ArgumentParser(
        description="DocuMind - A document analysis module"
    )
    parser.add_argument(
        "file_path", type=str, help="Path to the input document (.txt or .docx)"
    )
    parser.add_argument("output_path", type=str, help="Path for the output file")
    parser.add_argument(
        "no_of_sentences", type=int, help="Number of sentences for the summary"
    )

    args = parser.parse_args()
    file_path = args.file_path
    output_path = args.output_path
    no_of_sentences = args.no_of_sentences

    file_type = os.path.splitext(file_path)[1]

    try:
        os.makedirs(output_path, exist_ok=True)

        with tqdm(
            total=100, desc="Loading", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}"
        ) as pbar:
            output(file_path, output_path, no_of_sentences, file_type)
            pbar.update(100 - pbar.n)

        logger.info(f"Output saved successfully at: {output_path}")

    except Exception as e:
        logger.error(f"An error occurred during document analysis: {str(e)}")
