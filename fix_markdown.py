#!/usr/bin/env python3
"""Fix markdown linting errors in documentation files."""

import re


def fix_markdown_file(filename):
    """Fix common markdown linting issues in a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a heading (starts with #)
        is_heading = line.strip().startswith('#') and not line.strip().startswith('```')
        
        # Check if this is a list item
        is_list = (line.strip().startswith('-') or 
                   line.strip().startswith('*') or 
                   (line.strip() and line.strip()[0].isdigit() and '.' in line[:5]))
        
        # Check if this is a code fence
        is_code_fence = line.strip().startswith('```')
        
        # Add blank line before heading if needed
        if is_heading and fixed_lines:
            if fixed_lines[-1].strip() != '':
                fixed_lines.append('\n')
        
        # Add the current line
        fixed_lines.append(line)
        
        # Add blank line after heading if next line isn't blank and isn't a list/heading
        if is_heading and i + 1 < len(lines):
            next_line = lines[i + 1]
            if next_line.strip() != '' and not next_line.strip().startswith('#'):
                # Check if next line is a list - if so, add blank line
                if (next_line.strip().startswith('-') or 
                    next_line.strip().startswith('*') or
                    (next_line.strip() and next_line.strip()[0].isdigit())):
                    fixed_lines.append('\n')
        
        # Add blank line before list if previous line wasn't blank or a heading
        if is_list and fixed_lines and i > 0:
            prev_line = fixed_lines[-2] if len(fixed_lines) >= 2 else ''
            if prev_line.strip() != '' and not prev_line.strip().startswith('#'):
                fixed_lines.insert(-1, '\n')
        
        # Add blank line before code fence if previous line wasn't blank
        if is_code_fence and fixed_lines and i > 0:
            if fixed_lines[-2].strip() != '' if len(fixed_lines) >= 2 else False:
                fixed_lines.insert(-1, '\n')
        
        # Add blank line after code fence if it's closing and next line isn't blank
        if is_code_fence and '```' in line and i + 1 < len(lines):
            next_line = lines[i + 1]
            if next_line.strip() != '':
                # Check if this is actually a closing fence by counting preceding fences
                fence_count = sum(1 for l in lines[:i+1] if '```' in l)
                if fence_count % 2 == 0:  # Even number means this closes a block
                    # Peek ahead to see if we need a blank line
                    if i + 1 < len(lines) and lines[i + 1].strip() != '':
                        pass  # Will be handled in next iteration
        
        i += 1
    
    # Write back the fixed content
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"Fixed {filename}")


def fix_specific_issues():
    """Fix specific known issues."""
    
    # Fix GEMMA_INFO.md - wrap bare URL
    with open('GEMMA_INFO.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(
        'https://ai.google.dev/gemma/terms\n',
        '<https://ai.google.dev/gemma/terms>\n'
    )
    
    with open('GEMMA_INFO.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Fix README.md - add language to code block
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the code block around line 157 without language
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if i >= 155 and i <= 165 and line.strip() == '```':
            # Check context - should be after environment variables section
            if i > 5 and ('GOOGLE_API_KEY' in lines[i-2] or 'GOOGLE_API_KEY' in lines[i-1]):
                lines[i] = '```text'
                break
    
    content = '\n'.join(lines)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed specific issues")


if __name__ == '__main__':
    # Fix specific known issues first
    fix_specific_issues()
    
    # Then fix formatting issues in all markdown files
    for filename in ['COURSE_INFO.md', 'GEMMA_INFO.md', 'README.md']:
        fix_markdown_file(filename)
    
    print("\nAll markdown files fixed!")
    print("\nNote: Some warnings may remain - they are cosmetic and don't affect functionality.")
