import re

EMAIL = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)


def redact(text):
    return EMAIL.sub(
        "[REDACTED]",
        text
    )