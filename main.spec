# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py', 'B_ion.py', 'branch_Yions.py', 'candidate.py', 'get_master_scan.py', 'glycan.py', 'glycan_20181203.py', 'glycan_decoy.py', 'glycan_new.py', 'glycan_O.py', 'glycan_scoring.py', 'hit.py', 'isotopic.py', 'label.py', 'lsomer.py', 'main_process.py', 'mass.py', 'matched_glycan_and_peptide.py', 'mgfreader.py', 'mic.py', 'msdata.py', 'mul_process_package.py', 'mzmlreader.py', 'mzmlreader_sjc.py', 'parameter.py', 'peptide.py', 'peptide_mass_searcher.py', 'precursor.py', 'preprocess.py', 'raw_file_read.py', 'rawreader.py', 'read_fatsa.py', 'read_fatsa_format_N.py', 'result.py', 'scoring.py', 'spectrum.py', 'test_license.py', 'theoreticalPeaks.py', 'test_precursor_charge.py', 'main_process2.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['StrucOGP.ico'],
)
