# Extended-Cisco-NXOS-Shell
Cisco NXOS Shell extended to also configure VLANs on ports and port channels.

New commands reside in the **Resource Drivers - Python** folder, in the *cisco_nxos_ext.py* file.

<h2>Specific modifications</h2>

*cisco_nxos_resource_driver.py* file modifications:


* Changed ConfigCommandMode init commands by adding the following lines to initialize method inside the cisco_nxos_resource_driver.py:

    ConfigCommandMode.ENTER_COMMAND = "conf sync"
    
    ConfigCommandMode.ENTER_ACTION_COMMANDS = ["switch-profile configure-fex"]
    
    ConfigCommandMode.EXIT_COMMAND = "end"
  
  * Changed ConnectivityRunner to execute modified AddVlanFlow and RemoveVlanFlow

*cisco_nxos_ext.py* file modifications:

* Changed AddVlanFlow

* Changed RemoveVlanFlow
