# build.spec

block_cipher = None

a = Analysis(
    ['run_sfw.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
)

exe = EXE(
    pyz,
    a.scripts,
    name='StylometricWorkbench',
    console=True,
)