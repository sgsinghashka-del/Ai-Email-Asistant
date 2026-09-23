def validate_email(email_text: str, action: str = "Improve"):
    if not email_text or not email_text.strip():
        return "Please enter an email before processing it."

    if len(email_text.strip()) < 10:
        return "Please provide a little more text so the AI can produce a useful result."

    if len(email_text) > 12000:
        return "Please keep the input below 12,000 characters."

    return None
