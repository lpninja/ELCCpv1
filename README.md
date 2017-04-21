**OPEN standard for the Tx Message Space for IoT/blockchain interaction** 

This is to define the ELCC text space standard for ElectriCChain/ blockchain IoT standard that is **portable across blockchains**. For more information please see ElectriCChain.org project no.3 or some of the work we are doing at chainofthings/solcrypto.

We want to certify components into the blockchain TX message space. This means that if the component is in operation and confirmed in the field by a human, it can be added also by a human input. Otherwise this standard is designed to be working on IoT/Inverters, data-loggers as a python script that requests human input interactions at setup.

Additionally, if we just want to certify the existance of a solar industry product, we can do that as well. 
Also, if we want to link a certain GPS anchored system into the SolarCoin blockchain, we can do that too. We can see where it is and it links to off chain web layer web links. For privacy, if you want to certifiy your solar system you can limit the GPS decimal length to three characters.

API's can be written to specifically search and scrape this Tx data. For example with Node-red calling JSON requests.

This is also designed to work with the SolarCoin granting Engine. This will need to link with the existance of the module and components in the SolarCoin blockchain. And then it can assign a unique GUID, use the SolarCoin blockchain (or **any other blockchain** as a immutable ledger for other programs to search this ledger and grant rewards, or mine information about weather, climates, power generation etc.)

**Specifics**

These files are curently in Python 2.7 and should work natively on Raspberry Pi 2/3 with Raspian-lite/ ROKOS.
ROKOS is a Jessie 8 variant for Linux specifically running and designed for IoT/ RPI3b etc.

ElectriCChain certification syntax for SLR Blockchain Tx messaging field which is limited to 516 characters.

Example in SLR chain: https://chainz.cryptoid.info/slr/tx.dws?b9ceac11c9e2c1998f95897bea3f5545d019ed1727ac9cf46a31d8a7843eb32e.htm

**Example: {"module": "ReneSola Solar CS6U-315", "inverter": "E-tracer ET3415", "pyranometer": "Aedilis Cloud Industries WCC200 sn 1915040004", "windsensor": "Delta Ohm LP PYRA 10", generation: [{"Period1": "2016-07-19-10-10-00-2019-07-19-11-10-00", "MWh": 10.000000}, {"Period2": "2016-07-19-11-10-00-2019-07-19-12-10-00", "MWh": 10.000010}], "Size kW": 0.25, "Web layer API": "sunpulse.cloud.industries.eu", "lat": "35.655N", "long": "139.698E", "Comment": "Hello World- I am the Ninja Node and the first on the ElectriCChain.", "IoT": "Hello renewable future!"}"""**

**List of additions**

Updated 2017/04/21- Added elliptical curve cryptography standard for device identity based on the Chain of things protocol to the Tx Message Space. More information (here):-[https://www.chainofthings.com/].

Updated 2017/04/20- Open comments reduced to 40 characters (one-quarter twitter). Updated example for SLR chain.

Updated 2017/04/20- Supports JSON. Please limit your Open comment to about 80 characters (half twitter).
