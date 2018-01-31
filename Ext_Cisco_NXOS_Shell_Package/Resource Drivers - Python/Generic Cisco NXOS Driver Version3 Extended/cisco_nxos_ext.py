from cloudshell.networking.cisco.nxos.flows.cisco_nxos_add_vlan_flow import CiscoNXOSAddVlanFlow
from cloudshell.networking.cisco.nxos.flows.cisco_nxos_remove_vlan_flow import CiscoNXOSRemoveVlanFlow
from cloudshell.networking.cisco.runners.cisco_connectivity_runner import CiscoConnectivityRunner


class CiscoNXOSExtConnectivityRunner(CiscoConnectivityRunner):
    @property
    def add_vlan_flow(self):
        return CiscoNXOSExtAddVlanFlow(self.cli_handler, self._logger)

    @property
    def remove_vlan_flow(self):
        return CiscoNXOSExtRemoveVlanFlow(self.cli_handler, self._logger)


class CiscoNXOSExtAddVlanFlow(CiscoNXOSAddVlanFlow):
    def __init__(self, cli_handler, logger):
        super(CiscoNXOSExtAddVlanFlow, self).__init__(cli_handler, logger)

    def execute_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        """ Configures VLANs on multiple ports or port-channels

        :param vlan_range: VLAN or VLAN range
        :param port_mode: mode which will be configured on port. Possible Values are trunk and access
        :param port_name: full port name
        :param qnq:
        :param c_tag:
        :return:
        """

        self._logger.info("Add VLAN(s) {} configuration started".format(vlan_range))

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
            iface_action = self._get_iface_actions(config_session)
            vlan_actions = self._get_vlan_actions(config_session)
            config_session.send_command('buffer-delete all')
            port_name = iface_action.get_port_name(port_name)
            vlan_actions.create_vlan(vlan_range)

            current_config = iface_action.get_current_interface_config(port_name)

            iface_action.enter_iface_config_mode(port_name)
            iface_action.clean_interface_switchport_config(current_config)
            vlan_actions.set_vlan_to_interface(vlan_range, port_mode, port_name, qnq, c_tag)
            verify_error_map = {'(not.*|un)successful': 'Verify command was not successful'}
            config_session.send_command('verify', error_map=verify_error_map)
            commit_error_map = {'(not.*|un)successful': 'Commit command was not successful'}
            config_session.send_command('commit', error_map=commit_error_map)
            current_config = iface_action.get_current_interface_config(port_name)
            if not vlan_actions.verify_interface_configured(vlan_range, current_config):
                raise Exception(self.__class__.__name__, "[FAIL] VLAN(s) {} configuration failed".format(vlan_range))

        self._logger.info("VLAN(s) {} configuration completed successfully".format(vlan_range))
        return "[ OK ] VLAN(s) {} configuration completed successfully".format(vlan_range)


class CiscoNXOSExtRemoveVlanFlow(CiscoNXOSRemoveVlanFlow):
    def __init__(self, cli_handler, logger):
        super(CiscoNXOSExtRemoveVlanFlow, self).__init__(cli_handler, logger)

    def execute_flow(self, vlan_range, port_name, port_mode, action_map=None, error_map=None):
        """ Remove configuration of VLANs on multiple ports or port-channels

        :param vlan_range: VLAN or VLAN range
        :param port_name: full port name
        :param port_mode: mode which will be configured on port. Possible Values are trunk and access
        :param action_map:
        :param error_map:
        :return:
        """

        self._logger.info("Remove Vlan {} configuration started".format(vlan_range))
        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
            iface_action = self._get_iface_actions(config_session)
            vlan_actions = self._get_vlan_actions(config_session)
            config_session.send_command('buffer-delete all')
            port_name = iface_action.get_port_name(port_name)

            current_config = iface_action.get_current_interface_config(port_name)

            iface_action.enter_iface_config_mode(port_name)
            iface_action.clean_interface_switchport_config(current_config)
            verify_error_map = {'(not.*|un)successful': 'Verify command was not successful'}
            config_session.send_command('verify', error_map=verify_error_map)
            commit_error_map = {'(not.*|un)successful': 'Commit command was not successful'}
            config_session.send_command('commit', error_map=commit_error_map)
            current_config = iface_action.get_current_interface_config(port_name)
            if vlan_actions.verify_interface_configured(vlan_range, current_config):
                raise Exception(self.__class__.__name__, "[FAIL] VLAN(s) {} removing failed".format(vlan_range))

        self._logger.info("VLAN(s) {} removing completed successfully".format(vlan_range))
        return "[ OK ] VLAN(s) {} removing completed successfully".format(vlan_range)
