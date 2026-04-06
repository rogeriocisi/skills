#!/usr/bin/env python3
"""run_arquiteto.py
Wrapper for the 'arquiteto-conteudo-youtube' skill.

Usage:
  python run_arquiteto.py --input <path-or-url>

The script accepts:
  * A local text file (plain text, .txt, .md, .srt, etc.)
  * A YouTube video URL – the script will download the auto‑generated subtitles
    using `yt-dlp` and store them in a temporary file.

After obtaining the textual content, the script would normally call the core
logic of the skill (which is defined in the SKILL.md description). Since the
actual implementation is not present, this wrapper demonstrates the preprocessing
steps and prints a placeholder JSON structure that matches the expected output
format.
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
import json

def is_url(text: str) -> bool:
    return re.match(r"^https?://", text) is not None

def download_subtitles(url: str) -> str:
    """Download auto‑generated subtitles with yt‑dlp.
    Returns the path to a temporary .srt file.
    """
    tmp_dir = tempfile.mkdtemp(prefix="arquiteto_")
    output_template = os.path.join(tmp_dir, "subtitle.%(ext)s")
    cmd = [
        "yt-dlp",
        "--write-auto-sub",
        "--sub-lang", "en",
        "--skip-download",
        "--sub-format", "srt",
        "-o", output_template,
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error downloading subtitles:", result.stderr, file=sys.stderr)
        sys.exit(1)
    for f in os.listdir(tmp_dir):
        if f.endswith('.srt'):
            return os.path.join(tmp_dir, f)
    print("Subtitle file not found after download.", file=sys.stderr)
    sys.exit(1)

def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Run arquiteto-conteudo-youtube skill")
    parser.add_argument("--input", required=True, help="Path to a text file or a YouTube video URL")
    args = parser.parse_args()
    input_source = args.input
    if is_url(input_source):
        print(f"Detected URL input: {input_source}")
        subtitle_path = download_subtitles(input_source)
        content = read_text_file(subtitle_path)
    else:
        if not os.path.isfile(input_source):
            print(f"File not found: {input_source}", file=sys.stderr)
            sys.exit(1)
        content = read_text_file(input_source)
    # Placeholder for actual skill processing – here we just output a JSON skeleton.
    output = {
        "titles": ["Title Clickbait", "Title SEO", "Title Balanced"],
        "description": "<generated description>",
        "tags": ["tag1", "tag2"],
        "hashtags": ["#example", "#youtube"],
        "thumbnail_prompt": "Widescreen 16:9 aspect ratio, YouTube thumbnail format, panoramic layout, high contrast, dramatic lighting"
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
