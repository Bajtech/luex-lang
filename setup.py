from distutils.core import setup
import py2exe
import sys
sys.path.append("src")
packages = ["keywords", "tokens", "error", "function", "variable", "aliases", "boolean", "anonymous_function", "table", "strings", "exports"]

import glob

setup(
    options = {"py2exe": {
                          "packages": packages,
                         }
              },
    zipfile = None,
    #data_files = my_data_files,
    console=[{
      "script": 'main.py',
      "icon_resources": [(0, "luexlogo.ico")]
    }]
)