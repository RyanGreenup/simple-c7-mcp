### ORM Usage Examples - Interactive Database Operations

Source: https://docs.python.org/3.10/howto/descriptor

Demonstrates practical usage of the ORM system through interactive session examples. Shows database retrieval, attribute access, string formatting with retrieved data, and attribute updates. Examples illustrate how descriptor protocol enables transparent database access through normal attribute syntax.

```python
Movie('Star Wars').director
'George Lucas'
jaws = Movie('Jaws')
f'Released in {jaws.year} by {jaws.director}'
'Released in 1975 by Steven Spielberg'

Song('Country Roads').artist
'John Denver'

Movie('Star Wars').director = 'J.J. Abrams'
Movie('Star Wars').director
'J.J. Abrams'
```

--------------------------------

### Unattended Python Installation XML Configuration

Source: https://docs.python.org/3.10/using/windows

This XML file configures unattended installation options for Python. It mirrors the command-line example, specifying a 'no' for system-wide installation and launcher, 'no' for the test suite, and enabling a simple install with a custom description.

```xml
<Options>
    <Option Name="InstallAllUsers" Value="no" />
    <Option Name="Include_launcher" Value="0" />
    <Option Name="Include_test" Value="no" />
    <Option Name="SimpleInstall" Value="yes" />
    <Option Name="SimpleInstallDescription">Just for me, no test suite</Option>
</Options>

```

--------------------------------

### Demonstrate Simulated __slots__ Behavior

Source: https://docs.python.org/3.10/howto/descriptor

Interactive REPL examples demonstrating the slot simulation in action. Shows class inspection revealing Member descriptors, instance creation with _slotvalues storage, and attribute modification. Demonstrates error handling when accessing undefined attributes.

```python
>>> from pprint import pp
>>> pp(dict(vars(H)))
{'__module__': '__main__',
 '__doc__': 'Instance variables stored in slots',
 'slot_names': ['x', 'y'],
 '__init__': <function H.__init__ at 0x7fb5d302f9d0>,
 'x': <Member 'x' of 'H'>,
 'y': <Member 'y' of 'H'>}

>>> h = H(10, 20)
>>> vars(h)
{'_slotvalues': [10, 20]}
>>> h.x = 55
>>> vars(h)
{'_slotvalues': [55, 20]}

>>> h.xz
Traceback (most recent call last):
    ...
AttributeError: 'H' object has no attribute 'xz'
```

--------------------------------

### Python: Basic Range Creation Examples

Source: https://docs.python.org/3.10/library/stdtypes

Demonstrates the creation of `range` objects with different `start`, `stop`, and `step` values, and converts them to lists to show the resulting sequences. Covers default values and empty ranges.

```python
list(range(10))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(1, 11))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(range(0, 30, 5))
# Output: [0, 5, 10, 15, 20, 25]

list(range(0, 10, 3))
# Output: [0, 3, 6, 9]

list(range(0, -10, -1))
# Output: [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

list(range(0))
# Output: []

list(range(1, 0))
# Output: []
```

--------------------------------

### POP3 Complete Usage Example

Source: https://docs.python.org/3.10/library/poplib

Comprehensive example showing complete POP3 workflow from connection to message retrieval and cleanup.

```APIDOC
## POP3 Complete Usage Example

### Description
Complete working example demonstrating the entire POP3 workflow from connection establishment through message retrieval to proper cleanup.

### Methods
Demonstrates integration of multiple POP3 methods in a typical email retrieval scenario.

### Example
```python
import getpass
import poplib

# Establish connection
M = poplib.POP3('localhost')
M.set_debuglevel(1)  # Enable debugging for troubleshooting

# Authenticate user
greeting = M.getwelcome()  # Get server greeting
M.user(getpass.getuser())  # Send username
M.pass_(getpass.getpass())  # Send password

# Get mailbox status
message_count, mailbox_size = M.stat()
print(f"Messages: {message_count}, Size: {mailbox_size} bytes")

# List all messages
response, messages, octets = M.list()
print(f"Found {len(messages)} messages")

# Retrieve and print all messages
for i in range(message_count):
    print(f"\n--- Message {i+1} ---")
    for line in M.retr(i+1)[1]:
        print(line)

# Alternative: Get just headers (faster)
for i in range(message_count):
    print(f"\n--- Message {i+1} Headers ---")
    for line in M.top(i+1, 10)[1]:  # First 10 lines
        print(line)

# Clean up
M.quit()  # Commit changes and close connection
```

### Response
Shows complete email retrieval workflow with proper error handling and resource cleanup.

### Note
This example demonstrates the recommended pattern for POP3 usage: authenticate, query mailbox, retrieve messages, then properly quit to commit changes.
```

--------------------------------

### Python - Static Method Example

Source: https://docs.python.org/3.10/howto/descriptor

Demonstrates the usage of a static method `f` within a class `E`. Calls to the method from both the class and an instance result in the same output.

