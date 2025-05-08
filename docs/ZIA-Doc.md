
<h2>About the connector</h2>

<p>Zscaler Internet Access (ZIA) connector enables automated operations such as Get Firewall Filtering Rules, Get Specific Firewall Filtering Rule, Get Time Windows, Get Network Applications, Get Network Services, Get Network Services Groups, Get Network Applications Groups, and Execute an API Request.</p>

<p>This document provides information about the Zscaler Internet Access connector, which facilitates automated interactions, with a Zscaler Internet Access server using FortiSOAR&trade; playbooks. Add the Zscaler Internet Access connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Zscaler Internet Access.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-zscaler-internet-access</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of Zscaler Internet Access server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Zscaler Internet Access server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Zscaler Internet Access</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Server host URL for the Zscaler API.</td></tr>
<tr><td>Client ID</td><td>Specify the Client ID for Zscaler OneAPI authentication.</td></tr>
<tr><td>Client Secret</td><td>Specify the Client Secret for Zscaler OneAPI authentication.</td></tr>
<tr><td>ZIdentity's Auth Token Endpoint</td><td>Specify the ZIdentity auth token endpoint. This endpoint generates the Bearer token. Note: Here, <Vanity Domain> refers to the domain name used by your organization.</td></tr>
<tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified. <br/>By default, this option is selected, i.e., set to <code>true</code>.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>You can use the following automated operations in playbooks and also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Firewall Filtering Rules</td><td>Gets all configured rules within the Zscaler firewall filtering policy.</td><td>get_firewall_filtering_rules <br/>Utilities</td></tr>
<tr><td>Get Specific Firewall Filtering Rule</td><td>Get detailed information about a specific firewall filtering policy rule in the Zscaler platform, identified by its unique rule ID.</td><td>get_specific_firewall_filtering_rule <br/>Utilities</td></tr>
<tr><td>Get Time Windows</td><td>Gets a list of time intervals used for by the Firewall policy or the URL Filtering policy.</td><td>get_time_windows <br/>Utilities</td></tr>
<tr><td>Get Network Applications</td><td>Gets a list of all predefined network applications From Zscaler platform, including their associated categories, protocols, and other relevant metadata used for policy configuration and traffic filtering.</td><td>get_network_applications <br/>Utilities</td></tr>
<tr><td>Get Network Services</td><td>Gets a list of all network services. The search parameters find matching values within the name or description attributes.</td><td>get_network_services <br/>Utilities</td></tr>
<tr><td>Get Network Services Groups</td><td>Gets a list of all network service groups configured in the Zscaler platform.</td><td>get_network_service_groups <br/>Utilities</td></tr>
<tr><td>Get Network Applications Groups</td><td>Gets a list of all network application groups defined within the Zscaler platform.</td><td>get_network_application_groups <br/>Utilities</td></tr>
<tr><td>Execute an API Request</td><td>Execute any Zscaler OpenAI using the specified API method, endpoint, and payload as input parameters.</td><td>execute_api_request <br/>Utilities</td></tr>
</tbody></table>

<h3>operation: Get Firewall Filtering Rules</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "name": "",
    "order": "",
    "rank": "",
    "locations": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "locationGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "departments": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "groups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "users": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "timeWindows": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "workloadGroups": [
        {
            "id": "",
            "name": "",
            "description": "",
            "expressionJson": {
                "expressionContainers": [
                    {
                        "tagType": "",
                        "operator": "",
                        "tagContainer": {
                            "tags": [
                                {
                                    "key": "",
                                    "value": ""
                                }
                            ],
                            "operator": ""
                        }
                    }
                ]
            },
            "expression": "",
            "lastModifiedTime": "",
            "lastModifiedBy": {
                "id": "",
                "name": "",
                "externalId": "",
                "extensions": {
                    "additionalProp1": "",
                    "additionalProp2": "",
                    "additionalProp3": ""
                }
            }
        }
    ],
    "action": "",
    "state": "",
    "description": "",
    "lastModifiedTime": "",
    "lastModifiedBy": {
        "id": "",
        "name": "",
        "externalId": "",
        "extensions": {
            "additionalProp1": "",
            "additionalProp2": "",
            "additionalProp3": ""
        }
    },
    "srcIps": [],
    "srcIpGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "srcIpv6Groups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "sourceCountries": [],
    "excludeSrcCountries": "",
    "destAddresses": [],
    "destIpCategories": [],
    "destCountries": [],
    "destIpGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "destIpv6Groups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "nwServices": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "nwServiceGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "nwApplications": [],
    "nwApplicationGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "appServices": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "appServiceGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "devices": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "deviceGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "deviceTrustLevels": [],
    "labels": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "defaultRule": "",
    "predefined": ""
}</pre>

