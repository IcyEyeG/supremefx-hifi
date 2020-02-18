#!/usr/bin/python
import sys
import usb.core
import usb.util

# hex vendor and product values
dev = usb.core.find(idVendor=0x0b05, idProduct=0x1827)

#print dev can be used for testing

# http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
#if the OS kernel already claimed the device, 

interface = 0

if dev.is_kernel_driver_active(interface) is True:
  # tell the kernel to detach
  dev.detach_kernel_driver(interface)
  # claim the device
  usb.util.claim_interface(dev, interface)

BUFFER_SIZE = 16

#This is presently configured for using 6.3mm, low impedance headphones, with mic amplification on.

#Tell the DAC to turn off an output: this is only useful if you are running the script a second time to change outputs
#f9210600020000000000000000000000 turn off 6.3mm / mic in
#f92106000a0000000000000000000000 turn off 6.3mm / line in
#f9210600060000000000000000000000 turn off 3.5mm / mic in
#f92106000e0000000000000000000000 turn off 3.5mm / line in

data0 = [0x00] * BUFFER_SIZE
data0[0x00] = 0xf9
data0[0x01] = 0x21
data0[0x02] = 0x06
data0[0x04] = 0x02

#Tell the DAC which output to turn on, and whether or not to turn on mic amplification.

#f9210600000000000000000000000000 for 6.3mm / mic in
#f9210600080000000000000000000000 for 6.3mm / line in
#f9210600040000000000000000000000 for 3.5mm / mic in
#f92106000c0000000000000000000000 for 3.5mm / line in
data1 = [0x00] * BUFFER_SIZE
data1[0x00] = 0xf9
data1[0x01] = 0x21
data1[0x02] = 0x06
#data1[0x04] = 0x04

#I don't know what this does yet

#fa210700e80000000000000000000000
data2 = [0x00] * BUFFER_SIZE
data2[0x00] = 0xfa
data2[0x01] = 0x21
data2[0x02] = 0x07
data2[0x04] = 0xe8

#Sets headphone impedance -  low, medium or high. Test headphones with the SupremeFX utility on Windows to know how to configure this without risks.

#f9210a00140000000000000000000000
data3 = [0x00] * BUFFER_SIZE
data3[0x00] = 0xf9
data3[0x01] = 0x21
data3[0x02] = 0x0a
data3[0x04] = 0x14 #low 14; medium 0a; high 00


#https://stackoverflow.com/questions/37943825/pyusb-send-hid-report

def hid_set_report(dev, report):
      """ Implements HID SetReport via USB control transfer """
      dev.ctrl_transfer(
          0x21, # REQUEST_TYPE_CLASS | RECIPIENT_INTERFACE | ENDPOINT_OUT
          9, # SET_REPORT
          0x200, 0x00,
          report)
          
hid_set_report(dev, data0)
hid_set_report(dev, data1)
hid_set_report(dev, data2)
hid_set_report(dev, data3)
hid_set_report(dev, data3) #Wireshark shows it twice


# release the device
usb.util.release_interface(dev, interface)
# reattach the device to the OS kernel
dev.attach_kernel_driver(interface)
