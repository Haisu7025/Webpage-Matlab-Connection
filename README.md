# Demo for Webpage-Matlab Connection


## Deployment
***Set your codes in the following organizations:***    
Webpage Server  (*WpServer*)    
* testpage.html
* assets (js)

Matlab Calculating Server (*CalServer*)
* server.py
* A.m
* Matlab Core

## Requirements
### Matlab Engine
```
    cd $matlabroot/extern/engines/python
    python setup.py install
```
### Flask
```
    pip install flask
```