```python
class E:
    @staticmethod
    def f(x):
        return x * 10
```

--------------------------------

### Python: mailcap usage example

Source: https://docs.python.org/3.10/library/mailcap

This example demonstrates the usage of the mailcap module by importing it, getting the caps and using the findmatch function with video/mpeg MIME type.

```python
>>> import mailcap
>>> d = mailcap.getcaps()
>>> mailcap.findmatch(d, 'video/mpeg', filename='tmp1223')
('xmpeg tmp1223', {'view': 'xmpeg %s'})
```

--------------------------------

### Python - D Class Example

Source: https://docs.python.org/3.10/howto/descriptor

Shows how function descriptors work in practice by defining a simple class `D` and its method `f`. Accessing the method from the class or an instance demonstrates the behavior of the descriptor.

```python
class D:
    def f(self, x):
         return x
```

--------------------------------

### Create Basic HTTP Client with asyncore

Source: https://docs.python.org/3.10/library/asyncore

This code snippet demonstrates a basic HTTP client using asyncore. It initializes a socket, connects to a specified host and path, sends an HTTP GET request, and prints the received response. This example illustrates the fundamental principles of asynchronous socket communication with asyncore.

```python
import asyncore

class HTTPClient(asyncore.dispatcher):

    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.connect( (host, 80) )
        self.buffer = bytes('GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' % \
                            (path, host), 'ascii')

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print(self.recv(8192))

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]


client = HTTPClient('www.python.org', '/')
asyncore.loop()
```

--------------------------------

### install_opener

Source: https://docs.python.org/3.10/library/urllib

Installs an OpenerDirector instance as the default global opener. This allows urlopen to use the installed opener.

```APIDOC
## POST install_opener

### Description
Installs an `OpenerDirector` instance as the default global opener. This is necessary if you want `urlopen` to use that specific opener.

### Method
POST

### Endpoint
`/`

### Parameters
#### Request Body
- **opener** (OpenerDirector) - Required - The `OpenerDirector` instance to install as the default global opener.

### Request Example
```json
{
  "opener": "<OpenerDirector instance>"
}
```

### Response
#### Success Response (200)
- **message** (string) - Indicates that the opener was successfully installed.

#### Response Example
```json
{
  "message": "Opener installed successfully."
}
```
```

--------------------------------

### Personal Python Installation Command

Source: https://docs.python.org/3.10/using/windows

This command installs a personal copy of Python without the test suite, while also disabling the Python launcher and file associations. It presents a simplified initial installation page with a custom description.

```bash
python-3.9.0.exe InstallAllUsers=0 Include_launcher=0 Include_test=0
    SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite."

```

--------------------------------

### Define test classes with setUp and tearDown methods

Source: https://docs.python.org/3.10/library/test

Shows how to create test classes using unittest.TestCase with setUp and tearDown methods for test preparation and cleanup. This pattern is recognized by test runners and supports multiple test methods.

```Python
import unittest
from test import support

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        ... code to execute in preparation for tests ...

    def tearDown(self):
        ... code to execute to clean up after tests ...

    def test_feature_one(self):
        # Test feature one.
        ... testing code ...

    def test_feature_two(self):
        # Test feature two.
        ... testing code ...

    ... more test methods ...

class MyTestCase2(unittest.TestCase):
    ... same structure as MyTestCase1 ...

... more test classes ...

if __name__ == '__main__':
    unittest.main()
```

--------------------------------

### Python Logging Example with Filter

Source: https://docs.python.org/3.10/howto/logging-cookbook

A complete Python example demonstrating the logging configuration and filter usage, including the main script and its execution.

```python
import json
import logging
import logging.config

CONFIG = '''
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(levelname)-8s - %(message)s"
        }
    },
    "filters": {
        "warnings_and_below": {
            "()" : "__main__.filter_maker",
            "level": "WARNING"
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
            "filters": ["warnings_and_below"]
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "app.log",
            "mode": "w"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "stderr",
            "stdout",
            "file"
        ]
    }
}
'''

def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter

logging.config.dictConfig(json.loads(CONFIG))
logging.debug('A DEBUG message')
logging.info('An INFO message')
logging.warning('A WARNING message')
logging.error('An ERROR message')
logging.critical('A CRITICAL message')
```

--------------------------------

### Setup Python Extension Module (Python)

Source: https://docs.python.org/3.10/extending/newtypes_tutorial

Configures the setup script for building Python extension modules. It specifies the module name, version, and lists the C source files to be compiled into shared libraries (e.g., `custom.c` and `custom2.c`).

```python
from distutils.core import setup, Extension
setup(name="custom", version="1.0",
      ext_modules=[
         Extension("custom", ["custom.c"]),
         Extension("custom2", ["custom2.c"]),
         ])
```

--------------------------------

### Simple hashing with BLAKE2b in Python

