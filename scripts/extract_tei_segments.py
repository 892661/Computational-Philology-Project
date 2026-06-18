from lxml import etree
import csv
import re
from pathlib import Path

# Input and output paths
INPUT_FILE = Path("data/raw/merged manuscripts.xml")
OUTPUT_FILE = Path("data/processed/segments_dataset.csv")

# TEI namespace
NS = {"tei": "http://www.tei-c.org/ns/1.0"}


def clean_spaces(text):
    """Normalize whitespace."""
    if text is None:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def normalize_text(text):
    """
    Light normalization for computational comparison.
    This keeps the text close to the transcription.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def get_text_from_element(element):
    """
    Extract readable text from a TEI element.
    Text inside <ex>, <hi>, <sic>, <unclear>, etc. is preserved.
    XML markup itself is ignored.
    """
    return clean_spaces("".join(element.itertext()))


def main():
    tree = etree.parse(str(INPUT_FILE))
    root = tree.getroot()

    rows = []

    witnesses = {
        "D54": ".//tei:div[@n='1']",
        "4941": ".//tei:div[@n='2']",
    }

    for witness_id, xpath in witnesses.items():
        div = root.find(xpath, namespaces=NS)

        if div is None:
            print(f"Warning: witness {witness_id} not found.")
            continue

        # First paragraph = first argumentative section:
        # "Nota quod sacro concilio non est detrahendum"
        first_p = div.find(".//tei:p", namespaces=NS)

        if first_p is None:
            print(f"Warning: first paragraph not found for {witness_id}.")
            continue

        segments = first_p.findall(".//tei:seg[@type='argument']", namespaces=NS)

        for seg in segments:
            argument_n = seg.get("n")
            text_expanded = get_text_from_element(seg)
            text_normalized = normalize_text(text_expanded)

            rows.append({
                "witness": witness_id,
                "section": "sacro_concilio",
                "argument_n": argument_n,
                "text_expanded": text_expanded,
                "text_normalized": text_normalized,
            })

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "witness",
                "section",
                "argument_n",
                "text_expanded",
                "text_normalized",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Dataset created: {OUTPUT_FILE}")
    print(f"Rows extracted: {len(rows)}")


if __name__ == "__main__":
    main()
