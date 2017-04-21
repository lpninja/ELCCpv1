#!/usr/bin/env python
"""ELCCpv1.py: Sets the ElectriCChain standard syntax for the TXID space in the blockchain comments for connecting Solar PV inverters and data-loggers to the blockchain. Works with any blockchain running a daemon and having space to add a text comment only limited by the number of text characters. """
__author__ = "Luke Johnson AKA lpninja"
__copyright__ = "Copyright 2016, Luke Johnson"
__license__ = "The Unlicense"
__version__ = "1.0"

"""This is the TXID standard. 
Comment Component cert in JSON: 
{
  "module": "manufacturer modelcode",
  "inverter": "maufacturer modelcode", 
  "data-logger": "maufacturer modelcode",
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
"""Example: {"module": "ReneSola Solar CS6U-315", "inverter": "E-tracer ET3415", "pyranometer": "Aedilis Cloud Industries WCC200 sn 1915040004", "windsensor": "Delta Ohm LP PYRA 10", generation: [{"Period1": "2016-07-19-10-10-00-2019-07-19-11-10-00", "MWh": 10.000000}, {"Period2": "2016-07-19-11-10-00-2019-07-19-12-10-00", "MWh": 10.000010}], "Size kW": 0.25, "Web layer API": "sunpulse.cloud.industries.eu", "lat": "35.655N", "long": "139.698E", "Comment": "Hello World- I am the Ninja Node and the first on the ElectriCChain.", "IoT": "Hello renewable future!"}"""
