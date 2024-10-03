import importlib
import os

# List of packages to include in requirements.txt
packages = [
    "flask",
    "flask_cors",
    "tensorflow",
    "numpy",
    "Pillow",  # Pillow is the package name for PIL
    "keras",
    "werkzeug",
    "pandas"
]

def generate_requirements_txt(filename='requirements.txt'):
    with open(filename, 'w') as f:
        for package in packages:
            try:
                # Import the package
                pkg = importlib.import_module(package)
                # Write package name and version to requirements.txt
                f.write(f"{package}=={pkg.__version__}\n")
            except ImportError:
                print(f"Package {package} is not installed.")
            except AttributeError:
                print(f"Package {package} does not have a __version__ attribute.")

# Call the function to generate requirements.txt
generate_requirements_txt()
