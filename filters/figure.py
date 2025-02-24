#!/usr/bin/env python3

import re
import sys
from pandocfilters import toJSONFilter, Image

def rst_image_to_md(key, value, format, meta):
    """
    Filtr pro převod obrázků s popisem z RST do MD.
    """
    # Pokud se jedná o obrázek v Pandoc AST
    print(key, value, file=sys.stderr)
    if key == 'Para' and len(value) == 1:
        # Zkontrolujeme, zda je to obrázek ve formátu RST (obrázek začíná 'image::')
        image_pattern = re.compile(r'.. image::\s*(?P<url>\S+)\s*\n\s*(?P<caption>.*?)\n', re.DOTALL)
        print(value[0], file=sys.stderr)
        #match = image_pattern.match(value[0]['c'])
        match = None
        
        if match:
            url = match.group('url')
            caption = match.group('caption').strip()
            # Vytvoříme Pandoc Image objekt pro Markdown
            return Image(['', [], []], [caption, url])

def main():
    # Spustíme Pandoc filtr
    toJSONFilter(rst_image_to_md)

if __name__ == "__main__":
    main()
