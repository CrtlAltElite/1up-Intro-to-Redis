# Installing Redis for Development
### Mac:

1. **Homebrew Method**
    1. Open the Terminal.
    2. If you don't have Homebrew, install it by running:
       ```
       /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
       ```
    3. Update Homebrew:
       ```
       brew update
       ```
    4. Install Redis:
       ```
       brew install redis
       ```

2. **Start Redis Server**
    ```
    redis-server
    ```

### Windows w/ WSL and Chocolately:

1. **Windows Subsystem for Linux (WSL) Method**
    1. Open PowerShell as Administrator and run:
       ```
       wsl --install
       ```
       (Follow on-screen instructions to complete WSL installation)
    2. Install a Linux distribution like Ubuntu from Microsoft Store.
    3. Open your Linux distribution and then follow the Linux instructions below.

2. **Chocolatey Method**
    1. Open PowerShell as Administrator.
    2. Install Chocolatey by running:
       ```
       Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
       ```
    3. Install Redis:
       ```
       choco install redis-64
       ```
Certainly, for those who prefer a simpler installation process for Redis on Windows, there are pre-compiled Windows installers and .zip files available that simplify the installation process.

### Simplified Windows Installation:

1. **Download Installer or Zip**
    - Visit the Redis for Windows [GitHub page](https://github.com/microsoftarchive/redis/releases).
    - Download either the installer (.msi) or the .zip file.

2. **Install Using the Installer [Deprecated]**
    - Double-click on the downloaded `.msi` file and follow the installation prompts. 

    **OR**

    **Extract Zip File**
    - Extract the `.zip` file to a folder of your choice. Navigate to the folder and find `redis-server.exe`.

3. **Run Redis Server**
    - If you used the installer, Redis should be available as a service. You can also find `redis-server.exe` in the installation directory to run it.
  
    **OR**
  
    - If you used the .zip method, open Command Prompt, navigate to the folder containing `redis-server.exe`, and run the command:
      ```
      redis-server.exe
      ```

4. **Test Redis Installation**
    - Open a new Command Prompt window.
    - Navigate to the installation directory or the directory where you extracted the .zip.
    - Run the command:
      ```
      redis-cli ping
      ```
    - If it returns `PONG`, your Redis server is running.

Note that this Redis build is no longer maintained officially. It's generally fine for development and testing but might not receive security updates. For production environments, using Redis through WSL or Docker is recommended.

This method is easier but trades off some of the customizability and updates that come with other installation methods.


### Linux (Ubuntu):

1. **APT Method**
    1. Open the Terminal.
    2. Update package list:
       ```
       sudo apt update
       ```
    3. Install Redis:
       ```
       sudo apt install redis-server
       ```

2. **Start Redis Server**
    ```
    sudo service redis-server start
    ```

Note: Always make sure to check the official documentation for the most current and tailored installation instructions.

- **Mac**: [Homebrew Redis Formula](https://formulae.brew.sh/formula/redis)
- **Windows**: [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/install), [Chocolatey Redis Package](https://community.chocolatey.org/packages/redis-64/)
- **Linux**: [Redis Download Page](https://redis.io/download)