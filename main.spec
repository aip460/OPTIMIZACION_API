# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\AlbertoI\\PycharmProjects\\OPTIMIZACION_GG'],
              binaries=[('C:\\Users\\AlbertoI\\anaconda3\\envs\\OPTIMIZACION_GG\\Lib\\site-packages\\mip\\libraries\\*.dylib','.')],
             datas=[('.\\images\\*.gif','images'),
             ('.\\comprobaciones.py','.'),
             ('.\\FullScreenApp.py','.'),
             ('.\\optimizador.py','.'),
             ('.\\save.py','.'),
             ('.\\ScrollableFrame.py','.'),
              ( 'C:\\Users\\AlbertoI\\anaconda3\\envs\\OPTIMIZACION_GG\\Lib\\site-packages\\mip\\*', 'mip' ),
               ( 'C:\\Users\\AlbertoI\\anaconda3\\envs\\OPTIMIZACION_GG\\Lib\\site-packages\\mip\\libraries\\*.dylib', 'mip\\libraries' ),
                              ( 'C:\\Users\\AlbertoI\\anaconda3\\envs\\OPTIMIZACION_GG\\Lib\\site-packages\\mip\\libraries\\lin64\*', 'mip\\libraries\\lin64' ),
                             ( 'C:\\Users\\AlbertoI\\anaconda3\\envs\\OPTIMIZACION_GG\\Lib\\site-packages\\mip\\libraries\\win64\*', 'mip\\libraries\\win64' ) ],
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
