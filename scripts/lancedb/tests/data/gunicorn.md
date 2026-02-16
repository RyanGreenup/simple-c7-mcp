### Install Gunicorn from Source

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/install.rst

Installs Gunicorn directly from its GitHub repository. This allows users to get the latest development version.

```bash
pip install git+https://github.com/benoitc/gunicorn.git
```

```bash
pip install -U git+https://github.com/benoitc/gunicorn.git
```

--------------------------------

### Procfile for Gaffer

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Example of a Procfile to define Gunicorn applications for management by Gaffer. It lists the command to start the Gunicorn application.

```conf
gunicorn = gunicorn -w 3 test:app
```

--------------------------------

### Install and Run Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/site/index.html

This snippet shows how to install Gunicorn using pip and run a simple Python WSGI application. It includes the command to install Gunicorn, a basic Python app, and the command to start Gunicorn with the app.

```bash
$ pip install gunicorn
$ cat myapp.py
  def app(environ, start_response):
      data = b"Hello, World!\n"
      start_response("200 OK", [
          ("Content-Type", "text/plain"),
          ("Content-Length", str(len(data)))
      ])
      return iter([data])
$ gunicorn -w 4 myapp:app
[2014-09-10 10:22:28 +0000] [30869] [INFO] Listening at: http://127.0.0.1:8000 (30869)
[2014-09-10 10:22:28 +0000] [30869] [INFO] Using worker: sync
[2014-09-10 10:22:28 +0000] [30874] [INFO] Booting worker with pid: 30874
[2014-09-10 10:22:28 +0000] [30875] [INFO] Booting worker with pid: 30875
[2014-09-10 10:22:28 +0000] [30876] [INFO] Booting worker with pid: 30876
[2014-09-10 10:22:28 +0000] [30877] [INFO] Booting worker with pid: 30877
```

--------------------------------

### Gunicorn Command Line Example

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/settings.rst

Example of setting environment variables using the Gunicorn command line.

```console
gunicorn -b 127.0.0.1:8000 --env FOO=1 test:app
```

--------------------------------

### Virtualenv Setup and Gunicorn Installation

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Steps to create a virtual environment, activate it, install Gunicorn using pip, and then deactivate the environment. This ensures Gunicorn is installed in an isolated Python environment.

```bash
$ mkdir ~/
$ virtualenv ~/
$ source ~/bin/activate
$ pip install gunicorn
$ deactivate

```

--------------------------------

### Nginx Configuration Example

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

An example Nginx configuration file for serving Gunicorn applications. This configuration is designed for fast clients and includes directives for proxying requests to the Gunicorn application server.

```nginx
.. literalinclude:: ../../examples/nginx.conf
   :language: nginx
   :caption: **nginx.conf**
```

--------------------------------

### Gunicorn Example with Test App

Source: https://github.com/benoitc/gunicorn/blob/master/README.rst

Runs Gunicorn with 2 workers using the 'test:app' WSGI application from the examples directory.

```bash
cd examples
gunicorn --workers=2 test:app
```

--------------------------------

### Gunicorn Configuration File Example

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/configure.rst

An example of a Gunicorn configuration file written in Python. This file allows setting parameters like bind address and the number of workers.

```python
import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
```

--------------------------------

### Systemd Service Management for Nginx

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Commands to enable the Nginx service to start automatically at boot and to start the Nginx service immediately.

```bash
systemctl enable nginx.service
```

```bash
systemctl start nginx
```

--------------------------------

### Install Gunicorn with Extra Packages

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/install.rst

Installs Gunicorn along with additional packages for specific functionalities like async workers or process name management.

```bash
pip install gunicorn[eventlet]
pip install gunicorn[gevent]
pip install gunicorn[gthread]
pip install gunicorn[tornado]
pip install gunicorn[setproctitle]
pip install gunicorn[gevent,setproctitle]
```

--------------------------------

### Gaffer Configuration for Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Configuration example for Gaffer to monitor and manage Gunicorn processes. It specifies the command to run Gunicorn and the working directory.

```conf
[process:gunicorn]
cmd = gunicorn -w 3 test:app
cwd = /path/to/project
```

--------------------------------

### Install Gunicorn via Pip

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/install.rst

Installs the latest released version of Gunicorn using pip. This is the most common method for installing Gunicorn.

```bash
pip install gunicorn
```

--------------------------------

### Testing Gunicorn Socket Activation with curl

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Example command using curl to test if the Gunicorn service is automatically started by systemd when a request is made to the configured unix socket.

```sh
sudo -u www-data curl --unix-socket /run/gunicorn.sock http
```

--------------------------------

### Gunicorn Setup Migration

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/news.rst

The setup process for Gunicorn has been migrated to `pyproject.toml` in version 22.0.0.

