### Install MySQL on Ubuntu (WSL)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Commands to install MySQL server on an Ubuntu distribution running on WSL. This includes updating package lists, installing the server, checking the version, starting the server, and accessing the MySQL prompt.

```Bash
sudo apt update

```

```Bash
sudo apt install mysql-server

```

```Bash
mysql --version

```

```Bash
systemctl status mysql

```

```Bash
sudo mysql

```

--------------------------------

### Install and Manage MySQL on Ubuntu (WSL)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database

This snippet covers the essential bash commands for installing, starting, and managing MySQL server on an Ubuntu distribution within WSL. It includes updating packages, installing the MySQL server, checking the version, starting/checking status, accessing the MySQL prompt, and performing basic database operations like showing, creating, and dropping databases.

```bash
sudo apt update

```

```bash
sudo apt install mysql-server

```

```bash
mysql --version

```

```bash
systemctl status mysql

```

```bash
sudo mysql

```

```bash
SHOW DATABASES;

```

```bash
CREATE DATABASE database_name;

```

```bash
DROP DATABASE database_name;

```

--------------------------------

### Set Up Custom Aliases in .profile for WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Defines custom command aliases in the .profile file for WSL to simplify starting services and accessing shells. This example sets up aliases for PostgreSQL.

```bash
sudo nano .profile

# My Aliases
alias start-pg='sudo service postgresql start'
alias run-pg='sudo -u postgres psql'
```

--------------------------------

### Install and Manage PostgreSQL on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database

Installs PostgreSQL on Ubuntu WSL, including updating packages, installing the database and contrib package, checking the version, managing the service (status, start, stop), setting the admin password, and connecting to the psql shell. It also covers basic psql commands like listing users and exiting.

```Bash
sudo apt update
sudo apt install postgresql postgresql-contrib
psql --version
sudo service postgresql status
sudo service postgresql start
sudo service postgresql stop
sudo passwd postgres
sudo -u postgres psql
\du
:q
```

--------------------------------

### Verify PostgreSQL Installation on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Confirms that PostgreSQL has been successfully installed and displays the installed version number.

```Bash
psql --version
```

--------------------------------

### Distribution Manifest Example with Install Commands

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro_source=recommendations

This JSON example shows a distribution manifest and the corresponding `wsl --install` commands. The manifest defines distributions with names, default settings, and friendly names. The example also shows how the `wsl --install` command uses the manifest to install distributions based on flavor or version.

```JSON
{
    "ModernDistributions": {
        "my-distro": [
            {
                "Name": "my-distro-v3",
                "Default": true,
                "FriendlyName": "My distribution version 3 (latest)"
                [...]
            },
            {
                "Name": "my-distro-v2",
                "Default": false,
                "FriendlyName": "My distribution version 2"
                [...]
            }
        ]
    }
}
```

--------------------------------

### Verify SQLite Installation on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Confirms that SQLite3 has been successfully installed and displays the installed version number.

```Bash
sqlite3 --version
```

--------------------------------

### Install WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/release-notes

Introduces the `wsl.exe --install` command-line option, simplifying the setup process for WSL. This command handles the installation of WSL and default distributions, making it easier for new users to get started.

```Shell
wsl.exe --install

```

--------------------------------

### Secure MySQL Installation on Ubuntu (WSL)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Commands to start the MySQL server and run the security script for a MySQL installation on Ubuntu running on WSL. This script helps configure security settings, set the root password, and remove insecure defaults.

```Bash
sudo service mysql start

```

```Bash
sudo mysql_secure_installation

```

--------------------------------

### Install SQLite on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database

Installs SQLite3 on Ubuntu WSL, including updating packages, installing the sqlite3 package, and checking the version. It also demonstrates creating a test database, listing databases, viewing database info, and exiting the SQLite prompt.

```Bash
sudo apt update
sudo apt install sqlite3
sqlite3 --version
sqlite3 example.db
.databases
.dbinfo ?DB?
.exit
```

--------------------------------

### Install SQLite on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Installs the SQLite3 package on Ubuntu running in WSL. This command should be run after updating the package list.

```Bash
sudo apt install sqlite3
```

--------------------------------

### Set up Miniconda and Python Environment

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Downloads and installs Miniconda, a minimal installer for the conda package manager, and then creates and activates a dedicated Python 3.7 virtual environment named 'directml'.

```Bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
conda create --name directml python=3.7 -y
conda activate directml

```

--------------------------------

### Distribution Manifest JSON Example

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro_source=recommendations

This JSON example demonstrates the structure of a distribution manifest file. This file contains metadata about the distributions that are available for installation via `wsl --install <distribution>`. It lists distributions under `ModernDistribution`, including their names, friendly names, default status, and URLs/hashes for different architectures.

```JSON
{
    "ModernDistributions": {
        "<flavor>": [
            {
                "Name": "<version name>",
                "FriendlyName": "<friendly name>",
                "Default": true | false,
                "Amd64Url": {
                    "Url": "<tar url>",
                    "Sha256": "<tar sha256 hash>"
                },
                "Arm64Url": {
                    "Url": "<tar url>",
                    "Sha256": "<tar sha256 hash>"
                }
            },
            {
                ...
            }
        ],
        "<flavor>": [
            ...
        ]
    }
}
```

--------------------------------

### Install PostgreSQL on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Installs PostgreSQL and the PostgreSQL Contrib package on Ubuntu in WSL. The Contrib package includes helpful utilities.

```Bash
sudo apt install postgresql postgresql-contrib
```

--------------------------------

