These files are curently in Python 2.7 and should work natively on Raspberry Pi 2/3 with Raspian-lite/ ROKOS.

ElectriCChain certification syntax for SLR Blockchain Tx messaging field.

Updated 2017/04/20 Supports JSON. Please limit your Open comment to about 80 characters (half twitter).

Example in SLR chain: http://chainz.cryptoid.info/slr/api.dws?q=txinfo&t=b391aa1bcb0aefd8e8f661b1acd6fd0b784c0e8856ed6c2d8546b6246d623ae8

**Example: {"module": "ReneSola Solar CS6U-315", "inverter": "E-tracer ET3415", "pyranometer": "Aedilis Cloud Industries WCC200 sn 1915040004", "windsensor": "Delta Ohm LP PYRA 10", generation: [{"Period1": "2016-07-19-10-10-00-2019-07-19-11-10-00", "MWh": 10.000000}, {"Period2": "2016-07-19-11-10-00-2019-07-19-12-10-00", "MWh": 10.000010}], "Size kW": 0.25, "Web layer API": "sunpulse.cloud.industries.eu", "lat": "35.655N", "long": "139.698E", "Comment": "Hello World- I am the Ninja Node and the first on the ElectriCChain.", "IoT": "Hello renewable future!"}"""**

This is to define the ELCC text space standard for ElectriCChain. For more information please see ElectriCChain.org.

We want to certify components into the SLR blockchain. This means that if the component is in operation and confirmed in the field by a human, it can be added also by a human input. Otherwise this standard is designed to be working on IoT/Inverters, data-loggers as a python script.
In addition, if we just want to certify the existance of a solar industry product, we can do that as well. 
In addition, if we want to link a certain GPS anchored system into the SLR blockchain, we can do that too. We can see where it is and it links to off chain web layer web links.

Later, API can be written to specifically search this Tx data. 

This is also designed to work with the SolarCoin granting Engine. This will need to link with the existance of the module and components in the SolarCoin blockchain. And then it can assign a unique GUID, use the SolarCoin blockchain (or other blockchain as a immutable ledger for other programs to search this ledger and grant rewards, or mine information about weather, climates, power generation etc.)