```python
migrate setup to pyproject.toml
```

--------------------------------

### Install Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/README.rst

Installs Gunicorn using pip. Requires Python 3.7 or higher.

```bash
pip install gunicorn
```

--------------------------------

### Gunicorn Basic Usage

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/run.rst

Demonstrates the fundamental command-line structure for running Gunicorn with a WSGI application. It shows how to specify the application module and callable, and includes an example with a simple 'Hello, World!' WSGI app.

```bash
$ gunicorn [OPTIONS] [WSGI_APP]
```

```python
def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
```

```text
$ gunicorn --workers=2 test:app
```

--------------------------------

### Install Async Worker Dependencies

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/install.rst

Installs necessary packages for using Eventlet or Gevent async workers with Gunicorn. Greenlet is a prerequisite for both.

```bash
pip install greenlet
pip install eventlet
pip install gunicorn[eventlet]
pip install gevent
pip install gunicorn[gevent]
```

--------------------------------

### Runit Service Definition for Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

A runit service script for Gunicorn. This script defines how to start and manage a Gunicorn process, including setting environment variables, working directory, and PID file.

```sh
#!/bin/sh

GUNICORN=/usr/local/bin/gunicorn
ROOT=/path/to/project
PID=/var/run/gunicorn.pid

APP=main:application

if [ -f $PID ]; then rm $PID; fi

cd $ROOT
exec $GUNICORN -c $ROOT/gunicorn.conf.py --pid=$PID $APP
```

--------------------------------

### Gunicorn Configuration Example

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/index.rst

This example shows how to configure Gunicorn using a Python file. It sets worker class, number of workers, and binding address.

```python
workers = 4
worker_class = "sync"
bind = "0.0.0.0:8000"
```

--------------------------------

### Basic Gunicorn Usage

Source: https://github.com/benoitc/gunicorn/blob/master/README.rst

Starts the Gunicorn server with a specified WSGI application module. The APP_MODULE is in the format 'MODULE_NAME:VARIABLE_NAME'.

```bash
gunicorn [OPTIONS] APP_MODULE
```

--------------------------------

### Install Gunicorn on Debian (Stretch - Backports)

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/install.rst

Installs a more recent version of Gunicorn (19.7.1) from Debian Backports for the Stretch release.

```bash
deb http://ftp.debian.org/debian stretch-backports main
sudo apt-get update
sudo apt-get -t stretch-backports install gunicorn3
```

--------------------------------

### Gunicorn Usage Example

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/index.rst

This snippet demonstrates a basic command-line usage of Gunicorn to serve a WSGI application. It specifies the number of worker processes and the application binding address.

```bash
gunicorn myapp:app -w 4 -b 0.0.0.0:8000
```

--------------------------------

### Install Gunicorn on Debian (Buster - Backports)

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/install.rst

Installs a more recent version of Gunicorn (20.0.4) from Debian Backports for the Buster release.

```bash
deb http://ftp.debian.org/debian buster-backports main
sudo apt-get update
sudo apt-get -t buster-backports install gunicorn
```

--------------------------------

### Gunicorn Installation with Ignore Installed

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Command to install Gunicorn into a virtual environment, forcing the installation even if Gunicorn is already installed in the system's Python environment. This is done using the '-I' or '--ignore-installed' flag with pip.

```bash
$ source ~/bin/activate
$ pip install -I gunicorn

```

--------------------------------

### Gunicorn Documentation Updates (2015)

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2015-news.rst

Details documentation improvements in Gunicorn, including fixing broken links, tweaking markup, clarifying documentation for worker classes, graceful timeouts, NGINX configurations, pythonpath settings, and REMOTE_ADDR. Also includes adding framework examples, updating installation instructions, and fixing typos.

```rst
- fix: Fix Slowloris broken link. (:issue:`1142`)
- Tweak markup in faq.rst
- fix link to proc name setting (:issue:`1144`)
- fix worker class documentation (:issue:`1141`, :issue:`1104`)
- clarify graceful timeout documentation (:issue:`1137`)
- don't duplicate NGINX config files examples (:issue:`1050`, :issue:`1048`)
- add `web.py` framework example (:issue:`1117`)
- update Debian/Ubuntu installations instructions (:issue:`1112`)
- clarify `pythonpath` setting description (:issue:`1080`)
- tweak some example for python3
- clarify `sendfile` documentation
- miscellaneous typos in source code comments (thanks!)
- clarify why REMOTE_ADD may not be the user's IP address (:issue:`1037`)
- fix: :issue:`988` fix syntax errors in examples/gunicorn_rc
- document security mailing-list in the contributing page.
```

--------------------------------

### Gunicorn Documentation Updates

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2016-news.rst

