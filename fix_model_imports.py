#!/usr/bin/env python3
"""
Script to fix model interdependency issues by adding proper TYPE_CHECKING imports.
"""

import os
import re
from pathlib import Path

def extract_custom_types(content):
    """Extract custom types (capitalized classes) from type annotations."""
    # Find List[CustomType] patterns
    list_pattern = r'List\[([A-Z]\w*)\]'
    list_matches = re.findall(list_pattern, content)
    
    # Find Optional[CustomType] patterns  
    optional_pattern = r'Optional\[([A-Z]\w*)\]'
    optional_matches = re.findall(optional_pattern, content)
    
    # Find bare CustomType patterns
    bare_pattern = r':\s*([A-Z]\w+)(?:\s|$|=)'
    bare_matches = re.findall(bare_pattern, content)
    
    # Combine all matches and remove duplicates
    all_types = set(list_matches + optional_matches + bare_matches)
    
    # Filter out built-in types
    builtin_types = {'List', 'Dict', 'Optional', 'Union', 'Any', 'Tuple', 'Set'}
    custom_types = [t for t in all_types if t not in builtin_types]
    
    return custom_types

def fix_model_imports(file_path):
    """Fix imports in a single model file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract filename for class name detection
    filename = os.path.basename(file_path)
    current_class = filename.replace('.py', '')
    # Convert snake_case to PascalCase
    current_class = ''.join(word.capitalize() for word in current_class.split('_'))
    
    # Extract custom types
    custom_types = extract_custom_types(content)
    
    # Remove self-references
    custom_types = [t for t in custom_types if t != current_class]
    
    if not custom_types:
        return False  # No changes needed
    
    # Check if TYPE_CHECKING is already imported
    has_type_checking = 'TYPE_CHECKING' in content
    
    # Create the import section
    imports_section = []
    for custom_type in custom_types:
        # Convert PascalCase to snake_case for filename
        snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', custom_type).lower()
        imports_section.append(f"    from .{snake_case} import {custom_type}")
    
    # Find the imports section
    lines = content.split('\n')
    
    # Find where to insert TYPE_CHECKING import and the conditional imports
    type_imports_line = -1
    type_checking_line = -1
    
    for i, line in enumerate(lines):
        if line.startswith('from typing import'):
            type_imports_line = i
        elif line.startswith('if TYPE_CHECKING:'):
            type_checking_line = i
            break
    
    # Update the typing import to include TYPE_CHECKING if needed
    if type_imports_line >= 0 and not has_type_checking:
        typing_line = lines[type_imports_line]
        if 'TYPE_CHECKING' not in typing_line:
            lines[type_imports_line] = typing_line.rstrip() + ', TYPE_CHECKING'
    
    # Add or update the TYPE_CHECKING section
    if type_checking_line >= 0:
        # Replace existing TYPE_CHECKING section
        j = type_checking_line + 1
        while j < len(lines) and (lines[j].startswith('    from .') or lines[j].strip() == ''):
            j += 1
        # Remove old imports
        del lines[type_checking_line + 1:j]
        # Insert new imports
        for imp in imports_section:
            lines.insert(type_checking_line + 1, imp)
            type_checking_line += 1
    else:
        # Add new TYPE_CHECKING section after the typing imports
        if type_imports_line >= 0:
            insert_pos = type_imports_line + 1
            lines.insert(insert_pos, '')
            lines.insert(insert_pos + 1, 'if TYPE_CHECKING:')
            for i, imp in enumerate(imports_section):
                lines.insert(insert_pos + 2 + i, imp)
    
    # Quote all custom type references
    new_content = '\n'.join(lines)
    for custom_type in custom_types:
        # Replace List[CustomType] with List['CustomType']
        new_content = re.sub(fr'List\[{custom_type}\]', f"List['{custom_type}']", new_content)
        # Replace Optional[CustomType] with Optional['CustomType']  
        new_content = re.sub(fr'Optional\[{custom_type}\]', f"Optional['{custom_type}']", new_content)
        # Replace bare CustomType with 'CustomType' (but be careful about class definitions)
        new_content = re.sub(fr':\s*{custom_type}(\s|$|=)', f": '{custom_type}'\\1", new_content)
    
    # Write back the fixed content
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    return True

def main():
    """Main function to fix all model files."""
    model_dir = Path('rbczpremiumapi/Model')
    
    fixed_count = 0
    for py_file in model_dir.glob('*.py'):
        if py_file.name != '__init__.py':
            print(f"Processing {py_file.name}...")
            if fix_model_imports(py_file):
                print(f"  ✅ Fixed imports in {py_file.name}")
                fixed_count += 1
            else:
                print(f"  ⏭️  No custom types found in {py_file.name}")
    
    print(f"\n🎉 Fixed {fixed_count} model files!")

if __name__ == '__main__':
    main()