import yaml
import glob
import sys

print("Starting validation...")
files = glob.glob('_data/*.yml') + glob.glob('_config.yml')
for f in files:
    try:
        with open(f, 'r') as stream:
            yaml.safe_load(stream)
            print(f"OK: {f}")
    except yaml.YAMLError as exc:
        print(f"Error in {f}: {exc}")
        sys.exit(1)
