# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['qt', 'ontologies', 'C:\\Python35\\Lib\\site-packages\\PyQt5\\Qt\\bin', '.'],
             binaries=None,
             datas= [ ('..\\nmrml2isa\\nmrml2isa\\default\\a_nmrML.txt', 'nmrml2isa\\default' ),
		              ('..\\nmrml2isa\\nmrml2isa\\default\\i_nmrML.txt', 'nmrml2isa\\default' ),
		              ('..\\nmrml2isa\\nmrml2isa\\default\\s_nmrML.txt', 'nmrml2isa\\default' ),
		              ('..\\nmrml2isa\\nmrml2isa\\nmrCV.owl', 'nmrml2isa' ),
		              ('ontologies\\pro.json', 'ontologies' ),
		              ('ontologies\\pso.json', 'ontologies' )],
             hiddenimports=['imzml2isa_qt'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
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
          name='nmrml2isa_gui',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='qt\\assets\\graphics\\ebi_icon.ico')