Updates and corrections made to Gunicorn's documentation, including simplifying installation instructions, fixing example configurations, updating Django URLs, and clarifying logging behavior.

```python
# Simplify installation instructions in gunicorn.org (:issue:`1072`)
# Fix URL and default worker type in example_config (:issue:`1209`)
# update django doc url to 1.8 lts (:issue:`1213`)
# fix: miscellaneous wording corrections (:issue:`1216`)
# Add PSF License Agreement of selectors.py to NOTICE (:issue: `1226`)
# document LOGGING overriding (:issue:`1051`)
# put a note that error logs are only errors from Gunicorn (:issue:`1124`)
# add a note about the requirements of the threads workers under python 2.x (:issue:`1200`)
# add access_log_format to config example (:issue:`1251`)
```

--------------------------------

### Gunicorn 0.12.1 - New hooks, RPM support, and protocol improvements

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2011-news.rst

Introduces the 'on_starting' hook for pre-arbiter setup, adds support for bdist_rpm, improves content-length handling according to PEP 3333, enhances Django support, and fixes daemonizing and IPv6 handling.

```python
- Add "on_starting" hook. This hook can be used to set anything before
  the arbiter really start
- Support bdist_rpm in setup
- Improve content-length handling (pep 3333)
- Improve Django support
- Fix daemonizing (#142)
- Fix ipv6 handling
```

--------------------------------

### Gunicorn PIP Requirements Example

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2021-news.rst

Provides an example of PIP requirements that can be used for setting up a Gunicorn environment.

```python
# requirements.txt
gunicorn>=20.1.0

```

--------------------------------

### Gunicorn Application Factory Pattern

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/run.rst

Illustrates the use of the application factory pattern with Gunicorn, where the WSGI application is obtained by calling a function. This is useful for more complex application setups.

```python
def create_app():
    app = FrameworkApp()
    ...
    return app
```

```text
$ gunicorn --workers=2 'test:create_app()'
```

--------------------------------

### Install Gunicorn on Debian (Stretch - Oldstable)

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/install.rst

Installs Gunicorn version 19.6.0 from Debian's oldstable repository. For Python 3 support, gunicorn3 must be installed.

```bash
sudo apt-get install gunicorn3
```

--------------------------------

### Gunicorn PasteDeploy Configuration

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/settings.rst

Enables loading Gunicorn configuration from a PasteDeploy config file, allowing for flexible application setup and management.

```APIDOC
paste: STRING
  Command line: --paste STRING or --paster STRING
  Default: None
  Description: Load a PasteDeploy config file. The argument can specify an app section using '#', e.g., 'production.ini#admin'. Alternate server blocks are not supported; use command-line arguments for server configuration.
```

--------------------------------

### Gunicorn Systemd and Deployment Documentation

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2019-news.rst

Covers documentation updates related to systemd deployment, including examples for setting up Gunicorn with systemd units and Unix sockets, and guidance on X-Forwarded-For access logs.

```python
- Documented  systemd deployment unit examples
- Added systemd sd_notify support
- Fixed systemd documentation to properly setup gunicorn unix socket
- Provide guidance on X-Forwarded-For access log in documentation
- Document how to serve WSGI app modules from Gunicorn
```

--------------------------------

### Gunicorn Server Hook Example (pre_fork)

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/custom.rst

This example shows how to define and use a server hook, specifically the `pre_fork` hook, within a custom Gunicorn application configuration. The hook function is executed before Gunicorn forks worker processes.

```python
import sys

def pre_fork(server, worker):
    print(f"pre-fork server {server} worker {worker}", file=sys.stderr)

# ...
if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('127.0.0.1', '8080'),
        'workers': number_of_workers(),
        'pre_fork': pre_fork,
    }
```

--------------------------------

### Install Test Requirements

Source: https://github.com/benoitc/gunicorn/blob/master/requirements_dev.txt

Installs the Python packages required for testing the Gunicorn project. This command reads dependencies from the 'requirements_test.txt' file.

```shell
pip install -r requirements_test.txt
```

--------------------------------

### Direct WSGI App Execution with Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/custom.rst

Demonstrates how to run a WSGI-compatible application directly using Gunicorn's `wsgiapp` module. This method is useful for bundling Gunicorn and the application together, for example, in PEX files.

```bash
python gunicorn.app.wsgiapp exampleapi:app --bind=0.0.0.0:8081 --workers=4
```

```bash
python gunicorn.app.wsgiapp exampleapi:app -c config.py
```

--------------------------------

### Install Gunicorn on Debian (Buster - Stable)

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/install.rst

Installs Gunicorn version 19.9.0 from Debian's stable repository. For a newer version, Debian Backports can be used.

