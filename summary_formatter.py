def format_check_summary(checks: list[dict], lang: str = "ru") -> str:
    lines = []
    
    header = "Проверки" if lang == "ru" else "Checks"
    lines.append(f"{header}: {len(checks)}")
    
    for check in checks:
        name = check.get("name", "?")
        ok = check.get("ok", False)
        message = check.get("message")
        icon = "✅" if ok else "❌"
        
        if message:
            line = f"{icon} {name} — {message}"
        else:
            status = "ок" if lang == "ru" else "ok"
            line = f"{icon} {name} — {status}"
        
        lines.append(line)
    
    return "\n".join(lines)
