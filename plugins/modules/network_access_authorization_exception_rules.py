#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_authorization_exception_rules
short_description: Resource module for Network Access Authorization Exception Rules
description:
- Manage operations create, update and delete of the resource Network Access Authorization Exception Rules.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Rule id.
    type: str
  policyId:
    description: PolicyId path parameter. Policy id.
    type: str
  profile:
    description: The authorization profile/s.
    elements: str
    type: list
  rule:
    description: Common attributes in rule authentication/authorization.
    suboptions:
      condition:
        description: Network Access Authorization Exception Rules's condition.
        suboptions:
          attributeId:
            description: Dictionary attribute id (Optional), used for additional verification.
            type: str
          attributeName:
            description: Dictionary attribute name.
            type: str
          attributeValue:
            description: <ul><li>Attribute value for condition</li> <li>Value type is
              specified in dictionary object</li> <li>if multiple values allowed is
              specified in dictionary object</li></ul>.
            type: str
          children:
            description: In case type is andBlock or orBlock addtional conditions will
              be aggregated under this logical (OR/AND) condition.
            suboptions:
              conditionType:
                description: <ul><li>Inidicates whether the record is the condition
                  itself(data) or a logical(or,and) aggregation</li> <li>Data type enum(reference,single)
                  indicates than "conditonId" OR "ConditionAttrs" fields should contain
                  condition data but not both</li> <li>Logical aggreation(and,or) enum
                  indicates that additional conditions are present under the children
                  field</li></ul>.
                type: str
              isNegate:
                description: Indicates whereas this condition is in negate mode.
                type: bool
            type: list
          conditionType:
            description: <ul><li>Inidicates whether the record is the condition itself(data)
              or a logical(or,and) aggregation</li> <li>Data type enum(reference,single)
              indicates than "conditonId" OR "ConditionAttrs" fields should contain
              condition data but not both</li> <li>Logical aggreation(and,or) enum indicates
              that additional conditions are present under the children field</li></ul>.
            type: str
          datesRange:
            description: <p>Defines for which date/s TimeAndDate condition will be matched
              or NOT matched if used in exceptionDates prooperty<br> Options are - Date
              range, for specific date, the same date should be used for start/end date
              <br> Default - no specific dates<br> In order to reset the dates to have
              no specific dates Date format - yyyy-mm-dd (MM = month, dd = day, yyyy
              = year)</p>.
            suboptions:
              endDate:
                description: Network Access Authorization Exception Rules's endDate.
                type: str
              startDate:
                description: Network Access Authorization Exception Rules's startDate.
                type: str
            type: dict
          datesRangeException:
            description: <p>Defines for which date/s TimeAndDate condition will be matched
              or NOT matched if used in exceptionDates prooperty<br> Options are - Date
              range, for specific date, the same date should be used for start/end date
              <br> Default - no specific dates<br> In order to reset the dates to have
              no specific dates Date format - yyyy-mm-dd (MM = month, dd = day, yyyy
              = year)</p>.
            suboptions:
              endDate:
                description: Network Access Authorization Exception Rules's endDate.
                type: str
              startDate:
                description: Network Access Authorization Exception Rules's startDate.
                type: str
            type: dict
          description:
            description: Condition description.
            type: str
          dictionaryName:
            description: Dictionary name.
            type: str
          dictionaryValue:
            description: Dictionary value.
            type: str
          hoursRange:
            description: <p>Defines for which hours a TimeAndDate condition will be
              matched or not matched if used in exceptionHours property<br> Time foramt
              - hh mm ( h = hour , mm = minutes ) <br> Default - All Day </p>.
            suboptions:
              endTime:
                description: Network Access Authorization Exception Rules's endTime.
                type: str
              startTime:
                description: Network Access Authorization Exception Rules's startTime.
                type: str
            type: dict
          hoursRangeException:
            description: <p>Defines for which hours a TimeAndDate condition will be
              matched or not matched if used in exceptionHours property<br> Time foramt
              - hh mm ( h = hour , mm = minutes ) <br> Default - All Day </p>.
            suboptions:
              endTime:
                description: Network Access Authorization Exception Rules's endTime.
                type: str
              startTime:
                description: Network Access Authorization Exception Rules's startTime.
                type: str
            type: dict
          id:
            description: Network Access Authorization Exception Rules's id.
            type: str
          isNegate:
            description: Indicates whereas this condition is in negate mode.
            type: bool
          name:
            description: Condition name.
            type: str
          operator:
            description: Equality operator.
            type: str
          weekDays:
            description: <p>Defines for which days this condition will be matched<br>
              Days format - Arrays of WeekDay enums <br> Default - List of All week
              days</p>.
            elements: str
            type: list
          weekDaysException:
            description: <p>Defines for which days this condition will NOT be matched<br>
              Days format - Arrays of WeekDay enums <br> Default - Not enabled</p>.
            elements: str
            type: list
        type: dict
      default:
        description: Indicates if this rule is the default one.
        type: bool
      description:
        description: The description of the rule.
        type: str
      hitCounts:
        description: The amount of times the rule was matched.
        type: int
      id:
        description: The identifier of the rule.
        type: str
      name:
        description: Rule name, Valid characters are alphanumerics, underscore, hyphen,
          space, period, parentheses.
        type: str
      rank:
        description: The rank(priority) in relation to other rules. Lower rank is higher
          priority.
        type: int
      state:
        description: The state that the rule is in. A disabled rule cannot be matched.
        type: str
    type: dict
  securityGroup:
    description: Security group used in authorization policies.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_authorization_exception_rules
