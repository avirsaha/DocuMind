def tokenizer(corpus: str) -> list:
    """Advanced tokenization algorithm for tokenizing cleaned text.
    Takes str value and returns list entity.

    Args:
        corpus (str): Cleaned text to be tokenized.

    Returns:
        list: List of tokens.
    """
    if not corpus:
        return []
    return corpus.split(" ")
