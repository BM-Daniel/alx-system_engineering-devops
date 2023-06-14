# Postmortem Project

![UPS connected to a computer](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.tdk.co.ke%2Fadvantages-of-using-uninterrupted-power-supply-ups%2F&psig=AOvVaw3sIpSSqqV7mabGij4DGpjR&ust=1686858523330000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCNDYuOrDw_8CFQAAAAAdAAAAABAO)

## Issue Summary

The outage lasted for about 6 hours. That is from 10am GMT to 4pm GMT. The cashiers of the company at vending points could not render services to customers. About 40% of vending point cashiers had this issue.
During the early hours of that day, we had a power outage in the region. When power was restored, there was a surge which destroyed some components that employees use to operate.


## Timeline

The issue was detected 15 minutes after power was restored. The cashiers who use the system couldn’t boot-up their systems and others too couldn’t access the site of the company.
The sockets and UPS were tested and it was observed that the UPS had damaged batteries. For those who couldn’t access the site, we tried pinging other sites to see if they worked but they also didn’t. So we realized it was the cellular tower that the system uses that has the problem.
We had to replace the UPS battery and also work on the cellular tower.


## Root Cause

The root cause of the issue was the surge in power when power was restored. The surge in power caused both the UPS and cell tower to be unstable which caused the damage.
We simply had to buy new batteries to replace the damaged UPS battery. For the tower, the transmitter had to be fixed.


## Corrective and Preventive Measures

A voltage stabilizer has to be installed for electrical devices so that they are not destroyed during power outages and surges

![Voltage Stabiliser](https://image.made-in-china.com/202f0j00gSrThWosOGzV/PC-DVR-10000va-Relay-Control-Automatic-Voltage-Stabilizer.jpg)
