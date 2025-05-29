# utils/setup.py

import subprocess
import sys
import pkg_resources
import os

def install_requirements():
    print("🔍 Checking and Installing Requirements...")

    if os.path.exists(".installed"):
        print("✅ Requirements already satisfied (cached).")
        return

    try:
        with open('requirements.txt') as f:
            required = f.read().splitlines()

        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = [pkg for pkg in required if pkg.split('==')[0].lower() not in installed]

        if missing:
            print(f"📦 Installing: {', '.join(missing)}")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
        else:
            print("✅ All requirements are already satisfied.")

        # Flag file to skip next time
        with open('.installed', 'w') as f:
            f.write('done')

    except Exception as e:
        print(f'❌ Error installing requirements: {e}')
