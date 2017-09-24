#!/usr/bin/env python
"""ELCCpv1.py: Sets the ElectriCChain standard syntax for the TXID space in the blockchain comments for connecting Solar PV inverters and data-loggers to the blockchain. Works with any blockchain running a daemon and having space to add a text comment only limited by the number of text characters. """
__author__ = "Luke Johnson AKA lpninja lp@solcrypto.com"
__copyright__ = "Copyright 2017, Luke Johnson"
__license__ = "The Unlicense"
__version__ = "1.8"

"""This is the TXID standard. 
Comment Component cert in JSON: 
sysv1{
  "UserID":"SolarCoin affiliate website, or blockpass User ID",
  """The UserID is linked to the appropriate solarcoin affiliate websites UserID, or a third-party service protocol such as blockpass.org, any third party can implement their ID system up to 40 Characters."""
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
"""Example: {"UserID":"009mx87m543567nqnnbvcdretyupam3mmmwiqw4r","module": "Solarworld Sunmodule Plus SW 265 mono black SW-01-6023US","inverter":"Enphase M250 Microinverter 800-00181-r06","data-logger":"","pyranometer":"","windsensor":"","rainsensor":"","Web_layer_API":"","Size_kW":"3.975","lat":"51.678N","long":"0.301E","Comment":"any comment up to 40char, RPI 2b, static, solar powered","generation":"2017-04-20-14:10:25-2017-04-20-14:15:27","MWh":"9.046878"}"""

Generation cert in JSON:
  genv1{"UID":"7859bc519a67977e06d5e9d58860ab0546f65a29",
        "t0":"2017-09-23 14:42:19","MWh0":"11.339875",
        "t1":"2017-09-23 16:20:32","MWh1":"11.341858",
        "t2":"2017-09-23 18:45:24","MWh2":"11.3429",
        "t3":"2017-09-23 20:56:31","MWh3":"11.3429",
        "t4":"2017-09-23 23:21:25","MWh4":"11.3429",
        "t5":"2017-09-24 01:46:19","MWh5":"11.3429",
        "t6":"2017-09-24 04:11:13","MWh6":"11.3429",
        "t7":"2017-09-24 06:36:09","MWh7":"11.342917",
        "t8":"2017-09-24 08:50:08","MWh8":"11.343934",
        "t9":"2017-09-24 11:15:03","MWh9":"11.348254"}
