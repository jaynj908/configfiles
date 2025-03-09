#!/usr/bin/env python3

import os
import re
import sys

def pad_episode_numbers(directory='.', pattern=r'Episode\s*(\d+)', padding=2, dry_run=False):
    """
    Renames files by padding the episode numbers with zeros.
    
    Args:
        directory: Directory to scan for files
        pattern: Regex pattern to match episode numbers
        padding: Number of digits to pad to
        dry_run: If True, only print what would be done without actually renaming
    """
    file_count = 0
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Walk through the specified directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
        
        # Check if the filename matches our pattern
        match = regex.search(filename)
        if match:
            episode_num = match.group(1)
            padded_num = episode_num.zfill(padding)
            
            # Only proceed if the number needs padding
            if episode_num != padded_num:
                new_filename = filename.replace(match.group(0), 
                                               match.group(0).replace(episode_num, padded_num))
                new_filepath = os.path.join(directory, new_filename)
                
                if dry_run:
                    print(f"Would rename: {filename} → {new_filename}")
                else:
                    try:
                        os.rename(filepath, new_filepath)
                        print(f"Renamed: {filename} → {new_filename}")
                        file_count += 1
                    except Exception as e:
                        print(f"Error renaming {filename}: {e}")
    
    if dry_run:
        print(f"\nDry run completed. {file_count} files would be renamed.")
    else:
        print(f"\nCompleted. {file_count} files renamed.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Pad episode numbers in filenames with zeros")
    parser.add_argument("-d", "--directory", default=".", 
                        help="Directory to scan (default: current directory)")
    parser.add_argument("-p", "--pattern", default=r'Episode\s*(\d+)', 
                        help="Regex pattern to match episode numbers (default: 'Episode\\s*(\\d+)')")
    parser.add_argument("-z", "--zero-pad", type=int, default=2, 
                        help="Number of digits to pad to (default: 2)")
    parser.add_argument("--dry-run", action="store_true", 
                        help="Don't actually rename files, just show what would be done")
    
    args = parser.parse_args()
    
    pad_episode_numbers(args.directory, args.pattern, args.zero_pad, args.dry_run)
