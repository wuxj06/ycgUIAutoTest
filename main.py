__author__ = 'wuxj06'
from Common.config import *
import pytest
import os

pytest.main(["-m smoke","-s","-q","--alluredir",'./allureresult','--clean-alluredir'])
##os.system("allure generate %s -o %s --clean"%('    ./allureresult',report_dir))