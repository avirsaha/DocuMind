import os
from doc_analyzer import TextDocument, WordDocument
from tqdm import tqdm

FOOTER = "\n©Aviraj Saha 2023"
START_UP_MESSAGE = """
\033[1m\033[94mDocuMind - A document analysis module.\033[0m

\033[92mThis module provides functionality to analyze text documents, including summarization and sentiment analysis.\033[0m

\033[93mAuthor:\033[0m \033[1mAviraj Saha\033[0m
\033[93mCopyright:\033[0m \033[1;35m©Aviraj Saha 2023\033[0m
"""


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
    """
    if file_type != ".txt":
        document = WordDocument(file_path)
        output_file_path = os.path.join(output_path, "output_documind.txt")
        with open(output_file_path, "w") as file:
            summary = "\n".join(document.summarize(no_of_sentences).split("."))
            sentiment = document.analyze_sentiment()
            file.write(
                f"{summary}\nsentiment as analyzed by the model: {sentiment}\n{FOOTER}"
            )
    else:
        document = TextDocument(file_path)
        output_file_path = os.path.join(output_path, "output_documind.txt")
        with open(output_file_path, "w") as file:
            summary = document.summarize(no_of_sentences)
            sentiment = document.analyze_sentiment()
            file.write(
                f"{summary}sentiment as analyzed by the model: {sentiment}{FOOTER}"
            )


def main() -> None:
    """
    Main function to run the DocuMind document analysis module.
    """
    print(START_UP_MESSAGE)
    file_path = input("Enter a valid file path for .txt or a .docx file: ")
    file_type = os.path.splitext(file_path)[1]

    if file_type not in [".txt", ".docx"]:
        raise ValueError("Invalid file type. Please provide a .txt or .docx file.")

    output_path = input("Enter path for output: ")
    no_of_sentences = int(input("Enter number of lines for summary: "))

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Create a progress bar using tqdm
    with tqdm(
        total=100, desc="Loading", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}"
    ) as pbar:
        # Call the function
        output(file_path, output_path, no_of_sentences, file_type)

        # Update the progress bar to 100%
        pbar.update(100 - pbar.n)

    print(
        "\n\n" + "\033[92m" + f"Sucessfully saved output at: {output_path}" + "\033[0m"
    )


if __name__ == "__main__":
    main()