```bash
sudo apt-get install gunicorn3
```

--------------------------------

### Generate HTML Documentation

Source: https://github.com/benoitc/gunicorn/blob/master/docs/README.rst

This command initiates the documentation generation process, creating HTML output in the 'build/html' directory. Ensure Sphinx is installed and Python version 3.7 or higher is available.

```bash
make html
```

--------------------------------

### Systemd Socket Activation Command

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Command to enable and start a systemd socket, which in turn will automatically start the associated Gunicorn service when traffic is detected on the socket.

```sh
systemctl enable --now gunicorn.socket
```

--------------------------------

### Standalone WSGI Application Example

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/custom.rst

This snippet demonstrates a basic WSGI application that can be loaded and run using a custom Gunicorn Application class. It shows the structure for integrating a WSGI app directly with Gunicorn.

```python
from gunicorn.app.base import BaseApplication

class StandaloneApplication(BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
            if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    from myapp import myapp_app

    options = {
        'bind': '%s:%s' % ('127.0.0.1', '8080'),
        'workers': 1,
    }
    StandaloneApplication(myapp_app, options).run()
```

--------------------------------

### Set Process Names with setproctitle

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/faq.rst

Install the 'setproctitle' Python package to assign more meaningful names to Gunicorn processes. This aids in distinguishing master processes and multiple applications running on the same machine when viewed with tools like 'ps' and 'top'.

```bash
pip install setproctitle
```

--------------------------------

### Gunicorn Secure Scheme Headers Behavior Examples

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/settings.rst

Illustrates how Gunicorn determines 'wsgi.url_scheme' based on 'forwarded_allow_ips' and 'secure_scheme_headers' values, showing various scenarios and their outcomes.

```APIDOC
Example Scenarios for secure_scheme_headers and forwarded_allow_ips:

Assumptions:
  - Remote Address: 134.213.44.18
  - Default secure_scheme_headers: {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}

Scenario 1:
  forwarded-allow-ips: ["127.0.0.1"]
  Secure Request Headers: X-Forwarded-Proto: https
  Result: wsgi.url_scheme = "http"
  Explanation: IP address was not allowed.

Scenario 2:
  forwarded-allow-ips: "*"
  Secure Request Headers: <none>
  Result: wsgi.url_scheme = "http"
  Explanation: IP address allowed, but no secure headers provided.

Scenario 3:
  forwarded-allow-ips: "*"
  Secure Request Headers: X-Forwarded-Proto: https
  Result: wsgi.url_scheme = "https"
  Explanation: IP address allowed, one request header matched.

Scenario 4:
  forwarded-allow-ips: ["134.213.44.18"]
  Secure Request Headers:
    X-Forwarded-Ssl: on
    X-Forwarded-Proto: http
  Result: InvalidSchemeHeaders() raised
  Explanation: IP address allowed, but the two secure headers disagreed on if HTTPS was used.
```

--------------------------------

### Gunicorn Hooks and Refactoring

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2010-news.rst

Adds the 'when_ready' hook, called after the server starts, and the 'preload' setting to load application code before worker processes fork. Includes refactoring of Config, fixes for pidfile and QUIT/HUP in async workers, and documentation improvements.

```python
Added *when_ready* hook. Called just after the server is started
Added *preload* setting. Load application code before the worker processes
    are forked.
Refactored Config
Fix pidfile
Fix QUIT/HUP in async workers
Fix reexec
Documentation improvements
```

--------------------------------

### Gunicorn Binary Upgrade with USR2

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/signals.rst

Illustrates the process of upgrading Gunicorn to a new binary without downtime. This involves replacing the binary, sending a USR2 signal to start a new master, and then using WINCH to phase out old workers.

```bash
# Replace the old Gunicorn binary with the new one
# Then send USR2 signal to the current master process
kill -USR2 <old_master_pid>

# To phase out old workers gracefully, send WINCH to the old master
kill -WINCH <old_master_pid>

# To revert, send HUP to the old master and TERM to the new master
# kill -HUP <old_master_pid>
# kill -TERM <new_master_pid>

# To finalize the upgrade, send TERM to the old master
# kill -TERM <old_master_pid>
```

--------------------------------

### Gunicorn: Access Log Format with X-Forwarded-For

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Example of a Gunicorn access log format that includes the X-Forwarded-For header. This allows access logs to display the actual client IP address when Gunicorn is run behind a proxy, instead of the proxy's IP address.

```bash
%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"

```

--------------------------------

### JavaScript WebSocket Client for Plotting

Source: https://github.com/benoitc/gunicorn/blob/master/examples/websocket/websocket.html

This JavaScript code establishes a WebSocket connection, receives data, processes it, and updates a plot using jQuery.plot. It handles data buffering and displays the last 200 data points.

