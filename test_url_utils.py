import pytest
from url_utils import normalize_url, validate_url


# Тесты для normalize_url

def test_normalize_adds_https():
    """URL без схемы должен получить https://"""
    assert normalize_url("example.com") == "https://example.com"

def test_normalize_keeps_http():
    """Существующий http:// не должен измениться"""
    assert normalize_url("http://example.com") == "http://example.com"

def test_normalize_strips_spaces():
    """Пробелы по краям должны убираться"""
    assert normalize_url("  https://example.com  ") == "https://example.com"

def test_normalize_empty_string():
    """Пустая строка должна бросать ValueError"""
    with pytest.raises(ValueError):
        normalize_url("")

def test_normalize_none():
    """None должен бросать ValueError"""
    with pytest.raises(ValueError):
        normalize_url(None)


# Тесты для validate_url

def test_validate_valid_url():
    """Обычный валидный URL должен проходить"""
    ok, msg = validate_url("https://example.com")
    assert ok is True
    assert msg == ""

def test_validate_blocked_localhost():
    """localhost должен быть заблокирован"""
    ok, msg = validate_url("https://localhost/admin")
    assert ok is False
    assert "localhost" in msg

def test_validate_blocked_ip_with_port():
    """127.0.0.1 с портом должен быть заблокирован"""
    ok, msg = validate_url("https://127.0.0.1:8080/page")
    assert ok is False
    assert "127.0.0.1" in msg

def test_validate_ftp_scheme():
    """ftp:// должен быть отклонён"""
    ok, msg = validate_url("ftp://files.com")
    assert ok is False
    assert "схема" in msg

def test_validate_too_long_url():
    """URL длиннее 2048 символов должен быть отклонён"""
    ok, msg = validate_url("https://example.com/" + "a" * 3000)
    assert ok is False
    assert "2048" in msg