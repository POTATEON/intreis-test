from bs4 import BeautifulSoup
from urllib.parse import urljoin

html = """
<a href="https://example.com">Главная</a>
<a href="/about">О нас</a>
<a href="#">Пропустить</a>
<a href="">Пустая</a>
"""



def extract_links(html: str, base_url: str) -> list[dict]:
    result = []
    seen = set()  # для отслеживания уже добавленных URL
    try:
        soup = BeautifulSoup(html, "html.parser")
    except Exception:
        return result
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if not href or href == "#":
            continue
        url = urljoin(base_url, href)
        if url in seen:  # пропускаем дубликат
            continue
        seen.add(url)
        text = " ".join(tag.get_text().split())
        result.append({"url": url, "text": text})
    return result




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