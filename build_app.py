import os
import sys
import shutil
import glob
import multiprocessing
import PyInstaller.__main__

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def run_build():
    # Automatically clear stale build folders from previous user/system
    for folder in ["build", "dist"]:
        if os.path.exists(folder):
            shutil.rmtree(folder, ignore_errors=True)
    if os.path.exists("NPCS.spec"):
        os.remove("NPCS.spec")

    user_home = os.path.expanduser("~")
    paddlex_models = os.path.join(user_home, ".paddlex")
    cache_models = os.path.join(user_home, ".cache")

    conda_library_bin = os.path.join(sys.prefix, "Library", "bin")
    conda_dlls = os.path.join(sys.prefix, "DLLs")

    print(f"--- Active Environment: {sys.prefix} ---")
    print(f"--- Conda DLL Location: {conda_library_bin} ---")
    print("--- Preparing PyInstaller Build Configuration ---")

    pyinstaller_args = [
        "NPCS.py",
        "--noconsole",
        "--noconfirm",
        "--onedir",
        "--name=NPCS",
        "--clean",

        f"--paths={sys.prefix}",
        f"--paths={conda_library_bin}",
        f"--paths={conda_dlls}",

        "--collect-all=paddleocr",
        "--collect-all=paddlex",
        "--collect-all=paddle",
        "--collect-all=pyclipper",
        "--collect-all=cv2",
        "--collect-all=pygame",
        "--collect-all=albumentations",

        "--hidden-import=_ctypes",
        "--hidden-import=Cython",
        "--hidden-import=Cython.Compiler.Code",
        "--hidden-import=Cython.Compiler.Symtab",
        "--hidden-import=Cython.Compiler.PyrexTypes",
        "--hidden-import=paddle.lazy_space",

        "--icon=NPCS_logotype.ico",
    ]

    # Explicitly include Python DLLs from Conda root to prevent missing DLL errors on target machines
    for dll in glob.glob(os.path.join(sys.prefix, "python*.dll")):
        pyinstaller_args.append(f"--add-binary={dll};.")

    if os.path.exists("NPCS_logotype.ico"):
        pyinstaller_args.append("--add-data=NPCS_logotype.ico;.")

    if os.path.exists("good.mp3"):
        pyinstaller_args.append("--add-data=good.mp3;.")

    if os.path.exists("bad.mp3"):
        pyinstaller_args.append("--add-data=bad.mp3;.")

    if os.path.exists(paddlex_models):
        pyinstaller_args.append(f"--add-data={paddlex_models};.paddlex")

    if os.path.exists(cache_models):
        pyinstaller_args.append(f"--add-data={cache_models};.cache")

    print("\nStarting PyInstaller build process...")
    PyInstaller.__main__.run(pyinstaller_args)
    print("\n--- Build Complete! ---")


if __name__ == '__main__':
    multiprocessing.freeze_support()
    run_build()