```javascript
window.onload = function() {
  var data = {};
  var s = new WebSocket("ws://%(HTTP_HOST)s/data");
  s.onopen = function() {
    //alert('open');
    s.send('hi');
  };
  s.onmessage = function(e) {
    //alert('got ' + e.data);
    var lines = e.data.split('\n');
    for (var i = 0; i < lines.length - 1; i++) {
      var parts = lines[i].split(' ');
      var d = parts[0],
        x = parseFloat(parts[1]),
        y = parseFloat(parts[2]);
      if (!(d in data)) data[d] = [];
      data[d].push([x, y]);
    }
    var plots = [];
    for (var d in data) plots.push({
      data: data[d].slice(data[d].length - 200)
    });
    $.plot($("#holder"), plots, {
      series: {
        lines: {
          show: true,
          fill: true
        }
      },
      yaxis: {
        min: 0
      }
    });
    s.send('');
  };
};
```

--------------------------------

### Gunicorn Configuration and Application Loading

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2010-news.rst

Fixes built-in imports in the config, installation with pip, and Tornado WSGI support. Delays application loading until after all configuration is processed.

```python
Fix builtins import in config
Fix installation with pip
Fix Tornado WSGI support
Delay application loading until after processing all configuration
```

--------------------------------

### Gunicorn: Trust Forwarded IPs

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Command-line example for running Gunicorn with the --forwarded-allow-ips option. This tells Gunicorn to trust the X-Forwarded-* headers when the connection originates from specified IP addresses, typically those of trusted proxy servers.

```bash
$ gunicorn -w 3 --forwarded-allow-ips="10.170.3.217,10.170.3.220" test:app

```

--------------------------------

### Django Template Block

Source: https://github.com/benoitc/gunicorn/blob/master/examples/frameworks/django/testing/testing/apps/someapp/templates/base.html

This snippet represents a standard Django template block, commonly used for content inheritance and structure.

```django
{% block content %}{% endblock %}
```

--------------------------------

### Gunicorn Core Changes and Options (2014)

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2014-news.rst

Introduces the 'gthread' async worker and the `--threads` option for setting multiple listen threads. Deprecates the `--debug` option. Adds universal wheel support, uses `email.utils.formatdate` for HTTP dates, and fixes issues related to SSL options with Python 2.6, exceptions after response start, pyc file loading, raw_env config parsing, dynamic timeouts, Python 3 notification, and honoring $WEB_CONCURRENCY.

```rst
- fix: remove incompatible SSL option with python 2.6
- add new async gthread worker and `--threads` options allows to set multiple
  threads to listen on connection
- deprecate `gunicorn_django` and `gunicorn_paster`
- switch QUIT and TERM signal
- reap workers in SIGCHLD handler
- add universal wheel support
- use `email.utils.formatdate` in gunicorn.util.http_date
- deprecate the `--debug` option
- fix: log exceptions that occur after response start …
- allows loading of applications from `.pyc` files (#693)
- fix: issue #691, raw_env config file parsing
- use a dynamic timeout to wait for the optimal time. (Reduce power
  usage)
- fix python3 support when notifying the arbiter
- add: honor $WEB_CONCURRENCY environment variable. Useful for heroku
  setups.
- add: include tz offset in access log
- add: include access logs in the syslog handler.
- add --reload option for code reloading
- add the capability to load `gunicorn.base.Application` without the loading of
```

--------------------------------

### Gunicorn Debugging and Async Fixes

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2010-news.rst

Adds the --spew option for debugging, which installs a system trace hook. Includes fixes in async arbiters and a bug fix in start_response on error.

```python
Added --spew option to help debugging (installs a system trace hook)
Some fixes in async arbiters
Fix a bug in start_response on error
```

--------------------------------

### Custom SSL Context Factory

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/settings.rst

Allows customizing the SSL context by providing a callable that accepts configuration and a default SSL context factory. The callable should return a customized SSLContext object. This example sets the minimum TLS version to 1.3.

```python
import ssl

def ssl_context(conf, default_ssl_context_factory):
    context = default_ssl_context_factory()
    context.minimum_version = ssl.TLSVersion.TLSv1_3
    return context
```

--------------------------------

### Gunicorn Worker Scaling Recommendation

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/design.rst

Provides a general recommendation for the number of Gunicorn worker processes based on the number of CPU cores. It suggests starting with (2 x $num_cores) + 1 workers and tuning based on load.

```python
# Recommended number of workers: (2 * number_of_cores) + 1
# Example: If you have 4 cores, start with (2 * 4) + 1 = 9 workers.
```

--------------------------------

### Upstart Configuration for Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Upstart job configuration for running Gunicorn, especially from a virtual environment. It defines start/stop conditions, user, group, working directory, and the execution command.

