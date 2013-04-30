#-------------------------------------------------------------------------------
# Purpose:     Installs the packages required by this application
# Author:      abuchanan
# Created:     03/2013
#-------------------------------------------------------------------------------

# Requirements definition and automatic installation.

def install_requirements():
    import os
    root_dir = os.path.split(os.path.abspath(__file__))[0].replace('\\', '/')
    reqs_file = ''.join([root_dir, "/requirements.txt"])
    if os.path.exists(reqs_file):
        try:
            import pip
        except ImportError:
            import urllib2;
            f=urllib2.urlopen('http://python-distribute.org/distribute_setup.py').read();
            exec(f)
            f=urllib2.urlopen('https://raw.github.com/pypa/pip/master/contrib/get-pip.py').read();
            exec(f)

        from pip import main as pip_install
        ''' the following code is just running pip install -r on the requirements file,
            but it has some extra code to capture stdout & stderr and then log them if
            pip has an error
        '''
        from cStringIO import StringIO
        import sys
        old_stdout, old_stderr = sys.stdout, sys.stderr
        capture = StringIO()
        sys.stdout = sys.stderr = capture
        exitval = pip_install(['install', '--requirement', reqs_file])
        sys.stdout, sys.stderr = old_stdout, old_stderr
        if( not exitval is 0 ):
            print(capture.getvalue())
        capture.close()
        return exitval

if __name__ == "__main__":
    exit(install_requirements())