### Install Software using apt-get (Ubuntu)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Installs a specified application package using the apt-get package manager in Ubuntu. Requires root privileges via sudo. Replace `<app_name>` with the actual package name.

```Bash
sudo apt-get install <app_name>
```

--------------------------------

### Install Redis Server on Ubuntu (WSL)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Installs the Redis server package on an Ubuntu distribution within WSL. This involves updating package lists and then installing the redis-server package.

```bash
sudo apt update
sudo apt install redis-server
```

--------------------------------

### Create and Interact with SQLite Database on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Creates a new SQLite database file named 'example.db' and provides commands to interact with the SQLite prompt, including exiting.

```Bash
sqlite3 example.db
.databases
.dbinfo ?DB?
CREATE TABLE empty (kol INTEGER);
.exit
```

--------------------------------

### Install Docker Engine in WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Installs the Docker engine directly within WSL using a curl script and starts the Docker service. This is a prerequisite for using Docker containers, including ML framework containers.

```Bash
curl https://get.docker.com | sh
sudo service docker start

```

--------------------------------

### Set up NVIDIA Container Toolkit Repository

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Configures the stable repository for the NVIDIA Container Toolkit by downloading GPG keys and creating a sources list file. This enables the installation of NVIDIA-specific Docker packages.

```Bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-docker-keyring.gpg
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-docker-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

```

--------------------------------

### Install PyTorch-DirectML Dependencies and Package

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Installs necessary system libraries (libblas3, libomp5, liblapack3) and then installs the PyTorch-DirectML package using pip. This allows PyTorch to use DirectML for GPU acceleration.

```Bash
sudo apt install libblas3 libomp5 liblapack3
pip install torch-directml

```

--------------------------------

### Install Software using Zypper (openSUSE)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Installs a specified application package using the Zypper package manager, common in openSUSE. Requires root privileges via sudo. Replace `<app_name>` with the actual package name.

```Bash
sudo zypper install <app_name>
```

--------------------------------

### Install TensorFlow-DirectML

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Installs the TensorFlow-DirectML package using pip. This enables TensorFlow to leverage DirectML for GPU acceleration on compatible hardware.

```Bash
pip install tensorflow-directml

```

--------------------------------

### View Running Services on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Displays a list of all services currently running on your WSL distribution.

```bash
service --status-all
```

--------------------------------

### Run ResNet Sample in TensorFlow Container

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Navigates to the example directory within the running TensorFlow container and executes a pre-trained ResNet model sample. This demonstrates GPU acceleration for image recognition tasks.

```Bash
cd nvidia-examples/cnn/
python resnet.py --batch_size=64

```

--------------------------------

### Install Software using rpm (Red Hat/CentOS)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux_source=recommendations

Installs a specified application package using the RPM package manager, often used in conjunction with YUM or DNF on Red Hat-based systems. Requires root privileges. Replace `<app_name>` with the software to install.

```Bash
sudo rpm -i <app_name>
```

--------------------------------

### Example wsl.conf File Configuration

Source: https://learn.microsoft.com/en-us/windows/wsl/manage

A comprehensive example of a wsl.conf file demonstrating various configuration options for WSL. This includes settings for automounting, network, interop, user, and boot configurations.

```bash
# Automatically mount Windows drive when the distribution is launched
[automount]

# Set to true will automount fixed drives (C:/ or D:/) with DrvFs under the root directory set above. Set to false means drives won't be mounted automatically, but need to be mounted manually or with fstab.
enabled=true

# Sets the directory where fixed drives will be automatically mounted. This example changes the mount location, so your C-drive would be /c, rather than the default /mnt/c.
root = /

# DrvFs-specific options can be specified.
options = "metadata,uid=1003,gid=1003,umask=077,fmask=11,case=off"

# Sets the `/etc/fstab` file to be processed when a WSL distribution is launched.
mountFsTab=true

# Network host settings that enable the DNS server used by WSL 2. This example changes the hostname, sets generateHosts to false, preventing WSL from the default behavior of auto-generating /etc/hosts, and sets generateResolvConf to false, preventing WSL from auto-generating /etc/resolv.conf, so that you can create your own (ie. nameserver 1.1.1.1).
[network]
hostname=DemoHost
generateHosts=false
generateResolvConf=false

# Set whether WSL supports interop processes like launching Windows apps and adding path variables. Setting these to false will block the launch of Windows processes and block adding $PATH environment variables.
[interop]
enabled=false
appendWindowsPath=false

# Set the user when launching a distribution with WSL.
[user]
default=DemoUser

# Set a command to run when a new WSL instance launches. This example starts the Docker container service.
[boot]
command=service docker start

```

--------------------------------

### WSL Install Commands (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro_source=recommendations

These PowerShell commands demonstrate how to install a WSL distribution using the `wsl --install` command. The commands install different versions of a distribution based on the manifest file. The first command installs the default version, while the others install specific versions.

```PowerShell
wsl --install my-distro # Installs 'my-distro-v3' since it's the default for 'my-distro' flavor
wsl --install my-distro-v3 # Installs 'my-distro-v3' explicitly
wsl --install my-distro-v2 # Installs 'my-distro-v2' explicitly
```

--------------------------------

### Install NVIDIA Docker Runtime

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Updates the package list and installs the nvidia-docker2 package along with its dependencies. This enables Docker to utilize NVIDIA GPUs for accelerated tasks.

```Bash
sudo apt-get update
sudo apt-get install -y nvidia-docker2

```

--------------------------------

