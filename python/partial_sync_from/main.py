"""
                            CISCO SAMPLE CODE LICENSE
                                  Version 1.0
                Copyright (c) 2020 Cisco and/or its affiliates

   These terms govern this Cisco example or demo source code and its
   associated documentation (together, the "Sample Code"). By downloading,
   copying, modifying, compiling, or redistributing the Sample Code, you
   accept and agree to be bound by the following terms and conditions (the
   "License"). If you are accepting the License on behalf of an entity, you
   represent that you have the authority to do so (either you or the entity,
   "you"). Sample Code is not supported by Cisco TAC and is not tested for
   quality or performance. This is your only license to the Sample Code and
   all rights not expressly granted are reserved.
"""
# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service
from ncs.dp import Action


# ---------------
# ACTIONS EXAMPLE
# ---------------
class PartialSyncFrom(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        self.log.info('action name: ', name)
        self.log.info('action input.device: ', input.device)
        self.log.info('action input.xpath: ', input.xpath)
        with ncs.maapi.Maapi() as m:
            with ncs.maapi.Session(m, "admin", 'python', groups=['ncsadmin']):
                with m.start_write_trans() as trans_write:
                    root = ncs.maagic.get_root(trans_write)
                    self.log.info("Executing a partial sync from device {}...".format(input.device))
                    input_params = root.devices.partial_sync_from.get_input()
                    input_params.path = ["/devices/device[name='" + input.device + "']/config/" + input.xpath]
                    partial_sync_output = root.devices.partial_sync_from(input_params)
                    self.log.info(
                        "Output of partial sync-from: {}".format(partial_sync_output.sync_result[input.device].result))

        output.result = partial_sync_output.sync_result[input.device].result


# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        # The application class sets up logging for us. It is accessible
        # through 'self.log' and is a ncs.log.Log instance.
        self.log.info('Main RUNNING')

        # When using actions, this is how we register them:
        #
        self.register_action('partial-sync-from-action', PartialSyncFrom)

        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
