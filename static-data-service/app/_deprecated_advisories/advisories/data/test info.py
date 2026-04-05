import xml.etree.ElementTree as ET
import json
from bs4 import BeautifulSoup

tree = ET.parse("C:/Users/Quang/Downloads/CountryTravelInformation.xml")
root = tree.getroot()

cleaned = []
for country in root:
    country_data = {}
    for field in country:
        value = field.text or ""
        # strip HTML entities and tags
        country_data[field.tag] = BeautifulSoup(value, "html.parser").get_text(separator=" ").strip()
    cleaned.append(country_data)

with open("advisory_review.json", "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=2, ensure_ascii=False)