### Manage PostgreSQL Service on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Provides commands to check the status, start, and stop the PostgreSQL database service on Ubuntu in WSL.

```Bash
sudo service postgresql status
```

```Bash
sudo service postgresql start
```

```Bash
sudo service postgresql stop
```

--------------------------------

### WSL Distribution Configuration File Example

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro

This is an example of the /etc/wsl-distribution.conf file, showing common configuration options for a WSL distribution. It includes settings for OOBE, default user, shortcuts, and Windows Terminal integration.

```ini
[oobe]
command = /etc/oobe.sh
defaultUid = 1000
defaultName = my-distro

[shortcut]
enabled = true
icon = /usr/lib/wsl/my-icon.ico

[windowsterminal]
enabled = true
ProfileTemplate = /usr/lib/wsl/terminal-profile.json
```

--------------------------------

### Configure WSL Boot Settings

Source: https://learn.microsoft.com/en-us/windows/wsl/manage

Define commands to run automatically when a WSL instance starts using the [boot] section of wsl.conf. This is useful for starting services or performing other setup tasks upon launch. This feature is available on Windows 11 and Server 2022.

```bash
# Set a command to run when a new WSL instance launches. This example starts the Docker container service.
[boot]
command=service docker start
```

--------------------------------

### WSL Install Commands (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro

These PowerShell commands demonstrate how to install a WSL distribution using the `wsl --install` command with different arguments. You can install the default version of a flavor, a specific version by name, or a specific version explicitly.

```powershell
wsl --install my-distro # Installs 'my-distro-v3' since it's the default for 'my-distro' flavor
wsl --install my-distro-v3 # Installs 'my-distro-v3' explicitly
wsl --install my-distro-v2 # Installs 'my-distro-v2' explicitly

```

--------------------------------

### Connect to PostgreSQL psql Shell on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Starts the PostgreSQL service and connects to it, opening the psql interactive shell. An alternative method using 'su - postgres' is also mentioned.

```Bash
sudo service postgresql start
sudo -u postgres psql
```

--------------------------------

### Install Software using pacman (Arch Linux)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Installs a specified application package using the pacman package manager, common in Arch Linux. Requires root privileges via sudo. Replace `<app_name>` with the actual package name.

```Bash
sudo pacman -S <app_name>
```

--------------------------------

### Install Git on Ubuntu/Debian via WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git_source=recommendations

This command installs the latest stable version of Git on Ubuntu or Debian distributions running within the Windows Subsystem for Linux. It utilizes the Advanced Packaging Tool (APT) for package management.

```Bash
sudo apt-get install git
```

--------------------------------

### Install Software using rpm (Red Hat)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Installs a specified application package using the RPM package manager, common in Red Hat-based distributions. Requires root privileges via sudo. Replace `<app_name>` with the actual package name.

```Bash
sudo rpo -i <app_name>
```

--------------------------------

### Example WSL Distribution Manifest (JSON)

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro

This is an example of a distribution manifest file, illustrating how to define different versions of a custom distribution. It shows how to specify a default version and provides placeholders for architecture-specific download URLs and hashes.

```json
{
    "ModernDistributions": {
        "my-distro": [
            {
                "Name": "my-distro-v3",
                "Default": true,
                "FriendlyName": "My distribution version 3 (latest)"
                "[...]"
            },
            {
                "Name": "my-distro-v2",
                "Default": false,
                "FriendlyName": "My distribution version 2"
                "[...]"
            }
        ]
    }
}

```

--------------------------------

### Install WSL and Distributions

Source: https://learn.microsoft.com/en-us/windows/wsl/release-notes_source=recommendations

Introduces the `wsl.exe --install` command for easily setting up WSL and its distributions. The `--list-distributions` option allows users to see available distributions for installation.

```bash
wsl.exe --install --list-distributions

```

--------------------------------

### List Appx Contents with tar.exe (Windows Command Prompt)

Source: https://learn.microsoft.com/en-us/windows/wsl/install-on-server_source=recommendations

This command lists the contents of a downloaded Linux distribution's appx file using the tar.exe utility in Windows Command Prompt. It helps identify the specific appx file needed for installation based on the system's architecture.

```batch
> tar -xf .\debian.appx
DistroLauncher-Appx_1.12.2.0_ARM64.appx
DistroLauncher-Appx_1.12.2.0_scale-100.appx
DistroLauncher-Appx_1.12.2.0_scale-125.appx
DistroLauncher-Appx_1.12.2.0_scale-150.appx
DistroLauncher-Appx_1.12.2.0_scale-400.appx
DistroLauncher-Appx_1.12.2.0_x64.appx

```

--------------------------------

### Verify Docker Installation and Run Hello World

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers

After installing Docker Desktop, these commands confirm the installation by displaying the Docker version and then running a simple 'hello-world' container to test its functionality. This ensures Docker is properly integrated with your WSL 2 environment.

```shell
docker --version

```

```shell
docker run hello-world

```

--------------------------------

### Install Software using apk (Alpine Linux)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Installs a specified application package using the Alpine Package Keeper (apk) manager, common in Alpine Linux. Requires root privileges via sudo. Replace `<app_name>` with the actual package name.

```Bash
sudo apk add <app_name>
```

--------------------------------

### Install Software using yum (Red Hat)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Installs a specified application package using the YUM package manager, common in Red Hat-based distributions like CentOS. Requires root privileges via sudo. Replace `<app_name>` with the actual package name.

```Bash
sudo yum install <app_name>
```

--------------------------------

