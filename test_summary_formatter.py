from summary_formatter import format_check_summary

def test_empty_list():
    """Пустой список — только заголовок"""
    assert format_check_summary([]) == "Проверки: 0"

def test_all_ok():
    """Все проверки успешны"""
    checks = [{"name": "SSL", "ok": True}, {"name": "WHOIS", "ok": True}]
    result = format_check_summary(checks)
    assert result == "Проверки: 2\n✅ SSL — ок\n✅ WHOIS — ок"

def test_mix_with_message():
    """Смесь успехов и ошибок с message"""
    checks = [
        {"name": "SSL", "ok": True},
        {"name": "DNS", "ok": False, "message": "таймаут"},
    ]
    result = format_check_summary(checks)
    assert result == "Проверки: 2\n✅ SSL — ок\n❌ DNS — таймаут"