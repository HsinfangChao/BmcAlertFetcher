## BmcAlertFetcher

### What is BAF?
BmcAlertFetcher (aka BAF) - A tool for retrieving out-of-band BMC web alerts of physical machines/bare-metal servers.

### How BAF works?
The BAF tool uses the Selenium module to simulate login to the BMC interface, scrape current alert information, and push it to a Feishu (Lark) group bot.

### Why need BAF?
Obtaining the current alerts from the out-of-band management of a physical server varies depending on the server manufacturer. Normally, hardware alerts can be retrieved through the IPMI tool's SEL (System Event Log) within the operating system. 
However, the limitation of using ipmitool sel to monitor hardware alert in physical machines is that the alert information is not as comprehensive as the alerts in the BMC interface. Some alert information that appears in the current alert section of the BMC interface is not captured in ipmitool sel outputs.Directly retrieving the current alerts from the out-of-band BMC (Baseboard Management Controller) provides better timeliness. The "Current Alerts" section in the BMC web interface displays only the active alerts at that moment. If an alert is resolved, the "Current Alerts" section will be empty, ensuring up-to-date status monitoring.

### Supported Server Model
Inspur NF5688-M7

### Installation
bash install.sh
### Config
Configure BMC IP, BMC password, and webhook URL in config/bmc_info.yml
 
