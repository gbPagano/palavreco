from unicodedata import normalize


def remove_accents(word: str) -> str:
    return normalize("NFKD", word).encode("ASCII","ignore").decode("ASCII")