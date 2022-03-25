#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_standalone_to_primary
short_description: Resource module for Node Standalone To Primary
description:
- Manage operation create of the resource Node Standalone To Primary.
- This API promotes the standalone node on which the API is invoked to the primary Policy Administration node (PAN).
version_added: '2.1.0'
extends_documentation_fragment:
  - cisco.ise.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk >= 2.0.1
- python >= 3.5
notes:
  - SDK Method used are
    node_deployment.NodeDeployment.make_primary,

  - Paths used are
    post /api/v1/deployment/primary,

"""

EXAMPLES = r"""
- name: Create
  cisco.ise.node_standalone_to_primary:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "success": {
        "message": "string"
      },
      "version": "string"
    }
"""