### Manage Redis Server Service on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Commands to start, stop, and check the status of the Redis server service on WSL. It also includes a command to verify Redis functionality using the redis-cli.

```bash
sudo service redis-server start
redis-server --version
redis-cli ping
sudo service redis-server stop
```

--------------------------------

### List WSL Distributions and Versions (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/install_source=recommendations

Displays a list of installed Linux distributions and their current WSL version (1 or 2). This is useful for understanding your current WSL setup.

```powershell
wsl.exe --list --verbose
```

--------------------------------

### Install WSL Distributions

Source: https://learn.microsoft.com/en-us/windows/wsl/release-notes

Demonstrates how to list available Linux distributions that can be installed using the `wsl --install --list-distributions` command. This is part of the simplified WSL installation process.

```Shell
wsl --install --list-distributions

```

--------------------------------

### Create New File (touch)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Creates a new, empty file with the specified name in the current working directory. Replace `hello_world.txt` with your desired file name.

```Bash
touch hello_world.txt
```

--------------------------------

### Install Packages from List (apt)

Source: https://learn.microsoft.com/en-us/windows/wsl/faq

Installs packages on a WSL distribution based on a list of package names provided in a text file. This command is used after transferring the package list file to a new machine. It requires the package list file as input.

```bash
sudo apt install -y $(cat package_list.txt)
```

--------------------------------

### Install WSL on Windows Server 2022/2025

Source: https://learn.microsoft.com/en-us/windows/wsl/install-on-server_source=recommendations

This command installs WSL on Windows Server 2022 and 2025 Desktop Experience. It enables required components, downloads the kernel, sets WSL 2 as default, and installs Ubuntu by default. Run this in an administrator PowerShell and restart.

```PowerShell
wsl.exe --install
```

--------------------------------

### List Available Linux Distributions for WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/install

This command displays a list of all Linux distributions that can be installed through the online store. It's helpful for choosing a distribution when using the `wsl --install -d <DistroName>` command or when the default installation needs to be changed.

```powershell
wsl.exe --list --online

```

--------------------------------

### Create New Directory (mkdir)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Creates a new directory with the specified name in the current working directory. Replace `hello_world` with your desired directory name.

```Bash
mkdir hello_world
```

--------------------------------

### WSL Local Settings Configuration - /etc/wsl.conf

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro

An example of the /etc/wsl.conf file, used for configuring local settings on a per-distribution basis within WSL. This snippet shows how to enable or disable systemd.

```bash
# /etc/wsl.conf

[boot]
systemd=true|false

```

--------------------------------

### Example Development Server Output

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers

This is an example output from running a development server within a container. It indicates the address and port where your application is accessible. Pressing Control-C in this terminal will stop the server.

```plaintext
Starting development server at `http://127.0.0.1:8000/` Quit the server with CONTROL-C.
```

--------------------------------

### Update Software using apt (Ubuntu)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Updates the list of available software packages and upgrades installed packages to their latest versions using the apt package manager in Ubuntu. Requires root privileges via sudo.

```Bash
sudo apt update && sudo apt upgrade
```

--------------------------------

### Unzip Distribution Appx and Create Directory (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/install-on-server_source=recommendations

This PowerShell script creates a new directory for the Linux distribution and then uses tar.exe to extract the contents of the architecture-specific appx file into that directory. This prepares the distribution for use with WSL.

```powershell
$debianWSLPath = Join-Path -Path $env:LocalAppData -ChildPath DebianWSL
New-Item -Path $debianWSLPath -ItemType Directory | Out-Null
tar -xf .\DistroLauncher-Appx_1.12.2.0_x64.appx -C "$env:USERPROFILE\AppData\Local\DebianWSL"

```

--------------------------------

### Install WSL Kernel Update for WSL 2

Source: https://learn.microsoft.com/en-us/windows/wsl/install-on-server_source=recommendations

This script downloads and installs the WSL 2 Linux kernel update. It is not necessary for Server Core 2025. The script downloads an MSI installer and then runs it silently. Run this in an administrator PowerShell.

```PowerShell
Invoke-WebRequest -Uri "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi" -OutFile ".\wsl_update_x64.msi"
Start-Process "msiexec.exe" -ArgumentList "/i .\wsl_update_x64.msi /quiet" -NoNewWindow -Wait
```

--------------------------------

### Install Downloaded Linux Distribution Appx Package

Source: https://learn.microsoft.com/en-us/windows/wsl/install-manual

This command installs a downloaded Linux distribution .appx package using the `Add-AppxPackage` cmdlet in PowerShell. Navigate to the directory containing the .appx file and replace `app_name.Appx` with the actual file name. This command may not work on Server Core installations.

```PowerShell
Add-AppxPackage .\app_name.Appx
```

--------------------------------

### Enable WSL and Virtual Machine Platform on Windows Server

Source: https://learn.microsoft.com/en-us/windows/wsl/install-on-server_source=recommendations

This command enables the 'Windows Subsystem for Linux' and 'VirtualMachinePlatform' optional features on Windows Server. This is a prerequisite for installing WSL on older versions or Server Core. Run this in an administrator PowerShell.

```PowerShell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux, VirtualMachinePlatform
```

--------------------------------

### Start Debugging Application

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers_source=recommendations

Initiates the debugging process for the application within the VS Code environment. Pressing F5 or selecting 'Run > Start debugging' will launch the application, typically showing a development server address.

```bash
F5
```

--------------------------------

### Manage Redis Server Service on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database

Commands to start, stop, and check the status of the Redis server on WSL. The `redis-cli ping` command is used to verify if the Redis server is running and responding.

```bash
sudo service redis-server start
redis-cli ping
sudo service redis-server stop
```

--------------------------------

### Install X11 Apps on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps

Installs a collection of X11 applications and tools for Linux on WSL. This command uses the apt package manager to install the 'x11-apps' package. The '-y' flag automatically confirms the installation.

```bash
sudo apt install x11-apps -y
```

--------------------------------

### Install Google Chrome on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps_source=recommendations

Installs the downloaded Google Chrome .deb package. The -f option is used to fix any broken dependencies that might occur during the installation. The ./ prefix indicates that the file is in the current directory.

```bash
sudo apt install -f ./google-chrome-stable_current_amd64.deb
```

--------------------------------

### Install WSL and Ubuntu

Source: https://learn.microsoft.com/en-us/windows/wsl/install

This command installs all necessary features for WSL and the default Ubuntu distribution. It requires administrator privileges in PowerShell. After running, a restart is needed. This command is for initial WSL installation.

```powershell
wsl --install

