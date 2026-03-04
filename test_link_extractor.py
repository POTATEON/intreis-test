import pytest
from link_extractor import extract_links

def test_relative_to_absolute():
    """Относительная ссылка должна стать абсолютной, пробелы схлопнуть"""
    html = '<a href="/about">  О      нас      </a>'
    result = extract_links(html, "https://example.com")
    assert result == [{"url": "https://example.com/about", "text": "О нас"}]

def test_duplicates_filtered():
    """Одинаковые URL должны включаться только один разь убрать пробелы"""
    html = '''
    <a href="/page">   Первая</a>
    <a href="/page">Вторая</a>
    '''
    result = extract_links(html, "https://example.com")
    assert len(result) == 1
    assert result[0]["url"] == "https://example.com/page"

def test_broken_html():
    """Битый HTML не должен ломать функцию"""
    html = '<a href="/page">Текст без закрывающего тега'
    result = extract_links(html, "https://example.com")
    assert isinstance(result, list)