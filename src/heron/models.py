from dataclasses import dataclass

@dataclass
class ParsedEmail:
    """A dataclass to hold the parsed email data."""
    email_id: str
    sender: str
    from_domain:str | None
    reply_to_domain:str | None=None
    auth_results: str
    text: str
    links: tuple[str]

email=ParsedEmail(
    email_id="1",
    sender="aaa@a.it",
    from_domain="a.it",
    reply_to_domain="b.it",
    auth_result="spf=pass",
    text="This is a test email.",
    links=("http://example.com", "https://xn--example.com")
)

email.email_id="2"