```

--------------------------------

### Clone Project using Git in WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers

This command clones the 'Hello World Django' web application from GitHub into your WSL environment. Ensure you have Git installed in your WSL distribution. Replace '<username>' with the actual GitHub username.

```bash
git clone https://github.com/<username>/helloworld-django.git
```

--------------------------------

### Run NVIDIA TensorFlow Container

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Launches an NVIDIA NGC TensorFlow container with GPU acceleration enabled. It configures shared memory, memory locking, and stack limits for optimal performance.

```Bash
docker run --gpus all -it --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/tensorflow:20.03-tf2-py3

```

--------------------------------

### Manage MySQL Databases on Ubuntu (WSL)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Basic SQL commands to manage databases within the MySQL prompt on an Ubuntu distribution running on WSL. Includes commands to view existing databases, create a new database, and delete a database.

```SQL
SHOW DATABASES;

```

```SQL
CREATE DATABASE database_name;

```

```SQL
DROP DATABASE database_name;

```

--------------------------------

### Install a Specific Linux Distribution with WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/install

Use this command to install a specific Linux distribution instead of the default Ubuntu. Replace `[Distro]` with the desired distribution's name. This command is useful when the default installation is not suitable or when installing additional distributions.

```powershell
wsl.exe --install [Distro]

```

--------------------------------

### Add WSL Distribution to Windows PATH (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/install-on-server_source=recommendations

This PowerShell command appends the directory of the newly installed Linux distribution to the user's environment PATH variable. This allows the distribution to be launched from any command prompt or PowerShell session by simply typing its executable name.

```powershell
$userenv = [System.Environment]::GetEnvironmentVariable("Path", "User")
[System.Environment]::SetEnvironmentVariable("PATH", $userenv + ";$env:USERPROFILE\AppData\Local\DebianWSL", "User")

```

--------------------------------

### Export Installed Packages List (apt)

Source: https://learn.microsoft.com/en-us/windows/wsl/faq

Exports a list of installed packages from an apt-based WSL distribution to a text file. This is useful for replicating the software environment on another machine. The output is a text file containing package names.

```bash
dpkg --get-selections | grep -v deinstall | awk '{print $1}' > package_list.txt
```

--------------------------------

### View File Contents (cat)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Displays the entire content of a specified file directly in the command line. Replace `hello_world.txt` with the name of the file whose content you want to view.

```Bash
cat hello_world.txt
```

--------------------------------

### Verify WSL Online Distributions After Override

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro

This command lists the available distributions for installation via `wsl --install` after a custom manifest has been configured. It should display the `test-distro-v1` with its friendly name, confirming the override was successful.

```PowerShell
$ wsl --list --online
The following is a list of valid distributions that can be installed.
Install using 'wsl.exe --install <Distro>'.

NAME              FRIENDLY NAME
test-distro-v1    Test distribution version 1

```

--------------------------------

### Download and Install Google Chrome on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps

Installs Google Chrome for Linux on WSL. This involves changing to the temporary directory, downloading the .deb package using wget, and then installing it using apt, which also handles dependency issues.

```bash
cd /tmp
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -f ./google-chrome-stable_current_amd64.deb
```

--------------------------------

### Example Windows Terminal Profile Template for WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro

An example JSON file defining a Windows Terminal profile template for a WSL distribution. This template customizes appearance settings like aliasing, font weight, and color schemes.

```json
{
  "profiles": [
    {
      "antialiasingMode": "aliased",
      "fontWeight": "bold",
      "colorScheme": "Postmodern Tango Light"
    }
  ],
  "schemes": [
    {
      "name": "Postmodern Tango Light",
      "black": "#0C0C0C",
      "red": "#C50F1F",
      "green": "#13A10E",
      "yellow": "#C19C00",
      "blue": "#0037DA",
      "purple": "#881798",
      "cyan": "#3A96DD",
      "white": "#CCCCCC",
      "brightBlack": "#767676",
      "brightRed": "#E74856",
      "brightGreen": "#16C60C",
      "brightYellow": "#F9F1A5",
      "brightBlue": "#3B78FF",
      "brightPurple": "#B4009E",
      "brightCyan": "#61D6D6",
      "brightWhite": "#F2F2F2"
    }
  ]
}

```

--------------------------------

### Configure WSL Boot Commands

Source: https://learn.microsoft.com/en-us/windows/wsl/release-notes_source=recommendations

This configuration snippet shows how to specify a command to be executed when the WSL environment starts. It is part of the `/etc/wsl.conf` file.

```ini
[boot]
command=<string>

