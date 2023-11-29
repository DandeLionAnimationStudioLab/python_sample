import os
import logging

logger = logging.getLogger(__name__)

version_file_path = os.path.join(os.path.dirname(__file__), 'version.txt')
if os.path.exists(version_file_path):
    with open(version_file_path, 'r') as f:
        __version__ = f.read().strip()
else:
    __version__ = 'v0.0.0'
