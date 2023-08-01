1. Install Python 3.11 or later.
2. Create a new file with project name
3. Create a virtual environment for your project, by navigating the directory (2) and running the following command in a command prompt: python -m venv fastapi-env
4. Activate the virtual environment.by cmd run :
cd fastapi-env
.\Scripts\activate
5. Install the Lazop Python SDK.by cmd run in the virtual environment :
pip install lazop-sdk
6. create a file requirements.txt and run pip install -r requirements.txt
7. main.py , enviroment terminal run: uvicorn main:app --reload : reload auto when we change the file
8. uvicorn test_token:app --reload
9. uvicorn create_token:app --reload
# lazop_fastapi

download sdk https://pypi.org/project/lazop-sdk/ or from open.lazada.com

# import lazop problems :
https://www.youtube.com/watch?v=DKR0VYSOqLc&list=WL&index=1 ( copy lazop file in python 3.11 C:\Program Files\Python311\Lib\site-packages )
sometime needs uninstall and install python newest version

need set the path in enviroment