```conf
description "myapp"

start on (filesystem)
stop on runlevel [016]

respawn
setuid nobody
setgid nogroup
chdir /path/to/app/directory

exec /path/to/virtualenv/bin/gunicorn myapp:app
```

--------------------------------

### Gunicorn Logging and IPV6 Support

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2010-news.rst

Adds support for logging configuration via INI files using Python's standard logging module format. Also includes IPV6 support, a multidomain application example, and improvements to the gunicorn_django command.

```python
Add support for logging configuration using a ini file.
  It uses the standard Python logging's module Configuration
  file format and allows anyone to use his custom file handler
Add IPV6 support
Add multidomain application example
Improve gunicorn_django command when importing settings module
  using DJANGO_SETTINGS_MODULE environment variable
Send appropriate error status on http parsing
Fix pidfile, set permissions so other user can read
  it and use it.
Fix temporary file leaking
Fix setpgrp issue, can now be launched via ubuntu upstart
Set the number of workers to zero on WINCH
```

--------------------------------

### Gunicorn Command Line Help

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/configure.rst

Command to display the full list of available command-line settings for Gunicorn.

```bash
$ gunicorn -h
```

--------------------------------

### Paste Deployment Configuration for Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/run.rst

Shows how to configure Gunicorn to serve applications using Paste Deployment configuration files, specifying Gunicorn as the server runner.

```ini
[server:main]
use = egg:gunicorn#main
host = 127.0.0.1
port = 8080
workers = 3
```

--------------------------------

### Nginx Reverse Proxy Configuration for Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/site/index.html

This snippet provides an example Nginx configuration to use as a reverse proxy for a Gunicorn server. It demonstrates how to listen on port 80, set the server name, log access, and proxy requests to a Gunicorn instance running on localhost:8000.

```nginx
server {
  listen 80;
  server_name example.org;
  access_log  /var/log/nginx/example.log;

  location / {
      proxy_pass http://127.0.0.1:8000;
      proxy_set_header Host $host;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
```

--------------------------------

### Gunicorn Configuration Options

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/settings.rst

This section details various command-line and configuration file options for Gunicorn. It covers application preloading, sendfile usage, socket reuse, directory changes, daemonization, environment variable settings, PID file creation, temporary directory usage, user/group switching, umask configuration, group initialization, and temporary upload directory.

```APIDOC
preload_app:
  Command line: --preload
  Default: False
  Description: Load application code before the worker processes are forked. This can save RAM and speed up server boot times, but may hinder easy application code reloading.

sendfile:
  Command line: --no-sendfile
  Default: None
  Description: Disables the use of sendfile(). If not set, the value of the SENDFILE environment variable is used. Initially, it was --sendfile, but was swapped to --no-sendfile to allow disabling. Support for the SENDFILE environment variable was added later.

reuse_port:
  Command line: --reuse-port
  Default: False
  Description: Set the SO_REUSEPORT flag on the listening socket.

chdir:
  Command line: --chdir
  Default: '.'
  Description: Change directory to the specified directory before loading applications.

daemon:
  Command line: -D or --daemon
  Default: False
  Description: Daemonize the Gunicorn process, detaching the server from the controlling terminal and entering the background.

raw_env:
  Command line: -e ENV or --env ENV
  Default: []
  Description: Set environment variables in the execution environment. Should be a list of strings in the 'key=value' format. Example: gunicorn -b 127.0.0.1:8000 --env FOO=1 test:app or raw_env = ["FOO=1"] in config.

pidfile:
  Command line: -p FILE or --pid FILE
  Default: None
  Description: A filename to use for the PID file. If not set, no PID file will be written.

worker_tmp_dir:
  Command line: --worker-tmp-dir DIR
  Default: None
  Description: A directory to use for the worker heartbeat temporary file. If not set, the default temporary directory will be used. Note: This may involve os.fchmod and could block workers on disk-backed filesystems.

user:
  Command line: -u USER or --user USER
  Default: os.geteuid()
  Description: Switch worker processes to run as this user. Accepts a user ID (integer) or username. If None, the user is not changed.

group:
  Command line: -g GROUP or --group GROUP
  Default: os.getegid()
  Description: Switch worker processes to run as this group. Accepts a group ID (integer) or group name. If None, the group is not changed.

umask:
  Command line: -m INT or --umask INT
  Default: 0
  Description: A bit mask for the file mode on files written by Gunicorn. Affects unix socket permissions. Accepts values compatible with os.umask(mode), including decimal, hex, and octal representations.

initgroups:
  Command line: --initgroups
  Default: False
  Description: If true, set the worker process's group access list with all groups of which the specified username is a member, plus the specified group ID.

tmp_upload_dir:
  Default: None
  Description: Directory to store temporary request data as they are read. This may change in future versions.
```