```

--------------------------------

### Edit File with Notepad (notepad.exe)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Opens the specified file using the Windows Notepad application. This command allows editing of WSL files from a familiar Windows graphical interface. Replace `hello_world.txt` with the file you want to edit.

```Bash
notepad.exe hello_world.txt
```

--------------------------------

### Install VLC Media Player in Linux (Bash)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps

This command installs VLC media player, a versatile free and open-source cross-platform multimedia player, within your Linux distribution on WSL. The `-y` flag automatically confirms any prompts during installation. You can launch VLC by typing `vlc` in the terminal.

```bash
sudo apt install vlc -y
```

--------------------------------

### Install WSL with Linux GUI App Support (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps

This command installs the Windows Subsystem for Linux (WSL) and its dependencies, including support for running Linux GUI applications. It requires an administrator PowerShell prompt and a machine restart to complete the installation. After rebooting, you will be prompted to set up your Linux username and password.

```powershell
wsl --install
```

--------------------------------

### Enable Virtual Machine Platform (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/install-manual_source=recommendations

This command enables the 'Virtual Machine Platform' optional feature, which is required before installing WSL 2. Your machine must have virtualization capabilities enabled. This command is run in PowerShell as an Administrator.

```PowerShell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

--------------------------------

### Configure Local Manifest for WSL Distribution Testing

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro

This command configures the local manifest for WSL distribution testing by executing the `override-manifest.ps1` script with the path to the distribution tarball. This allows `wsl --install` to recognize and install the custom distribution.

```PowerShell
.\override-manifest.ps1 -TarPath /path/to/tar

```

--------------------------------

### Check 9p Filesystem Support (Bash)

Source: https://learn.microsoft.com/en-us/windows/wsl/troubleshooting_source=recommendations

This Bash snippet shows how to check for 9p filesystem support, which is crucial for accessing WSL files from Windows. The `dmesg | grep 9p` command will display messages related to the 9p protocol, indicating if it has started correctly. Successful output confirms the installation of v9fs and FS-Cache registration.

```bash
[    0.363323] 9p: Installing v9fs 9p2000 file system support
[    0.363336] FS-Cache: Netfs '9p' registered for caching
[    0.398989] 9pnet: Installing 9P2000 support
```

--------------------------------

### Install WSL Plugin via Registry in PowerShell

Source: https://learn.microsoft.com/en-us/windows/wsl/wsl-plugins

Installs a WSL plugin by setting a registry key that points to the plugin's DLL file. Replace 'demo-plugin' with your desired plugin name and update the DLL path accordingly. This requires administrator privileges.

```PowerShell
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\Plugins" -Name "demo-plugin" -Value "C:\Path\to\plugin.dll" -Force

```

--------------------------------

### Import WSL Distribution from a Tar File

Source: https://learn.microsoft.com/en-us/windows/wsl/enterprise_source=recommendations

Imports a tar archive file as a new WSL distribution. This command is used to deploy a custom WSL image onto a machine. It requires the desired distribution name, the installation location, and the path to the tar file.

```bash
wsl --import <Distro> <InstallLocation> <FileName> [Options]
```

--------------------------------

### VS Code Debugging: Start Debugging

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers

This action initiates the debugging process for your application within the development container using VS Code. It utilizes the 'launch.json' configuration file to define how the application should be run and debugged.

```plaintext
Run > Start debugging
```

--------------------------------

### Verify Git and Git Credential Manager Versions

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git

This command checks the installed versions of Git and Git Credential Manager within a WSL distribution. It's a basic verification step after installing Git for Windows, which includes GCM.

```shell
git --version; git credential-manager --version

```

--------------------------------

### Install GIMP in Linux (Bash)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps

This command installs GIMP (GNU Image Manipulation Program), a powerful free and open-source raster graphics editor, within your Linux distribution on WSL. The `-y` flag automatically confirms any prompts during installation. GIMP can be launched by typing `gimp` in the terminal.

```bash
sudo apt install gimp -y
```

--------------------------------

### Run a Specific WSL Distribution (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/install_source=recommendations

Launches a specific installed Linux distribution without changing the default. This is useful for executing commands within a particular distribution on demand.

```powershell
wsl.exe --distribution <DistroName>
```

--------------------------------

### WSL Distribution Manifest Structure (JSON)

Source: https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro

This JSON structure defines the metadata for Linux distributions available for installation via `wsl --install`. It includes details like distribution name, friendly name, default status, and URLs for different architectures (Amd64, Arm64) along with their SHA256 hashes.

```json
{
    "ModernDistributions": {
        "<flavor>": [
            {
                "Name": "<version name>",
                "FriendlyName": "<friendly name>",
                "Default": true | false,
                "Amd64Url": {
                    "Url": "<tar url>",
                    "Sha256": "<tar sha256 hash>"
                },
                "Arm64Url": {
                    "Url": "<tar url>",
                    "Sha256": "<tar sha256 hash>"
                }
            },
            {
                "..."
            }
        ],
        "<flavor>": [
            "..."
        ]
    }
}

```

--------------------------------

### Mounting Remote Shares with DrvFs in WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/release-notes

Shows how to mount network shares using the DrvFs file system in WSL. This example illustrates the use of forward slashes in Windows paths for mounting, enabling access to remote resources.

```bash
sudo mount -t drvfs //server/share /mnt/share
```

--------------------------------

### Install systemd packages on Debian/Ubuntu/Kali

Source: https://learn.microsoft.com/en-us/windows/wsl/systemd_source=recommendations

