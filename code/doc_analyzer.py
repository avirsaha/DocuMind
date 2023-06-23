"""
doc_analyzer.py - A document analysis module.

This module provides functionality to analyze text documents, including summarization and sentiment analysis.

Author: Aviraj Saha
Copyright: ©Aviraj Saha 2023
"""

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from textblob import TextBlob
from docx2txt import process


_SUMMARIZER = LexRankSummarizer()


class Document:
    """
    Represents a document object that encapsulates a text file.

    Args:
        path (str): The path to the text file.

    Attributes:
        path (str): The path to the text file.

    Methods:
        summarize(sentences_count: int = 7) -> str:
            Summarizes the content of the document.
        analyze_sentiment() -> str:
            Performs sentiment analysis on the document.
    """

    def __init__(self, path: str):
        self._path = path
        self._dataset = None

    @property
    def path(self) -> str:
        """
        Get the path to the text file.

        Returns:
            str: The path to the text file.
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """
        Set the path to the text file.

        Args:
            path (str): The path to the text file.
        """
        self._path = path
        self._dataset = None

    def __eq__(self, other: object) -> bool:
        """
        Compare if two Document objects are equal.

        Args:
            other (object): Another Document object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if isinstance(other, Document):
            return self.path == other.path
        return False

    def __str__(self) -> str:
        """
        Get a string representation of the Document object.

        Returns:
            str: A string representation of the Document object.
        """
        return f"This is a Document object that refers to the file at {self._path}"

    def summarize(self, sentences_count: int = 7) -> str:
        """
        Summarize the content of the document.

        Args:
            sentences_count (int): The number of sentences in the summary. Defaults to 7.

        Returns:
            str: The summarized text.

        Raises:
            ValueError: If the document contains fewer sentences than the requested summary length.
        """
        if len(self.dataset.split(".")) < sentences_count:
            raise ValueError(
                "The document contains fewer sentences than the requested summary length."
            )
        parser = PlaintextParser.from_string(self.dataset, Tokenizer("english"))
        summarized_sentences = _SUMMARIZER(parser.document, sentences_count)
        summarized_text = " ".join(str(sentence) for sentence in summarized_sentences)
        return summarized_text

    def analyze_sentiment(self) -> str:
        """
        Perform sentiment analysis on the document.

        Returns:
            str: The sentiment polarity of the document ('positive', 'negative', or 'neutral').
        """
        blob = TextBlob(self.dataset)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "positive"
        elif polarity < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        return sentiment


class TextDocument(Document):
    def __init__(self, path: str):
        super().__init__(path)

    @property
    def dataset(self) -> str:
        """
        Get the content of the document.

        Returns:
            str: The content of the document.
        """
        if self._dataset is None:
            with open(self._path, "r") as file:
                self._dataset = file.read()
        return self._dataset


class WordDocument(Document):
    def __init__(self, path: str):
        super().__init__(path)

    @property
    def dataset(self) -> str:
        """
        Get the content of the document.

        Returns:
            str: The content of the document.
        """
        if self._dataset is None:
            self._dataset = process(self._path)
        return self._dataset