--------------------------------

### Systemd Service Configuration for Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Systemd service file for Gunicorn. This configuration defines the service's description, dependencies, user, working directory, and the command to execute Gunicorn.

```systemd
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
# gunicorn can let systemd know when it is ready
Type=notify
NotifyAccess=main
# the specific user that our service will run as
User=someuser
Group=someuser
# this user can be transiently created by systemd
# DynamicUser=true
RuntimeDirectory=gunicorn
WorkingDirectory=/home/someuser/applicationroot
ExecStart=/usr/bin/gunicorn applicationname.wsgi
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true
# if your app does not need administrative capabilities, let systemd know
# ProtectSystem=strict

[Install]
WantedBy=multi-user.target
```

--------------------------------

### Setuptools Versioning for pyproject.toml

Source: https://github.com/benoitc/gunicorn/blob/master/requirements_dev.txt

Specifies the version requirement for the 'setuptools' package. Version 68.0 or higher is recommended to avoid issues with 'pyproject.toml' validation, with 61.2 being the oldest known working version.

```python
setuptools>=68.0
```

--------------------------------

### Test Proxy Configuration with Hey

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/faq.rst

Use the Hey program to benchmark and test proxy configurations by sending a large number of concurrent HTTP requests to the Gunicorn server. This helps verify response buffering for synchronous workers.

```bash
hey -n 10000 -c 100 http://127.0.0.1:5000/
```

--------------------------------

### Running Gunicorn with PasteDeploy

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/run.rst

Demonstrates how to run Gunicorn using a PasteDeploy configuration file. This allows Gunicorn to use the application defined in the file, while Gunicorn itself is configured via command-line arguments. It also shows how to specify a specific application within the PasteDeploy file.

```bash
$ gunicorn --paste development.ini -b :8080 --chdir /path/to/project

$ gunicorn --paste development.ini#admin -b :8080 --chdir /path/to/project
```

--------------------------------

### PEX Build and Execution for WSGI Apps

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/custom.rst

Provides commands for building a PEX file containing a WSGI application and Gunicorn, and then running the compiled application. This is a common deployment strategy for Python applications.

```bash
# Generic pex build command via bash from root of exampleapi project
$ pex . -v -c gunicorn -o compiledapp.pex
# Running it
./compiledapp.pex exampleapi:app -c gunicorn_config.py
```

--------------------------------

### Gunicorn Configuration Settings

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/settings.rst

This section details various configuration settings for Gunicorn, including how to specify them via configuration files or command-line arguments. It covers settings related to application loading, debugging, logging, and worker management.

```APIDOC
config:
  Command line: -c CONFIG or --config CONFIG
  Default: './gunicorn.conf.py'
  Description: Path to the Gunicorn config file. Can be a file path, 'file:PATH', or 'python:MODULE_NAME'. Defaults to 'gunicorn.conf.py' in the current directory. Loading from a Python module requires the 'python:' prefix.

wsgi_app:
  Default: None
  Description: WSGI application path in the pattern $(MODULE_NAME):$(VARIABLE_NAME). Added in version 20.1.0.

reload:
  Command line: --reload
  Default: False
  Description: Restarts workers when application code changes. Intended for development. Incompatible with application preloading. Uses inotify by default with a fallback to file system polling. Requires the 'inotify' package for inotify reloader.

reload_engine:
  Command line: --reload-engine STRING
  Default: 'auto'
  Description: The implementation used for reloading. Valid engines are 'auto', 'poll', and 'inotify'. Added in version 19.7.

reload_extra_files:
  Command line: --reload-extra-file FILES
  Default: []
  Description: Extends the reload option to watch and reload on additional files like templates or configurations. Added in version 19.8.

spew:
  Command line: --spew
  Default: False
  Description: Installs a trace function that executes every line of code executed by the server.

check_config:
  Command line: --check-config
  Default: False
  Description: Checks the configuration and exits with status 0 if correct, 1 otherwise.

print_config:
  Command line: --print-config
  Default: False
  Description: Prints the fully resolved configuration settings. Implies check_config.

accesslog:
  Command line: --access-logfile FILE
  Default: None
  Description: The access log file path. '-' logs to stdout.

disable_redirect_access_to_syslog:
  Command line: --disable-redirect-access-to-syslog
  Default: False
  Description: Disables redirecting access logs to syslog. Added in version 19.8.

access_log_format:
  Command line: --access-logformat STRING
  Default: '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
  Description: The format string for access logs. Supports various identifiers like remote address (h), request method (m), URL path (U), status (s), response length (b), referrer (f), user agent (a), and more. Custom headers can be included using {header}i for request headers and {header}o for response headers. Environment variables can be accessed with {variable}e.
```

