# Copyright 2018 AT&T Corp
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from airship_tempest_plugin.tests.api.shipyard.rbac import rbac_base

from patrole_tempest_plugin import rbac_rule_validation

from tempest.lib import decorators
from tempest.lib import exceptions


class AirflowMonitoringRbacTest(rbac_base.BaseShipyardRbacTest):

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:list_workflows"])
    @decorators.idempotent_id('fc75a269-04cb-4a8d-a627-907f72081b8a')
    def test_list_workflows(self):
        with self.rbac_utils.override_role(self):
            self.shipyard_airflow_monitoring_client.list_workflows()

    @rbac_rule_validation.action(
        service="shipyard",
        rules=["workflow_orchestrator:get_workflow"])
    @decorators.idempotent_id('1679c5fa-571a-4af8-8f14-ca0c0a49761b')
    def test_get_workflow(self):
        with self.rbac_utils.override_role(self):
            # As this is a RBAC test, we only care about whether the role has
            # permission or not. Role permission is checked prior to validating
            # the post body, therefore we will ignore a BadRequest exception
            try:
                self.shipyard_airflow_monitoring_client.get_workflow()
            except exceptions.BadRequest:
                pass