Source: https://docs.python.org/3.10/library/hashlib

Example of basic hashing workflow: creating a hash object, updating it with data, and getting the hex digest. Shows both iterative updating and single-call methods.

```Python
from hashlib import blake2b
h = blake2b()
h.update(b'Hello world')
h.hexdigest()
```

```Python
from hashlib import blake2b
blake2b(b'Hello world').hexdigest()
```

```Python
from hashlib import blake2b
items = [b'Hello', b' ', b'world']
h = blake2b()
for item in items:
    h.update(item)
h.hexdigest()
```

--------------------------------

### List installed Python versions

Source: https://docs.python.org/3.10/using/windows

Displays all currently installed versions of Python on the system using the launcher.

```bash
py --list
```

--------------------------------

### POP3 Client Example in Python

Source: https://docs.python.org/3.10/library/poplib

This Python code snippet demonstrates a basic example of using the poplib module to connect to a local POP3 server, authenticate, retrieve the number of messages, and then fetch and print each message. It requires the getpass module for secure password input.

```python
import getpass, poplib

M = poplib.POP3('localhost')
M.user(getpass.getuser())
M.pass_(getpass.getpass())
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)

```

--------------------------------

### DocTestSuite and DocFileSuite Functions

Source: https://docs.python.org/3.10/library/doctest

These functions create a unittest.TestSuite from doctests in a module or docstrings and text files, with options for setup, teardown, and more.

```APIDOC
## Function DocTestSuite

### Description
This function creates a unittest.TestSuite from doctests in a module. Optional argument _test_finder_ is the DocTestFinder object (or a drop-in replacement) that is used to extract doctests from the module. Optional arguments _setUp_, _tearDown_, and _optionflags_ are the same as for function DocFileSuite() below. This function uses the same search technique as testmod(). Changed in version 3.5: DocTestSuite() returns an empty unittest.TestSuite if _module_ contains no docstrings instead of raising ValueError. Under the covers, DocTestSuite() creates a unittest.TestSuite out of doctest.DocTestCase instances.

### Method
Python Function

### Endpoint
doctest.DocTestSuite(module=None, globs=None, extraglobs=None, test_finder=None, setUp=None, tearDown=None, optionflags=0)

### Parameters
#### Arguments
- **module** (module) - Optional - Module to extract doctests from. Default is None, meaning the caller's module.
- **globs** (dict) - Optional - Global namespace to use for executing examples. Default is module.__dict__.
- **extraglobs** (dict) - Optional - Additional global variables to merge into globs.
- **test_finder** (DocTestFinder) - Optional - Finder object to use. Default creates a new one.
- **setUp** (callable) - Optional - Called before each doctest.
- **tearDown** (callable) - Optional - Called after each doctest.
- **optionflags** (int) - Optional - Option flags to control behavior.

### Request Example
import doctest
suite = doctest.DocTestSuite(module=my_module)

### Response
#### Success Response
Returns a unittest.TestSuite containing DocTestCase instances.

#### Response Example
unittest.TestSuite object with doctest cases.

## Function DocFileSuite

### Description
Creates a unittest.TestSuite from doctests in text files. Optional arguments _setUp_, _tearDown_, and _optionflags_ are the same as for DocTestSuite() above. Under the covers, DocFileSuite() creates a unittest.TestSuite out of doctest.DocFileCase instances, and DocFileCase is a subclass of DocTestCase.

### Method
Python Function

### Endpoint
doctest.DocFileSuite(*paths, module_relative=True, package=None, globs=None, extraglobs=None, setUp=None, tearDown=None, optionflags=0, encoding=None)

### Parameters
#### Arguments
- **paths** (str) - Required - Paths to text files containing doctests.
- **module_relative** (bool) - Optional - If True, paths are relative to the calling module.
- **package** (module) - Optional - Package for relative paths.
- **globs** (dict) - Optional - Global namespace for execution.
- **extraglobs** (dict) - Optional - Additional globals.
- **setUp** (callable) - Optional - Set up function.
- **tearDown** (callable) - Optional - Tear down function.
- **optionflags** (int) - Optional - Option flags.
- **encoding** (str) - Optional - File encoding.

### Request Example
import doctest
suite = doctest.DocFileSuite('test.txt')

### Response
#### Success Response
Returns a unittest.TestSuite containing DocFileCase instances.

#### Response Example
unittest.TestSuite object with doctest cases from files.
```

--------------------------------

### Install portable Python using nuget.exe command line

Source: https://docs.python.org/3.10/using/windows

Shows how to download and run nuget.exe to install the Python package (both 64‑bit and 32‑bit) into a local directory without version numbers. After installation, the snippet demonstrates checking the installed Python version using the provided executable path. Requires nuget.exe available in the command prompt; no additional libraries are needed. Suitable for CI/build systems lacking a system‑wide Python install.

