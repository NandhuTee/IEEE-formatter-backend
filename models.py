from pydantic import BaseModel

class GenerateRequest(BaseModel):

    title: str

    authors: list[str]

    affiliations: list[str]

    abstract: str

    keywords: list[str]

    paragraphs: list

    headings: list

    tables: list

    figures: list

    references: list