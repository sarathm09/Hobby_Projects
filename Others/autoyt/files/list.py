import os
import sys
 
for root, _, files in os.walk("."):
    for f in files:
        fname = os.path.join(root, f)
        print fname