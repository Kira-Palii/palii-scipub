def normalize_title(raw: str) -> str:
    """Прибирає зайві пробіли й переводить назву в нижній регістр."""
    return " ".join(raw.split()).lower()


def truncate_title(title: str, limit: int = 80) -> str:
    if limit < 1:
        raise ValueError("limit must be at least 1")
    return title if len(title) <= limit else title[: limit - 1] + "…"
