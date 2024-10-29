# Django-Oemof Standalone

This repository can be used to store/restore simulated oemof.tabular datapackages using djangos ORM.
Additionally, hooks from django-oemof to 
- change parameters before simulation,
- change ES after building from datapackage or 
- changing model before simulating 

are available.

**Note:** 
This repo is currently only a showcase on how to use django-oemof as standalone. 
This means, scenario name, paramters and database connection are hardcoded and 
any changes to this settings would affect other users as well.
So, it is recommended to not push changes to remote.

## Usage

Steps to run simulation:
1. Set up database and set correct credentials in setup.py
2. Migrate django models via `python manage.py migrate`
3. Download or create a valid oemof.tabular datapackage and store it in folder `media/oemof`
4. Adapt scenario (datapackage) name and parameters in `setup.py`
5. Run simulation via `python simulate.py`
6. Access stored simulation results for further processing via `python postprocessing.py`
