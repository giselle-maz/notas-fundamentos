### Descripción
Decode this [message](https://challenge-files.picoctf.net/c_fickle_tempest/c9834b19f74a20802d7c53dc42fe1ccd8a69da4cf5c38fa5b6aab8ec472efdd3/message.wav) from the moon.
### Solución
### Solución 1 - consola
```
vamos a descargar y seguir pista 
└─$ wget -q https://challenge-files.picoctf.net/c_fickle_tempest/c9834b19f74a20802d7c53dc42fe1ccd8a69da4cf5c38fa5b6aab8ec472efdd3/message.wav  
                                                                             
┌──(kali㉿kali)-[~]
└─$ file message.wav 
message.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz
                                                                                                
┌──(kali㉿kali)-[~]
└─$ open message.wav 

descargamos una herramienta para decodificar y la usamos

─(kali㉿kali)-[~]
└─$ git clone https://github.com/colaclanth/sstv.git
Cloning into 'sstv'...
remote: Enumerating objects: 221, done.
remote: Counting objects: 100% (59/59), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 221 (delta 51), reused 49 (delta 49), pack-reused 162 (from 1)
Receiving objects: 100% (221/221), 1.01 MiB | 1.85 MiB/s, done.
Resolving deltas: 100% (139/139), done.
                                                                                                
┌──(kali㉿kali)-[~]
└─$ python3 setup.py install
python3: can't open file '/home/kali/setup.py': [Errno 2] No such file or directory
                                                                                                
┌──(kali㉿kali)-[~]
└─$ cd sstv      
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ python3 setup.py install
/usr/lib/python3/dist-packages/setuptools/dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
!!

        ********************************************************************************
        Please consider removing the following classifiers in favor of a SPDX license expression:

        License :: OSI Approved :: GNU General Public License v3 (GPLv3)

        See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
        ********************************************************************************

!!
  self._finalize_license_expression()
running install
/usr/lib/python3/dist-packages/setuptools/_distutils/cmd.py:90: SetuptoolsDeprecationWarning: setup.py install is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************

!!
  self.initialize_options()
/usr/lib/python3/dist-packages/setuptools/_distutils/cmd.py:90: EasyInstallDeprecationWarning: easy_install command is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` and ``easy_install``.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        See https://github.com/pypa/setuptools/issues/917 for details.
        ********************************************************************************

!!
  self.initialize_options()
error: can't create or remove files in install directory

The following error occurred while trying to add or remove files in the
installation directory:

    [Errno 13] Permission denied: '/usr/local/lib/python3.13/dist-packages/test-easy-install-134446.write-test'

The installation directory you specified (via --install-dir, --prefix, or
the distutils default setting) was:

    /usr/local/lib/python3.13/dist-packages/

Perhaps your account does not have write access to this directory?  If the
installation directory is a system-owned directory, you may need to sign in
as the administrator or "root" account.  If you do not have administrative
access to this machine, you may wish to choose a different installation
directory, preferably one that is listed in your PYTHONPATH environment
variable.

For information on other options, you may wish to consult the
documentation at:

  https://setuptools.pypa.io/en/latest/deprecated/easy_install.html

Please make the appropriate changes for your system and try again.


me dio error asi que cambie el comando por uno que me dio una AI
┌──(kali㉿kali)-[~/sstv]
└─$ python3 setup.py install --user
/usr/lib/python3/dist-packages/setuptools/dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
!!

        ********************************************************************************
        Please consider removing the following classifiers in favor of a SPDX license expression:

        License :: OSI Approved :: GNU General Public License v3 (GPLv3)

        See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
        ********************************************************************************

!!
  self._finalize_license_expression()
running install
/usr/lib/python3/dist-packages/setuptools/_distutils/cmd.py:90: SetuptoolsDeprecationWarning: setup.py install is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************

!!
  self.initialize_options()
/usr/lib/python3/dist-packages/setuptools/_distutils/cmd.py:90: EasyInstallDeprecationWarning: easy_install command is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` and ``easy_install``.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.

        See https://github.com/pypa/setuptools/issues/917 for details.
        ********************************************************************************

!!
  self.initialize_options()
running bdist_egg
running egg_info
creating sstv.egg-info
writing sstv.egg-info/PKG-INFO
writing dependency_links to sstv.egg-info/dependency_links.txt
writing entry points to sstv.egg-info/entry_points.txt
writing requirements to sstv.egg-info/requires.txt
writing top-level names to sstv.egg-info/top_level.txt
writing manifest file 'sstv.egg-info/SOURCES.txt'
reading manifest file 'sstv.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'sstv.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build/lib/sstv
copying sstv/__main__.py -> build/lib/sstv
copying sstv/decode.py -> build/lib/sstv
copying sstv/spec.py -> build/lib/sstv
copying sstv/__init__.py -> build/lib/sstv
copying sstv/command.py -> build/lib/sstv
copying sstv/common.py -> build/lib/sstv
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/__main__.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/decode.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/spec.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/__init__.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/command.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/common.py -> build/bdist.linux-x86_64/egg/sstv
byte-compiling build/bdist.linux-x86_64/egg/sstv/__main__.py to __main__.cpython-313.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/decode.py to decode.cpython-313.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/spec.py to spec.cpython-313.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/__init__.py to __init__.cpython-313.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/command.py to command.cpython-313.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/common.py to common.cpython-313.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/sstv-0.1-py3.13.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing sstv-0.1-py3.13.egg
Copying sstv-0.1-py3.13.egg to /home/kali/.local/lib/python3.13/site-packages
Adding sstv 0.1 to easy-install.pth file
Installing sstv script to /home/kali/.local/bin

Installed /home/kali/.local/lib/python3.13/site-packages/sstv-0.1-py3.13.egg
Processing dependencies for sstv==0.1
Searching for PySoundFile
Reading https://pypi.org/simple/PySoundFile/
Downloading https://files.pythonhosted.org/packages/2a/b3/0b871e5fd31b9a8e54b4ee359384e705a1ca1e2870706d2f081dc7cc1693/PySoundFile-0.9.0.post1-py2.py3-none-any.whl#sha256=db14f84f4af1910f54766cf0c0f19d52414fa80aa0e11cb338b5614946f39947
Best match: PySoundFile 0.9.0.post1
Processing PySoundFile-0.9.0.post1-py2.py3-none-any.whl
Installing PySoundFile-0.9.0.post1-py2.py3-none-any.whl to /home/kali/.local/lib/python3.13/site-packages
Adding PySoundFile 0.9.0.post1 to easy-install.pth file
detected new path './sstv-0.1-py3.13.egg'

Installed /home/kali/.local/lib/python3.13/site-packages/PySoundFile-0.9.0.post1-py3.13.egg
Searching for scipy==1.16.3
Best match: scipy 1.16.3
Adding scipy 1.16.3 to easy-install.pth file
detected new path './PySoundFile-0.9.0.post1-py3.13.egg'

Using /usr/lib/python3/dist-packages
Searching for numpy==2.3.5
Best match: numpy 2.3.5
Adding numpy 2.3.5 to easy-install.pth file
Installing f2py script to /home/kali/.local/bin
Installing numpy-config script to /home/kali/.local/bin
Installing f2py3 script to /home/kali/.local/bin
Installing f2py3.13 script to /home/kali/.local/bin

Using /usr/lib/python3/dist-packages
Searching for pillow==11.3.0
Best match: pillow 11.3.0
Adding pillow 11.3.0 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Searching for cffi==2.0.0
Best match: cffi 2.0.0
Adding cffi 2.0.0 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Searching for pycparser==2.23
Best match: pycparser 2.23
Adding pycparser 2.23 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Finished processing dependencies for sstv==0.1

─$ sstv -d ../message.wav -o flag
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [##############################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
[sstv] Error saving file, saved to result.png instead
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ open flag         
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ sstv -d ../message.wav -o flag.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [##############################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
                                                                                                
┌──(kali㉿kali)-[~/sstv]
└─$ open flag.png                     
AL ABRIR LA IMAGEN CREADA ESTA LA FLAG
picoCTF{beep_boop_im_in_space}

```
### Notas adicionales 
picoCTF{beep_boop_im_in_space}
### Referencias
https://github.com/colaclanth/sstv