<h3>operation: Get Specific Firewall Filtering Rule</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ID</td><td>Specify the ID of the firewall filtering rule for which you want to retrieve the details.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "name": "",
    "order": "",
    "rank": "",
    "locations": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "locationGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "departments": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "groups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "users": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "timeWindows": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "workloadGroups": [
        {
            "id": "",
            "name": "",
            "description": "",
            "expressionJson": {
                "expressionContainers": [
                    {
                        "tagType": "",
                        "operator": "",
                        "tagContainer": {
                            "tags": [
                                {
                                    "key": "",
                                    "value": ""
                                }
                            ],
                            "operator": ""
                        }
                    }
                ]
            },
            "expression": "",
            "lastModifiedTime": "",
            "lastModifiedBy": {
                "id": "",
                "name": "",
                "externalId": "",
                "extensions": {
                    "additionalProp1": "",
                    "additionalProp2": "",
                    "additionalProp3": ""
                }
            }
        }
    ],
    "action": "",
    "state": "",
    "description": "",
    "lastModifiedTime": "",
    "lastModifiedBy": {
        "id": "",
        "name": "",
        "externalId": "",
        "extensions": {
            "additionalProp1": "",
            "additionalProp2": "",
            "additionalProp3": ""
        }
    },
    "srcIps": [],
    "srcIpGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "srcIpv6Groups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "sourceCountries": [],
    "excludeSrcCountries": true,
    "destAddresses": [],
    "destIpCategories": [],
    "destCountries": [],
    "destIpGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "destIpv6Groups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "nwServices": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "nwServiceGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "nwApplications": [],
    "nwApplicationGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "appServices": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "appServiceGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "devices": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "deviceGroups": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "deviceTrustLevels": [],
    "labels": [
        {
            "id": "",
            "name": "",
            "externalId": "",
            "extensions": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": ""
            }
        }
    ],
    "defaultRule": "",
    "predefined": ""
}</pre>

<h3>operation: Get Time Windows</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "name": "",
    "startTime": "",
    "endTime": "",
    "dayOfWeek": []
}</pre>

<h3>operation: Get Network Applications</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "name": "",
    "networkApplications": [],
    "description": "string"
}</pre>

<h3>operation: Get Network Services</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter String</td><td>(Optional) Specify the filter string used to filter services based on their name or description attributes.</td></tr>
<tr><td>Protocol</td><td>(Optional) Select the protocol by which to filter network services.</td></tr>
<tr><td>Language</td><td>(Optional) Specify one of the supported locales (i.e., en-US, dead, Estes, friar, AJP, which), the network service's description is localized into the requested language.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "name": "",
    "tag": "",
    "srcTcpPorts": [
        {
            "start": "",
            "end": ""
        }
    ],
    "destTcpPorts": [
        {
            "start": "",
            "end": ""
        }
    ],
    "srcUdpPorts": [
        {
            "start": "",
            "end": ""
        }
    ],
    "destUdpPorts": [
        {
            "start": "",
            "end": ""
        }
    ],
    "type": "",
    "description": "",
    "isNameL10nTag": ""
}</pre>

<h3>operation: Get Network Services Groups</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "name": "",
    "services": [
        {
            "id": "",
            "name": "",
            "tag": "",
            "srcTcpPorts": [
                {
                    "start": "",
                    "end": ""
                }
            ],
            "destTcpPorts": [
                {
                    "start": "",
                    "end": ""
                }
            ],
            "srcUdpPorts": [
                {
                    "start": "",
                    "end": ""
                }
            ],
            "destUdpPorts": [
                {
                    "start": "",
                    "end": ""
                }
            ],
            "type": "",
            "description": "",
            "isNameL10nTag": ""
        }
    ],
    "description": ""
}</pre>

<h3>operation: Get Network Applications Groups</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "name": "",
    "networkApplications": [],
    "description": ""
}</pre>

<h3>operation: Execute an API Request</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Endpoint</td><td>Specify the REST API endpoint for the action to perform. Note: Do not include the host URL in the endpoint. Ex /via/API/v1/firewallFilteringRules or /via/API/v1/networkApplications.</td></tr>
<tr><td>Method</td><td>The HTTP Method to use</td></tr>
<tr><td>query_params</td><td>(Optional) Specify the Rest API query parameters object in JSON format.</td></tr>
<tr><td>Request Body/Payload</td><td>(Optional) The payload needed for the call. Use empty brackets if there is no payload.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - Zscaler Internet Access - 1.0.0</code> playbook collection comes bundled with the Zscaler Internet Access connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Zscaler Internet Access connector.</p>

<ul>
<li>Execute an API Request</li>
<li>Get Firewall Filtering Rules</li>
<li>Get Network Applications</li>
<li>Get Network Applications Groups</li>
<li>Get Network Services</li>
<li>Get Network Services Groups</li>
<li>Get Specific Firewall Filtering Rule</li>
<li>Get Time Windows</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
