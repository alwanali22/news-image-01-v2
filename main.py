"""
Main execution script for the 13 November 2026 World News Infographic entry.
Copies the pre-rendered entry.png to the target output directory specified by
MAKEFUN_OUTPUT_DIR (defaulting to /output). Standard library only, always exits 0.
"""

import os
import shutil

def main() -> None:
    # Determine output directory from environment or fallback to default
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Locate source entry.png adjacent to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_image = os.path.join(script_dir, "entry.png")
    destination_image = os.path.join(output_dir, "entry.png")
    
    # Copy entry.png to destination
    shutil.copyfile(source_image, destination_image)

if __name__ == "__main__":
    main()