--------------------------------

### Configuring Worker Temporary Directory with tmpfs

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/faq.rst

Illustrates how to use a tmpfs mount for the worker temporary directory to avoid blocking issues with os.fchmod on disk-backed filesystems. Includes steps for checking existing tmpfs mounts, creating a new one, and configuring Gunicorn.

```bash
# Check if /tmp is RAM-backed
df /tmp

# Check if /dev/shm is available (often tmpfs)
df /dev/shm

# If /dev/shm is available, use it:
gunicorn --worker-tmp-dir /dev/shm ...

# If not, create a new tmpfs mount:
sudo cp /etc/fstab /etc/fstab.orig
sudo mkdir /mem
echo 'tmpfs       /mem tmpfs defaults,size=64m,mode=1777,noatime,comment=for-gunicorn 0 0' | sudo tee -a /etc/fstab
sudo mount /mem

# Verify the new mount
df /mem

# Configure Gunicorn to use the new tmpfs mount
gunicorn --worker-tmp-dir /mem ...
```

--------------------------------

### Supervisor Configuration for Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Supervisor configuration file for managing a Gunicorn process. It specifies the command, working directory, user, and auto-start/restart policies.

```conf
[program:gunicorn]
command=/path/to/gunicorn main:application -c /path/to/gunicorn.conf.py
directory=/path/to/project
user=nobody
autostart=true
autorestart=true
redirect_stderr=true
```

--------------------------------

### Print and Check Gunicorn Configuration

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/configure.rst

Commands to print the resolved configuration when using the command line or a configuration file, and to check if the application can be launched.

```bash
$ gunicorn --print-config APP_MODULE
$ gunicorn --check-config APP_MODULE
```

--------------------------------

### Gunicorn Common Arguments

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/run.rst

Details commonly used command-line arguments for Gunicorn, such as configuration file path, bind address, number of workers, worker class, and process name.

```APIDOC
gunicorn [OPTIONS] [WSGI_APP]

Commonly Used Arguments:

* -c CONFIG, --config=CONFIG - Specify a config file in the form $(PATH), file:$(PATH), or python:$(MODULE_NAME).
* -b BIND, --bind=BIND - Specify a server socket to bind. Server sockets can be any of $(HOST), $(HOST):$(PORT), fd://$(FD), or unix:$(PATH). An IP is a valid $(HOST).
* -w WORKERS, --workers=WORKERS - The number of worker processes. This number should generally be between 2-4 workers per core in the server.
* -k WORKERCLASS, --worker-class=WORKERCLASS - The type of worker process to run. You can set this to $(NAME) where $(NAME) is one of sync, eventlet, gevent, tornado, gthread. sync is the default.
* -n APP_NAME, --name=APP_NAME - If setproctitle_ is installed you can adjust the name of Gunicorn process as they appear in the process system table (which affects tools like ps and top).
```

--------------------------------

### Django Integration with Gunicorn

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/run.rst

Explains how to run Gunicorn with Django projects, including the default behavior of looking for an 'application' WSGI callable and how to specify settings modules or Python paths.

```bash
$ gunicorn myproject.wsgi
```

```bash
$ gunicorn --env DJANGO_SETTINGS_MODULE=myproject.settings myproject.wsgi
```

--------------------------------

### Gunicorn SCRIPT_NAME and PATH_INFO Header Handling

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2024-news.rst

The SCRIPT_NAME and PATH_INFO headers, when received from allowed forwarders, are no longer restricted for containing an underscore. This change mitigates a regression and improves compatibility with certain proxy setups.

```python
the SCRIPT_NAME and PATH_INFO headers, when received from allowed forwarders, are no longer restricted for containing an underscore
```

--------------------------------

### Systemd Process Management Commands

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/deploy.rst

Demonstrates how to manage Gunicorn processes using systemd, including sending signals (like HUP for reload) and retrieving the main process ID.

```sh
systemctl show --value -p MainPID gunicorn.service
systemctl kill -s HUP gunicorn.service
```

--------------------------------

### Gunicorn AioHttp Worker Updates (2014)

Source: https://github.com/benoitc/gunicorn/blob/master/docs/source/2014-news.rst

Details updates for the AioHttp worker, including ensuring it is shipped with Gunicorn, fixing body fetching in input, preventing installation on Python versions below 3.3, and adding support for UNIX sockets.

```rst
- fix :issue:`830` make sure gaiohttp worker is shipped with gunicorn.

- fix: fetch all body in input. fix :issue:`803`
- fix: don't install the worker if python < 3.3
- fix :issue:`822`: Support UNIX sockets in gaiohttp worker
```