```shell
nuget.exe install python -ExcludeVersion -OutputDirectory .\nnuget.exe install pythonx86 -ExcludeVersion -OutputDirectory .\n\n# Verify installed Python version\n.\\python\\tools\\python.exe -V\n.\\pythonx86\\tools\\python.exe -V
```

--------------------------------

### Extending EnvBuilder to Install Setuptools and Pip

Source: https://docs.python.org/3.10/library/venv

A Python class that extends venv.EnvBuilder to automatically install setuptools and pip into created virtual environments. The implementation includes progress monitoring and handles downloading and executing installation scripts. Dependencies include the venv module and urllib for downloading installation scripts.

```python
import os
import os.path
from subprocess import Popen, PIPE
import sys
from threading import Thread
from urllib.parse import urlparse
from urllib.request import urlretrieve
import venv

class ExtendedEnvBuilder(venv.EnvBuilder):
    """
    This builder installs setuptools and pip so that you can pip or
    easy_install other packages into the created virtual environment.

    :param nodist: If true, setuptools and pip are not installed into the
                   created virtual environment.
    :param nopip: If true, pip is not installed into the created
                  virtual environment.
    :param progress: If setuptools or pip are installed, the progress of the
                     installation can be monitored by passing a progress
                     callable. If specified, it is called with two
                     arguments: a string indicating some progress, and a
                     context indicating where the string is coming from.
                     The context argument can have one of three values:
                     'main', indicating that it is called from virtualize()
                     itself, and 'stdout' and 'stderr', which are obtained
                     by reading lines from the output streams of a subprocess
                     which is used to install the app.

                     If a callable is not specified, default progress
                     information is output to sys.stderr.
    """

    def __init__(self, *args, **kwargs):
        self.nodist = kwargs.pop('nodist', False)
        self.nopip = kwargs.pop('nopip', False)
        self.progress = kwargs.pop('progress', None)
        self.verbose = kwargs.pop('verbose', False)
        super().__init__(*args, **kwargs)

    def post_setup(self, context):
        """
        Set up any packages which need to be pre-installed into the
        virtual environment being created.

        :param context: The information for the virtual environment
                        creation request being processed.
        """
        os.environ['VIRTUAL_ENV'] = context.env_dir
        if not self.nodist:
            self.install_setuptools(context)
        # Can't install pip without setuptools
        if not self.nopip and not self.nodist:
            self.install_pip(context)

    def reader(self, stream, context):
        """
        Read lines from a subprocess' output stream and either pass to a progress
        callable (if specified) or write progress information to sys.stderr.
        """
        progress = self.progress
        while True:
            s = stream.readline()
            if not s:
                break
            if progress is not None:
                progress(s, context)
            else:
                if not self.verbose:
                    sys.stderr.write('.')
                else:
                    sys.stderr.write(s.decode('utf-8'))
                sys.stderr.flush()
        stream.close()

    def install_script(self, context, name, url):
        _, _, path, _, _, _ = urlparse(url)
        fn = os.path.split(path)[-1]
        binpath = context.bin_path
        distpath = os.path.join(binpath, fn)
        # Download script into the virtual environment's binaries folder
        urlretrieve(url, distpath)
        progress = self.progress
        if self.verbose:
            term = '\n'
        else:
            term = ''
        if progress is not None:
            progress('Installing %s ...%s' % (name, term), 'main')
        else:
            sys.stderr.write('Installing %s ...%s' % (name, term))
            sys.stderr.flush()
        # Install in the virtual environment
        args = [context.env_exe, fn]
        p = Popen(args, stdout=PIPE, stderr=PIPE, cwd=binpath)
        t1 = Thread(target=self.reader, args=(p.stdout, 'stdout'))
        t1.start()
        t2 = Thread(target=self.reader, args=(p.stderr, 'stderr'))
        t2.start()
        p.wait()
        t1.join()
        t2.join()
        if progress is not None:
            progress('done.', 'main')
        else:
            sys.stderr.write('done.\n')
        # Clean up - no longer needed
        os.unlink(distpath)

    def install_setuptools(self, context):
        """
        Install setuptools in the virtual environment.

        :param context: The information for the virtual environment
                        creation request being processed.
        """
        url = 'https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py'
        self.install_script(context, 'setuptools', url)
        # clear up the setuptools archive which gets downloaded
        pred = lambda o: o.startswith('setuptools-') and o.endswith('.tar.gz')
        files = filter(pred, os.listdir(context.bin_path))
        for f in files:

```

--------------------------------

### init_database

Source: https://docs.python.org/3.10/library/msilib

Creates and initializes a new MSI database with product information.

