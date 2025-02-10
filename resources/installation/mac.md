# How to Create an Ubuntu Virtual Machine on VirtualBox for Mac

## Prerequisites
1. **VirtualBox**: Ensure you have VirtualBox installed on your Mac. You can download it from the [VirtualBox website](https://www.virtualbox.org/).
2. **Ubuntu ISO**: Download the latest Ubuntu ISO file from the [official Ubuntu website](https://ubuntu.com/download).

## Step-by-Step Guide

### Step 1: Install VirtualBox
1. **Download VirtualBox**: Go to the [VirtualBox download page](https://www.virtualbox.org/) and download the latest version for macOS.
2. **Install VirtualBox**: Open the downloaded file and follow the installation instructions to install VirtualBox on your Mac.

### Step 2: Download Ubuntu ISO
1. **Visit the Ubuntu Download Page**: Go to the [Ubuntu download page](https://ubuntu.com/download).
2. **Select Version**: Choose the version of Ubuntu you want to download (e.g., Ubuntu Desktop).
3. **Download the ISO**: Click on the download link to get the ISO file. Save it to a location you can easily access.

### Step 3: Create a New Virtual Machine
1. **Open VirtualBox**: Launch the VirtualBox application on your Mac.
2. **Click "New"**: In the VirtualBox Manager, click the "New" button to create a new virtual machine.
3. **Name Your VM**: Enter a name for your virtual machine (e.g., "Ubuntu VM"). The type should be set to "Linux" and the version to "Ubuntu (64-bit)".
4. **Click "Continue"**.

### Step 4: Allocate Memory
1. **Set Memory Size**: Choose the amount of RAM to allocate to your VM. A minimum of 2048 MB (2 GB) is recommended, but you can allocate more if your Mac has sufficient RAM.
2. **Click "Continue"**.

### Step 5: Create a Virtual Hard Disk
1. **Select "Create a virtual hard disk now"** and click "Create".
2. **Choose Hard Disk File Type**: Select "VDI (VirtualBox Disk Image)" and click "Continue".
3. **Storage on Physical Hard Disk**: Choose "Dynamically allocated" and click "Continue".
4. **Set Disk Size**: Allocate at least 20 GB for the virtual hard disk. Adjust as needed, then click "Create".

### Step 6: Configure the Virtual Machine
1. **Select Your VM**: In the VirtualBox Manager, select the newly created VM and click on "Settings".
2. **Go to Storage**: In the settings window, click on "Storage".
3. **Add the ISO File**:
   - Under "Controller: IDE", click on the empty disk icon.
   - Click on the disk icon on the right side and select "Choose a disk file".
   - Navigate to the location where you downloaded the Ubuntu ISO and select it.
4. **Click "OK"** to save the settings.

### Step 7: Start the Virtual Machine
1. **Select Your VM**: In the VirtualBox Manager, select your Ubuntu VM.
2. **Click "Start"**: This will boot the VM from the Ubuntu ISO.

### Step 8: Install Ubuntu
1. **Boot from ISO**: The VM should boot into the Ubuntu installation screen.
2. **Select "Install Ubuntu"**: Follow the on-screen instructions to begin the installation.
3. **Choose Language**: Select your preferred language and click "Continue".
4. **Keyboard Layout**: Choose your keyboard layout and click "Continue".
5. **Updates and Other Software**: Choose whether to install updates and third-party software, then click "Continue".
6. **Installation Type**: Select "Erase disk and install Ubuntu" (this only affects the virtual disk) and click "Install Now".
7. **Confirm Changes**: Click "Continue" to confirm the changes.
8. **Set Time Zone**: Choose your time zone and click "Continue".
9. **Create User Account**: Enter your name, computer name, username, and password. Click "Continue".

### Step 9: Complete Installation
- Once the installation is complete, you will be prompted to restart the VM. Make sure to remove the ISO from the virtual drive if prompted.

### Step 10: Post-Installation Setup
1. **Log In**: After rebooting, log in with the credentials you created.
2. **Update Your System**: Open a terminal and run the following commands to update your system:
   ```bash
   sudo apt update
   sudo apt upgrade
