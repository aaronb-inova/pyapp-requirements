
from install_requirements import install_requirements
''' When I tried to just import install_requirements directly it caused pip to hang, but
    doing it as a function seems to work. '''
exit_code = install_requirements()
if( not exit_code is 0 ): exit(exit_code)

