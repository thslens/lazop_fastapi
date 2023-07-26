# lazop_fastapi

download sdk from open.lazada.com
run cmd for setup.py file in sdk : python setup.py install --user

Python will be able to find the lazop and lazop_api packages that you installed. The .pydistutils.cfg file is a configuration file that tells Python where to look for packages. The line site-packages = C:\Users\Admin\AppData\Roaming\Python\Python311\site-packages tells Python to look for packages in the site-packages directory
run cmd to create file cd ... site-packages : echo > .pydistutils.cfg
