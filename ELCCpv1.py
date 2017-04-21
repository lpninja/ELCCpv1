#!/usr/bin/env python
"""ELCCpv1.py: Sets the ElectriCChain standard syntax for the TXID space in the blockchain comments for connecting Solar PV inverters and data-loggers to the blockchain. Works with any blockchain running a daemon and having space to add a text comment only limited by the number of text characters. """
__author__ = "Luke Johnson AKA lpninja"
__copyright__ = "Copyright 2016, Luke Johnson"
__license__ = "The Unlicense"
__version__ = "1.2"

"""This is the TXID standard. 
Comment Component cert in JSON: 
{
   "module": "manufacturer modelcode",
  "inverter": "maufacturer modelcode", 
  "data-logger": "maufacturer modelcode",
  "data-logger-ECDHE-Pub": "Public key Hardware generated ID birth certificate", 
  "pyranometer": "manufacturer modelcode",
  "windsensor": "manufacturer modelcode",
  "rainsensor": "manufacturer modelcode",
  "waterflow": "manufacturer modelcode",
  "generation": [
    {"Period1": "20XX-XX-XX-HH-MM-SS-20XX-XX-XX-HH-MM-SS", "MWh": 1.000000}, 
    {"Period2": "20XX-XX-XX-HH-MM-SS-20XX-XX-XX-HH-MM-SS", "MWh": 1.005000}
    ],
  "Web layer API": "off chain name weblink login",
  "Size kW": X.XXX,
  "lat": "00.000N/S",
  "long": "000.000E/W",
  "Comment": "anything up to 40 characters",
  "IoT": "The type of IoT running this py script e.g. RPi3b, RPi2 etc."
  }
"""
"""Example: {"module":"Solarworld Sunmodule Plus SW 265 mono black SW-01-6023US","inverter":"Enphase M250 Microinverter 800-00181-r06","data-logger":"","data-logger-ECDHE-Pub":"","pyranometer":"","windsensor":"","rainsensor":"","waterflow":"","Web_layer_API":"","Size_kW":"3.975","lat":"51.678N","long":"0.301E","Comment":"Hello World- I am the first Raspberry Pi Node","IoT":"RPI 2b, static, solar powered","generation":"2017-04-20-14-10-25-2017-04-20-14-15-27","MWh":"9.046878"}"""
