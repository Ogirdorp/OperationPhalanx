import shutil, sys, os
import settings as cfg
import subprocess

mish = "RisingScimitar.Takistan"
#subprocess.call("python make.py")
shutil.copytree(mish, os.path.join(cfg.mpmissions_folder,mish))
