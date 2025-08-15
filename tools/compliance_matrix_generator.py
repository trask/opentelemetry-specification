#!/usr/bin/env python3
"""
OpenTelemetry Spec Compliance Matrix Generator

This tool generates compliance matrices and documentation from the 
spec-requirements.yaml file and language implementation YAML files.

Usage:
    python compliance_matrix_generator.py [options]

Options:
    --spec-file SPEC_FILE       Path to spec requirements YAML file
    --lang-dir LANG_DIR         Directory containing language implementation YAML files  
    --output-format FORMAT      Output format: markdown, html, json (default: markdown)
    --output OUTPUT             Output file path (default: stdout)
    --include-experimental      Include experimental features in output
"""

import argparse
import sys
import yaml
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class FeatureRequirement:
    """Represents a single feature requirement."""
    id: str
    name: str
    status: str
    optional: bool = False
    spec_url: Optional[str] = None
    note: Optional[str] = None


@dataclass
class Feature:
    """Represents a feature with its requirements."""
    id: str
    name: str
    description: str
    status: str
    optional: bool = False
    spec_url: Optional[str] = None
    requirements: List[FeatureRequirement] = field(default_factory=list)


@dataclass
class Category:
    """Represents a category of features."""
    name: str
    description: str
    features: List[Feature] = field(default_factory=list)


@dataclass
class LanguageImplementation:
    """Represents language implementation status."""
    name: str
    features: Dict[str, str] = field(default_factory=dict)  # feature_id -> status


