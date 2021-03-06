# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_footprint.generated._client_factory import cf_profile
    footprint_profile = CliCommandType(
        operations_tmpl='azext_footprint.vendored_sdks.footprint.operations._profile_operations#ProfileOperations.{}',
        client_factory=cf_profile)
    with self.command_group('footprint profile', footprint_profile, client_factory=cf_profile,
                            is_experimental=True) as g:
        g.custom_command('list', 'footprint_profile_list')
        g.custom_show_command('show', 'footprint_profile_show')
        g.custom_command('create', 'footprint_profile_create')
        g.custom_command('update', 'footprint_profile_update')
        g.custom_command('delete', 'footprint_profile_delete')

    from azext_footprint.generated._client_factory import cf_measurement_endpoint
    footprint_measurement_endpoint = CliCommandType(
        operations_tmpl='azext_footprint.vendored_sdks.footprint.operations._measurement_endpoint_operations#Measuremen'
        'tEndpointOperations.{}',
        client_factory=cf_measurement_endpoint)
    with self.command_group('footprint measurement-endpoint', footprint_measurement_endpoint,
                            client_factory=cf_measurement_endpoint, is_experimental=True) as g:
        g.custom_command('list', 'footprint_measurement_endpoint_list')
        g.custom_show_command('show', 'footprint_measurement_endpoint_show')
        g.custom_command('create', 'footprint_measurement_endpoint_create')
        g.custom_command('update', 'footprint_measurement_endpoint_update')
        g.custom_command('delete', 'footprint_measurement_endpoint_delete')

    from azext_footprint.generated._client_factory import cf_measurement_endpoint_condition
    footprint_measurement_endpoint_condition = CliCommandType(
        operations_tmpl='azext_footprint.vendored_sdks.footprint.operations._measurement_endpoint_condition_operations#'
        'MeasurementEndpointConditionOperations.{}',
        client_factory=cf_measurement_endpoint_condition)
    with self.command_group('footprint measurement-endpoint-condition', footprint_measurement_endpoint_condition,
                            client_factory=cf_measurement_endpoint_condition, is_experimental=True) as g:
        g.custom_command('list', 'footprint_measurement_endpoint_condition_list')
        g.custom_show_command('show', 'footprint_measurement_endpoint_condition_show')
        g.custom_command('create', 'footprint_measurement_endpoint_condition_create')
        g.custom_command('update', 'footprint_measurement_endpoint_condition_update')
        g.custom_command('delete', 'footprint_measurement_endpoint_condition_delete')

    from azext_footprint.generated._client_factory import cf_experiment
    footprint_experiment = CliCommandType(
        operations_tmpl='azext_footprint.vendored_sdks.footprint.operations._experiment_operations#ExperimentOperations'
        '.{}',
        client_factory=cf_experiment)
    with self.command_group('footprint experiment', footprint_experiment, client_factory=cf_experiment,
                            is_experimental=True) as g:
        g.custom_command('list', 'footprint_experiment_list')
        g.custom_show_command('show', 'footprint_experiment_show')
        g.custom_command('create', 'footprint_experiment_create')
        g.custom_command('update', 'footprint_experiment_update')
        g.custom_command('delete', 'footprint_experiment_delete')
