# -*- mode: python -*-
import os, sys
block_cipher = None
CONSOLE = False # True - console. False - no console.

a = Analysis(['javaparser.py', 'run.spec'],
             pathex=[os.path.abspath('')],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += Tree('img', prefix='img')

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='JavaParserAI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=CONSOLE,
          icon='img/icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='JavaParserAI')