For Debian, Ubuntu, or Kali Rolling distributions running on WSL, this command ensures that both the `systemd` and `systemd-sysv` packages are installed. These are necessary for systemd to function correctly.

```bash
sudo apt-get update -y && sudo apt-get install systemd systemd-sysv -y

```

--------------------------------

### Enable Windows Subsystem for Linux (PowerShell)

Source: https://learn.microsoft.com/en-us/windows/wsl/install-manual_source=recommendations

This command enables the 'Windows Subsystem for Linux' optional feature. It is a prerequisite for installing any Linux distributions on Windows. This command is run in PowerShell as an Administrator.

```PowerShell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

--------------------------------

### Edit File with VS Code (code)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Opens the specified file in Visual Studio Code for editing. This command assumes VS Code is installed and configured to work with WSL. Replace `hello_world.txt` with the file you want to edit.

```Bash
code hello_world.txt
```

--------------------------------

### Download Linux Distribution using PowerShell Invoke-WebRequest

Source: https://learn.microsoft.com/en-us/windows/wsl/install-manual_source=recommendations

This snippet demonstrates how to download a Linux distribution's .appx package using PowerShell's Invoke-WebRequest cmdlet. It requires the URI of the distribution and an output file name. The UseBasicParsing parameter is recommended for compatibility.

```PowerShell
Invoke-WebRequest -Uri https://aka.ms/wslubuntu2004 -OutFile Ubuntu.appx -UseBasicParsing
```

--------------------------------

### Common Docker CLI Commands

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers

A collection of essential Docker commands for managing images, containers, and system information. These commands are useful for interacting with your Docker installation within a WSL distribution.

```shell
docker

```

```shell
docker <COMMAND> --help

```

```shell
docker image ls --all

```

```shell
docker container ls --all

```

```shell
docker ps -a

```

```shell
docker info

```

--------------------------------

### Check WSL Version and Set to WSL 2

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers_source=recommendations

This command checks the version of your installed WSL distributions and allows you to set a specific distribution to use WSL 2. WSL 2 offers better performance and compatibility for running Linux containers compared to WSL 1.

```bash
wsl -l -v
wsl --set-version <Distro> 2
```

--------------------------------

### Open a file with Windows 'notepad.exe' from Linux

Source: https://learn.microsoft.com/en-us/windows/wsl/filesystems_source=recommendations

This example shows how to launch the Windows Notepad application (`notepad.exe`) from within a Linux distribution to open a specific file, passing the file path as an argument. It illustrates launching Windows GUI applications from WSL.

```bash
notepad.exe "C:\temp\foo.txt"

```

```bash
notepad.exe C:\\temp\\foo.txt

```

--------------------------------

### Get WSL Version for Troubleshooting

Source: https://learn.microsoft.com/en-us/windows/wsl/troubleshooting_source=recommendations

This command checks the version of your Windows Subsystem for Linux installation, particularly if you installed it from the Microsoft Store. This information is crucial for diagnosing WSL-specific problems.

```shell
wsl.exe -v
```

--------------------------------

### Configure WSL 2 VM and Experimental Settings

Source: https://learn.microsoft.com/en-us/windows/wsl/wsl-config_source=recommendations

This snippet shows how to configure various settings for the WSL 2 virtual machine and enable experimental features using the .wslconfig file. It demonstrates how to set VM memory, processors, custom kernel paths, swap space, networking options, and experimental features like sparse VHDs.

```bash
# Settings apply across all Linux distros running on WSL 2
[wsl2]

# Limits VM memory to use no more than 4 GB, this can be set as whole numbers using GB or MB
memory=4GB

# Sets the VM to use two virtual processors
processors=2

# Specify a custom Linux kernel to use with your installed distros. The default kernel used can be found at https://github.com/microsoft/WSL2-Linux-Kernel
kernel=C:\\temp\\myCustomKernel

# Specify the modules VHD for the custum Linux kernel to use with your installed distros.
kernelModules=C:\\temp\\modules.vhdx

# Sets additional kernel parameters, in this case enabling older Linux base images such as Centos 6
kernelCommandLine = vsyscall=emulate

# Sets amount of swap storage space to 8GB, default is 25% of available RAM
swap=8GB

# Sets swapfile path location, default is %UserProfile%\\AppData\\Local\\Temp\\swap.vhdx
swapfile=C:\\temp\\wsl-swap.vhdx

# Turn on default connection to bind WSL 2 localhost to Windows localhost. Setting is ignored when networkingMode=mirrored
localhostforwarding=true

# Disables nested virtualization
nestedVirtualization=false

# Turns on output console showing contents of dmesg when opening a WSL 2 distro for debugging
debugConsole=true

# Sets the maximum number of crash dump files to retain (default is 5)
maxCrashDumpCount=10

# Enable experimental features
[experimental]
sparseVhd=true