```APIDOC
## `msilib.init_database`

### Description
Create and initialize a new MSI database.

### Method
FUNCTION

### Parameters
#### Positional Parameters
- **name** (string) - Required - Database name.
- **schema** (module) - Required - Schema module with tables and validation records.
- **ProductName** (string) - Required - Product name property.
- **ProductCode** (string) - Required - Product code property.
- **ProductVersion** (string) - Required - Product version property.
- **Manufacturer** (string) - Required - Manufacturer property.

### Returns
- **Database object** - New initialized database.

### Notes
- Typically uses `msilib.schema` for the schema parameter.
- Database contains only schema and validation records initially.
```

--------------------------------

### Python importlib.metadata - Version Information

Source: https://docs.python.org/3.10/whatsnew/3

Demonstrates how to use the `importlib.metadata` module to retrieve version information for installed Python packages. This example shows how to get version and dependencies.

```python
>>> from importlib.metadata import version, requires, files
>>> version('requests')
'2.22.0'
>>> list(requires('requests'))
['chardet (<3.1.0,>=3.0.2)']
>>> list(files('requests'))[:5]
[PackagePath('requests-2.22.0.dist-info/INSTALLER'),
 PackagePath('requests-2.22.0.dist-info/LICENSE'),
 PackagePath('requests-2.22.0.dist-info/METADATA'),
 PackagePath('requests-2.22.0.dist-info/RECORD'),
 PackagePath('requests-2.22.0.dist-info/WHEEL')]
```

--------------------------------

### Sched Event Scheduler Example using Python

Source: https://docs.python.org/3.10/library/sched

This example demonstrates how to use the sched.scheduler class in Python to schedule events. It shows how to create a scheduler instance, define event functions, and schedule them using enter() and enterabs() methods. The example also illustrates the priority-based execution of events and their relative ordering.

```python
import sched, time
s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print("From print_time", time.time(), a)

def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    # despite having higher priority, 'keyword' runs after 'positional' as enter() is relative
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.enterabs(1_650_000_000, 10, print_time, argument=("first enterabs",))
    s.enterabs(1_650_000_000, 5, print_time, argument=("second enterabs",))
    s.run()
    print(time.time())

print_some_times()
```

--------------------------------

### WSGI Application Environment Setup

Source: https://docs.python.org/3.10/library/wsgiref

A simple WSGI application that demonstrates how to set up a testing environment and return environment variables as response content.

```APIDOC
## WSGI Application Example

### Description
A simple WSGI application that uses setup_testing_defaults to configure the environment and returns all environment variables as plain text.

### Method
Application initialization

### Endpoint
N/A (Application example)

### Parameters
#### Function Parameters
- **environ** (dict) - Required - WSGI environment dictionary
- **start_response** (function) - Required - WSGI start_response function

### Response
#### Success Response (200)
- **Content-type** (header) - text/plain; charset=utf-8

#### Response Example
```
SERVER_NAME: localhost
SERVER_PORT: 8000
REQUEST_METHOD: GET
...
```
```

--------------------------------

### Get Multiprocessing Context using get_context

Source: https://docs.python.org/3.10/library/multiprocessing

Illustrates obtaining a multiprocessing context object to manage process creation, allowing for multiple start methods within a single program. This example uses the 'spawn' context to create a Process and Queue. Objects created with one context may not be compatible with others.

```python
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

--------------------------------

### INI File Structure Example for ConfigParser

Source: https://docs.python.org/3.10/library/configparser

Provides an example of a well-structured INI configuration file, showcasing different sections and value types. It includes examples of simple values, all string values, multiline values, keys without values, empty string values, comments, and indented sections.

```ini
[Simple Values]
key=value
spaces in keys=allowed
spaces in values=allowed as well
spaces around the delimiter = obviously
you can also use : to delimit keys from values

[All Values Are Strings]
values like this: 1000000
or this: 3.14159265359
are they treated as numbers? : no
integers, floats and booleans are held as: strings
can use the API to get converted values directly: true

[Multiline Values]
chorus: I'm a lumberjack, and I'm okay
    I sleep all night and I work all day

[No Values]
key_without_value
empty string value here =

[You can use comments]
# like this
; or this

# By default only in an empty line.
# Inline comments can be harmful because they prevent users
# from using the delimiting characters as parts of values.
# That being said, this can be customized.

    [Sections Can Be Indented]
        can_values_be_as_well = True
        does_that_mean_anything_special = False
        purpose = formatting for readability
        multiline_values = are
            handled just fine as
            long as they are indented
            deeper than the first line
            of a value
        # Did I mention we can indent comments, too?
```

--------------------------------

### ftplib FTP_TLS Session Example

Source: https://docs.python.org/3.10/library/ftplib

Illustrates establishing a secure FTP connection using the FTP_TLS class. This example connects to a server, logs in anonymously, and then secures the data connection using prot_p() before listing directory contents.

```python
from ftplib import FTP_TLS

ftps = FTP_TLS('ftp.pureftpd.org')
ftps.login()
print('230 Anonymous user logged in')
ftps.prot_p()
print('200 Data protection level set to "private"')
ftps.nlst()

