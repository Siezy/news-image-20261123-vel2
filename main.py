# news-image-20261123 entry v2: deterministic copy, verified identical
# No network; deterministic (same bytes every run).
import shutil, os
os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.png"), "/output/entry.png")