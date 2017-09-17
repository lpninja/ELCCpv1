#!/usr/bin/env python
"""ELCCpv1.py: Sets the ElectriCChain standard syntax for the TXID space in the blockchain comments for connecting Solar PV inverters and data-loggers to the blockchain. Works with any blockchain running a daemon and having space to add a text comment only limited by the number of text characters. """
__author__ = "Luke Johnson AKA lpninja lp@solcrypto.com"
__copyright__ = "Copyright 2017, Luke Johnson"
__license__ = "The Unlicense"
__version__ = "1.7"

"""This is the TXID standard. 
Comment Component cert in JSON: 
{
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
  "generation": [
    {"Period1":"20XX-XX-XX-HH:MM:SS-20XX-XX-XX-HH:MM:SS", "MWh": 1.000000}, 
    {"Period2":"20XX-XX-XX-HH:MM:SS-20XX-XX-XX-HH:MM:SS", "MWh": 1.005000}
    ],
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
