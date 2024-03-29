# coding: utf-8
'''python makeexe.py build'''
name = 'matrix'
filename = name + '.py'
from cx_Freeze import setup, Executable

import sys
'''
import argparse
parser = argparse.ArgumentParser(description='Enter filename')
parser.add_argument(
    '-f',
    '--filename',
    default='example',
    help='provide an filename with out extension -f=filename (default: example )'
)
my_namespace = parser.parse_args()
print(my_namespace)
name = my_namespace.filename
filename = my_namespace.filename + '.py'
'''

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [Executable(filename,
                          targetName=name + '_wx.exe',
                          base=base,
                          icon='example.ico')]

#buildOptions = dict(packages = [], excludes = [])
excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml',
            'bz2', 'select']

zip_include_packages = ['collections', 'encodings', 'importlib']  # , 'wx'

# options = dict(build_exe = buildOptions),
options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
    }
}

setup(name=name,
      version='0.0.13',
      description='My {} App!'.format(name),
      options=options,
      executables=executables)  # options = dict(build_exe = buildOptions),
