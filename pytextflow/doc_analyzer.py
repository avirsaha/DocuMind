from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from textblob import TextBlob
from pathlib import Path


class Document:
    """
    Represents a document object that encapsulates a text file.

    Args:
        path (str): The path to the text file.

    Attributes:
        path (Path): The path to the text file.

    Methods:
        summarize(sentences_count: int = 7) -> str:
            Summarizes the content of the document.
        analyze_sentiment() -> str:
            Performs sentiment analysis on the document.
    """

    def __init__(self, path: str):
        self.path = Path(path)
        self._dataset = None
        self._summarizer = LexRankSummarizer()

    @property
    def dataset(self) -> str:
        """
        Get the content of the document.

        Returns:
            str: The content of the document.
        """
        if self._dataset is None:
            try:
                with self.path.open("r") as file:
                    self._dataset = file.read()
            except FileNotFoundError:
                raise ValueError("The document file was not found.")
            except PermissionError:
                raise ValueError("Permission denied to access the document file.")
        return self._dataset

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
        summarized_sentences = self._summarizer(parser.document, sentences_count)
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
    """
    Represents a text document object that encapsulates a text file.
    Inherits from the Document class.
    """

    def __init__(self, path: str):
        super().__init__(path)


class WordDocument(Document):
    """
    Represents a Word document object that encapsulates a DOCX file.
    Inherits from the Document class.
    """

    def __init__(self, path: str):
        super().__init__(path)
