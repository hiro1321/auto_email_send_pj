import dataclasses


@dataclasses.dataclass
class Mail:
    address: str = ""
    title: str = ""
    letter_body: str = ""
