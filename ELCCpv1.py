#!/usr/bin/env python
"""ELCCpv1.py: Sets the ElectriCChain standard syntax for the TXID space in the blockchain comments for connecting Solar PV inverters and data-loggers to the blockchain. Works with any blockchain running a daemon and having space to add a text comment only limited by the number of text characters. """
__author__ = "Luke Johnson AKA lpninja lp@solcrypto.com"
__copyright__ = "Copyright 2017, Luke Johnson"
__license__ = "The Unlicense"
__version__ = "1.9"

"""This is the TXID standard. 
Comment Component cert in JSON: 
sysv1{
"""'sys' denotes the following JSON string contains details about the system logging the data, 'v1' allows for version control and changes to future datalogging syntax"""
  "UID":"SolarCoin affiliate website, or blockpass User ID",
  """The UserID is linked to the appropriate solarcoin affiliate websites UserID, or a third-party service protocol such as blockpass.org, any third party can implement their ID system up to 40 Characters."""
  "tilt":"tilt angle of the solar panels in degrees to the surface horizontal of the mounting plane.",
  "azimuth":"azimuth angle of the solar panels in degrees (0-180), with 0 be magnetic N in the Northern hemisphere.",
  "tracking":"Type of mounting system used commented as fixed (no tracking), single or dual."
  "module":"manufacturer modelcode",
  "inverter":"maufacturer modelcode", 
  "data-logger":"maufacturer modelcode",
  "pyranometer":"manufacturer modelcode",
  """ If there is no pyranometer used, then leave it blank."""
  "windsensor":"manufacturer modelcode",
  """ If there is no windsensor used, then leave it blank."""
  "rainsensor":"manufacturer modelcode",
  """ If there is no rainsensor used, then leave it blank."""
  "Web layer API":"off chain name weblink login",
  "Size kW":X.XXX,
  "lat":"00.000N/S",
  """For on-chain privacy, your can leave it to less decimals places for Lat/Long"""
  "long":"000.000E/W",
  """For on-chain privacy, your can leave it to less decimals places for Lat/Long"""
  "Comment":"anything up to 40 characters, The type of IoT running this py script e.g. RPi3b, RPi2, OdroidXU4 etc.",
   }
"""
"""Example: sysv1{"UID":"7859bc519a67977e06d5e9d58860ab0546f65a29","tilt":"40", "azimuth":"180", "tracking":"fixed", "module":"Solarworld Sunmodule Plus SW 265 mono black SW-01-6023US","inverter":"Enphase M250 Microinverter 800-00181-r06","data-logger":"","pyranometer":"","windsensor":"","rainsensor":"","waterflow":"","Web_layer_API":"","Size_kW":"3.975","lat":"51.678N","long":"0.301E","Comment":"Hello World- I am the first Raspberry Pi Node"}"""

Generation cert in JSON:
  genv1
"""'gen' denotes the following JSON string contains details of energy generated, 'v1' allows for version control and changes to future datalogging syntax"""
        {"UID":"7859bc519a67977e06d5e9d58860ab0546f65a29",
"""The UserID is linked to the appropriate solarcoin affiliate websites UserID, or a third-party service protocol such as blockpass.org, any third party can implement their ID system up to 40 Characters."""
        "t0":"XXXX-XX-XX XX:XX:XX","MWh0":XXXX.XXXXXX,
        "t1":"XXXX-XX-XX XX:XX:XX","MWh1":XXXX.XXXXXX,
        "t2":"XXXX-XX-XX XX:XX:XX","MWh2":XXXX.XXXXXX,
        "t3":"XXXX-XX-XX XX:XX:XX","MWh3":XXXX.XXXXXX,
        "t4":"XXXX-XX-XX XX:XX:XX","MWh4":XXXX.XXXXXX,
        "t5":"XXXX-XX-XX XX:XX:XX","MWh5":XXXX.XXXXXX,
        "t6":"XXXX-XX-XX XX:XX:XX","MWh6":XXXX.XXXXXX,
        "t7":"XXXX-XX-XX XX:XX:XX","MWh7":XXXX.XXXXXX,
        "t8":"XXXX-XX-XX XX:XX:XX","MWh8":XXXX.XXXXXX,
        "t9":"XXXX-XX-XX XX:XX:XX","MWh9":XXXX.XXXXXX}
  """'tX' denotes this is a time period, all dates and times in Gregorian calendar, 'MWhX' denotes the system total amount of energy logged
  at the timestamp, to 11 characters"""
  Example: genv1{"UID":"7859bc519a67977e06d5e9d58860ab0546f65a29","t0":"2017-09-24 16:13:57","MWh0":11.358824,"t1":"2017-09-24 16:50:12","MWh1":11.358953,"t2":"2017-09-24 17:26:26","MWh2":11.358986,"t3":"2017-09-25 06:43:19","MWh3":11.359,"t4":"2017-09-25 07:19:33","MWh4":11.359062,"t5":"2017-09-25 07:55:46","MWh5":11.359141,"t6":"2017-09-25 08:31:59","MWh6":11.359224,"t7":"2017-09-25 09:08:13","MWh7":11.359468,"t8":"2017-09-25 09:44:26","MWh8":11.359678,"t9":"2017-09-25 10:20:41","MWh9":11.360017}
