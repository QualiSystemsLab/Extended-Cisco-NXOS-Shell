# Extended-Cisco-NXOS-Shell
Cisco NXOS Shell extended to also configure VLANs on Cisco NXOS ports and port channels. The modified VLAN commands reside in the **Resource Drivers - Python** folder, in the *cisco_nxos_ext.py* file, while the modified commands reside in the *cisco_nxos_ext.py* file.

If you'd like to see how this shell works, import the [Ext_Cisco_NXOS_Shell_Package.zip](https://github.com/QualiSystemsLab/Extended-Cisco-NXOS-Shell/raw/master/Ext_Cisco_NXOS_Shell_Package.zip) into CloudShell.

<h2>Specific modifications</h2>

Implemented the following capabilities for the *cisco_nxos_ext.py* file:

* AddVlanFlow

* RemoveVlanFlow

Modified the ConfigCommandMode init commands (in the *cisco_nxos_resource_driver.py* file) to support the configuration of the VLANs:

    ConfigCommandMode.ENTER_COMMAND = "conf sync"
    
    ConfigCommandMode.ENTER_ACTION_COMMANDS = ["switch-profile configure-fex"]
    
    ConfigCommandMode.EXIT_COMMAND = "end"
  
Overrode ConnectivityRunner to execute the modified AddVlanFlow and RemoveVlanFlow commands
