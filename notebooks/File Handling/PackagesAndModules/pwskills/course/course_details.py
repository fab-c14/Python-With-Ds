# from payment import payment_details  # wil not work not module found, now i need to collapse path 
import os,sys # os nd  sys module

from os.path import dirname,join,abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..'))) # index and what to insert
from payment import payment_details
def course():
    print("this is my course details")

# how de we use course details in here, package is a folder which contains modules, module is a python file used by another python file

payment_details.payment()