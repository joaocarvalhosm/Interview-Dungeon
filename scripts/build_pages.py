"""Assemble the public landing page and playable demo for GitHub Pages."""

from argparse import ArgumentParser
from html.parser import HTMLParser
from pathlib import Path
from shutil import copytree
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]


class PageReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        for name in ("href", "src"):
            if attributes.get(name):
                self.references.append(attributes[name])


def validate_references(page: Path, site_root: Path) -> None:
    references = PageReferences()
    references.feed(page.read_text(encoding="utf-8"))
    for reference in references.references:
        if reference.startswith("#"):
            if reference[1:] not in references.ids:
                raise ValueError(f"Missing anchor in {page}: {reference}")
            continue
        parsed = urlsplit(reference)
        if parsed.scheme or reference.startswith("//"):
            continue
        target = (page.parent / parsed.path).resolve()
        if not target.is_relative_to(site_root.resolve()):
            raise ValueError(f"Reference escapes published site: {reference}")
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            raise ValueError(f"Missing published file: {reference}")


def build(output: Path) -> None:
    if output.exists():
        raise FileExistsError(f"Output already exists: {output}")
    copytree(ROOT / "website", output)
    copytree(ROOT / "prototype", output / "prototype")

    homepage = output / "index.html"
    html = homepage.read_text(encoding="utf-8")
    local_demo_link = 'href="../prototype/"'
    if html.count(local_demo_link) != 4:
        raise ValueError("Expected four local demo links in the landing page")
    homepage.write_text(
        html.replace(local_demo_link, 'href="prototype/"'), encoding="utf-8"
    )

    validate_references(homepage, output)
    validate_references(output / "prototype" / "index.html", output)
    print(f"Built {output} with homepage and playable prototype")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    build(parser.parse_args().output)
