#!/usr/bin/env python3
"""
Quick installation script for Gemma Kaggle Project
Run this to install all dependencies and verify setup
"""

import subprocess
import sys
import os
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")

def run_command(command, description):
    """Run a shell command and report results"""
    print(f"→ {description}...")
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            capture_output=True, 
            text=True
        )
        print(f"✓ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is adequate"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 8:
        print("✓ Python version is adequate (3.8+)")
        return True
    else:
        print("✗ Python version must be 3.8 or higher")
        return False

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if env_file.exists():
        print("✓ .env file already exists")
        return True
    
    if env_example.exists():
        try:
            env_example.read_text()
            with open(env_file, 'w') as f:
                f.write(env_example.read_text())
            print("✓ Created .env file from template")
            print("⚠ Remember to add your GOOGLE_API_KEY to .env")
            return True
        except Exception as e:
            print(f"✗ Failed to create .env file: {e}")
            return False
    else:
        print("⚠ .env.example not found, skipping .env creation")
        return True

def main():
    """Main installation process"""
    print_header("Gemma Kaggle Project - Installation Script")
    
    # Check Python version
    print_header("Checking Python Version")
    if not check_python_version():
        sys.exit(1)
    
    # Install packages
    print_header("Installing Required Packages")
    
    packages = [
        ("pip install --upgrade pip", "Upgrading pip"),
        ("pip install -U keras>=3.0.0", "Installing Keras 3"),
        ("pip install -U keras-hub", "Installing Keras Hub"),
        ("pip install jax[cpu]", "Installing JAX (CPU)"),
        ("pip install google-generativeai", "Installing Google Generative AI"),
        ("pip install python-dotenv", "Installing python-dotenv"),
        ("pip install numpy pandas matplotlib", "Installing data science packages"),
        ("pip install jupyter ipykernel", "Installing Jupyter"),
    ]
    
    failed = []
    for command, description in packages:
        if not run_command(command, description):
            failed.append(description)
    
    # Create .env file
    print_header("Setting Up Environment")
    create_env_file()
    
    # Summary
    print_header("Installation Summary")
    
    if failed:
        print("⚠ The following installations had issues:")
        for item in failed:
            print(f"  - {item}")
        print("\nYou may need to install these manually.")
    else:
        print("✓ All packages installed successfully!")
    
    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("1. Edit .env and add your GOOGLE_API_KEY")
    print("   Get key from: https://aistudio.google.com/app/apikey")
    print("\n2. Run setup verification:")
    print("   jupyter notebook setup.ipynb")
    print("\n3. Review the getting started guide:")
    print("   Open GETTING_STARTED.md")
    print("\n4. Join Discord:")
    print("   https://discord.gg/kaggle")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
