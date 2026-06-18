# tools/site_summary.py
"""
Provides structured summary generation for a predefined site configuration.
"""

import json
from datetime import datetime
from typing import Dict, List

SITE_DATA: Dict[str, object] = {
    "name": "Instant Kaiyun Open",
    "url": "https://www.instant-kaiyunopen.com.cn",
    "keywords": ["开云", "instant", "kaiyun", "open platform"],
    "description": "A platform offering instant cloud-based services and open integration.",
    "tags": ["cloud", "integration", "open-source", "kaiyun"],
    "last_reviewed": "2024-12-01",
    "category": "Technology / Cloud Services"
}

def format_summary(data: Dict[str, object]) -> str:
    """
    Formats a structured summary string from site data.
    """
    lines: List[str] = [
        "=== Site Summary ===",
        f"Name: {data.get('name', 'Unknown')}",
        f"URL: {data.get('url', 'N/A')}",
        f"Description: {data.get('description', '')}",
        f"Category: {data.get('category', 'Uncategorized')}",
        f"Keywords: {', '.join(data.get('keywords', []))}",
        f"Tags: {', '.join(data.get('tags', []))}",
        f"Last Reviewed: {data.get('last_reviewed', 'Unknown')}",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "======================"
    ]
    return "\n".join(lines)

def to_json_summary(data: Dict[str, object]) -> str:
    """
    Returns a JSON representation of the summary.
    """
    summary = {
        "site": data.get("name"),
        "url": data.get("url"),
        "keywords": data.get("keywords", []),
        "tags": data.get("tags", []),
        "description": data.get("description"),
        "generated_at": datetime.now().isoformat()
    }
    return json.dumps(summary, indent=2, ensure_ascii=False)

def analyze_keyword_presence(data: Dict[str, object], target: str) -> Dict[str, bool]:
    """
    Checks if a given keyword appears in various fields.
    """
    keyword_lower = target.lower()
    result = {
        "in_name": keyword_lower in data.get("name", "").lower(),
        "in_description": keyword_lower in data.get("description", "").lower(),
        "in_keywords": any(keyword_lower == kw.lower() for kw in data.get("keywords", [])),
        "in_url": keyword_lower in data.get("url", "").lower(),
        "in_tags": any(keyword_lower == tag.lower() for tag in data.get("tags", []))
    }
    return result

def print_summary_verbose(data: Dict[str, object]) -> None:
    """
    Prints a detailed summary to stdout.
    """
    print(format_summary(data))
    print("\nKeyword analysis for '开云':")
    analysis = analyze_keyword_presence(data, "开云")
    for field, present in analysis.items():
        status = "✓" if present else "✗"
        print(f"  {field}: {status}")

def main() -> None:
    """
    Entry point: demonstrate summary generation.
    """
    print("Generating site summary...\n")
    print_summary_verbose(SITE_DATA)
    print("\nJSON representation:")
    print(to_json_summary(SITE_DATA))

if __name__ == "__main__":
    main()