# Reference by Internet resource
- name: Network Access Authorization Exception Rules reference
  description: Complete reference of the Network Access Authorization Exception Rules object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_access_authorization_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    profile:
    - string
    rule:
      condition:
        attributeId: string
        attributeName: string
        attributeValue: string
        children:
        - conditionType: string
          isNegate: true
        conditionType: string
        datesRange:
          endDate: string
          startDate: string
        datesRangeException:
          endDate: string
          startDate: string
        description: string
        dictionaryName: string
        dictionaryValue: string
        hoursRange:
          endTime: string
          startTime: string
        hoursRangeException:
          endTime: string
          startTime: string
        id: string
        isNegate: true
        name: string
        operator: string
        weekDays:
        - string
        weekDaysException:
        - string
      default: true
      description: string
      hitCounts: 0
      id: string
      name: string
      rank: 0
      state: string
    securityGroup: string

- name: Update by id
  cisco.ise.network_access_authorization_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    id: string
    policyId: string
    profile:
    - string
    rule:
      condition:
        attributeId: string
        attributeName: string
        attributeValue: string
        children:
        - conditionType: string
          isNegate: true
        conditionType: string
        datesRange:
          endDate: string
          startDate: string
        datesRangeException:
          endDate: string
          startDate: string
        description: string
        dictionaryName: string
        dictionaryValue: string
        hoursRange:
          endTime: string
          startTime: string
        hoursRangeException:
          endTime: string
          startTime: string
        id: string
        isNegate: true
        name: string
        operator: string
        weekDays:
        - string
        weekDaysException:
        - string
      default: true
      description: string
      hitCounts: 0
      id: string
      name: string
      rank: 0
      state: string
    securityGroup: string

- name: Delete by id
  cisco.ise.network_access_authorization_exception_rules:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
    policyId: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "rule": {
        "id": "string",
        "name": "string",
        "description": "string",
        "hitCounts": 0,
        "rank": 0,
        "state": "string",
        "default": true,
        "condition": {
          "conditionType": "string",
          "isNegate": true,
          "name": "string",
          "id": "string",
          "description": "string",
          "dictionaryName": "string",
          "attributeName": "string",
          "attributeId": "string",
          "operator": "string",
          "dictionaryValue": "string",
          "attributeValue": "string",
          "children": [
            {
              "conditionType": "string",
              "isNegate": true
            }
          ],
          "hoursRange": {
            "startTime": "string",
            "endTime": "string"
          },
          "hoursRangeException": {
            "startTime": "string",
            "endTime": "string"
          },
          "weekDays": [
            "string"
          ],
          "weekDaysException": [
            "string"
          ],
          "datesRange": {
            "startDate": "string",
            "endDate": "string"
          },
          "datesRangeException": {
            "startDate": "string",
            "endDate": "string"
          }
        }
      },
      "profile": [
        "string"
      ],
      "securityGroup": "string"
    }
"""
