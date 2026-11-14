def normalize_title(raw: str) -> str:
    """Прибирає зайві пробіли й переводить назву в нижній регістр."""
    return " ".join(raw.split()).lower()


def truncate_title(title: str, limit: int = 80) -> str:
    return title if len(title) <= limit else title[: limit - 1] + "…"
