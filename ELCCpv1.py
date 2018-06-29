#!/usr/bin/env python
"""ELCCpv1.py: Sets the ElectriCChain standard syntax for the TXID space in the blockchain comments for connecting Solar PV inverters and data-loggers to the blockchain. Works with any blockchain running a daemon and having space to add a text comment only limited by the number of text characters. """
__author__ = "lpninja lp@solcrypto.com"
__copyright__ = "Copyright 2017, Luke Johnson"
__license__ = "The Unlicense"
__version__ = "2.0"
__comment__= "無"

"""This is the TXID standard. 
Comment Component cert in JSON: 
sysv1{
"""'sys' denotes the following JSON string contains details about the system logging the data, 'v1' allows for version control and changes to future datalogging syntax"""
  "UID":"SolarCoin affiliate website, or blockpass User ID",
  """The UserID is linked to the appropriate solarcoin affiliate websites UserID, or a third-party service protocol such as blockpass.org, any third party can implement their ID system up to 40 Characters."""
  "SigAddr":"a new random address selected from the SolarCoin wallet used solely to sign and verify tx-messages"
  "tilt":"tilt angle of the solar panels in degrees to the surface horizontal of the mounting plane, or 'tracked' for systems with tracking.",
  "azimuth":"azimuth angle of the solar panels in degrees (0-359), with 0 be magnetic North in the Northern hemisphere, 180 degrees is magnetic South and 'tracked' for systems with tracking.",
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
   "Sig": "digital signature based on SigAddr, and using the concatenation of sysv1 message {.....} + SHA1 checksum of the datalogger.py program"
"""
"""Example: text:sysv1{"UID":"14dac6fffd768ee96250acd8bd0ff55eae03eae5","SigAddr":"8HZUxJZb2dBmhiMtXhBzNETqBj9NWotxUv","module":"Solarworld Sunmodule Plus SW 265 mono black SW-01-6023US","tilt":"50","azimuth":"210","inverter":"Enphase M250 Microinverter 800-00181-r06","data-logger":"Raspberry Pi2b","pyranometer":"","windsensor":"","rainsensor":"","Web layer API":"","Size_kW":"3.975","lat":"51.678N","long":"0.301E","Comment":"I am the first Raspberry Pi Node"}Sig:IDRMXcpAgHzoVSHFINS0YLx73wtrfMA0AatpbPqdKilQ9kbJM9eAfN3wDpctXpmsewrgGOA2efvpi5fT7gq8h7w="""

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
        }"Sig":"digital signature based on SigAddr from sysv1 and using the contatenation of genv1 message {.....} + SHA1 checksum of datalogger.py program"
  """'tX' denotes this is a time period, all dates and times in Gregorian calendar, 'MWhX' denotes the system total amount of energy logged
  at the timestamp, to 11 characters"""
  """Example: genv1{"UID":"14dac6fffd768ee96250acd8bd0ff55eae03eae5","t0":"2017-10-09 15:00:30","MWh0":11.490584,"t1":"2017-10-09 15:15:34","MWh1":11.490653,"t2":"2017-10-09 15:31:07","MWh2":11.490673,"t3":"2017-10-09 15:45:40","MWh3":11.490693,"t4":"2017-10-09 16:00:14","MWh4":11.49071,"t5":"2017-10-09 16:15:48","MWh5":11.490718,"t6":"2017-10-09 16:30:50","MWh6":11.490725,"t7":"2017-10-09 16:45:23","MWh7":11.490731}Sig:IGLDDNxi/GEljzT1xyf6+6Y8kuQAwEcllWZkaUBeNfWSgaM8E7OYs4uZBXbDsJysCQY98Ik1fSSpexPpKAwaLTI="""
