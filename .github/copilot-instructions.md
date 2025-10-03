# GitHub Copilot Instructions for RBC Premium API Python Library

## Project Overview

This project creates a client Python library generated from OpenAPI schema that interacts with Raiffeisen bank API. The library is generated from an OpenAPI specification using OpenAPI Generator with custom templates to provide a complete, type-safe Python client for the Raiffeisenbank Czech Republic (RBC) Premium API.

## Template-to-Source Code Relationship

### 🔄 **Critical Understanding: Template-Driven Architecture**

This project creates a client Python library using a **template-driven code generation** approach where:

1. **Source of Truth**: OpenAPI specification (`01rbczpremiumapi.yaml`) defining Raiffeisen bank API
2. **Code Generator**: OpenAPI Generator 7.13.0 with custom Python templates
3. **Custom Templates**: Located in `.openapi-generator/templates/`
4. **Generated Client Library**: All files in `rbczpremiumapi/` directory providing Python client for bank API

### 📁 **Template Structure**

```
.openapi-generator/
├── config.yaml                 # Generator configuration
└── templates/                  # Custom Mustache templates
    ├── __init__.mustache       # Package __init__.py files
    ├── model_init.mustache     # Model package __init__.py
    ├── api.mustache            # Individual API class files
    ├── model.mustache          # Individual model class files
    └── [other templates...]
```

### 🎯 **Template-to-File Mapping**

| Template File | Generates | Purpose |
|---------------|-----------|---------|
| `__init__.mustache` | `rbczpremiumapi/__init__.py` | Main package imports |
| `model_init.mustache` | `rbczpremiumapi/Model/__init__.py` | Model package imports |
| `api_init.mustache` | `rbczpremiumapi/PremiumAPI/__init__.py` | API package imports |
| `model.mustache` | `rbczpremiumapi/Model/*.py` | Individual model classes |
| `api.mustache` | `rbczpremiumapi/PremiumAPI/*.py` | Individual API classes |

### 🔧 **Generation Process**

1. **Trigger**: Run `./regenerate.sh`
2. **Input**: `01rbczpremiumapi.yaml` + Custom templates
3. **Process**: OpenAPI Generator applies templates with OpenAPI data
4. **Output**: Generated Python files in `rbczpremiumapi/`

## ⚠️ **CRITICAL RULE: Template Synchronization**

### 🚨 **NEVER Edit Generated Files Directly**

**Rule**: Every change in source code MUST be applied to the corresponding templates, NOT to the generated files directly.

### ❌ **Wrong Approach**
```bash
# DON'T DO THIS - Changes will be lost on next regeneration
vim rbczpremiumapi/__init__.py
vim rbczpremiumapi/Model/currency_list_simple.py
```

### ✅ **Correct Approach**
```bash
# DO THIS - Edit templates, then regenerate
vim .openapi-generator/templates/__init__.mustache
vim .openapi-generator/templates/model.mustache
./regenerate.sh
```

### 🔄 **Workflow for Code Changes**

1. **Identify Issue**: Find problem in generated code
2. **Locate Template**: Find corresponding `.mustache` template
3. **Edit Template**: Make changes using Mustache syntax
4. **Regenerate**: Run `./regenerate.sh` to apply changes
5. **Test**: Verify the fix works in generated code
6. **Commit**: Commit template changes, not generated code changes

### 📝 **Example: Fixing Import Issues**

**Problem**: Generated `__init__.py` has wrong imports
```python
# Generated (WRONG - don't edit this file)
from PremiumAPI.download_statement_api import DownloadStatementApi
```

**Solution**: Edit template
```mustache
{{!-- .openapi-generator/templates/__init__.mustache --}}
from .{{apiPackage}}.{{classFilename}} import {{classname}}
```

**Result**: After regeneration
```python
# Generated (CORRECT)
from .PremiumAPI.download_statement_api import DownloadStatementApi
```

## 🎨 **Mustache Template Syntax**

### Common Variables
- `{{package}}` - Package name (rbczpremiumapi)
- `{{apiPackage}}` - API package name (PremiumAPI)
- `{{modelPackage}}` - Model package name (Model)
- `{{classname}}` - Class name
- `{{classFilename}}` - File name for class

### Template Examples
```mustache
{{!-- Import with relative path --}}
from .{{apiPackage}}.{{classFilename}} import {{classname}}

{{!-- Conditional generation --}}
{{#models}}
from .{{classFilename}} import {{classname}}
{{/models}}

{{!-- Comments in templates --}}
{{! This is a comment that won't appear in generated code }}
```

## 🔍 **Debugging Template Issues**

### When Generated Code is Wrong:

1. **Check Template**: Look at corresponding `.mustache` file
2. **Check Variables**: Verify Mustache variables are correct
3. **Test Locally**: Edit template and run `./regenerate.sh`
4. **Verify Output**: Check if generated code is now correct

### Common Issues:
- **Import Paths**: Use relative imports (`.module`) not absolute
- **Package Names**: Use `{{apiPackage}}` and `{{modelPackage}}` variables
- **Syntax Errors**: Check Mustache syntax in templates

## 📚 **Key Files to Understand**

### Configuration
- `.openapi-generator/config.yaml` - Generator settings
- `regenerate.sh` - Regeneration script

### Templates (Source of Truth)
- `.openapi-generator/templates/*.mustache` - All template files

### Generated (Do Not Edit Directly)
- `rbczpremiumapi/**/*.py` - All generated Python files

## 🚀 **Development Workflow**

```bash
# 1. Edit templates
vim .openapi-generator/templates/__init__.mustache

# 2. Regenerate code
./regenerate.sh

# 3. Test changes
source venv/bin/activate
python -c "import rbczpremiumapi; print('Success')"

# 4. Commit template changes
git add .openapi-generator/templates/
git commit -m "Fix: Update template imports"
```

## 🎯 **Best Practices**

1. **Always edit templates, never generated files**
2. **Test after every template change**
3. **Use relative imports in templates**
4. **Commit template changes, not generated code**
5. **Document template modifications**

## 🔧 **Troubleshooting**

### If imports fail after regeneration:
1. Check `.openapi-generator/templates/__init__.mustache`
2. Verify relative import syntax: `from .{{package}}`
3. Run `./regenerate.sh` again
4. Test with `python -c "import rbczpremiumapi"`

### If API classes have syntax errors:
1. Check `.openapi-generator/templates/api.mustache`
2. Look for malformed import statements
3. Fix template syntax
4. Regenerate and test

Remember: **Templates are the source of truth** - all changes must go through them!
