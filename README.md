# intreis-test

Python 3.14+

## Установка

pip install -r requirements.txt

## Запуск тестов

pytest test_url_utils.py -v  

pytest test_link_extractor.py -v  

pytest test_summary_formatter.py -v  


## Что не сделано

Задача 3 (fetch_utils) — Для реализации изучил бы документацию httpx.AsyncClient,  
реализовал GET-запрос с таймаутом 15 секунд и обработкой ошибок через try/except.
