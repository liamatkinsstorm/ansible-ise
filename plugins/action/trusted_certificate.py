from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.ise.plugins.module_utils.ise import (
    ISESDK,
    ise_argument_spec,
    ise_compare_equality,
    get_dict_result,
)
from ansible_collections.cisco.ise.plugins.module_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    name=dict(type="str"),
    status=dict(type="str"),
    description=dict(type="str"),
    enableOCSPValidation=dict(type="bool"),
    selectedOCSPService=dict(type="str"),
    rejectIfNoStatusFromOCSP=dict(type="bool"),
    rejectIfUnreachableFromOCSP=dict(type="bool"),
    downloadCRL=dict(type="bool"),
    crlDistributionUrl=dict(type="str"),
    automaticCRLUpdate=dict(type="bool"),
    automaticCRLUpdatePeriod=dict(type="int"),
    automaticCRLUpdateUnits=dict(type="str"),
    nonAutomaticCRLUpdatePeriod=dict(type="int"),
    nonAutomaticCRLUpdateUnits=dict(type="str"),
    crlDownloadFailureRetries=dict(type="int"),
    crlDownloadFailureRetriesUnits=dict(type="str"),
    enableServerIdentityCheck=dict(type="bool"),
    authenticateBeforeCRLReceived=dict(type="bool"),
    ignoreCRLExpiration=dict(type="bool"),
    trustForIseAuth=dict(type="bool"),
    trustForClientAuth=dict(type="bool"),
    trustForCiscoServicesAuth=dict(type="bool"),
    trustForCertificateBasedAdminAuth=dict(type="bool"),
    id=dict(type="str"),
))

required_if = [
    ("state", "present", ["id", "name"], True),
    ("state", "absent", ["id", "name"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class TrustedCertificate(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            name=params.get("name"),
            status=params.get("status"),
            description=params.get("description"),
            enable_ocs_p_validation=params.get("enableOCSPValidation"),
            selected_ocs_p_service=params.get("selectedOCSPService"),
            reject_if_no_status_from_ocs_p=params.get("rejectIfNoStatusFromOCSP"),
            reject_if_unreachable_from_ocs_p=params.get("rejectIfUnreachableFromOCSP"),
            download_crl=params.get("downloadCRL"),
            crl_distribution_url=params.get("crlDistributionUrl"),
            automatic_crl_update=params.get("automaticCRLUpdate"),
            automatic_crl_update_period=params.get("automaticCRLUpdatePeriod"),
            automatic_crl_update_units=params.get("automaticCRLUpdateUnits"),
            non_automatic_crl_update_period=params.get("nonAutomaticCRLUpdatePeriod"),
            non_automatic_crl_update_units=params.get("nonAutomaticCRLUpdateUnits"),
            crl_download_failure_retries=params.get("crlDownloadFailureRetries"),
            crl_download_failure_retries_units=params.get("crlDownloadFailureRetriesUnits"),
            enable_server_identity_check=params.get("enableServerIdentityCheck"),
            authenticate_before_crl_received=params.get("authenticateBeforeCRLReceived"),
            ignore_crl_expiration=params.get("ignoreCRLExpiration"),
            trust_for_ise_auth=params.get("trustForIseAuth"),
            trust_for_client_auth=params.get("trustForClientAuth"),
            trust_for_cisco_services_auth=params.get("trustForCiscoServicesAuth"),
            trust_for_certificate_based_admin_auth=params.get("trustForCertificateBasedAdminAuth"),
            id=params.get("id"),
        )

    def get_object_by_name(self, name):
        try:
            result = self.ise.exec(
                family="certificates",
                function="get_all_trusted_certificates",
                params={"filter": "name.EQ.{0}".format(name)}
            ).response
            result = get_dict_result(result, 'name', name)
        except Exception as e:
            result = None
        return result

    def get_object_by_id(self, id):
        try:
            result = self.ise.exec(
                family="certificates",
                function="get_trusted_certificate_by_id",
                params={"id": id}
            ).response.get('response', {})
        except Exception as e:
            result = None
        return result

    def exists(self):
        prev_obj = None
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("id")
        name = self.new_object.get("name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters("The 'id' and 'name' params don't refer to the same object")
            if _id:
                prev_obj = self.get_object_by_id(_id)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("name", "name"),
            ("status", "status"),
            ("description", "description"),
            ("enableOCSPValidation", "enable_ocs_p_validation"),
            ("selectedOCSPService", "selected_ocs_p_service"),
            ("rejectIfNoStatusFromOCSP", "reject_if_no_status_from_ocs_p"),
            ("rejectIfUnreachableFromOCSP", "reject_if_unreachable_from_ocs_p"),
            ("downloadCRL", "download_crl"),
            ("crlDistributionUrl", "crl_distribution_url"),
            ("automaticCRLUpdate", "automatic_crl_update"),
            ("automaticCRLUpdatePeriod", "automatic_crl_update_period"),
            ("automaticCRLUpdateUnits", "automatic_crl_update_units"),
            ("nonAutomaticCRLUpdatePeriod", "non_automatic_crl_update_period"),
            ("nonAutomaticCRLUpdateUnits", "non_automatic_crl_update_units"),
            ("crlDownloadFailureRetries", "crl_download_failure_retries"),
            ("crlDownloadFailureRetriesUnits", "crl_download_failure_retries_units"),
            ("enableServerIdentityCheck", "enable_server_identity_check"),
            ("authenticateBeforeCRLReceived", "authenticate_before_crl_received"),
            ("ignoreCRLExpiration", "ignore_crl_expiration"),
            ("trustForIseAuth", "trust_for_ise_auth"),
            ("trustForClientAuth", "trust_for_client_auth"),
            ("trustForCiscoServicesAuth", "trust_for_cisco_services_auth"),
            ("trustForCertificateBasedAdminAuth", "trust_for_certificate_based_admin_auth"),
            ("id", "id"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not ise_compare_equality(current_obj.get(ise_param),
                                            requested_obj.get(ansible_param))
                   for (ise_param, ansible_param) in obj_params)

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if not id:
            id_ = self.get_object_by_name(name).get("id")
            self.new_object.update(dict(id=id_))
        result = self.ise.exec(
            family="certificates",
            function="update_trusted_certificate",
            params=self.new_object
        ).response
        return result

    def delete(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if not id:
            id_ = self.get_object_by_name(name).get("id")
            self.new_object.update(dict(id=id_))
        result = self.ise.exec(
            family="certificates",
            function="delete_trusted_certificate_by_id",
            params=self.new_object
        ).response
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = True
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        ise = ISESDK(self._task.args)
        obj = TrustedCertificate(self._task.args, ise)

        state = self._task.args.get("state")

        response = None
        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    response = obj.update()
                    ise.object_updated()
                else:
                    response = prev_obj
                    ise.object_already_present()
            else:
                ise.fail_json("Object does not exists, plugin only has update")
        elif state == "absent":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                response = obj.delete()
                ise.object_deleted()
            else:
                ise.object_already_absent()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
