# HSG IoT Workshop System Setup Instructions

## Setup of RaspBerry Pi

### Latest python version
Currently, Raspbian still ships python 3.5, which does not yet have our
beloved f-strings. So we need to compile a more recent version from source.
In the code below, select the most recent sources available on the
[official site](https://www.python.org/downloads/source/).
```sh
# install build dependencies
sudo apt-get update
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev \
    libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev \
    libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev uuid-dev
# download and compile python
cd ~/Downloads
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xf Python-3.7.0.tar.xz
cd Python-3.7.0
# the following might take 1-2 mins
./configure --enable-optimizations
# make will take 30 mins+. Furthermore, for me, _uuid failed (non-critical).
make -j 4
sudo make altinstall
# Optionally: remove what is not needed anymore
cd ..
sudo rm -r Python-3.7.0
rm Python-3.7.0.tar.xz
sudo apt-get --purge remove build-essential tk-dev
sudo apt-get --purge remove libncurses5-dev libncursesw5-dev libreadline6-dev
sudo apt-get --purge remove libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev
sudo apt-get --purge remove libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
sudo apt-get autoremove
sudo apt-get clean
```

### SPI
Needed for ADC. Enable SPI in *interfaces* of the RPi configuration untility.
Either use the GUI or `sudo raspi-config`.

### Remote GPIO
```sh
sudo apt install pigpio
```
Use RPi configuration utility to enable *Remote GPIO*.
Either use the GUI or `sudo raspi-config`.
Then, ensure the dameon is running, either using `sudo systemctl enable pigpiod`
(start at every boot) or `sudo systemctl start pigpiod` (start just once).

## Setup of development PC

### IDE

This course uses the [Atom IDE](https://ide.atom.io/) together with the
[ide-python](https://atom.io/packages/ide-python) plugin.

Installation proceeds as follows (having python, pip and atom already installed):
```sh
pip install "python-language-server[all]"

apm install atom-ide-ui
apm install ide-python
```

### Remote GPIO

```sh
pip install gpiozero pigpio
```

## Reference
### RPi GPIO
- [RPi GPIO](https://www.raspberrypi.org/documentation/usage/gpio/)
- [Printable RPi Pinout Leaf](https://github.com/splitbrain/rpibplusleaf)
- [Remote GPIO using GPIO Zero](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html)