```

--------------------------------

### Get Current Directory Path (pwd)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Prints the full path of the current working directory to the command line. This command is fundamental for understanding your location within the file system.

```Bash
pwd
```

--------------------------------

### Display WSL help and available commands

Source: https://learn.microsoft.com/en-us/windows/wsl/basic-commands_source=recommendations

Shows a comprehensive list of all available options and commands for the WSL command-line interface. This is the primary command for discovering WSL functionalities.

```powershell
wsl --help
```

--------------------------------

### Change Directory (cd)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Changes the current working directory to the specified directory. Replace `hello_world` with the name of the directory you wish to navigate to.

```Bash
cd hello_world
```

--------------------------------

### List Directory Contents (ls)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Lists the names of files and directories within the current working directory. This is a basic command for viewing the contents of a directory.

```Bash
ls
```

--------------------------------

### Set PostgreSQL Admin Password on WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database_source=recommendations

Assigns a password to the default 'postgres' admin user, which is required for connecting to the database. Requires closing and reopening the terminal after setting.

```Bash
sudo passwd postgres
```

--------------------------------

### Accessing C: Drive in WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/faq

Demonstrates how to access the Windows C: drive from within a WSL distribution. This is achieved by navigating to the '/mnt/c' directory.

```bash
cd /mnt/c
```

--------------------------------

### Redirect Sorted Output to File with Pipe in Bash

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux_source=recommendations

Illustrates how to sort the contents of a file and redirect the sorted output into a new file using `cat`, `sort`, and the `>` redirect operator. The sorted output is saved to `sorted_fruit.txt`.

```Bash
$ cat fruits.txt | sort > sorted_fruit.txt
$ cat sorted_fruit.txt
Apple
Banana
Kiwi
Orange
Peach
Pear
Plum
Strawberry

```

--------------------------------

### Redirect Sorted Output to File

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Shows how to redirect the output of a command pipeline (in this case, `cat` piped to `sort`) into a new file using the `>` operator. This allows for persistent storage of command results.

```Bash
$ cat fruits.txt | sort > sorted_fruit.txt
$ cat sorted_fruit.txt
Apple
Banana
Kiwi
Orange
Peach
Pear
Plum
Strawberry
```

--------------------------------

### Sort File Contents with Pipe

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Demonstrates how to sort the contents of a text file using the `cat` command piped to the `sort` command. This method efficiently arranges lines alphabetically without manual intervention.

```Bash
$ cat fruits.txt | sort
Apple
Banana
Kiwi
Orange
Peach
Pear
Plum
Strawberry
```

--------------------------------

### Download Linux Distribution using PowerShell

Source: https://learn.microsoft.com/en-us/windows/wsl/install-manual

This snippet demonstrates how to download a Linux distribution's .appx package using the `Invoke-WebRequest` cmdlet in PowerShell. It requires the URI of the distribution and an output file name. The `$ProgressPreference` variable can be set to 'SilentlyContinue' to disable the progress bar for long downloads.

```PowerShell
Invoke-WebRequest -Uri https://aka.ms/wslubuntu2004 -OutFile Ubuntu.appx -UseBasicParsing
$ProgressPreference = 'SilentlyContinue'
```

--------------------------------

### Set Default GPU Adapter Name

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gpu-compute

Sets the MESA_D3D12_DEFAULT_ADAPTER_NAME environment variable to specify which GPU to use when multiple GPUs are present. The value should match a part of the GPU's name as seen in device manager.

```Bash
export MESA_D3D12_DEFAULT_ADAPTER_NAME="<NameFromDeviceManager>"

```

--------------------------------

### Configure Git Global User Email

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git_source=recommendations

Sets the global user email address for Git commits within a WSL distribution. This email is associated with your contributions to the repository. Replace 'youremail@domain.com' with your preferred email address.

```Bash
git config --global user.email "youremail@domain.com"
```

--------------------------------

### Search File Contents with Pipe and Grep

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Illustrates how to search for specific lines within a text file using the `cat` command piped to the `grep` command. This is useful for quickly finding lines that match a particular pattern.

```Bash
cat fruits.txt | grep P
Pear
Plum
Peach
```

--------------------------------

### Implementing Timer System Calls in WSL

Source: https://learn.microsoft.com/en-us/windows/wsl/release-notes_source=recommendations

This describes the implementation of timer_create and related system calls in WSL, which is necessary for GHC support.

```c
# Implement timer_create and related system calls.
# This enables GHC support (GH #307)
```

--------------------------------

### Configure Git Global User Name

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git_source=recommendations

Sets the global user name for Git commits within a WSL distribution. This configuration is essential for identifying the author of changes in version control history. Replace 'Your Name' with your actual username.

```Bash
git config --global user.name "Your Name"
```

--------------------------------

### Filter File Contents with Grep and Pipe in Bash

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux_source=recommendations

Shows how to filter lines from a text file that contain a specific character using `cat`, `grep`, and a pipe. The output of `cat fruits.txt` is piped as input to `grep P` to find lines containing 'P'.

```Bash
cat fruits.txt | grep P
Pear
Plum
Peach

```

--------------------------------

### List Directory Contents with Details (ls -l)

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

Lists the contents of the current working directory with detailed information, including file permissions, owner, size, and last modification time. The `-l` flag enables the long listing format.

```Bash
ls -l
```

--------------------------------

### Configure Azure DevOps HTTP Path for GCM

Source: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-git

This command configures Git to use a specific HTTP path for Azure DevOps, which is necessary for Git Credential Manager to authenticate correctly with Azure Repos or Azure DevOps. This is a global configuration setting.

```bash
git config --global credential.https://dev.azure.com.useHttpPath true

```

--------------------------------

### Download Linux Distribution using curl

Source: https://learn.microsoft.com/en-us/windows/wsl/install-manual

This snippet shows how to download a Linux distribution's .appx package using the `curl` command-line utility within PowerShell. It uses the `-LR -o` flags for recursive, location-following downloads and specifying the output file. It's important to use `curl.exe` to ensure the actual executable is invoked, not a PowerShell alias.

```PowerShell
curl.exe -LR -o ubuntu-2004.Appx https://aka.ms/wslubuntu2204
```