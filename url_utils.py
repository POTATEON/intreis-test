from urllib.parse import urlparse
import pytest

def normalize_url(url: str) -> str:
    """Добавляет https://, если схема отсутствует.
    Убирает пробелы в начале и в конце.
    Если передан None или пустая строка — бросает ValueError,
    так как лучше отловить чем ошибиться потом.
    """

    if not url:
        raise ValueError("URL не может быть пустым или None")

    url = url.strip()

    parsed = urlparse(url)
    if not parsed.scheme:
        url = "https://" + url

    return url


def validate_url(url: str) -> tuple[bool, str]:
    """Проверяет URL.
    Возвращает (True, "") если URL валиден,
    иначе (False, "причина").
    """

    if not url:
        return False, "URL не может быть пустым"

    if len(url) > 2048:
        return False, "URL превышает 2048 символов"

    try:
        parsed = urlparse(url)
    except Exception:
        return False, "Не удалось разобрать URL"

    if parsed.scheme not in ("http", "https"):
        return False, f"Недопустимая схема: {parsed.scheme or 'отсутствует'}"

    if not parsed.netloc:
        return False, "Отсутствует хост"

    blocked_hosts = {"localhost", "127.0.0.1", "0.0.0.0"}
    hostname = parsed.hostname

    if hostname in blocked_hosts:
        return False, f"Недопустимый хост: {parsed.netloc}"

    return True, ""