```

--------------------------------

### Getting Start and End Indices of Regex Matches in Python

Source: https://docs.python.org/3.10/library/re

Explains the `start()` and `end()` methods for retrieving the start and end indices of a substring matched by a specific group (or the entire match if no group is specified). This is useful for locating matched patterns within the original string.

```python
import re

m = re.match(r"(\\w+) (\\w+)", "Isaac Newton, physicist")

start_index = m.start(1)
end_index = m.end(1)

print(f"Substring matched by group 1: {m.string[start_index:end_index]}")

```

--------------------------------

### Configure Window Setup in Python

Source: https://docs.python.org/3.10/library/turtle

Sets window size and position with flexible parameter types. Integer values specify pixels while floats specify screen fractions. startx and starty control positioning relative to screen edges, with None centering the window. Default values can be configured via turtle.cfg file.

```python
screen.setup(width=200, height=200, startx=0, starty=0)
# sets window to 200x200 pixels, in upper left of screen
screen.setup(width=.75, height=0.5, startx=None, starty=None)
# sets window to 75% of screen by 50% of screen and centers
```

--------------------------------

### Python Locale Settings Example

Source: https://docs.python.org/3.10/library/locale

Demonstrates setting the locale using `locale.setlocale()` and retrieving the current locale. The example includes setting the locale to different values, including the user's preferred locale and the default 'C' locale.

```Python
import locale

loc = locale.getlocale()  # get current locale
# use German locale; name might vary with platform
locale.setlocale(locale.LC_ALL, 'de_DE')
locale.strcoll('f\xe4n', 'foo')  # compare a string containing an umlaut
locale.setlocale(locale.LC_ALL, '')   # use user’s preferred locale
locale.setlocale(locale.LC_ALL, 'C')  # use default (C) locale
locale.setlocale(locale.LC_ALL, loc)  # restore saved locale
```

--------------------------------

### Get root directory with PurePath in Python

Source: https://docs.python.org/3.10/library/pathlib

Shows how to get the root directory from a path using PureWindowsPath and PurePosixPath. Includes examples with UNC shares.

```python
>>> PureWindowsPath('c:/Program Files/').root
'\\'
>>> PureWindowsPath('c:Program Files/').root
''
>>> PurePosixPath('/etc').root
'/'
```

```python
>>> PureWindowsPath('//host/share').root
'\\'
```

```python
>>> PurePosixPath('//etc').root
'//'
>>> PurePosixPath('///etc').root
'/'
>>> PurePosixPath('////etc').root
'/'
```

--------------------------------

### Python Dictionary Initialization Examples

Source: https://docs.python.org/3.10/library/stdtypes

Illustrates multiple ways to initialize dictionaries to an equivalent state, showcasing the flexibility of Python's dict constructor and literal syntax.

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f)
```

--------------------------------

### XML-RPC Protocol Error Example

Source: https://docs.python.org/3.10/library/xmlrpc

Illustrates how to intentionally cause and potentially handle an xmlrpc.client.ProtocolError. This example focuses on the client-side setup for making a request that is expected to fail due to an invalid URI, which would trigger a protocol-level error.

```python
import xmlrpc.client

# Example of creating a proxy with an invalid URI to potentially cause a ProtocolError
# Note: The actual error handling (try-except block) would typically follow this.
proxy = xmlrpc.client.ServerProxy("http://invalid-url:8000/")

```

--------------------------------

### Multi-Process Logging with QueueHandler and Listener Process in Python

Source: https://docs.python.org/3.10/howto/logging-cookbook

This Python example illustrates a common approach for logging to a single file from multiple processes. It involves a listener process that receives log records via a queue from worker processes. Dependencies include `logging`, `logging.handlers`, and `multiprocessing`. The listener configuration is separate from the worker configuration, allowing for distinct logging setups.

```python
# You'll need these imports in your own code
import logging
import logging.handlers
import multiprocessing

# Next two import lines for this demo only
from random import choice, random
import time

#
# Because you'll want to define the logging configurations for listener and workers, the
# listener and worker process functions take a configurer parameter which is a callable
# for configuring logging for that process. These functions are also passed the queue,
# which they use for communication.
#
# In practice, you can configure the listener however you want, but note that in this
# simple example, the listener does not apply level or filter logic to received records.
# In practice, you would probably want to do this logic in the worker processes, to avoid
# sending events which would be filtered out between processes.
#
# The size of the rotated files is made small so you can see the results easily.
def listener_configurer():
    root = logging.getLogger()
    h = logging.handlers.RotatingFileHandler('mptest.log', 'a', 300, 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)

# This is the listener process top-level loop: wait for logging events

```

--------------------------------

### Main function to run PyQt Application

Source: https://docs.python.org/3.10/howto/logging-cookbook

Initializes the PyQt application, sets the logging level, creates the main window instance, shows the window, and starts the application's event loop. Ensures proper thread naming for the main thread.

