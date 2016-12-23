#!/usr/bin/env python
"""ELCCpv1.py: Sets the ElectriCChain standard syntax for the TXID space in the blockchain comments for connecting Solar PV inverters and data-loggers to the blockchain. Works with any blockchain running a daemon and having space to add a text comment only limited by the number of text characters. """
__author__ = "Luke Johnson AKA lpninja"
__copyright__ = "Copyright 2016, Luke Johnson"
__license__ = "The Unlicense"
__version__ = "1.0"

"""This is the TXID standard. 
Comment Component cert: 
str ('Note this is all public information module maufacturer modelcode inverter maufacturer modelcode;
data-logger maufacturer modelcode sn;
sensor pyranometer modelcode sensor wind speed modelcode;
sensor rain modelcode;
sensor water flow modelcode; 
sensor xx modelcode;
Time period: 
20XX-XX-XX-20XX-XX-XX
Web layer API frontend: off chain name weblink login
System size kW: X.XX
Component latitude-longitude: 
00.00000000N/S, 000.00000000E/W
Comment 1: anything
IoT Comment: The type of IoT running this py script.
"""
"""Example: Note this is all public information ReneSola Solar CS6U-315 E-tracer ET3415 Aedilis Cloud Industries WCC200 sn 1915040004 Delta Ohm LP PYRA 10 2016-07-19-2019-07-19 0.25kW off chain sunpulse.cloud.industries.eu 35.6556177971N, 139.698872606E operation Hello World- I am the Ninja Node and the first on the ElectriCChain. Hello renewable future!"""

print("Initiating SolarCoin")
energylifetime = str('Note this is all public information '+solar_panel+'; '+solar_inverter+'; '+peak_watt+'kW ;'+latitude+','+longitude+'; '+message+'; '+rpi+'; Total MWh: {}' .format(total_energy)+'; )
print("SolarCoin TXID:")