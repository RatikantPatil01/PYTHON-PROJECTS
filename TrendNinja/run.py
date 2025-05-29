import subprocess
import sys
import importlib.util
import os

# List all required packages except TA-Lib
required_packages = [
    "streamlit",
    "pandas",
    "numpy",
    "matplotlib",
    "plotly",
    "scipy",
    "scikit-learn",
    "requests",
    "yfinance",
]

def is_installed(pkg):
    return importlib.util.find_spec(pkg) is not None

def install_package(pkg):
    print(f"📦 Installing {pkg} ...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

def main():
    print("📂 Current working directory:", os.getcwd())
    print("📄 Files here:", os.listdir())

    for pkg in required_packages:
        # import names for some packages differ from pip package names
        check_name = pkg.replace("-", "_")
        if not is_installed(check_name):
            install_package(pkg)
        else:
            print(f"✔️ {pkg} is already installed.")

    print("🚀 Launching PatternScope Dashboard...")
    subprocess.call([sys.executable, "-m", "streamlit", "run", "main.py"])

if __name__ == "__main__":
    main()