```python
def main():
    QtCore.QThread.currentThread().setObjectName('MainThread')
    logging.getLogger().setLevel(logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    example = Window(app)
    example.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

```

--------------------------------

### Usage Examples for BraceMessage and DollarMessage

Source: https://docs.python.org/3.10/howto/logging-cookbook

Demonstrates practical usage of custom message objects with str.format() and string.Template formatting. Shows how to alias class names for convenience and includes examples with positional arguments and object attributes.

```python
>>> __ = BraceMessage
>>> print(__('Message with {0} {1}', 2, 'placeholders'))
Message with 2 placeholders
>>> class Point: pass
...
>>> p = Point()
>>> p.x = 0.5
>>> p.y = 0.5
>>> print(__('Message with coordinates: ({point.x:.2f}, {point.y:.2f})', point=p))
Message with coordinates: (0.50, 0.50)

>>>
>>> __ = DollarMessage
>>> print(__('Message with $num $what', num=2, what='placeholders'))
Message with 2 placeholders
>>>
```

--------------------------------

### GET /enumerate

Source: https://docs.python.org/3.10/library/functions

Returns an enumerate object yielding index, item pairs for the provided iterable, starting at index 0 by default.

```APIDOC
## GET /enumerate

### Description
Returns an enumerate object yielding index, item pairs for the provided iterable; start defaults to 0.

### Method
GET

### Endpoint
/enumerate

### Parameters
#### Query Parameters
- **iterable** (any) - Required - A sequence, iterator, or object supporting iteration.
- **start** (int) - Optional - Starting index (defaults to 0).

### Request Example
{
  "iterable": ["Spring", "Summer", "Fall", "Winter"],
  "start": 0
}

### Response
#### Success Response (200)
- **pairs** (list of [int, any]) - List of (index, item) pairs.

#### Response Example
{
  "pairs": [
    [0, "Spring"],
    [1, "Summer"],
    [2, "Fall"],
    [3, "Winter"]
}

### Notes
Equivalent to:

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
```

--------------------------------

### Basic ftplib FTP Session Example

Source: https://docs.python.org/3.10/library/ftplib

Demonstrates a typical FTP session using the ftplib.FTP class, including connecting, logging in, changing directories, listing contents, and downloading a file. It utilizes the 'with' statement for resource management.

```python
from ftplib import FTP

ftp = FTP('ftp.us.debian.org')  # connect to host, default port
ftp.login()                     # user anonymous, passwd anonymous@
print('230 Login successful.')
ftp.cwd('debian')               # change into "debian" directory
print('250 Directory successfully changed.')
ftp.retrlines('LIST')           # list directory contents
print('-rw-rw-r--    1 1176     1176         1063 Jun 15 10:18 README
...\ndrwxr-sr-x    5 1176     1176         4096 Dec 19  2000 pool
drwxr-sr-x    4 1176     1176         4096 Nov 17  2008 project
drwxr-xr-x    3 1176     1176         4096 Oct 10  2012 tools')
print('226 Directory send OK.')

with open('README', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write)
print('226 Transfer complete.')
ftp.quit()
print('221 Goodbye.')
```

--------------------------------

### Check Python launcher availability

Source: https://docs.python.org/3.10/using/windows

Executes the Python launcher to check if it is available on the system. The launcher starts the latest installed version of Python.

```bash
py
```

--------------------------------

### WSGI Hello World Application

Source: https://docs.python.org/3.10/library/wsgiref

A basic WSGI application that responds with 'Hello World'. It demonstrates the fundamental structure of a WSGI application, including the environ and start_response arguments, and returning an iterable response. This example uses `wsgiref.simple_server` to run the application.

```python
from wsgiref.simple_server import make_server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object.
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"Hello World"]

with make_server('', 8000, hello_world_app) as httpd:
    print("Serving on port 8000...")

    # Serve until process is killed
    httpd.serve_forever()

```

--------------------------------

### Example of ioctl for getting process group (Python)

Source: https://docs.python.org/3.10/library/fcntl

This example demonstrates using fcntl.ioctl with termios.TIOCGPGRP to retrieve the process group ID associated with a file descriptor (standard input, file descriptor 0). It shows how to unpack the result and also how to use a mutable buffer to set the process group.

```python
>>> import array, fcntl, struct, termios, os
>>> os.getpgrp()
13341
>>> struct.unpack('h', fcntl.ioctl(0, termios.TIOCGPGRP, "  "))[0]
13341
>>> buf = array.array('h', [0])
>>> fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
0
>>> buf
array('h', [13341])
```

--------------------------------

### report_start

Source: https://docs.python.org/3.10/library/doctest

Reports that the test runner is about to process a given example. This method is intended for subclass customization and should not be called directly.

