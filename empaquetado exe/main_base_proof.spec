# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\AlbertoI\\PycharmProjects\\OPTIMIZACION_GG'],
             binaries=[],
             datas=[('.\\images\\*.gif','images'),
             ('.\\comprobaciones.py','.'),
             ('.\\FullScreenApp.py','.'),
             ('.\\optimizador.py','.'),
             ('.\\save.py','.'),
             ('.\\ScrollableFrame.py','.')],
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
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main',
               icon='images\\wood_icon_158050.ico')