class ComplianceMatrixGenerator:
    """Generates compliance matrices from specification and implementation data."""
    
    def __init__(self):
        self.spec_categories: Dict[str, Category] = {}
        self.language_implementations: Dict[str, LanguageImplementation] = {}
        
    def load_spec_requirements(self, spec_file: Path) -> None:
        """Load specification requirements from YAML file."""
        with open(spec_file, 'r', encoding='utf-8') as f:
            spec_data = yaml.safe_load(f)
            
        categories_data = spec_data.get('categories', {})
        
        for category_id, category_data in categories_data.items():
            category = Category(
                name=category_data['name'],
                description=category_data['description']
            )
            
            for feature_data in category_data.get('features', []):
                feature = Feature(
                    id=feature_data['id'],
                    name=feature_data['name'],
                    description=feature_data['description'],
                    status=feature_data['status'],
                    optional=feature_data.get('optional', False),
                    spec_url=feature_data.get('spec_url')
                )
                
                for req_data in feature_data.get('requirements', []):
                    requirement = FeatureRequirement(
                        id=req_data['id'],
                        name=req_data['name'],
                        status=req_data['status'],
                        optional=req_data.get('optional', False),
                        spec_url=req_data.get('spec_url'),
                        note=req_data.get('note')
                    )
                    feature.requirements.append(requirement)
                
                category.features.append(feature)
            
            self.spec_categories[category_id] = category
    
    def load_language_implementations(self, lang_dir: Path) -> None:
        """Load language implementation data from YAML files."""
        if not lang_dir.exists():
            return
            
        for yaml_file in lang_dir.glob('*.yaml'):
            with open(yaml_file, 'r', encoding='utf-8') as f:
                lang_data = yaml.safe_load(f)
                
            lang_name = lang_data.get('language', yaml_file.stem)
            implementation = LanguageImplementation(name=lang_name)
            
            # Load feature implementations
            for feature_id, status in lang_data.get('features', {}).items():
                implementation.features[feature_id] = status
                
            self.language_implementations[lang_name] = implementation
    
    def get_status_symbol(self, status: str) -> str:
        """Convert status string to display symbol."""
        symbol_map = {
            'stable': '+',
            'experimental': '🧪',
            'not_supported': '-',
            'not_applicable': 'N/A',
            'unknown': ''
        }
        return symbol_map.get(status.lower(), status)
    
    def get_spec_status_indicator(self, status: str) -> str:
        """Get indicator for specification status."""
        if status.lower() in ['experimental', 'development', 'alpha']:
            return ' 🚧'
        elif status.lower() == 'deprecated':
            return ' ⚠️'
        return ''
    
    def generate_markdown_matrix(self, category_id: str, include_experimental: bool = True) -> str:
        """Generate markdown compliance matrix for a category."""
        if category_id not in self.spec_categories:
            return f"Category '{category_id}' not found"
            
        category = self.spec_categories[category_id]
        
        # Define language order to match original compliance matrix
        language_order = ["Go", "Java", "JS", "Python", "Ruby", "Erlang", "PHP", "Rust", "C++", ".NET", "Swift"]
        all_languages = set(self.language_implementations.keys())
        
        # Use ordered languages that exist in implementations
        languages = [lang for lang in language_order if lang in all_languages]
        # Add any additional languages not in the predefined order
        additional_langs = sorted(all_languages - set(languages))
        languages.extend(additional_langs)
        
        # Header
        output = [f"## {category.name}\n"]
        
        # Table header
        header = "| Feature | Optional | " + " | ".join(languages) + " |"
        separator = "|" + "|".join(["-" * max(len(col), 3) for col in ["Feature", "Optional"] + languages]) + "|"
        
        output.extend([header, separator])
        
        # Process features and requirements
        for feature in category.features:
            # Skip experimental features if not including them
            if not include_experimental and feature.status.lower() in ['experimental', 'development']:
                continue
                
            # Feature header row (if it has multiple requirements)
            if len(feature.requirements) > 1:
                spec_indicator = self.get_spec_status_indicator(feature.status)
                optional_indicator = "Optional" if feature.optional else ""
                
                feature_name = f"[{feature.name}]({feature.spec_url}){spec_indicator}" if feature.spec_url else f"{feature.name}{spec_indicator}"
                
                # Language columns for feature header show all language names
                lang_cols = languages if languages else []
                
                row = f"| {feature_name} | {optional_indicator} | " + " | ".join(lang_cols) + " |"
                output.append(row)
            
            # Requirement rows
            for req in feature.requirements:
                # Skip experimental requirements if not including them
                if not include_experimental and req.status.lower() in ['experimental', 'development']:
                    continue
                    
                spec_indicator = self.get_spec_status_indicator(req.status)
                optional_indicator = "X" if req.optional else ""
                
                req_name = f"[{req.name}]({req.spec_url}){spec_indicator}" if req.spec_url else f"{req.name}{spec_indicator}"
                
                # Get implementation status for each language
                lang_statuses = []
                for lang_name in languages:
                    implementation = self.language_implementations[lang_name]
                    status = implementation.features.get(req.id, 'unknown')
                    symbol = self.get_status_symbol(status)
                    lang_statuses.append(symbol)
                
                row = f"| {req_name} | {optional_indicator} | " + " | ".join(lang_statuses) + " |"
                output.append(row)
        
        return "\n".join(output)
    
    def generate_full_markdown_matrix(self, include_experimental: bool = True) -> str:
        """Generate full markdown compliance matrix."""
        output = []
        
        # Header with legend
        output.append("# Compliance of Implementations with Specification\n")
        output.append("The following tables show which features are implemented by each OpenTelemetry")
        output.append("language implementation.\n")
        
        output.append("## Legend\n")
        output.append("### Implementation Status\n")
        output.append("- `+` means the feature is supported and stable in the language implementation")
        output.append("- `-` means the feature is not supported")
        output.append("- `🧪` means the feature has experimental support in the language implementation")
        output.append("- `N/A` means the feature is not applicable to the particular language")
        output.append("- blank cell means the status of the feature is not known\n")
        
        output.append("### Specification Status\n")
        output.append("- Features marked with `🚧` are experimental in the specification")
        output.append("- Features marked with `⚠️` are deprecated in the specification")
        output.append("- Features with no symbol are stable in the specification\n")
        
        # Generate matrix for each category
        for category_id in self.spec_categories:
            matrix = self.generate_markdown_matrix(category_id, include_experimental)
            output.append(matrix)
            output.append("")  # Empty line between categories
        
        return "\n".join(output)
    
    def generate_json_output(self, include_experimental: bool = True) -> str:
        """Generate JSON format output."""
        result = {
            'version': '1.0.0',
            'spec_categories': {},
            'language_implementations': {},
            'matrix': {}
        }
        
        # Spec categories
        for cat_id, category in self.spec_categories.items():
            cat_data = {
                'name': category.name,
                'description': category.description,
                'features': []
            }
            
            for feature in category.features:
                if not include_experimental and feature.status.lower() in ['experimental', 'development']:
                    continue
                    
                feature_data = {
                    'id': feature.id,
                    'name': feature.name,
                    'description': feature.description,
                    'status': feature.status,
                    'optional': feature.optional,
                    'spec_url': feature.spec_url,
                    'requirements': []
                }
                
                for req in feature.requirements:
                    if not include_experimental and req.status.lower() in ['experimental', 'development']:
                        continue
                        
                    req_data = {
                        'id': req.id,
                        'name': req.name,
                        'status': req.status,
                        'optional': req.optional,
                        'spec_url': req.spec_url,
                        'note': req.note
                    }
                    feature_data['requirements'].append(req_data)
                
                cat_data['features'].append(feature_data)
            
            result['spec_categories'][cat_id] = cat_data
        
        # Language implementations
        for lang_name, implementation in self.language_implementations.items():
            result['language_implementations'][lang_name] = {
                'name': implementation.name,
                'features': implementation.features
            }
        
        return json.dumps(result, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Generate OpenTelemetry compliance matrices')
    parser.add_argument('--spec-file', type=Path, default='spec-requirements.yaml',
                       help='Path to spec requirements YAML file')
    parser.add_argument('--lang-dir', type=Path, default='spec-compliance-matrix',
                       help='Directory containing language implementation YAML files')
    parser.add_argument('--output-format', choices=['markdown', 'html', 'json'], default='markdown',
                       help='Output format')
    parser.add_argument('--output', type=Path, help='Output file path (default: stdout)')
    parser.add_argument('--include-experimental', action='store_true', default=True,
                       help='Include experimental features in output')
    parser.add_argument('--category', help='Generate matrix for specific category only')
    
    args = parser.parse_args()
    
    generator = ComplianceMatrixGenerator()
    
    # Load specification requirements
    if args.spec_file.exists():
        generator.load_spec_requirements(args.spec_file)
    else:
        print(f"Warning: Spec file {args.spec_file} not found", file=sys.stderr)
    
    # Load language implementations
    if args.lang_dir.exists():
        generator.load_language_implementations(args.lang_dir)
    else:
        print(f"Warning: Language implementations directory {args.lang_dir} not found", file=sys.stderr)
    
    # Generate output
    if args.output_format == 'markdown':
        if args.category:
            content = generator.generate_markdown_matrix(args.category, args.include_experimental)
        else:
            content = generator.generate_full_markdown_matrix(args.include_experimental)
    elif args.output_format == 'json':
        content = generator.generate_json_output(args.include_experimental)
    else:
        print(f"Output format {args.output_format} not yet implemented", file=sys.stderr)
        return 1
    
    # Write output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Output written to {args.output}")
    else:
        # Use UTF-8 encoding for stdout to handle Unicode characters
        sys.stdout.reconfigure(encoding='utf-8')
        print(content)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
