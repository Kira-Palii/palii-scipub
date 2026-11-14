def normalize_title(raw: str) -> str:
    """Прибирає зайві пробіли й переводить назву в нижній регістр."""
    return " ".join(raw.split()).lower()