```APIDOC
## report_start

### Description
Report that the test runner is about to process the given example. This method is provided to allow subclasses of `DocTestRunner` to customize their output; it should not be called directly.

### Method
`report_start(out, test, example)`

#### Parameters
- **out** (function) - Required - The output function passed to `DocTestRunner.run()`.
- **test** (DocTest) - Required - The test containing the example.
- **example** (Example) - Required - The example about to be processed.
```

--------------------------------

### Get matching blocks in Python

Source: https://docs.python.org/3.10/library/difflib

Returns a list of triples describing non-overlapping matching subsequences between the two sequences. Each triple indicates matching segments with their start indices and size.

```python
get_matching_blocks()
```

```python
s = SequenceMatcher(None, "abxcd", "abcd")
s.get_matching_blocks()
```

--------------------------------

### Python Optparse: Help Output Example

Source: https://docs.python.org/3.10/library/optparse

This shows the formatted help and usage text generated by optparse when the -h or --help flag is encountered or when parser.print_help() is called. It includes the program's usage string and detailed descriptions for each defined option.

```text
Usage: <yourscript> [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -v, --verbose         make lots of noise [default]
  -q, --quiet           be vewwy quiet (I'm hunting wabbits)
  -f FILE, --filename=FILE
                        write output to FILE
  -m MODE, --mode=MODE  interaction mode: novice, intermediate,
                        or expert [default: intermediate]

```

--------------------------------

### Demonstrate quick_ratio and real_quick_ratio methods of SequenceMatcher in Python

Source: https://docs.python.org/3.10/library/difflib

Illustrates the use of quick_ratio() and real_quick_ratio() as fast upper bounds for the full ratio calculation. The example creates a matcher for two strings and prints all three ratio values. Useful for performance‑critical similarity checks.

```python
s = SequenceMatcher(None, "abcd", "bcde")
 print(s.ratio())
 print(s.quick_ratio())
 print(s.real_quick_ratio())
```

--------------------------------

### Install pip in Virtual Environment (Python)

Source: https://docs.python.org/3.10/library/venv

Installs pip into a virtual environment using a provided URL. This function requires a context object containing virtual environment information and calls a helper function 'install_script'.

```python
def install_pip(self, context):
        """
        Install pip in the virtual environment.

        :param context: The information for the virtual environment
                        creation request being processed.
        """
        url = 'https://bootstrap.pypa.io/get-pip.py'
        self.install_script(context, 'pip', url)
```

--------------------------------

### Start and Run Manager Server

Source: https://docs.python.org/3.10/library/multiprocessing

Demonstrates how to initialize a BaseManager, retrieve its server object, and start the server to listen for connections. This is crucial for setting up shared object management.

```python
from multiprocessing.managers import BaseManager

manager = BaseManager(address=('', 50000), authkey=b'abc')
server = manager.get_server()
server.serve_forever()
```

--------------------------------

### Providing Setup Imports for timeit

Source: https://docs.python.org/3.10/library/timeit

Demonstrates how to make functions or modules defined in the main script available to the timeit module's execution environment using the 'setup' parameter with an import statement.

```python
def test():
    """Stupid test function"""
    L = [i for i in range(100)]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
```

--------------------------------

### Python Generator Execution Example with send() and next()

Source: https://docs.python.org/3.10/howto/functional

An example demonstrating the usage of a Python generator `counter`. It shows how to initialize the generator, retrieve values using `next()`, send values to resume execution using `send()`, and handle `StopIteration` when the generator is exhausted.

```python
it = counter(10)  
next(it)  
next(it)  
it.send(8)  
next(it)  
next(it)  

```

--------------------------------

### Get drive letter with PureWindowsPath in Python

Source: https://docs.python.org/3.10/library/pathlib

Demonstrates how to retrieve the drive letter from a path using PureWindowsPath. Shows examples with and without a drive letter.

```python
>>> PureWindowsPath('c:/Program Files/').drive
'c:'
>>> PureWindowsPath('/Program Files/').drive
''
>>> PurePosixPath('/etc').drive
''
```

```python
>>> PureWindowsPath('//host/share/foo.txt').drive
'\\\\host\\share'
```

--------------------------------

### Python glob.glob() Matching Hidden Files

Source: https://docs.python.org/3.10/library/glob

Examples showing how glob.glob() handles matching files starting with dot (.) in patterns, unlike some other matching functions. Requires Python's glob module. Inputs are pathname strings with patterns; outputs are lists of matching hidden or regular files. Note that patterns must start with dot to match hidden files.

```python
>>> import glob
>>> glob.glob('*.gif')
['card.gif']
>>> glob.glob('.c*')
['.card.gif']

```

--------------------------------

### Python 'from ... import' Examples

Source: https://docs.python.org/3.10/reference/simple_stmts

Demonstrates the usage of the `from ... import` statement in Python, showing how to import specific attributes or submodules from a module and bind them locally.

```python
from foo.bar import baz    # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as baz
from foo import attr       # foo imported and foo.attr bound as attr
```