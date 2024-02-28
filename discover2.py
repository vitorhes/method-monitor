given the following:

#package datautils
#__init__.py

from pyfiling.factory import Factory
Factory.start(module_profile="datautils")

#catalog.py
class Catalog():
    def __init__(self):
        pass


#package pyfiling
#factory.py
class Factory:
    def __init__(self,module_profile):
        self.module_profile = module_profile
     def import_classes(self):
          

