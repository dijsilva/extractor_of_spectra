# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/dsilva/projects/extractor_of_spectra'],
             binaries=[],
             datas=[('/home/dsilva/projects/extractor_of_spectra/images/start.png', '/home/dsilva/projects/extractor_of_spectra/images'), ('/home/dsilva/projects/extractor_of_spectra/images/select.png', '/home/dsilva/projects/extractor_of_spectra/images')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='/home/dsilva/projects/extractor_of_spectra/images/icon.ico')
