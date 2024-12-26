"""Script to generate a batch of test CVs."""

import os
import argparse
from cv_generator import CVGenerator
from ..utils.constants import ENTRY_LEVEL, MID_LEVEL

def generate_test_cvs(num_entry: int = 5, num_mid: int = 5, output_dir: str = None):
    """Generate a batch of test CVs.
    
    Args:
        num_entry: Number of entry-level CVs to generate
        num_mid: Number of mid-level CVs to generate
        output_dir: Directory to save the generated CVs
    """
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'synthetic')
    
    generator = CVGenerator(output_dir)
    
    # Generate entry-level CVs
    print(f"Generating {num_entry} entry-level CVs...")
    for _ in range(num_entry):
        cv_path = generator.generate_cv(ENTRY_LEVEL)
        print(f"Generated: {os.path.basename(cv_path)}")
    
    # Generate mid-level CVs
    print(f"\nGenerating {num_mid} mid-level CVs...")
    for _ in range(num_mid):
        cv_path = generator.generate_cv(MID_LEVEL)
        print(f"Generated: {os.path.basename(cv_path)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic CVs for testing")
    parser.add_argument("--entry", type=int, default=5, help="Number of entry-level CVs to generate")
    parser.add_argument("--mid", type=int, default=5, help="Number of mid-level CVs to generate")
    parser.add_argument("--output", type=str, help="Output directory for generated CVs")
    
    args = parser.parse_args()
    generate_test_cvs(args.entry, args.mid, args.output)
