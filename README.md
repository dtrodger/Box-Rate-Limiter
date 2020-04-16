## Box Python Client Rate Limiter
### Runtime Requirements  
[Python 3.6+](https://www.python.org/downloads/)  
[PIP package manager](https://pip.pypa.io/en/stable/installing/)  
[virtualenv](https://virtualenv.pypa.io/en/latest/)  
### Set up and Run  
1. From the project root folder, create a Python 3.6+ virtual environment  
`$ virtualenv --python=python3 env`  
2. Activate the virtual environment  
`$ source env/bin/activate`  
3. Install the project dependencies  
`$ pip install -r requirements.txt`  
4. Copy the configuration from from  
`sample-box-auth.json`  
to  
`box-auth.json`  
5. Add Box Platform JWT keys to the box-auth.json file  
6. Run the app  
`$ python main.py`  