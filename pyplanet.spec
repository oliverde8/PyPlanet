# -*- mode: python -*-

block_cipher = None


a = Analysis(['cli.py'],
             pathex=['./'],
             binaries=[],
             datas=[('pyplanet', 'pyplanet')],
             hiddenimports=['watchdog', 'watchdog.events', 'colorlog', 'aiofiles'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['__pycache__', '*/__pycache__'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pyplanet',
          debug=False,
          strip=False,
          upx=True,
          console=True )
