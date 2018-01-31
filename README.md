# Extended-Cisco-NXOS-Shell
Cisco NXOS Shell extended to also configure VLANs on Cisco NXOS ports and port channels. The modified VLAN commands reside in the **Resource Drivers - Python** folder, in the *cisco_nxos_ext.py* file, while the modified commands reside in the *cisco_nxos_ext.py* file.

<h2>Specific modifications</h2>

Implemented the following capabilities for the *cisco_nxos_ext.py* file:

* AddVlanFlow

* RemoveVlanFlow

Modified the ConfigCommandMode init commands (in the *cisco_nxos_resource_driver.py* file) to support the configuration of the VLANs:

    ConfigCommandMode.ENTER_COMMAND = "conf sync"
    
    ConfigCommandMode.ENTER_ACTION_COMMANDS = ["switch-profile configure-fex"]
    
    ConfigCommandMode.EXIT_COMMAND = "end"
  
Modified ConnectivityRunner to execute the AddVlanFlow and RemoveVlanFlow commands
