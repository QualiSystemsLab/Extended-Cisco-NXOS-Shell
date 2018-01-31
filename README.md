# Extended-Cisco-NXOS-Shell
Cisco NXOS Shell extended to also configure VLANs on ports and port channels. The new commands reside in the **Resource Drivers - Python** folder, in the *cisco_nxos_ext.py* file.

<h2>Specific modifications</h2>


Modified the ConfigCommandMode init commands (in the *cisco_nxos_resource_driver.py* file) to initialize the AddVlanFlow and RemoveVlanFlow methods:

    ConfigCommandMode.ENTER_COMMAND = "conf sync"
    
    ConfigCommandMode.ENTER_ACTION_COMMANDS = ["switch-profile configure-fex"]
    
    ConfigCommandMode.EXIT_COMMAND = "end"
  
Modified ConnectivityRunner to execute modified AddVlanFlow and RemoveVlanFlow

Modified the following commands in the *cisco_nxos_ext.py* file:

* AddVlanFlow

* RemoveVlanFlow
