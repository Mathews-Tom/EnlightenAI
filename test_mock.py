#!/usr/bin/env python3
"""
Test script for EnlightenAI with mock data.

This script tests the EnlightenAI tutorial generation workflow with mock data
instead of making actual API calls or network requests.
"""

import os
import sys
import argparse
from dotenv import load_dotenv
from utils.mock_data import create_mock_tutorial_flow

# Load environment variables from .env file
load_dotenv()


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Test EnlightenAI with mock data"
    )
    
    parser.add_argument(
        "--output-dir",
        default="mock_output",
        help="Output directory for generated tutorial (default: mock_output/)"
    )
    
    parser.add_argument(
        "--include",
        default="*.py,*.md",
        help="Comma-separated list of file patterns to include (default: *.py,*.md)"
    )
    
    parser.add_argument(
        "--exclude",
        default="test_*,*__pycache__*",
        help="Comma-separated list of file patterns to exclude (default: test_*,*__pycache__*)"
    )
    
    parser.add_argument(
        "--llm-provider",
        default="openai",
        choices=["openai", "anthropic", "palm", "local"],
        help="LLM provider to use (default: openai)"
    )
    
    parser.add_argument(
        "--api-key",
        help="API key for the LLM provider (defaults to environment variable)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    return parser.parse_args()


def main():
    """Main entry point for the test script."""
    args = parse_arguments()
    
    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Create shared context for the workflow
    context = {
        "repo_url": "https://github.com/mock/repo",  # Not used with mock data
        "web_url": "https://example.com/mock",  # Not used with mock data
        "output_dir": args.output_dir,
        "include_patterns": args.include.split(","),
        "exclude_patterns": args.exclude.split(","),
        "llm_provider": args.llm_provider,
        "api_key": args.api_key,
        "verbose": args.verbose,
        "files": {},  # Will store {path: content} pairs
        "web_content": {},  # Will store web crawl results
        "abstractions": [],  # Will store identified components
        "relationships": [],  # Will store component relationships
        "chapter_order": [],  # Will store ordered chapter sequence
    }
    
    # Create and run the tutorial generation flow with mock data
    try:
        flow = create_mock_tutorial_flow(use_mock_repo=True, use_mock_web=True)
        result = flow.run(context)
        
        print(f"Tutorial generated successfully in {args.output_dir}")
        print(f"Main index file: {os.path.join(args.output_dir, 'index.md')}")
        
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
