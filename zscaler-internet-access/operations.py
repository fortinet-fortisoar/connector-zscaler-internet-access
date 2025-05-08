"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

from .zscaler_authorizations import ZscalerAuth


def get_firewall_filtering_rules(config, connector_info, params):
    endpoint = "/zia/api/v1/firewallFilteringRules"
    zs_one_api = ZscalerAuth(config)
    return zs_one_api.make_api_call(config, connector_info, endpoint=endpoint)


def get_specific_firewall_filtering_rule(config, connector_info, params):
    endpoint = f"/zia/api/v1/firewallFilteringRules/{params.get('id')}"
    zs_one_api = ZscalerAuth(config)
    return zs_one_api.make_api_call(config, connector_info, endpoint=endpoint)


def get_time_windows(config, connector_info, params):
    zs_one_api = ZscalerAuth(config)
    return zs_one_api.make_api_call(config, connector_info, endpoint='/zia/api/v1/v1/timeWindows')


def get_network_applications(config, connector_info, params):
    zs_one_api = ZscalerAuth(config)
    return zs_one_api.make_api_call(config, connector_info, endpoint='/zia/api/v1/networkApplications')


def get_network_services(config, connector_info, params):
    zs_one_api = ZscalerAuth(config)
    return zs_one_api.make_api_call(config, connector_info, endpoint='/zia/api/v1/networkServices',params=params)


def get_network_service_groups(config, connector_info, params):
    zs_one_api = ZscalerAuth(config)
    return zs_one_api.make_api_call(config, connector_info, endpoint='/zia/api/v1/networkServiceGroups')


def get_network_application_groups(config, connector_info, params):
    zs_one_api = ZscalerAuth(config)
    return zs_one_api.make_api_call(config, connector_info, endpoint='/zia/api/v1/networkApplicationGroups')


def execute_api_request(config, connector_info, params):
    endpoint = params.get('endpoint')
    zs_one_api = ZscalerAuth(config)
    method = params.get('method')
    query_params = params.get('query_params')
    payload = params.get('payload')
    return zs_one_api.make_api_call(config, connector_info, endpoint=endpoint, method=method, params=query_params,
                                    data=payload)


operations_map = {
    'get_firewall_filtering_rules': get_firewall_filtering_rules,
    'get_specific_firewall_filtering_rule': get_specific_firewall_filtering_rule,
    'get_time_windows': get_time_windows,
    'get_network_applications': get_network_applications,
    'get_network_services': get_network_services,
    'get_network_service_groups': get_network_service_groups,
    'get_network_application_groups': get_network_application_groups,
    'execute_api_request': execute_api_request
}
