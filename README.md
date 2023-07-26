# lazop_fastapi

download sdk from open.lazada.com
run cmd for setup.py file in sdk : python setup.py install --user

download https://pypi.org/search/?q=lazop 

open Notepad and create a new file. Save the file as .bashrc or .profile, depending on which file you want to edit
export PYTHONPATH=$PYTHONPATH:C:\Users\Admin\AppData\Roaming\Python\Python311\site-packages
This line will set the PYTHONPATH environment variable to include the directory where the lazop-sdk package is installed

Python will be able to find the lazop and lazop_api packages that you installed. The .pydistutils.cfg file is a configuration file that tells Python where to look for packages. The line site-packages = C:\Users\Admin\AppData\Roaming\Python\Python311\site-packages tells Python to look for packages in the site-packages directory
run cmd to create file cd ... site-packages : echo > .pydistutils.cfg

