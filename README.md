# TABATA DESKTOP APP

## ABOUT

    A configurable Tabata timer for desktop made in Python 3.11.
    
    author: Marco Baturan
    date: 26.4.21
    License: CC0
    Warranty: None

## PICTURES

![Application](assets/pictures/Tabata_application_2026-04-22_01-41-23.jpg)

## Install instructions

This program runs in Python 3.11.2, is not tested with other versions.
You can use virtual environment or UV to install and run.
Classic:

$ python -m venv env && pip install -r requirements.txt

$ python app.py

UV:

$ uv sync

$ uv run app.py


## Agreements

    Sounds are courtesy of https://freesound.org

## Use instructions

    Set the seconds (until 60) of intense part, set the seconds of rest part (until 60)
    and save configuration. Set the number of sets for one Tabata.
    Then push the button to start the session. 
    If you need to pause, you can push the button pause. 
    If you need to continue, then push the button to continue.
    If you need to stop, then push the button to stop and get out of the cycle.
    The button save stores the configuration in an internal file, and if you need to delete, 
    just push the button delete to erase the file. The program can run with and without 
    the configuration file. 

## 🖥️ Hardware & test OS:

    System:
      Kernel: 6.1.0-44-amd64 arch: x86_64 bits: 64 compiler: gcc v: 12.2.0
        Desktop: Xfce v: 4.18.1 Distro: Debian GNU/Linux 12 (bookworm)
    Machine:
      Type: Laptop System: HP product: HP Laptop 15s-eq1xxx v: N/A
        serial: <superuser required>
      Mobo: HP model: 8707 v: 37.26 serial: <superuser required> UEFI: AMI
        v: F.67 date: 12/22/2022
    Battery:
      ID-1: BAT0 charge: 29.8 Wh (88.4%) condition: 33.7/33.7 Wh (100.0%)
        volts: 12.2 min: 11.3 model: Hewlett-Packard Primary status: discharging
    CPU:
      Info: 8-core model: AMD Ryzen 7 4700U with Radeon Graphics bits: 64
        type: MCP arch: Zen 2 rev: 1 cache: L1: 512 KiB L2: 4 MiB L3: 8 MiB
      Speed (MHz): avg: 1400 min/max: 1400/2000 boost: enabled cores: 1: 1400
        2: 1400 3: 1400 4: 1400 5: 1400 6: 1400 7: 1400 8: 1400 bogomips: 31939
      Flags: avx avx2 ht lm nx pae sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3 svm
    Graphics:
      Device-1: AMD Renoir vendor: Hewlett-Packard driver: amdgpu v: kernel
        arch: GCN-5 bus-ID: 03:00.0 temp: 44.0 C
      Device-2: Luxvisions Innotech HP TrueVision HD Camera type: USB
        driver: uvcvideo bus-ID: 1-3:3
      Display: x11 server: X.Org v: 1.21.1.7 with: Xwayland v: 22.1.9 driver: X:
        loaded: amdgpu unloaded: fbdev,modesetting,vesa dri: radeonsi gpu: amdgpu
        resolution: 1280x720~60Hz
      API: OpenGL v: 4.6 Mesa 22.3.6 renderer: AMD Radeon Graphics (renoir LLVM
        15.0.6 DRM 3.49 6.1.0-44-amd64) direct-render: Yes
    Audio:
      Device-1: AMD Renoir Radeon High Definition Audio vendor: Hewlett-Packard
        driver: snd_hda_intel v: kernel bus-ID: 03:00.1
      Device-2: AMD ACP/ACP3X/ACP6x Audio Coprocessor vendor: Hewlett-Packard
        driver: snd_rn_pci_acp3x v: kernel bus-ID: 03:00.5
      Device-3: AMD Family 17h/19h HD Audio vendor: Hewlett-Packard
        driver: snd_hda_intel v: kernel bus-ID: 03:00.6
      API: ALSA v: k6.1.0-44-amd64 status: kernel-api
      Server-1: PipeWire v: 0.3.65 status: active
    Network:
      Device-1: Realtek RTL8822CE 802.11ac PCIe Wireless Network Adapter
        vendor: Hewlett-Packard driver: rtw_8822ce v: N/A port: f000 bus-ID: 01:00.0
      IF: wlo1 state: up mac: <filter>
    Bluetooth:
      Device-1: Realtek Bluetooth Radio type: USB driver: btusb v: 0.8
        bus-ID: 1-4:4
      Report: hciconfig ID: hci0 rfk-id: 1 state: up address: <filter> bt-v: 3.0
        lmp-v: 5.1
    Drives:
      Local Storage: total: 476.94 GiB used: 377.71 GiB (79.2%)
      ID-1: /dev/nvme0n1 vendor: Samsung model: MZVLB512HBJQ-000H1
        size: 476.94 GiB temp: 40.9 C
    Partition:
      ID-1: / size: 451.86 GiB used: 377.71 GiB (83.6%) fs: ext4
        dev: /dev/nvme0n1p2
      ID-2: /boot/efi size: 299.4 MiB used: 5.8 MiB (2.0%) fs: vfat
        dev: /dev/nvme0n1p1
    Swap:
      ID-1: swap-1 type: partition size: 16.48 GiB used: 0 KiB (0.0%)
        dev: /dev/nvme0n1p3
    Sensors:
      System Temperatures: cpu: 45.5 C mobo: N/A gpu: amdgpu temp: 44.0 C
      Fan Speeds (RPM): fan-1: 0 fan-2: 0
    Info:
      Processes: 306 Uptime: 5h 39m Memory: 14.98 GiB used: 8.9 GiB (59.4%)
      Init: systemd target: graphical (5) Compilers: gcc: 12.2.0 Packages: 3502
      Shell: Bash v: 5.2.15 inxi: 3.3.26
