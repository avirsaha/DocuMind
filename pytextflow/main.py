import os
from doc_analyzer import TextDocument, WordDocument
from tqdm import tqdm
from pathlib import Path

FOOTER = "\n©Aviraj Saha 2023"
START_UP_MESSAGE = """
\033[1m\033[94mDocuMind - A document analysis module.\033[0m

\033[92mThis module provides functionality to analyze text documents, including summarization and sentiment analysis.\033[0m

\033[93mAuthor:\033[0m \033[1mAviraj Saha\033[0m
\033[93mCopyright:\033[0m \033[1;35m©Aviraj Saha 2023\033[0m
"""


def output(
    file_path: str, file_type: str, output_path: str, no_of_sentences: int
) -> None:
    """
    Analyzes the document and writes the summary and sentiment to the output file.

    Args:
        file_path (str): The path to the input document.
        file_type (str): The type of the input document ('.txt' or '.docx').
        output_path (str): The path to the output file.
        no_of_sentences (int): The number of sentences for the summary.
    """
    document = (
        WordDocument(file_path) if file_type != ".txt" else TextDocument(file_path)
    )
    output_file_name = f"{Path(file_path).stem}_documind_output.txt"
    output_file_path = Path(output_path) / output_file_name
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file_path, "w") as file:
        summary = "\n".join(document.summarize(no_of_sentences).split("."))
        sentiment = document.analyze_sentiment()
        file.write(
            f"{summary}sentiment as analyzed by the model: {sentiment}\n{FOOTER}"
        )


def input_validation() -> tuple:
    """
    Validates and retrieves input values from the user.

    Returns:
        tuple: A tuple containing the validated input values.
    """
    file_path = input("Enter a valid file path for .txt or a .docx file: ")
    file_type = os.path.splitext(file_path)[1]

    if file_type not in [".txt", ".docx"]:
        raise ValueError("Invalid file type. Please provide a .txt or .docx file.")

    output_path = input("Enter path for output: ")
    no_of_sentences = int(input("Enter number of lines for summary: "))

    return file_path, file_type, output_path, no_of_sentences


def process(
    file_path: str, file_type: str, output_path: str, no_of_sentences: int
) -> None:
    """
    Process the document analysis and display progress.

    Args:
        file_path (str): The path to the input document.
        file_type (str): The type of the input document ('.txt' or '.docx').
        output_path (str): The path to the output file.
        no_of_sentences (int): The number of sentences for the summary.
    """
    try:
        with tqdm(
            total=100, desc="Loading", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}"
        ) as pbar:
            output(file_path, file_type, output_path, no_of_sentences)
            pbar.update(100 - pbar.n)

        print("\n\n" + "\033[92m" + "Process finished successfully!" + "\033[0m")
        output_file_name = f"{Path(file_path).stem}_documind_output.txt"
        print(f"Results saved at: {Path(output_path) / output_file_name}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main() -> None:
    """
    Main function to run the DocuMind document analysis module.
    """
    print(START_UP_MESSAGE)

    try:
        file_path, file_type, output_path, no_of_sentences = input_validation()
        process(file_path, file_type, output_path, no_of_sentences)
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
