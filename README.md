# Asus SupremeFX Hifi DAC for Linux

This script is a proof of concept for enabling the Asus SupremeFX Hifi DAC on Linux. This is an USB DAC included in Asus ROG Rampage V Edition 10 and Asus ROG MAXIMUS VIII EXTREME/ASSEMBLY motherboards.

## Usage

> If you run the script, hear the relays clicking but no sound, turn the volume wheel up.

```bash
# Requires pyusb to be installed
sudo apt install libusb-1.0-0-dev python-pip
sudo pip install pyusb
# run the script
sudo python supremefx-hifi.py
```

## Todo list:

 * Improve documentation (including detailed hardware specifications);
 * Figure out how Impedance Sense works;
 * Implement indicator app.

Pull requests, forks, bug reports/fixes welcome!

## Copying or Reusing

Included script is free software licensed under the terms of the [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.txt).

