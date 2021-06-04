#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sponsor_portal
short_description: Resource module for Sponsor Portal
description:
- Manage operations create, update and delete of the resource Sponsor Portal.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  customizations:
    description: Sponsor Portal's customizations.
    suboptions:
      globalCustomizations:
        description: Sponsor Portal's globalCustomizations.
        suboptions:
          bannerImage:
            description: Sponsor Portal's bannerImage.
            suboptions:
              data:
                description: Sponsor Portal's data.
                type: str
            type: dict
          bannerTitle:
            description: Sponsor Portal's bannerTitle.
            type: str
          contactText:
            description: Sponsor Portal's contactText.
            type: str
          desktopLogoImage:
            description: Sponsor Portal's desktopLogoImage.
            suboptions:
              data:
                description: Sponsor Portal's data.
                type: str
            type: dict
          footerElement:
            description: Sponsor Portal's footerElement.
            type: str
          mobileLogoImage:
            description: Sponsor Portal's mobileLogoImage.
            suboptions:
              data:
                description: Sponsor Portal's data.
                type: str
            type: dict
        type: dict
      language:
        description: Sponsor Portal's language.
        suboptions:
          viewLanguage:
            description: Sponsor Portal's viewLanguage.
            type: str
        type: dict
      pageCustomizations:
        description: Sponsor Portal's pageCustomizations.
        suboptions:
          data:
            description: Sponsor Portal's data.
            suboptions:
              key:
                description: Sponsor Portal's key.
                type: str
              value:
                description: Sponsor Portal's value.
                type: str
            type: list
        type: dict
      portalTheme:
        description: Sponsor Portal's portalTheme.
        suboptions:
          id:
            description: Sponsor Portal's id.
            type: str
          name:
            description: Sponsor Portal's name.
            type: str
          themeData:
            description: Sponsor Portal's themeData.
            type: str
        type: dict
      portalTweakSettings:
        description: Sponsor Portal's portalTweakSettings.
        suboptions:
          bannerColor:
            description: Sponsor Portal's bannerColor.
            type: str
          bannerTextColor:
            description: Sponsor Portal's bannerTextColor.
            type: str
          pageBackgroundColor:
            description: Sponsor Portal's pageBackgroundColor.
            type: str
          pageLabelAndTextColor:
            description: Sponsor Portal's pageLabelAndTextColor.
            type: str
        type: dict
    type: dict
  description:
    description: Sponsor Portal's description.
    type: str
  id:
    description: Sponsor Portal's id.
    type: str
  name:
    description: Sponsor Portal's name.
    type: str
  portalTestUrl:
    description: Sponsor Portal's portalTestUrl.
    type: str
  portalType:
    description: Sponsor Portal's portalType.
    type: str
  settings:
    description: Sponsor Portal's settings.
    suboptions:
      aupSettings:
        description: Sponsor Portal's aupSettings.
        suboptions:
          displayFrequency:
            description: Sponsor Portal's displayFrequency.
            type: str
          includeAup:
            description: IncludeAup flag.
            type: bool
          requireAccessCode:
            description: RequireAccessCode flag.
            type: bool
          requireScrolling:
            description: RequireScrolling flag.
            type: bool
          skipAupForEmployees:
            description: SkipAupForEmployees flag.
            type: bool
          useDiffAupForEmployees:
            description: UseDiffAupForEmployees flag.
            type: bool
        type: dict
      loginPageSettings:
        description: Sponsor Portal's loginPageSettings.
        suboptions:
          allowAlternateGuestPortal:
            description: AllowAlternateGuestPortal flag.
            type: bool
          allowGuestToChangePassword:
            description: AllowGuestToChangePassword flag.
            type: bool
          allowGuestToCreateAccounts:
            description: AllowGuestToCreateAccounts flag.
            type: bool
          allowGuestToUseSocialAccounts:
            description: AllowGuestToUseSocialAccounts flag.
            type: bool
          allowShowGuestForm:
            description: AllowShowGuestForm flag.
            type: bool
          aupDisplay:
            description: Sponsor Portal's aupDisplay.
            type: str
          includeAup:
            description: IncludeAup flag.
            type: bool
          maxFailedAttemptsBeforeRateLimit:
            description: Sponsor Portal's maxFailedAttemptsBeforeRateLimit.
            type: int
          requireAccessCode:
            description: RequireAccessCode flag.
            type: bool
          requireAupAcceptance:
            description: RequireAupAcceptance flag.
            type: bool
          requireAupScrolling:
            description: RequireAupScrolling flag.
            type: bool
          socialConfigs:
            description: Sponsor Portal's socialConfigs.
            type: list
          timeBetweenLoginsDuringRateLimit:
            description: Sponsor Portal's timeBetweenLoginsDuringRateLimit.
            type: int
        type: dict
      portalSettings:
        description: Sponsor Portal's portalSettings.
        suboptions:
          allowedInterfaces:
            description: Sponsor Portal's allowedInterfaces.
            elements: str
            type: list
          alwaysUsedLanguage:
            description: Sponsor Portal's alwaysUsedLanguage.
            type: str
          authenticationMethod:
            description: Sponsor Portal's authenticationMethod.
            type: str
          availableSsids:
            description: Sponsor Portal's availableSsids.
            elements: str
            type: list
          certificateGroupTag:
            description: Sponsor Portal's certificateGroupTag.
            type: str
          displayLang:
            description: Sponsor Portal's displayLang.
            type: str
          fallbackLanguage:
            description: Sponsor Portal's fallbackLanguage.
            type: str
          fqdn:
            description: Sponsor Portal's fqdn.
            type: str
          httpsPort:
            description: Sponsor Portal's httpsPort.
            type: int
          idleTimeout:
            description: Sponsor Portal's idleTimeout.
            type: int
        type: dict
      postLoginBannerSettings:
        description: Sponsor Portal's postLoginBannerSettings.
        suboptions:
          includePostAccessBanner:
            description: IncludePostAccessBanner flag.
            type: bool
        type: dict
      sponsorChangePasswordSettings:
        description: Sponsor Portal's sponsorChangePasswordSettings.
        suboptions:
          allowSponsorToChangePwd:
            description: AllowSponsorToChangePwd flag.
            type: bool
        type: dict
      supportInfoSettings:
        description: Sponsor Portal's supportInfoSettings.
        suboptions:
          emptyFieldDisplay:
            description: Sponsor Portal's emptyFieldDisplay.
            type: str
          includeBrowserUserAgent:
            description: IncludeBrowserUserAgent flag.
            type: bool
          includeFailureCode:
            description: IncludeFailureCode flag.
            type: bool
          includeIpAddress:
            description: IncludeIpAddress flag.
            type: bool
          includeMacAddr:
            description: IncludeMacAddr flag.
            type: bool
          includePolicyServer:
            description: IncludePolicyServer flag.
            type: bool
          includeSupportInfoPage:
            description: IncludeSupportInfoPage flag.
            type: bool
        type: dict
    type: dict
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sponsor_portal
# Reference by Internet resource
- name: Sponsor Portal reference
  description: Complete reference of the Sponsor Portal object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sponsor_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        bannerTitle: Sponsor Portal
        contactText: Contact Support
        footerElement: ''
      language:
        viewLanguage: English
      pageCustomizations:
        data:
        - key: ui_date_picker_month_august
          value: QXVndXN0
        - key: ui_error_content_label
          value: RXJyb3I=
        - key: ui_notify_import_done_button
          value: RG9uZQ==
        - key: ui_create_accounts_content_label
          value: Q3JlYXRlIEFjY291bnRz
        - key: ui_notify_copy_me_label
          value: Q29weSBtZQ==
        - key: ui_print_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_contact_optional_content_1
          value: ''
        - key: ui_contact_optional_content_2
          value: ''
        - key: ui_one_click_guest_approved
          value: R3Vlc3QgKCR1aV9ndWVzdF91c2VybmFtZSQpIGhhcyBiZWVuIGFwcHJvdmVkLg==
        - key: ui_create_random_number_accounts_label
          value: TnVtYmVyIG9mIGFjY291bnRzOg==
        - key: ui_date_picker_month_may
          value: TWF5
        - key: ui_approve_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_login_aup_link
          value: VGVybXMgYW5kIENvbmRpdGlvbnM=
        - key: ui_one_click_guest_denied
          value: R3Vlc3QgKCR1aV9ndWVzdF91c2VybmFtZSQpIGhhcyBiZWVuIGRlbmllZC4=
        - key: ui_column_user_name_header
          value: VXNlcm5hbWU=
        - key: ui_invalid_password_policy_error
          value: SW52YWxpZCBQYXNzd29yZCBQb2xpY3ku
        - key: ui_account_state_label
          value: U3RhdGU6
        - key: ui_reset_password_send_summary_email_label
          value: U2VuZCBtZSBhIHN1bW1hcnkgb2YgcGFzc3dvcmQgcmVzZXQ=
        - key: ui_notices_action_import_label
          value: Q3JlYXRlIEltcG9ydCBBY2NvdW50cw==
        - key: ui_location_label
          value: TG9jYXRpb246
        - key: ui_email_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGVtYWlsZWQ6
        - key: ui_resend_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_field_company_name_error
          value: UGxlYXNlIGVudGVyIGEgdmFsaWQgY29tcGFueSBuYW1lLg==
        - key: ui_one_click_sponsor_no_privilege
          value: U3BvbnNvciBkaWQgbm90IGhhdmUgcHJpdmlsZWdlIHRvIGFwcHJvdmUvZGVueSBndWVzdHMu
        - key: ui_unit_wednesday
          value: V2VkbmVzZGF5
        - key: ui_contact_sessioninfo_title
          value: U2Vzc2lvbiBJbmZvcm1hdGlvbg==
        - key: ui_first_name_label
          value: Rmlyc3QgbmFtZTo=
        - key: ui_aup_accept_button
          value: QWNjZXB0
        - key: ui_create_random_accounts_batch_limit_label
          value: TWF4aW11bTogIA==
        - key: ui_unit_sunday
          value: U3VuZGF5
        - key: ui_sms_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHRleHRlZDo=
        - key: ui_one_click_login_submit
          value: U3VibWl0
        - key: ui_changepwd_values_match_error
          value: WW91IG11c3QgZW50ZXIgdGhlIHNhbWUgcGFzc3dvcmQgaW4gdGhlIE5ldyBQYXNzd29yZCBhbmQgQ29uZmlybSBQYXNzd29yZCB...
        - key: ui_error_optional_content_2
          value: ''
        - key: ui_error_optional_content_1
          value: ''
        - key: ui_login_page_title
          value: IFNwb25zb3IgUG9ydGFsIFNpZ24gT24=
        - key: ui_notices_column_action_name_header
          value: QWN0aW9uIE5hbWU=
        - key: ui_create_random_tab_label
          value: UmFuZG9t
        - key: ui_suspend_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHN1c3BlbmQgdGhpcyBhY2NvdW50Pw==
        - key: ui_changepwd_content_label
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_create_known_total_failure_message
          value: VW5hYmxlIHRvIGNyZWF0ZSBhY2NvdW50Lg==
        - key: ui_reinstate_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgcmVpbnN0YXRlZCBzdWNjZXNzZnVsbHku
        - key: ui_create_accounts_access_info_instruction_message
          value: ''
        - key: ui_changepwd_values_unique_error
          value: WW91IGNhbm5vdCBlbnRlciB0aGUgc2FtZSBwYXNzd29yZCBpbiB0aGUgQ3VycmVudCBQYXNzd29yZCBhbmQgTmV3IFBhc3N3b3J...
        - key: ui_deny_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGRlbnkgdGhpcyBhY2NvdW50Pw==
        - key: ui_ssid_label
          value: U1NJRDo=
        - key: ui_contact_instruction_message
          value: Q29udGFjdCBIZWxwIERlc2s=
        - key: ui_notify_email_label
          value: RW1haWw=
        - key: ui_time_label
          value: VGltZTo=
        - key: ui_create_accounts_access_info_from_date_label
          value: RnJvbSBEYXRlICh5eXl5LW1tLWRkKQ==
        - key: ui_contact_helpdesk_text
          value: TmVlZCBoZWxwPyBDb250YWN0IG91ciBIZWxwIERlc2sgYXQgKHh4eCkgeHh4LXh4eHgu
        - key: ui_notices_status_pending_label
          value: UGVuZGluZw==
        - key: ui_guest_location_label
          value: TG9jYXRpb246
        - key: ui_username_mismatch_policy_error
          value: VXNlcm5hbWUgZGlkIG5vdCBtYXRjaCBVc2VybmFtZSBQb2xpY3k=
        - key: ui_manage_accounts_filter_label
          value: YWNjb3VudHMgZm91bmQ=
        - key: ui_resend_account_send_summary_email_label
          value: U2VuZCBtZSBhIHN1bW1hcnk=
        - key: ui_menu_switch_desktop_button
          value: U3dpdGNoIHRvIGRlc2t0b3AgbW9kZQ==
        - key: ui_resend_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHJlc2VudDo=
        - key: ui_reset_password_cancel_button
          value: Q2FuY2Vs
        - key: ui_create_accounts_import_button
          value: SW1wb3J0
        - key: ui_sms_account_success_single_message
          value: QWNjb3VudCB0ZXh0ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_suspend_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHN1c3BlbmR...
        - key: ui_contact_link
          value: Q29udGFjdCBTdXBwb3J0
        - key: ui_notices_filter_label
          value: Tm90aWNlcyBmb3VuZA==
        - key: ui_contact_user_agent_label
          value: VXNlciBhZ2VudDo=
        - key: ui_reset_password_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHJlc2V0Og==
        - key: ui_create_known_success_single_message
          value: QWNjb3VudCBjcmVhdGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_delete_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbGV0ZSB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_extend_account_extend_by_label
          value: RXh0ZW5kIGJ5
        - key: ui_create_known_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_changepwd_page_title
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_create_random_instruction_message
          value: ''
        - key: ui_notices_status_success_label
          value: U3VjY2Vzcw==
        - key: ui_account_state_denied_state_label
          value: RGVuaWVk
        - key: ui_notices_edit_button
          value: RWRpdA==
        - key: ui_group_tag_label
          value: R3JvdXAgdGFnOg==
        - key: ui_date_picker_short_day_friday
          value: Rg==
        - key: ui_extend_account_total_failure_message
          value: VW5hYmxlIHRvIGV4dGVuZCBhY2NvdW50Lg==
        - key: ui_notices_column_end_time_header
          value: RW5k
        - key: ui_one_click_login_title
          value: QXBwcm92ZS9EZW55IEd1ZXN0
        - key: ui_account_details_content_label
          value: QWNjb3VudCBEZXRhaWxz
        - key: ui_print_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIG51bWJlciBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhIHByaW50IGpvYiB3aWxsIGJlIGNyZWF0ZWQ...
        - key: ui_create_random_total_failure_message
          value: VW5hYmxlIHRvIGNyZWF0ZSByYW5kb20gYWNjb3VudC4=
        - key: ui_manage_accounts_empty_error
          value: Tm8gZ3Vlc3QgYWNjb3VudHMgYXQgdGhpcyBtb21lbnQu
        - key: ui_create_random_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiByYW5kb20gYWNjb3VudHMgd2VyZSBwcm92aWRlZC4gUmFuZG9tIGFjY291bnRzIHd...
        - key: ui_create_accounts_aup_agreement_label
          value: QWdyZWUgdG8=
        - key: ui_use_mobile_number_as_username_label
          value: VXNlIE1vYmlsZSBudW1iZXIgYXMgdXNlcm5hbWU=
        - key: ui_date_picker_short_day_monday
          value: TQ==
        - key: ui_time_duration_label
          value: RHVyYXRpb246
        - key: ui_date_picker_month_february
          value: RmVicnVhcnk=
        - key: ui_resend_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlc2VuZCB0aGlzIGFjY291bnQ/
        - key: ui_notify_known_ok_button
          value: T2s=
        - key: ui_suspend_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHN1c3BlbmRlZDo=
        - key: ui_help_link
          value: SGVscA==
        - key: ui_one_click_login_username
          value: VXNlcm5hbWU6
        - key: ui_user_last_login_ipaddr_label
          value: RnJvbTo=
        - key: ui_create_accounts_batch_limit_label
          value: TWF4aW11bTo=
        - key: ui_date_picker_month_july
          value: SnVseQ==
        - key: ui_resend_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlc2VuZCB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_delete_notice_success_multi_message
          value: U2VsZWN0ZWQgbm90aWNlcyBkZWxldGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_sms_provider_label
          value: U01TIHByb3ZpZGVyOg==
        - key: ui_first_login_text
          value: Rmlyc3QgTG9naW4=
        - key: ui_login_username_label
          value: VXNlcm5hbWU6
        - key: ui_account_action_reset_password_button
          value: UmVzZXQgUGFzc3dvcmQ=
        - key: ui_create_accounts_access_info_from_time_label
          value: RnJvbSBUaW1l
        - key: ui_approve_accounts_empty_error
          value: Tm8gcGVuZGluZyBndWVzdCBhY2NvdW50cyBhdCB0aGlzIG1vbWVudC4=
        - key: ui_create_import_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_create_accounts_access_info_content_label
          value: QWNjZXNzIEluZm9ybWF0aW9u
        - key: ui_date_picker_month_june
          value: SnVuZQ==
        - key: ui_notices_status_inprogress_label
          value: SW4gUHJvZ3Jlc3M=
        - key: ui_email_account_success_single_message
          value: QWNjb3VudCBlbWFpbGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_approve_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGFwcHJvdmV...
        - key: ui_one_click_login_password
          value: UGFzc3dvcmQ6
        - key: ui_invalid_username_policy_error
          value: SW52YWxpZCBVc2VybmFtZSBQb2xpY3ku
        - key: ui_edit_accounts_guest_info_content_label
          value: R3Vlc3QgSW5mb3JtYXRpb24=
        - key: ui_delete_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_field_required_error
          value: VGhpcyBmaWVsZCBpcyByZXF1aXJlZC4=
        - key: ui_print_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgcHJpbnRlZCBzdWNjZXNzZnVsbHku
        - key: ui_field_date_mdy_error
          value: SW52YWxpZCBkYXRlIGZvcm1hdCAobW0vZGQveXl5eSku
        - key: ui_suspend_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHN1c3BlbmQgdGhlIHNlbGVjdGVkIGFjY291bnRzPw==
        - key: ui_column_first_name_header
          value: Rmlyc3QgTmFtZQ==
        - key: ui_notices_action_email_label
          value: RW1haWwgR3Vlc3Rz
        - key: ui_create_accounts_access_info_days_label
          value: RGF5cw==
        - key: ui_lastname_mismatch_policy_error
          value: TGFzdE5hbWUgZGlkIG5vdCBtYXRjaCBVc2VybmFtZSBQb2xpY3k=
        - key: ui_create_accounts_guest_type_instruction_message
          value: ''
        - key: ui_suspend_account_ok_button
          value: T2s=
        - key: ui_sms_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgdGV4dGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_expiration_date_label
          value: RXhwaXJhdGlvbiBkYXRlOg==
        - key: ui_changepwd_policy_error_message
          value: WW91ciBwYXNzd29yZCBkb2VzIG5vdCBtZWV0IHRoZSBwYXNzd29yZCBwb2xpY3kgcmVxdWlyZW1lbnRzLiBQbGVhc2UgY29udGF...
        - key: ui_approve_account_success_single_message
          value: QWNjb3VudCBhcHByb3ZlZCBzdWNjZXNzZnVsbHku
        - key: ui_edit_accounts_access_info_content_label
          value: QWNjZXNzIEluZm9ybWF0aW9u
        - key: ui_to_date_label
          value: VG8gZGF0ZSAoeXl5eS1tbS1kZCk6
        - key: ui_delete_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGRlbGV0ZWQ...
        - key: ui_end_of_day_label
          value: RW5kIG9mIGJ1c2luZXNzIGRheQ==
        - key: ui_column_phone_number_header
          value: TW9iaWxlIE51bWJlcg==
        - key: ui_deny_account_ok_button
          value: T0s=
        - key: ui_field_time_error
          value: SW52YWxpZCB0aW1lIGZvcm1hdCAoaGg6bW0pLg==
        - key: ui_resend_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_extend_account_maximum_label
          value: TWF4aW11bTog
        - key: ui_account_state_awaiting_login_state_label
          value: Q3JlYXRlZA==
        - key: ui_home_welcome_message
          value: V2VsY29tZQ==
        - key: ui_notify_import_notify_button
          value: Tm90aWZ5
        - key: ui_remote_db_connect_error
          value: VGhlcmUgd2FzIGEgcHJvYmxlbSB1cGRhdGluZyB0aGUgcmVtb3RlIGRhdGFiYXNlLiBQbGVhc2UgY29udGFjdCBoZWxwIGRlc2s...
        - key: ui_changepwd_submit_button
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_one_click_guest_signon
          value: U2lnbiBPbg==
        - key: ui_post_access_content_label
          value: UG9zdCBBY2Nlc3M=
        - key: ui_column_sponsor_header
          value: U3BvbnNvcg==
        - key: ui_aup_sponsor_text
          value: WW91IGFyZSByZXNwb25zaWJsZSBmb3IgbWFpbnRhaW5pbmcgdGhlIGNvbmZpZGVudGlhbGl0eSBvZiB0aGUgcGFzc3dvcmQgYW5...
        - key: ui_reset_password_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_create_import_total_failure_message
          value: VW5hYmxlIHRvIGltcG9ydCBhY2NvdW50cy4gQSBmYWlsdXJlIG9jY3VycmVkIGluIGxpbmUg
        - key: ui_suspend_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_deny_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_approve_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGFwcHJvdmUgdGhlIHNlbGVjdGVkIGFjY291bnRzPw==
        - key: ui_create_accounts_access_info_maximum_duration_label
          value: TWF4aW11bTo=
        - key: ui_one_click_guest_processed
          value: VGhpcyBndWVzdCBhY2NvdW50IHJlcXVlc3QgaGFzIGFscmVhZHkgYmVlbiBwcm9jZXNzZWQu
        - key: ui_account_action_reinstate_button
          value: UmVpbnN0YXRl
        - key: ui_menu_sign_out_button
          value: U2lnbiBPdXQ=
        - key: ui_notify_random_notify_button
          value: UHJpbnQ=
        - key: ui_reinstate_account_success_single_message
          value: QWNjb3VudCByZWluc3RhdGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_contact_content_label
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_reinstate_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHJlaW5zdGF0ZWQ6
        - key: ui_login_failed_error
          value: QXV0aGVudGljYXRpb24gZmFpbGVkLg==
        - key: ui_deny_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_menu_change_password_button
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_create_accounts_guest_type_access_allowed_label
          value: QWNjZXNzIGFsbG93ZWQ6
        - key: ui_notices_status_failed_label
          value: RmFpbGVk
        - key: ui_notices_status_partial_success_label
          value: Q29tcGxldGUvRXJyb3Jz
        - key: ui_extend_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGV4dGVuZGV...
        - key: ui_create_known_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHByb3ZpZGVkLCBhY2NvdW50cyB3aWxsIGJlIGNyZWF0ZWQ...
        - key: ui_changepwd_cancel_button
          value: Q2FuY2Vs
        - key: ui_account_state_active_state_label
          value: QWN0aXZl
        - key: ui_post_access_instruction_message
          value: ''
        - key: ui_aup_content_label
          value: QWNjZXB0YWJsZSBVc2UgUG9saWN5
        - key: ui_delete_notice_success_single_message
          value: Tm90aWNlIGRlbGV0ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_create_accounts_access_info_minutes_label
          value: TWludXRlcw==
        - key: ui_to_time_label
          value: VG8gdGltZTo=
        - key: ui_resend_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgcmVzZW50IHN1Y2Nlc3NmdWxseS4=
        - key: ui_last_name_label
          value: TGFzdCBuYW1lOg==
        - key: ui_account_action_resend_button
          value: UmVzZW5k
        - key: ui_print_account_total_failure_message
          value: VW5hYmxlIHRvIHByaW50Lg==
        - key: ui_login_aup_text
          value: WW91IGFyZSByZXNwb25zaWJsZSBmb3IgbWFpbnRhaW5pbmcgdGhlIGNvbmZpZGVudGlhbGl0eSBvZiB0aGUgcGFzc3dvcmQgYW5...
        - key: ui_changepwd_optional_content_2
          value: ''
        - key: ui_deny_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgZGVuaWVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_email_address_label
          value: RW1haWwgYWRkcmVzczo=
        - key: ui_changepwd_optional_content_1
          value: ''
        - key: ui_column_location_header
          value: TG9jYXRpb24=
        - key: ui_date_picker_short_day_wednesday
          value: Vw==
        - key: ui_extend_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_approve_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGFwcHJvdmUgdGhpcyBhY2NvdW50Pw==
        - key: ui_create_random_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_reset_password_account_total_failure_message
          value: VW5hYmxlIHRvIHJlc2V0IHBhc3N3b3JkLg==
        - key: ui_contact_failure_code_label
          value: RmFpbHVyZSBjb2RlOg==
        - key: ui_date_picker_month_november
          value: Tm92ZW1iZXI=
        - key: ui_field_phone_error
          value: SW52YWxpZCBtb2JpbGUgbnVtYmVyIGZvcm1hdC4=
        - key: ui_reinstate_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_notification_language_label
          value: TGFuZ3VhZ2U6
        - key: ui_column_sms_provider_header
          value: U01TIFByb3ZpZGVy
        - key: ui_suspend_account_instruction_message
          value: ''
        - key: ui_account_state_pending_approval_state_label
          value: UGVuZGluZyBBcHByb3ZhbA==
        - key: ui_reinstate_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlaW5zdGF0ZSB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_notices_column_status_header
          value: U3RhdHVz
        - key: ui_deny_account_success_single_message
          value: QWNjb3VudCBkZW5pZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_unit_thursday
          value: VGh1cnNkYXk=
        - key: ui_list_refresh_button
          value: UmVmcmVzaA==
        - key: ui_notify_import_ok_button
          value: T2s=
        - key: ui_column_password_header
          value: UGFzc3dvcmQ=
        - key: ui_create_known_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGNyZWF0ZSB0aGVzZSBhY2NvdW50cz8=
        - key: ui_delete_notice_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGRlbGV0ZSB0aGlzIG5vdGljZT8=
        - key: ui_deny_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGRlbmllZDo=
        - key: ui_account_state_suspended_state_label
          value: U3VzcGVuZGVk
        - key: ui_field_date_dmy_error
          value: SW52YWxpZCBkYXRlIGZvcm1hdCAoZGQvbW0veXl5eSku
        - key: ui_delete_notice_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_email_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGVtYWlsIHRoaXMgYWNjb3VudD8=
        - key: ui_one_click_login_instruction
          value: UGxlYXNlIGVudGVyIHlvdXIgY3JlZGVudGlhbHMgdG8gYXBwcm92ZSBvciBkZW55IHRoZSBndWVzdCBhY2NvdW50Lg==
        - key: ui_notify_email_address_label
          value: U3BvbnNvcidzIEVtYWlsIGFkZHJlc3M=
        - key: ui_email_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgZW1haWxlZCBzdWNjZXNzZnVsbHku
        - key: ui_notices_empty_error
          value: Tm8gbm90aWNlcyBhdCB0aGlzIG1vbWVudC4=
        - key: ui_create_random_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgcmFuZG9tIGFjY291bnRzIHN1Y2Nlc3NmdWxseSBjcmVhdGVkOg==
        - key: ui_suspend_account_success_single_message
          value: QWNjb3VudCBzdXNwZW5kZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_date_picker_short_day_thursday
          value: VA==
        - key: ui_login_optional_content_1
          value: ''
        - key: ui_date_picker_title
          value: U2V0IERhdGU=
        - key: ui_suspend_account_total_failure_message
          value: VW5hYmxlIHRvIHN1c3BlbmQgYWNjb3VudC4=
        - key: ui_login_optional_content_2
          value: ''
        - key: ui_reset_password_ok_button
          value: T0s=
        - key: ui_field_date_range_unlimited_error
          value: VmFsaWQgZGF0ZXMgc3RhcnQgZnJvbSB7MH0=
        - key: ui_one_click_guest_link_expired
          value: TGluayBoYXMgZXhwaXJlZC4gUGxlYXNlIHNpZ24gb24gdG8gdGhlIHNwb25zb3IgcG9ydGFsIHRvIGFwcHJvdmUvZGVueSBndWV...
        - key: ui_post_access_message
          value: WW91IGNhbiBwcm92aWRlIG5ldHdvcmsgYWNjZXNzIHRvIG90aGVycy4gQmUgc3VyZSB0byBmb2xsb3cgeW91ciBjb21wYW55J3M...
        - key: ui_extend_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGV4dGVuZGVkOg==
        - key: ui_field_first_name_error
          value: UGxlYXNlIGVudGVyIGEgdmFsaWQgZmlyc3QgbmFtZS4=
        - key: ui_account_action_delete_button
          value: RGVsZXRl
        - key: ui_notify_import_send_summary_email_label
          value: U2VuZCBtZSBhIHN1bW1hcnkgb2YgaW1wb3J0
        - key: ui_extend_account_ok_button
          value: T2s=
        - key: ui_login_password_label
          value: UGFzc3dvcmQ6
        - key: ui_account_details_sponsor_label
          value: U3BvbnNvcjo=
        - key: ui_notify_random_done_button
          value: RG9uZQ==
        - key: ui_user_name_label
          value: VXNlcm5hbWU6
        - key: ui_approve_account_ok_button
          value: T0s=
        - key: ui_create_import_select_file_label
          value: U2VsZWN0IGZpbGU6
        - key: ui_reset_password_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlc2V0IHRoZSBwYXNzd29yZCBmb3IgdGhpcyBhY2NvdW50Pw==
        - key: ui_account_action_edit_button
          value: RWRpdA==
        - key: ui_contact_ip_address_label
          value: SVAgYWRkcmVzczo=
        - key: ui_password_label
          value: UGFzc3dvcmQ6
        - key: ui_extend_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgZXh0ZW5kZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_create_known_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGNyZWF0ZWQ6
        - key: ui_reset_password_notify_guests_label
          value: U2VuZCBndWVzdCBub3RpZmljYXRpb24gdXNpbmc6
        - key: ui_resend_account_success_single_message
          value: QWNjb3VudCByZXNlbnQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_create_random_success_single_message
          value: UmFuZG9tIGFjY291bnQgY3JlYXRlZCBzdWNjZXNzZnVsbHku
        - key: ui_delete_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_approve_accounts_filter_label
          value: UGVuZGluZyBhY2NvdW50cyBmb3VuZA==
        - key: ui_delete_notice_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2Ygbm90aWNlcyBzdWNjZXNzZnVsbHkgZGVsZXRlZDo=
        - key: ui_post_access_optional_content_1
          value: ''
        - key: ui_post_access_optional_content_2
          value: ''
        - key: ui_sms_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIG51bWJlciBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHRleHRlZCB...
        - key: ui_create_known_success_multi_message
          value: QWNjb3VudHMgY3JlYXRlZCBzdWNjZXNzZnVsbHku
        - key: ui_date_picker_month_march
          value: TWFyY2g=
        - key: ui_create_import_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGltcG9ydGVkOg==
        - key: ui_email_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIG51bWJlciBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGVtYWlsZWQ...
        - key: ui_create_accounts_back_button
          value: QmFjaw==
        - key: ui_notify_import_cancel_button
          value: Q2FuY2Vs
        - key: ui_delete_notice_total_failure_message
          value: VW5hYmxlIHRvIGRlbGV0ZSBub3RpY2VzLg==
        - key: ui_delete_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgZGVsZXRlZCBzdWNjZXNzZnVsbHku
        - key: ui_notify_print_label
          value: UHJpbnQ=
        - key: ui_account_action_suspend_button
          value: U3VzcGVuZA==
        - key: ui_reinstate_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_edit_accounts_cancel_button
          value: Q2FuY2Vs
        - key: ui_time_picker_title
          value: Q2hvb3NlIFRpbWU=
        - key: ui_notices_action_random_label
          value: Q3JlYXRlIFJhbmRvbSBBY2NvdW50cw==
        - key: ui_from_time_label
          value: RnJvbSB0aW1lOg==
        - key: ui_create_accounts_guest_type_access_limit_label
          value: TWF4aW11bSBhY2Nlc3MgZHVyYXRpb246
        - key: ui_changepwd_confirmpwd_label
          value: Q29uZmlybSBwYXNzd29yZDo=
        - key: ui_field_min_error
          value: RmllbGQgdmFsdWUgY2Fubm90IGJlIGxlc3MgdGhhbiB7MH0=
        - key: ui_create_import_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGltcG9ydCB0aGlzIGFjY291bnQ/
        - key: ui_create_random_success_multi_message
          value: UmFuZG9tIGFjY291bnRzIGNyZWF0ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_unit_hours
          value: aG91cnM=
        - key: ui_print_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHByaW50IHRoZSBzZWxlY3RlZCBhY2NvdW50cz8=
        - key: ui_footer_label
          value: ''
        - key: ui_login_instruction_message
          value: VXNlIHRoZSBTcG9uc29yIHBvcnRhbCB0byBtYW5hZ2UgZ3Vlc3QgYWNjb3VudHMuIFNpZ24gb24gd2l0aCB5b3VyIHVzZXJuYW1...
        - key: ui_one_click_login_to_other_portals
          value: VHJ5IHJlLWVudGVyaW5nIHlvdXIgY3JlZGVudGlhbHMgb3IgbG9nZ2luZyBpbiB0byB0aGUgc3BvbnNvciBwb3J0YWwgeW91IHV...
        - key: ui_sms_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHRleHQgdGhlIHNlbGVjdGVkIGFjY291bnRzPw==
        - key: ui_post_access_page_title
          value: UG9zdCBBY2Nlc3M=
        - key: ui_contact_page_title
          value: Q29udGFjdCBJbmZvcm1hdGlvbg==
        - key: ui_notify_guests_delivery_label
          value: RGVsaXZlciBub3RpZmljYXRpb24gdXNpbmc6
        - key: ui_suspend_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgc3VzcGVuZGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_guest_type_label
          value: R3Vlc3QgdHlwZTo=
        - key: ui_delete_notice_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGRlbGV0ZSB0aGUgc2VsZWN0ZWQgbm90aWNlcz8=
        - key: ui_unit_friday
          value: RnJpZGF5
        - key: ui_account_state_expired_state_label
          value: RXhwaXJlZA==
        - key: ui_login_aup_agreement_label
          value: QWdyZWUgdG8=
        - key: ui_create_accounts_next_button
          value: TmV4dA==
        - key: ui_reinstate_account_ok_button
          value: T2s=
        - key: ui_menu_home_button
          value: SG9tZQ==
        - key: ui_notices_column_accounts_num_header
          value: TnVtYmVyIG9mIEFjY291bnRz
        - key: ui_login_change_password_button
          value: SSB3YW50IHRvIGNoYW5nZSBteSBwYXNzd29yZCBhZnRlciBsb2dpbg==
        - key: ui_notices_column_start_time_header
          value: U3RhcnQ=
        - key: ui_extend_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGV4dGVuZCB0aGlzIGFjY291bnQ/
        - key: ui_login_content_label
          value: U2lnbiBPbg==
        - key: ui_email_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_aup_page_title
          value: QWNjZXB0YWJsZSBVc2UgUG9saWN5
        - key: ui_column_ssid_header
          value: U1NJRA==
        - key: ui_changepwd_policy_help_label
          value: UGFzc3dvcmRzIG11c3QgYmUgOCBjaGFyYWN0ZXJzIGFuZCBjb250YWluIGEgbGV0dGVyIGFuZCBudW1iZXIu
        - key: ui_deny_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbnkgYWNjZXNzIGZvciB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_approve_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgYXBwcm92ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_print_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHByaW50ZWQ6
        - key: ui_delete_account_success_single_message
          value: QWNjb3VudCBkZWxldGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_list_sort_by_label
          value: U29ydCBieTo=
        - key: ui_sms_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHRleHQgdGhpcyBhY2NvdW50Pw==
        - key: ui_aup_optional_content_2
          value: ''
        - key: ui_column_person_visited_header
          value: UGVyc29uIEJlaW5nIFZpc2l0ZWQ=
        - key: ui_reinstate_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlaW5zdGF0ZSB0aGlzIGFjY291bnQ/
        - key: ui_contact_mac_address_label
          value: TUFDIGFkZHJlc3M6
        - key: ui_aup_optional_content_1
          value: ''
        - key: ui_error_instruction_message
          value: ''
        - key: ui_from_date_label
          value: RnJvbSBkYXRlICh5eXl5LW1tLWRkKTo=
        - key: ui_column_expiration_date_header
          value: RXhwaXJhdGlvbiBEYXRl
        - key: ui_date_picker_month_october
          value: T2N0b2Jlcg==
        - key: ui_contact_title_label
          value: Q29udGFjdCBJbmZvcm1hdGlvbg==
        - key: ui_column_group_tag_header
          value: R3JvdXAgVGFn
        - key: ui_resend_account_ok_button
          value: T0s=
        - key: ui_unit_days_symbol
          value: RA==
        - key: ui_print_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHByaW50IHRoaXMgYWNjb3VudD8=
        - key: ui_column_account_state_header
          value: U3RhdGU=
        - key: ui_sms_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_changepwd_instruction_message
          value: WW91IGFyZSByZXF1aXJlZCB0byBjaGFuZ2UgeW91ciBwYXNzd29yZCBub3cuIFBsZWFzZSBlbnRlciBhIG5ldyBwYXNzd29yZC4=
        - key: ui_unit_hours_symbol
          value: SA==
        - key: ui_field_last_name_error
          value: UGxlYXNlIGVudGVyIGEgdmFsaWQgbGFzdCBuYW1lLg==
        - key: ui_create_accounts_aup_link
          value: VGVybXMgYW5kIENvbmRpdGlvbnM=
        - key: ui_account_details_suspension_reason_label
          value: UmVhc29uIGZvciBzdXNwZW5zaW9uOg==
        - key: ui_no_user_error
          value: VXNlciBkb2Vzbid0IGV4aXN0Lg==
        - key: ui_create_accounts_access_info_location_label
          value: TG9jYXRpb246
        - key: ui_reinstate_account_total_failure_message
          value: VW5hYmxlIHRvIHJlaW5zdGF0ZSBhY2NvdW50Lg==
        - key: ui_reset_password_account_success_single_message
          value: QWNjb3VudCBwYXNzd29yZCByZXNldCBzdWNjZXNzZnVsbHku
        - key: ui_create_accounts_access_info_hours_label
          value: SG91cnM=
        - key: ui_notify_known_notify_button
          value: Tm90aWZ5
        - key: ui_create_import_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGltcG9ydCB0aGVzZSBhY2NvdW50cz8=
        - key: ui_home_page_title
          value: U3BvbnNvciBIb21l
        - key: ui_notify_known_auto_notify_text
          value: R3Vlc3Qgbm90aWZpY2F0aW9ucyBhcmUgc2VudCBhdXRvbWF0aWNhbGx5
        - key: ui_unit_pm
          value: UE0=
        - key: ui_reason_visit_label
          value: UmVhc29uIGZvciB2aXNpdDo=
        - key: ui_approve_accounts_content_label
          value: UGVuZGluZyBBY2NvdW50cw==
        - key: ui_column_notification_language_header
          value: TGFuZ3VhZ2U=
        - key: ui_column_guest_type_header
          value: R3Vlc3QgVHlwZQ==
        - key: ui_aup_instruction_message
          value: UGxlYXNlIHJlYWQgdGhlIEFjY2VwdGFibGUgVXNlIFBvbGljeS4=
        - key: ui_reset_password_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgcGFzc3dvcmQgcmVzZXQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_unit_am
          value: QU0=
        - key: ui_resend_account_total_failure_message
          value: VW5hYmxlIHRvIHJlc2VuZCBpbmZvcm1hdGlvbi4=
        - key: ui_unit_saturday
          value: U2F0dXJkYXk=
        - key: ui_portal_label
          value: UG9ydGFsIE5hbWU=
        - key: ui_notify_known_cancel_button
          value: Q2FuY2Vs
        - key: ui_print_account_success_single_message
          value: QWNjb3VudCBwcmludGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_create_random_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGNyZWF0ZSB0aGVzZSByYW5kb20gYWNjb3VudHM/
        - key: ui_account_action_print_button
          value: UHJpbnQ=
        - key: ui_edit_accounts_save_button
          value: U2F2ZQ==
        - key: ui_reset_password_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlc2V0IHRoZSBwYXNzd29yZCBmb3IgdGhlIHNlbGVjdGVkIGFjY291bnRzPw==
        - key: ui_home_instruction_message
          value: Q3JlYXRlLCBtYW5hZ2UsIGFuZCBhcHByb3ZlIGd1ZXN0IGFjY291bnRzLg==
        - key: ui_column_reason_visit_header
          value: UmVhc29uIGZvciBWaXNpdA==
        - key: ui_guest_duration_error
          value: VGhlIHBlcmlvZCBiZXR3ZWVuIHN0YXJ0IGFuZCBlbmQgZGF0ZSBleGNlZWRzIG1heGltdW0gZHVyYXRpb24gY29uZmlndXJlZCB...
        - key: ui_notices_action_sms_label
          value: VGV4dCBHdWVzdHM=
        - key: ui_create_accounts_guest_type_device_limit_label
          value: TWF4aW11bSBkZXZpY2VzIHRoYXQgY2FuIGJlIGNvbm5lY3RlZDo=
        - key: ui_create_accounts_access_info_to_time_label
          value: VG8gVGltZQ==
        - key: ui_time_left_label
          value: VGltZSBsZWZ0Og==
        - key: ui_user_last_login_pass_time_label
          value: TGFzdCBMb2dpbjo=
        - key: ui_email_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGVtYWlsIHRoZSBzZWxlY3RlZCBhY2NvdW50cz8=
        - key: ui_create_random_prefix_label
          value: VXNlcm5hbWUgcHJlZml4Og==
        - key: ui_approve_account_total_failure_message
          value: VW5hYmxlIHRvIGFwcHJvdmUgYWNjb3VudC4=
        - key: ui_manage_accounts_content_label
          value: TWFuYWdlIEFjY291bnRz
        - key: ui_notify_content_label
          value: QWNjb3VudCBJbmZvcm1hdGlvbg==
        - key: ui_login_signon_button
          value: U2lnbiBPbg==
        - key: ui_delete_notice_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBub3RpY2VzIHdlcmUgc2VsZWN0ZWQuIE5vdGljZXMgd2lsbCBiZSBkZWxldGVkIGl...
        - key: ui_error_page_title
          value: RXJyb3I=
        - key: ui_create_import_total_failure_message_suffix
          value: VGhlIGltcG9ydCBmaWxlIG1heSBjb250YWluIGFkZGl0aW9uYWwgZXJyb3JzLCBidXQgdGhlIGltcG9ydCBvcGVyYXRpb24gZGl...
        - key: ui_approve_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_contact_sessioninfo_text
          value: VGhlIGZvbGxvd2luZyBpbmZvcm1hdGlvbiBtaWdodCBiZSB1c2VmdWwgdG8gdGhlIEhlbHAgRGVzayByZXByZXNlbnRhdGl2ZSB...
        - key: ui_column_creation_date_header
          value: Q3JlYXRpb24gRGF0ZQ==
        - key: ui_home_title_label
          value: U3BvbnNvciBQb3J0YWw=
        - key: ui_edit_accounts_content_label
          value: RWRpdCBBY2NvdW50
        - key: ui_date_picker_month_april
          value: QXByaWw=
        - key: ui_email_account_total_failure_message
          value: VW5hYmxlIHRvIHNlbmQgZW1haWwu
        - key: ui_notices_action_print_label
          value: Q3JlYXRlIFByaW50IEpvYg==
        - key: ui_column_last_name_header
          value: TGFzdCBOYW1l
        - key: ui_create_import_success_single_message
          value: QWNjb3VudCBpbXBvcnRlZCBzdWNjZXNzZnVsbHku
        - key: ui_create_import_async_message
          value: QWNjb3VudCBpbXBvcnRpbmcgd2lsbCBiZSBwcm9jZXNzZWQgaW4gdGhlIGJhY2tncm91bmQuIENoZWNrIE5vdGljZXMgZm9yIHN...
        - key: ui_extend_account_success_single_message
          value: QWNjb3VudCBleHRlbmRlZCBzdWNjZXNzZnVsbHku
        - key: ui_unit_minutes_symbol
          value: TQ==
        - key: ui_notify_sms_label
          value: U01T
        - key: ui_extend_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_unit_days
          value: ZGF5cw==
        - key: ui_create_import_tab_label
          value: SW1wb3J0
        - key: ui_to_label
          value: VG86
        - key: ui_changepwd_currentpwd_label
          value: Q3VycmVudCBwYXNzd29yZDo=
        - key: ui_column_time_left_header
          value: VGltZSBMZWZ0
        - key: ui_account_action_approve_button
          value: QXBwcm92ZQ==
        - key: ui_create_known_instruction_message
          value: ''
        - key: ui_create_known_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGNyZWF0ZSB0aGlzIGFjY291bnQ/
        - key: ui_reinstate_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHJlaW5zdGF...
        - key: ui_date_picker_month_december
          value: RGVjZW1iZXI=
        - key: ui_notify_import_accounts_showing_label
          value: U2hvd2luZzog
        - key: ui_one_click_guest_link_invalid
          value: TGluayBpcyBpbnZhbGlkLiBQbGVhc2Ugc2lnbiBvbiB0byB0aGUgc3BvbnNvciBwb3J0YWwgdG8gYXBwcm92ZS9kZW55IGd1ZXN...
        - key: ui_date_picker_calendar_header_format
          value: JUIgJVk=
        - key: ui_resend_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHJlc2VudCB...
        - key: ui_field_email_error
          value: RW50ZXIgYSB2YWxpZCBlbWFpbCBhZGRyZXNzLg==
        - key: ui_suspend_account_reason_label
          value: UmVhc29uIGZvciBzdXNwZW5zaW9uOg==
        - key: ui_creation_date_label
          value: Q3JlYXRpb24gZGF0ZTo=
        - key: ui_field_date_range_limited_error
          value: VmFsaWQgZGF0ZXMgYXJlIHswfSB0byB7MX0=
        - key: ui_date_picker_short_day_tuesday
          value: VA==
        - key: ui_menu_switch_mobile_button
          value: U3dpdGNoIHRvIG1vYmlsZSBtb2Rl
        - key: ui_suspend_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_deny_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGRlbmllZCB...
        - key: ui_person_visited_label
          value: UGVyc29uIGJlaW5nIHZpc2l0ZWQgKGVtYWlsKTo=
        - key: ui_create_import_success_multi_message
          value: QWNjb3VudHMgaW1wb3J0ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_changepwd_newpwd_label
          value: TmV3IHBhc3N3b3JkOg==
        - key: ui_column_guest_location_header
          value: TG9jYXRpb24=
        - key: ui_field_digit_error
          value: RW50ZXIgYSB2YWxpZCBudW1iZXIu
        - key: ui_date_picker_short_day_sunday
          value: Uw==
        - key: ui_create_accounts_guest_info_content_label
          value: R3Vlc3QgSW5mb3JtYXRpb24=
        - key: ui_unit_minutes
          value: bWludXRlcw==
        - key: ui_account_action_extend_button
          value: RXh0ZW5k
        - key: ui_account_details_account_state_label
          value: U3RhdGU6
        - key: ui_from_label
          value: RnJvbQ==
        - key: ui_extend_account_instruction_message
          value: ''
        - key: ui_account_details_done_button
          value: RG9uZQ==
        - key: ui_unit_tuesday
          value: VHVlc2RheQ==
        - key: ui_notify_import_auto_notify_text
          value: R3Vlc3Qgbm90aWZpY2F0aW9ucyBhcmUgc2VudCBhdXRvbWF0aWNhbGx5
        - key: ui_company_label
          value: Q29tcGFueTo=
        - key: ui_date_picker_month_january
          value: SmFudWFyeQ==
        - key: ui_sms_account_total_failure_message
          value: VW5hYmxlIHRvIHNlbmQgdGV4dC4=
        - key: ui_delete_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGRlbGV0ZWQ6
        - key: ui_delete_account_ok_button
          value: T0s=
        - key: ui_notify_random_accounts_created_label
          value: QWNjb3VudHMgY3JlYXRlZDog
        - key: ui_notices_delete_button
          value: RGVsZXRlIE5vdGljZQ==
        - key: ui_create_known_tab_label
          value: S25vd24=
        - key: ui_extend_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGV4dGVuZCB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_create_accounts_access_info_to_date_label
          value: VG8gRGF0ZSAoeXl5eS1tbS1kZCk=
        - key: ui_time_picker_button
          value: U2V0IFRpbWU=
        - key: ui_post_access_continue_button
          value: Q29udGludWU=
        - key: ui_javascript_disabled_message
          value: WW91IG11c3QgdHVybiBvbiBKYXZhU2NyaXB0IHRvIHVzZSB0aGlzIHdlYiBzaXRlLg==
        - key: ui_field_date_ymd_error
          value: SW52YWxpZCBkYXRlIGZvcm1hdCAoeXl5eS1tbS1kZCku
        - key: ui_create_import_download_template_link
          value: RG93bmxvYWQgVGVtcGxhdGU=
        - key: ui_contact_policy_server_label
          value: UG9saWN5IHNlcnZlcjo=
        - key: ui_prefix_mismatch_policy_error
          value: UHJlZml4IGRpZCBub3QgbWF0Y2ggVXNlcm5hbWUgUG9saWN5
        - key: ui_column_company_header
          value: Q29tcGFueQ==
        - key: ui_notify_import_accounts_created_label
          value: QWNjb3VudHMgY3JlYXRlZDog
        - key: ui_date_picker_month_september
          value: U2VwdGVtYmVy
        - key: ui_reset_password_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHBhc3N3b3J...
        - key: ui_delete_account_total_failure_message
          value: VW5hYmxlIHRvIGRlbGV0ZSBhY2NvdW50Lg==
        - key: ui_create_accounts_create_button
          value: Q3JlYXRl
        - key: ui_contact_helpdesk_title
          value: SGVscCBEZXNrIEluZm9ybWF0aW9u
        - key: ui_notify_known_done_button
          value: RG9uZQ==
        - key: ui_notices_done_button
          value: RG9uZQ==
        - key: ui_phone_number_label
          value: TW9iaWxlIG51bWJlcjo=
        - key: ui_column_email_address_header
          value: RW1haWwgQWRkcmVzcw==
        - key: ui_deny_account_total_failure_message
          value: VW5hYmxlIHRvIGRlbnkgYWNjb3VudC4=
        - key: ui_email_mismatch_policy_error
          value: RW1haWwgZGlkIG5vdCBtYXRjaCBVc2VybmFtZSBQb2xpY3k=
        - key: ui_aup_decline_button
          value: RGVjbGluZQ==
        - key: ui_changepwd_username_label
          value: VXNlcm5hbWU6
        - key: ui_notify_random_accounts_showing_label
          value: U2hvd2luZzog
        - key: ui_notices_content_label
          value: Tm90aWNlcw==
        - key: ui_account_action_deny_button
          value: RGVueQ==
        - key: ui_delete_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbGV0ZSB0aGlzIGFjY291bnQ/
        - key: ui_field_max_error
          value: RmllbGQgdmFsdWUgY2Fubm90IGJlIGdyZWF0ZXIgdGhhbiB7MH0=
        - key: ui_contact_message
          value: Q29udGFjdCBJbmZvcm1hdGlvbg==
        - key: ui_approve_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGFwcHJvdmVkOg==
        - key: ui_create_accounts_guest_type_content_label
          value: R3Vlc3QgdHlwZTo=
        - key: ui_unit_monday
          value: TW9uZGF5
        - key: ui_create_accounts_access_info_ssid_label
          value: U1NJRDo=
        - key: ui_invalid_input_error
          value: SW52YWxpZCBpbnB1dC4=
        - key: ui_banner_label
          value: U3BvbnNvciBQb3J0YWw=
        - key: ui_date_label
          value: RGF0ZTo=
        - key: ui_create_import_instruction_message
          value: Q2xpY2sgdG8gZG93bmxvYWQgdGhlIGltcG9ydCB0ZW1wbGF0ZSBmaWxlLg==
        - key: ui_create_random_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGNyZWF0ZSB0aGlzIHJhbmRvbSBhY2NvdW50Pw==
        - key: ui_firstname_mismatch_policy_error
          value: Rmlyc3ROYW1lIGRpZCBub3QgbWF0Y2ggVXNlcm5hbWUgUG9saWN5
        - key: ui_date_picker_short_day_saturday
          value: Uw==
      portalTheme:
        id: 9eb421c0-8c01-11e6-996c-525400b48521
        name: Default Blue theme
      portalTweakSettings: {}
    description: Default portal used by sponsors to create and manage accounts for authorized
      visitors to securely access the network
    id: bd48c1a1-9477-4746-8e40-e43d20c9f429
    name: Sponsor Portal (default)
    portalTestUrl: https://198.18.133.27:8445/sponsorportal/PortalSetup.action?portal=bd48c1a1-9477-4746-8e40-e43d20...
    portalType: SPONSOR
    settings:
      aupSettings:
        displayFrequency: FIRSTLOGIN
        includeAup: true
        requireScrolling: false
      loginPageSettings:
        includeAup: false
        maxFailedAttemptsBeforeRateLimit: 5
        requireAupScrolling: false
        socialConfigs: []
        timeBetweenLoginsDuringRateLimit: 2
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        authenticationMethod: 92faba60-8c01-11e6-996c-525400b48521
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        fallbackLanguage: English
        httpsPort: 8445
        idleTimeout: 10
      postLoginBannerSettings:
        includePostAccessBanner: false
      sponsorChangePasswordSettings:
        allowSponsorToChangePwd: false
      supportInfoSettings:
        emptyFieldDisplay: HIDE
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: false

- name: Update by id
  cisco.ise.sponsor_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        bannerTitle: Sponsor Portal
        contactText: Contact Support
        footerElement: ''
      language:
        viewLanguage: English
      pageCustomizations:
        data:
        - key: ui_date_picker_month_august
          value: QXVndXN0
        - key: ui_error_content_label
          value: RXJyb3I=
        - key: ui_notify_import_done_button
          value: RG9uZQ==
        - key: ui_create_accounts_content_label
          value: Q3JlYXRlIEFjY291bnRz
        - key: ui_notify_copy_me_label
          value: Q29weSBtZQ==
        - key: ui_print_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_contact_optional_content_1
          value: ''
        - key: ui_contact_optional_content_2
          value: ''
        - key: ui_one_click_guest_approved
          value: R3Vlc3QgKCR1aV9ndWVzdF91c2VybmFtZSQpIGhhcyBiZWVuIGFwcHJvdmVkLg==
        - key: ui_create_random_number_accounts_label
          value: TnVtYmVyIG9mIGFjY291bnRzOg==
        - key: ui_date_picker_month_may
          value: TWF5
        - key: ui_approve_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_login_aup_link
          value: VGVybXMgYW5kIENvbmRpdGlvbnM=
        - key: ui_one_click_guest_denied
          value: R3Vlc3QgKCR1aV9ndWVzdF91c2VybmFtZSQpIGhhcyBiZWVuIGRlbmllZC4=
        - key: ui_column_user_name_header
          value: VXNlcm5hbWU=
        - key: ui_invalid_password_policy_error
          value: SW52YWxpZCBQYXNzd29yZCBQb2xpY3ku
        - key: ui_account_state_label
          value: U3RhdGU6
        - key: ui_reset_password_send_summary_email_label
          value: U2VuZCBtZSBhIHN1bW1hcnkgb2YgcGFzc3dvcmQgcmVzZXQ=
        - key: ui_notices_action_import_label
          value: Q3JlYXRlIEltcG9ydCBBY2NvdW50cw==
        - key: ui_location_label
          value: TG9jYXRpb246
        - key: ui_email_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGVtYWlsZWQ6
        - key: ui_resend_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_field_company_name_error
          value: UGxlYXNlIGVudGVyIGEgdmFsaWQgY29tcGFueSBuYW1lLg==
        - key: ui_one_click_sponsor_no_privilege
          value: U3BvbnNvciBkaWQgbm90IGhhdmUgcHJpdmlsZWdlIHRvIGFwcHJvdmUvZGVueSBndWVzdHMu
        - key: ui_unit_wednesday
          value: V2VkbmVzZGF5
        - key: ui_contact_sessioninfo_title
          value: U2Vzc2lvbiBJbmZvcm1hdGlvbg==
        - key: ui_first_name_label
          value: Rmlyc3QgbmFtZTo=
        - key: ui_aup_accept_button
          value: QWNjZXB0
        - key: ui_create_random_accounts_batch_limit_label
          value: TWF4aW11bTogIA==
        - key: ui_unit_sunday
          value: U3VuZGF5
        - key: ui_sms_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHRleHRlZDo=
        - key: ui_one_click_login_submit
          value: U3VibWl0
        - key: ui_changepwd_values_match_error
          value: WW91IG11c3QgZW50ZXIgdGhlIHNhbWUgcGFzc3dvcmQgaW4gdGhlIE5ldyBQYXNzd29yZCBhbmQgQ29uZmlybSBQYXNzd29yZCB...
        - key: ui_error_optional_content_2
          value: ''
        - key: ui_error_optional_content_1
          value: ''
        - key: ui_login_page_title
          value: IFNwb25zb3IgUG9ydGFsIFNpZ24gT24=
        - key: ui_notices_column_action_name_header
          value: QWN0aW9uIE5hbWU=
        - key: ui_create_random_tab_label
          value: UmFuZG9t
        - key: ui_suspend_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHN1c3BlbmQgdGhpcyBhY2NvdW50Pw==
        - key: ui_changepwd_content_label
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_create_known_total_failure_message
          value: VW5hYmxlIHRvIGNyZWF0ZSBhY2NvdW50Lg==
        - key: ui_reinstate_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgcmVpbnN0YXRlZCBzdWNjZXNzZnVsbHku
        - key: ui_create_accounts_access_info_instruction_message
          value: ''
        - key: ui_changepwd_values_unique_error
          value: WW91IGNhbm5vdCBlbnRlciB0aGUgc2FtZSBwYXNzd29yZCBpbiB0aGUgQ3VycmVudCBQYXNzd29yZCBhbmQgTmV3IFBhc3N3b3J...
        - key: ui_deny_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGRlbnkgdGhpcyBhY2NvdW50Pw==
        - key: ui_ssid_label
          value: U1NJRDo=
        - key: ui_contact_instruction_message
          value: Q29udGFjdCBIZWxwIERlc2s=
        - key: ui_notify_email_label
          value: RW1haWw=
        - key: ui_time_label
          value: VGltZTo=
        - key: ui_create_accounts_access_info_from_date_label
          value: RnJvbSBEYXRlICh5eXl5LW1tLWRkKQ==
        - key: ui_contact_helpdesk_text
          value: TmVlZCBoZWxwPyBDb250YWN0IG91ciBIZWxwIERlc2sgYXQgKHh4eCkgeHh4LXh4eHgu
        - key: ui_notices_status_pending_label
          value: UGVuZGluZw==
        - key: ui_guest_location_label
          value: TG9jYXRpb246
        - key: ui_username_mismatch_policy_error
          value: VXNlcm5hbWUgZGlkIG5vdCBtYXRjaCBVc2VybmFtZSBQb2xpY3k=
        - key: ui_manage_accounts_filter_label
          value: YWNjb3VudHMgZm91bmQ=
        - key: ui_resend_account_send_summary_email_label
          value: U2VuZCBtZSBhIHN1bW1hcnk=
        - key: ui_menu_switch_desktop_button
          value: U3dpdGNoIHRvIGRlc2t0b3AgbW9kZQ==
        - key: ui_resend_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHJlc2VudDo=
        - key: ui_reset_password_cancel_button
          value: Q2FuY2Vs
        - key: ui_create_accounts_import_button
          value: SW1wb3J0
        - key: ui_sms_account_success_single_message
          value: QWNjb3VudCB0ZXh0ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_suspend_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHN1c3BlbmR...
        - key: ui_contact_link
          value: Q29udGFjdCBTdXBwb3J0
        - key: ui_notices_filter_label
          value: Tm90aWNlcyBmb3VuZA==
        - key: ui_contact_user_agent_label
          value: VXNlciBhZ2VudDo=
        - key: ui_reset_password_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHJlc2V0Og==
        - key: ui_create_known_success_single_message
          value: QWNjb3VudCBjcmVhdGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_delete_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbGV0ZSB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_extend_account_extend_by_label
          value: RXh0ZW5kIGJ5
        - key: ui_create_known_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_changepwd_page_title
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_create_random_instruction_message
          value: ''
        - key: ui_notices_status_success_label
          value: U3VjY2Vzcw==
        - key: ui_account_state_denied_state_label
          value: RGVuaWVk
        - key: ui_notices_edit_button
          value: RWRpdA==
        - key: ui_group_tag_label
          value: R3JvdXAgdGFnOg==
        - key: ui_date_picker_short_day_friday
          value: Rg==
        - key: ui_extend_account_total_failure_message
          value: VW5hYmxlIHRvIGV4dGVuZCBhY2NvdW50Lg==
        - key: ui_notices_column_end_time_header
          value: RW5k
        - key: ui_one_click_login_title
          value: QXBwcm92ZS9EZW55IEd1ZXN0
        - key: ui_account_details_content_label
          value: QWNjb3VudCBEZXRhaWxz
        - key: ui_print_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIG51bWJlciBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhIHByaW50IGpvYiB3aWxsIGJlIGNyZWF0ZWQ...
        - key: ui_create_random_total_failure_message
          value: VW5hYmxlIHRvIGNyZWF0ZSByYW5kb20gYWNjb3VudC4=
        - key: ui_manage_accounts_empty_error
          value: Tm8gZ3Vlc3QgYWNjb3VudHMgYXQgdGhpcyBtb21lbnQu
        - key: ui_create_random_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiByYW5kb20gYWNjb3VudHMgd2VyZSBwcm92aWRlZC4gUmFuZG9tIGFjY291bnRzIHd...
        - key: ui_create_accounts_aup_agreement_label
          value: QWdyZWUgdG8=
        - key: ui_use_mobile_number_as_username_label
          value: VXNlIE1vYmlsZSBudW1iZXIgYXMgdXNlcm5hbWU=
        - key: ui_date_picker_short_day_monday
          value: TQ==
        - key: ui_time_duration_label
          value: RHVyYXRpb246
        - key: ui_date_picker_month_february
          value: RmVicnVhcnk=
        - key: ui_resend_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlc2VuZCB0aGlzIGFjY291bnQ/
        - key: ui_notify_known_ok_button
          value: T2s=
        - key: ui_suspend_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHN1c3BlbmRlZDo=
        - key: ui_help_link
          value: SGVscA==
        - key: ui_one_click_login_username
          value: VXNlcm5hbWU6
        - key: ui_user_last_login_ipaddr_label
          value: RnJvbTo=
        - key: ui_create_accounts_batch_limit_label
          value: TWF4aW11bTo=
        - key: ui_date_picker_month_july
          value: SnVseQ==
        - key: ui_resend_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlc2VuZCB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_delete_notice_success_multi_message
          value: U2VsZWN0ZWQgbm90aWNlcyBkZWxldGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_sms_provider_label
          value: U01TIHByb3ZpZGVyOg==
        - key: ui_first_login_text
          value: Rmlyc3QgTG9naW4=
        - key: ui_login_username_label
          value: VXNlcm5hbWU6
        - key: ui_account_action_reset_password_button
          value: UmVzZXQgUGFzc3dvcmQ=
        - key: ui_create_accounts_access_info_from_time_label
          value: RnJvbSBUaW1l
        - key: ui_approve_accounts_empty_error
          value: Tm8gcGVuZGluZyBndWVzdCBhY2NvdW50cyBhdCB0aGlzIG1vbWVudC4=
        - key: ui_create_import_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_create_accounts_access_info_content_label
          value: QWNjZXNzIEluZm9ybWF0aW9u
        - key: ui_date_picker_month_june
          value: SnVuZQ==
        - key: ui_notices_status_inprogress_label
          value: SW4gUHJvZ3Jlc3M=
        - key: ui_email_account_success_single_message
          value: QWNjb3VudCBlbWFpbGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_approve_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGFwcHJvdmV...
        - key: ui_one_click_login_password
          value: UGFzc3dvcmQ6
        - key: ui_invalid_username_policy_error
          value: SW52YWxpZCBVc2VybmFtZSBQb2xpY3ku
        - key: ui_edit_accounts_guest_info_content_label
          value: R3Vlc3QgSW5mb3JtYXRpb24=
        - key: ui_delete_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_field_required_error
          value: VGhpcyBmaWVsZCBpcyByZXF1aXJlZC4=
        - key: ui_print_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgcHJpbnRlZCBzdWNjZXNzZnVsbHku
        - key: ui_field_date_mdy_error
          value: SW52YWxpZCBkYXRlIGZvcm1hdCAobW0vZGQveXl5eSku
        - key: ui_suspend_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHN1c3BlbmQgdGhlIHNlbGVjdGVkIGFjY291bnRzPw==
        - key: ui_column_first_name_header
          value: Rmlyc3QgTmFtZQ==
        - key: ui_notices_action_email_label
          value: RW1haWwgR3Vlc3Rz
        - key: ui_create_accounts_access_info_days_label
          value: RGF5cw==
        - key: ui_lastname_mismatch_policy_error
          value: TGFzdE5hbWUgZGlkIG5vdCBtYXRjaCBVc2VybmFtZSBQb2xpY3k=
        - key: ui_create_accounts_guest_type_instruction_message
          value: ''
        - key: ui_suspend_account_ok_button
          value: T2s=
        - key: ui_sms_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgdGV4dGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_expiration_date_label
          value: RXhwaXJhdGlvbiBkYXRlOg==
        - key: ui_changepwd_policy_error_message
          value: WW91ciBwYXNzd29yZCBkb2VzIG5vdCBtZWV0IHRoZSBwYXNzd29yZCBwb2xpY3kgcmVxdWlyZW1lbnRzLiBQbGVhc2UgY29udGF...
        - key: ui_approve_account_success_single_message
          value: QWNjb3VudCBhcHByb3ZlZCBzdWNjZXNzZnVsbHku
        - key: ui_edit_accounts_access_info_content_label
          value: QWNjZXNzIEluZm9ybWF0aW9u
        - key: ui_to_date_label
          value: VG8gZGF0ZSAoeXl5eS1tbS1kZCk6
        - key: ui_delete_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGRlbGV0ZWQ...
        - key: ui_end_of_day_label
          value: RW5kIG9mIGJ1c2luZXNzIGRheQ==
        - key: ui_column_phone_number_header
          value: TW9iaWxlIE51bWJlcg==
        - key: ui_deny_account_ok_button
          value: T0s=
        - key: ui_field_time_error
          value: SW52YWxpZCB0aW1lIGZvcm1hdCAoaGg6bW0pLg==
        - key: ui_resend_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_extend_account_maximum_label
          value: TWF4aW11bTog
        - key: ui_account_state_awaiting_login_state_label
          value: Q3JlYXRlZA==
        - key: ui_home_welcome_message
          value: V2VsY29tZQ==
        - key: ui_notify_import_notify_button
          value: Tm90aWZ5
        - key: ui_remote_db_connect_error
          value: VGhlcmUgd2FzIGEgcHJvYmxlbSB1cGRhdGluZyB0aGUgcmVtb3RlIGRhdGFiYXNlLiBQbGVhc2UgY29udGFjdCBoZWxwIGRlc2s...
        - key: ui_changepwd_submit_button
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_one_click_guest_signon
          value: U2lnbiBPbg==
        - key: ui_post_access_content_label
          value: UG9zdCBBY2Nlc3M=
        - key: ui_column_sponsor_header
          value: U3BvbnNvcg==
        - key: ui_aup_sponsor_text
          value: WW91IGFyZSByZXNwb25zaWJsZSBmb3IgbWFpbnRhaW5pbmcgdGhlIGNvbmZpZGVudGlhbGl0eSBvZiB0aGUgcGFzc3dvcmQgYW5...
        - key: ui_reset_password_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_create_import_total_failure_message
          value: VW5hYmxlIHRvIGltcG9ydCBhY2NvdW50cy4gQSBmYWlsdXJlIG9jY3VycmVkIGluIGxpbmUg
        - key: ui_suspend_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_deny_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_approve_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGFwcHJvdmUgdGhlIHNlbGVjdGVkIGFjY291bnRzPw==
        - key: ui_create_accounts_access_info_maximum_duration_label
          value: TWF4aW11bTo=
        - key: ui_one_click_guest_processed
          value: VGhpcyBndWVzdCBhY2NvdW50IHJlcXVlc3QgaGFzIGFscmVhZHkgYmVlbiBwcm9jZXNzZWQu
        - key: ui_account_action_reinstate_button
          value: UmVpbnN0YXRl
        - key: ui_menu_sign_out_button
          value: U2lnbiBPdXQ=
        - key: ui_notify_random_notify_button
          value: UHJpbnQ=
        - key: ui_reinstate_account_success_single_message
          value: QWNjb3VudCByZWluc3RhdGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_contact_content_label
          value: U3VwcG9ydCBJbmZvcm1hdGlvbg==
        - key: ui_reinstate_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHJlaW5zdGF0ZWQ6
        - key: ui_login_failed_error
          value: QXV0aGVudGljYXRpb24gZmFpbGVkLg==
        - key: ui_deny_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_menu_change_password_button
          value: Q2hhbmdlIFBhc3N3b3Jk
        - key: ui_create_accounts_guest_type_access_allowed_label
          value: QWNjZXNzIGFsbG93ZWQ6
        - key: ui_notices_status_failed_label
          value: RmFpbGVk
        - key: ui_notices_status_partial_success_label
          value: Q29tcGxldGUvRXJyb3Jz
        - key: ui_extend_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGV4dGVuZGV...
        - key: ui_create_known_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHByb3ZpZGVkLCBhY2NvdW50cyB3aWxsIGJlIGNyZWF0ZWQ...
        - key: ui_changepwd_cancel_button
          value: Q2FuY2Vs
        - key: ui_account_state_active_state_label
          value: QWN0aXZl
        - key: ui_post_access_instruction_message
          value: ''
        - key: ui_aup_content_label
          value: QWNjZXB0YWJsZSBVc2UgUG9saWN5
        - key: ui_delete_notice_success_single_message
          value: Tm90aWNlIGRlbGV0ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_create_accounts_access_info_minutes_label
          value: TWludXRlcw==
        - key: ui_to_time_label
          value: VG8gdGltZTo=
        - key: ui_resend_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgcmVzZW50IHN1Y2Nlc3NmdWxseS4=
        - key: ui_last_name_label
          value: TGFzdCBuYW1lOg==
        - key: ui_account_action_resend_button
          value: UmVzZW5k
        - key: ui_print_account_total_failure_message
          value: VW5hYmxlIHRvIHByaW50Lg==
        - key: ui_login_aup_text
          value: WW91IGFyZSByZXNwb25zaWJsZSBmb3IgbWFpbnRhaW5pbmcgdGhlIGNvbmZpZGVudGlhbGl0eSBvZiB0aGUgcGFzc3dvcmQgYW5...
        - key: ui_changepwd_optional_content_2
          value: ''
        - key: ui_deny_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgZGVuaWVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_email_address_label
          value: RW1haWwgYWRkcmVzczo=
        - key: ui_changepwd_optional_content_1
          value: ''
        - key: ui_column_location_header
          value: TG9jYXRpb24=
        - key: ui_date_picker_short_day_wednesday
          value: Vw==
        - key: ui_extend_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_approve_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGFwcHJvdmUgdGhpcyBhY2NvdW50Pw==
        - key: ui_create_random_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_reset_password_account_total_failure_message
          value: VW5hYmxlIHRvIHJlc2V0IHBhc3N3b3JkLg==
        - key: ui_contact_failure_code_label
          value: RmFpbHVyZSBjb2RlOg==
        - key: ui_date_picker_month_november
          value: Tm92ZW1iZXI=
        - key: ui_field_phone_error
          value: SW52YWxpZCBtb2JpbGUgbnVtYmVyIGZvcm1hdC4=
        - key: ui_reinstate_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_notification_language_label
          value: TGFuZ3VhZ2U6
        - key: ui_column_sms_provider_header
          value: U01TIFByb3ZpZGVy
        - key: ui_suspend_account_instruction_message
          value: ''
        - key: ui_account_state_pending_approval_state_label
          value: UGVuZGluZyBBcHByb3ZhbA==
        - key: ui_reinstate_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlaW5zdGF0ZSB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_notices_column_status_header
          value: U3RhdHVz
        - key: ui_deny_account_success_single_message
          value: QWNjb3VudCBkZW5pZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_unit_thursday
          value: VGh1cnNkYXk=
        - key: ui_list_refresh_button
          value: UmVmcmVzaA==
        - key: ui_notify_import_ok_button
          value: T2s=
        - key: ui_column_password_header
          value: UGFzc3dvcmQ=
        - key: ui_create_known_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGNyZWF0ZSB0aGVzZSBhY2NvdW50cz8=
        - key: ui_delete_notice_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGRlbGV0ZSB0aGlzIG5vdGljZT8=
        - key: ui_deny_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGRlbmllZDo=
        - key: ui_account_state_suspended_state_label
          value: U3VzcGVuZGVk
        - key: ui_field_date_dmy_error
          value: SW52YWxpZCBkYXRlIGZvcm1hdCAoZGQvbW0veXl5eSku
        - key: ui_delete_notice_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_email_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGVtYWlsIHRoaXMgYWNjb3VudD8=
        - key: ui_one_click_login_instruction
          value: UGxlYXNlIGVudGVyIHlvdXIgY3JlZGVudGlhbHMgdG8gYXBwcm92ZSBvciBkZW55IHRoZSBndWVzdCBhY2NvdW50Lg==
        - key: ui_notify_email_address_label
          value: U3BvbnNvcidzIEVtYWlsIGFkZHJlc3M=
        - key: ui_email_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgZW1haWxlZCBzdWNjZXNzZnVsbHku
        - key: ui_notices_empty_error
          value: Tm8gbm90aWNlcyBhdCB0aGlzIG1vbWVudC4=
        - key: ui_create_random_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgcmFuZG9tIGFjY291bnRzIHN1Y2Nlc3NmdWxseSBjcmVhdGVkOg==
        - key: ui_suspend_account_success_single_message
          value: QWNjb3VudCBzdXNwZW5kZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_date_picker_short_day_thursday
          value: VA==
        - key: ui_login_optional_content_1
          value: ''
        - key: ui_date_picker_title
          value: U2V0IERhdGU=
        - key: ui_suspend_account_total_failure_message
          value: VW5hYmxlIHRvIHN1c3BlbmQgYWNjb3VudC4=
        - key: ui_login_optional_content_2
          value: ''
        - key: ui_reset_password_ok_button
          value: T0s=
        - key: ui_field_date_range_unlimited_error
          value: VmFsaWQgZGF0ZXMgc3RhcnQgZnJvbSB7MH0=
        - key: ui_one_click_guest_link_expired
          value: TGluayBoYXMgZXhwaXJlZC4gUGxlYXNlIHNpZ24gb24gdG8gdGhlIHNwb25zb3IgcG9ydGFsIHRvIGFwcHJvdmUvZGVueSBndWV...
        - key: ui_post_access_message
          value: WW91IGNhbiBwcm92aWRlIG5ldHdvcmsgYWNjZXNzIHRvIG90aGVycy4gQmUgc3VyZSB0byBmb2xsb3cgeW91ciBjb21wYW55J3M...
        - key: ui_extend_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGV4dGVuZGVkOg==
        - key: ui_field_first_name_error
          value: UGxlYXNlIGVudGVyIGEgdmFsaWQgZmlyc3QgbmFtZS4=
        - key: ui_account_action_delete_button
          value: RGVsZXRl
        - key: ui_notify_import_send_summary_email_label
          value: U2VuZCBtZSBhIHN1bW1hcnkgb2YgaW1wb3J0
        - key: ui_extend_account_ok_button
          value: T2s=
        - key: ui_login_password_label
          value: UGFzc3dvcmQ6
        - key: ui_account_details_sponsor_label
          value: U3BvbnNvcjo=
        - key: ui_notify_random_done_button
          value: RG9uZQ==
        - key: ui_user_name_label
          value: VXNlcm5hbWU6
        - key: ui_approve_account_ok_button
          value: T0s=
        - key: ui_create_import_select_file_label
          value: U2VsZWN0IGZpbGU6
        - key: ui_reset_password_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlc2V0IHRoZSBwYXNzd29yZCBmb3IgdGhpcyBhY2NvdW50Pw==
        - key: ui_account_action_edit_button
          value: RWRpdA==
        - key: ui_contact_ip_address_label
          value: SVAgYWRkcmVzczo=
        - key: ui_password_label
          value: UGFzc3dvcmQ6
        - key: ui_extend_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgZXh0ZW5kZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_create_known_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGNyZWF0ZWQ6
        - key: ui_reset_password_notify_guests_label
          value: U2VuZCBndWVzdCBub3RpZmljYXRpb24gdXNpbmc6
        - key: ui_resend_account_success_single_message
          value: QWNjb3VudCByZXNlbnQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_create_random_success_single_message
          value: UmFuZG9tIGFjY291bnQgY3JlYXRlZCBzdWNjZXNzZnVsbHku
        - key: ui_delete_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_approve_accounts_filter_label
          value: UGVuZGluZyBhY2NvdW50cyBmb3VuZA==
        - key: ui_delete_notice_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2Ygbm90aWNlcyBzdWNjZXNzZnVsbHkgZGVsZXRlZDo=
        - key: ui_post_access_optional_content_1
          value: ''
        - key: ui_post_access_optional_content_2
          value: ''
        - key: ui_sms_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIG51bWJlciBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHRleHRlZCB...
        - key: ui_create_known_success_multi_message
          value: QWNjb3VudHMgY3JlYXRlZCBzdWNjZXNzZnVsbHku
        - key: ui_date_picker_month_march
          value: TWFyY2g=
        - key: ui_create_import_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGltcG9ydGVkOg==
        - key: ui_email_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIG51bWJlciBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGVtYWlsZWQ...
        - key: ui_create_accounts_back_button
          value: QmFjaw==
        - key: ui_notify_import_cancel_button
          value: Q2FuY2Vs
        - key: ui_delete_notice_total_failure_message
          value: VW5hYmxlIHRvIGRlbGV0ZSBub3RpY2VzLg==
        - key: ui_delete_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgZGVsZXRlZCBzdWNjZXNzZnVsbHku
        - key: ui_notify_print_label
          value: UHJpbnQ=
        - key: ui_account_action_suspend_button
          value: U3VzcGVuZA==
        - key: ui_reinstate_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_edit_accounts_cancel_button
          value: Q2FuY2Vs
        - key: ui_time_picker_title
          value: Q2hvb3NlIFRpbWU=
        - key: ui_notices_action_random_label
          value: Q3JlYXRlIFJhbmRvbSBBY2NvdW50cw==
        - key: ui_from_time_label
          value: RnJvbSB0aW1lOg==
        - key: ui_create_accounts_guest_type_access_limit_label
          value: TWF4aW11bSBhY2Nlc3MgZHVyYXRpb246
        - key: ui_changepwd_confirmpwd_label
          value: Q29uZmlybSBwYXNzd29yZDo=
        - key: ui_field_min_error
          value: RmllbGQgdmFsdWUgY2Fubm90IGJlIGxlc3MgdGhhbiB7MH0=
        - key: ui_create_import_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGltcG9ydCB0aGlzIGFjY291bnQ/
        - key: ui_create_random_success_multi_message
          value: UmFuZG9tIGFjY291bnRzIGNyZWF0ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_unit_hours
          value: aG91cnM=
        - key: ui_print_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHByaW50IHRoZSBzZWxlY3RlZCBhY2NvdW50cz8=
        - key: ui_footer_label
          value: ''
        - key: ui_login_instruction_message
          value: VXNlIHRoZSBTcG9uc29yIHBvcnRhbCB0byBtYW5hZ2UgZ3Vlc3QgYWNjb3VudHMuIFNpZ24gb24gd2l0aCB5b3VyIHVzZXJuYW1...
        - key: ui_one_click_login_to_other_portals
          value: VHJ5IHJlLWVudGVyaW5nIHlvdXIgY3JlZGVudGlhbHMgb3IgbG9nZ2luZyBpbiB0byB0aGUgc3BvbnNvciBwb3J0YWwgeW91IHV...
        - key: ui_sms_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHRleHQgdGhlIHNlbGVjdGVkIGFjY291bnRzPw==
        - key: ui_post_access_page_title
          value: UG9zdCBBY2Nlc3M=
        - key: ui_contact_page_title
          value: Q29udGFjdCBJbmZvcm1hdGlvbg==
        - key: ui_notify_guests_delivery_label
          value: RGVsaXZlciBub3RpZmljYXRpb24gdXNpbmc6
        - key: ui_suspend_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgc3VzcGVuZGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_guest_type_label
          value: R3Vlc3QgdHlwZTo=
        - key: ui_delete_notice_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGRlbGV0ZSB0aGUgc2VsZWN0ZWQgbm90aWNlcz8=
        - key: ui_unit_friday
          value: RnJpZGF5
        - key: ui_account_state_expired_state_label
          value: RXhwaXJlZA==
        - key: ui_login_aup_agreement_label
          value: QWdyZWUgdG8=
        - key: ui_create_accounts_next_button
          value: TmV4dA==
        - key: ui_reinstate_account_ok_button
          value: T2s=
        - key: ui_menu_home_button
          value: SG9tZQ==
        - key: ui_notices_column_accounts_num_header
          value: TnVtYmVyIG9mIEFjY291bnRz
        - key: ui_login_change_password_button
          value: SSB3YW50IHRvIGNoYW5nZSBteSBwYXNzd29yZCBhZnRlciBsb2dpbg==
        - key: ui_notices_column_start_time_header
          value: U3RhcnQ=
        - key: ui_extend_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGV4dGVuZCB0aGlzIGFjY291bnQ/
        - key: ui_login_content_label
          value: U2lnbiBPbg==
        - key: ui_email_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_aup_page_title
          value: QWNjZXB0YWJsZSBVc2UgUG9saWN5
        - key: ui_column_ssid_header
          value: U1NJRA==
        - key: ui_changepwd_policy_help_label
          value: UGFzc3dvcmRzIG11c3QgYmUgOCBjaGFyYWN0ZXJzIGFuZCBjb250YWluIGEgbGV0dGVyIGFuZCBudW1iZXIu
        - key: ui_deny_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbnkgYWNjZXNzIGZvciB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_approve_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgYXBwcm92ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_print_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IHByaW50ZWQ6
        - key: ui_delete_account_success_single_message
          value: QWNjb3VudCBkZWxldGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_list_sort_by_label
          value: U29ydCBieTo=
        - key: ui_sms_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHRleHQgdGhpcyBhY2NvdW50Pw==
        - key: ui_aup_optional_content_2
          value: ''
        - key: ui_column_person_visited_header
          value: UGVyc29uIEJlaW5nIFZpc2l0ZWQ=
        - key: ui_reinstate_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlaW5zdGF0ZSB0aGlzIGFjY291bnQ/
        - key: ui_contact_mac_address_label
          value: TUFDIGFkZHJlc3M6
        - key: ui_aup_optional_content_1
          value: ''
        - key: ui_error_instruction_message
          value: ''
        - key: ui_from_date_label
          value: RnJvbSBkYXRlICh5eXl5LW1tLWRkKTo=
        - key: ui_column_expiration_date_header
          value: RXhwaXJhdGlvbiBEYXRl
        - key: ui_date_picker_month_october
          value: T2N0b2Jlcg==
        - key: ui_contact_title_label
          value: Q29udGFjdCBJbmZvcm1hdGlvbg==
        - key: ui_column_group_tag_header
          value: R3JvdXAgVGFn
        - key: ui_resend_account_ok_button
          value: T0s=
        - key: ui_unit_days_symbol
          value: RA==
        - key: ui_print_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHByaW50IHRoaXMgYWNjb3VudD8=
        - key: ui_column_account_state_header
          value: U3RhdGU=
        - key: ui_sms_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_changepwd_instruction_message
          value: WW91IGFyZSByZXF1aXJlZCB0byBjaGFuZ2UgeW91ciBwYXNzd29yZCBub3cuIFBsZWFzZSBlbnRlciBhIG5ldyBwYXNzd29yZC4=
        - key: ui_unit_hours_symbol
          value: SA==
        - key: ui_field_last_name_error
          value: UGxlYXNlIGVudGVyIGEgdmFsaWQgbGFzdCBuYW1lLg==
        - key: ui_create_accounts_aup_link
          value: VGVybXMgYW5kIENvbmRpdGlvbnM=
        - key: ui_account_details_suspension_reason_label
          value: UmVhc29uIGZvciBzdXNwZW5zaW9uOg==
        - key: ui_no_user_error
          value: VXNlciBkb2Vzbid0IGV4aXN0Lg==
        - key: ui_create_accounts_access_info_location_label
          value: TG9jYXRpb246
        - key: ui_reinstate_account_total_failure_message
          value: VW5hYmxlIHRvIHJlaW5zdGF0ZSBhY2NvdW50Lg==
        - key: ui_reset_password_account_success_single_message
          value: QWNjb3VudCBwYXNzd29yZCByZXNldCBzdWNjZXNzZnVsbHku
        - key: ui_create_accounts_access_info_hours_label
          value: SG91cnM=
        - key: ui_notify_known_notify_button
          value: Tm90aWZ5
        - key: ui_create_import_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGltcG9ydCB0aGVzZSBhY2NvdW50cz8=
        - key: ui_home_page_title
          value: U3BvbnNvciBIb21l
        - key: ui_notify_known_auto_notify_text
          value: R3Vlc3Qgbm90aWZpY2F0aW9ucyBhcmUgc2VudCBhdXRvbWF0aWNhbGx5
        - key: ui_unit_pm
          value: UE0=
        - key: ui_reason_visit_label
          value: UmVhc29uIGZvciB2aXNpdDo=
        - key: ui_approve_accounts_content_label
          value: UGVuZGluZyBBY2NvdW50cw==
        - key: ui_column_notification_language_header
          value: TGFuZ3VhZ2U=
        - key: ui_column_guest_type_header
          value: R3Vlc3QgVHlwZQ==
        - key: ui_aup_instruction_message
          value: UGxlYXNlIHJlYWQgdGhlIEFjY2VwdGFibGUgVXNlIFBvbGljeS4=
        - key: ui_reset_password_account_success_multi_message
          value: U2VsZWN0ZWQgYWNjb3VudHMgcGFzc3dvcmQgcmVzZXQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_unit_am
          value: QU0=
        - key: ui_resend_account_total_failure_message
          value: VW5hYmxlIHRvIHJlc2VuZCBpbmZvcm1hdGlvbi4=
        - key: ui_unit_saturday
          value: U2F0dXJkYXk=
        - key: ui_portal_label
          value: UG9ydGFsIE5hbWU=
        - key: ui_notify_known_cancel_button
          value: Q2FuY2Vs
        - key: ui_print_account_success_single_message
          value: QWNjb3VudCBwcmludGVkIHN1Y2Nlc3NmdWxseS4=
        - key: ui_create_random_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGNyZWF0ZSB0aGVzZSByYW5kb20gYWNjb3VudHM/
        - key: ui_account_action_print_button
          value: UHJpbnQ=
        - key: ui_edit_accounts_save_button
          value: U2F2ZQ==
        - key: ui_reset_password_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlc2V0IHRoZSBwYXNzd29yZCBmb3IgdGhlIHNlbGVjdGVkIGFjY291bnRzPw==
        - key: ui_home_instruction_message
          value: Q3JlYXRlLCBtYW5hZ2UsIGFuZCBhcHByb3ZlIGd1ZXN0IGFjY291bnRzLg==
        - key: ui_column_reason_visit_header
          value: UmVhc29uIGZvciBWaXNpdA==
        - key: ui_guest_duration_error
          value: VGhlIHBlcmlvZCBiZXR3ZWVuIHN0YXJ0IGFuZCBlbmQgZGF0ZSBleGNlZWRzIG1heGltdW0gZHVyYXRpb24gY29uZmlndXJlZCB...
        - key: ui_notices_action_sms_label
          value: VGV4dCBHdWVzdHM=
        - key: ui_create_accounts_guest_type_device_limit_label
          value: TWF4aW11bSBkZXZpY2VzIHRoYXQgY2FuIGJlIGNvbm5lY3RlZDo=
        - key: ui_create_accounts_access_info_to_time_label
          value: VG8gVGltZQ==
        - key: ui_time_left_label
          value: VGltZSBsZWZ0Og==
        - key: ui_user_last_login_pass_time_label
          value: TGFzdCBMb2dpbjo=
        - key: ui_email_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGVtYWlsIHRoZSBzZWxlY3RlZCBhY2NvdW50cz8=
        - key: ui_create_random_prefix_label
          value: VXNlcm5hbWUgcHJlZml4Og==
        - key: ui_approve_account_total_failure_message
          value: VW5hYmxlIHRvIGFwcHJvdmUgYWNjb3VudC4=
        - key: ui_manage_accounts_content_label
          value: TWFuYWdlIEFjY291bnRz
        - key: ui_notify_content_label
          value: QWNjb3VudCBJbmZvcm1hdGlvbg==
        - key: ui_login_signon_button
          value: U2lnbiBPbg==
        - key: ui_delete_notice_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBub3RpY2VzIHdlcmUgc2VsZWN0ZWQuIE5vdGljZXMgd2lsbCBiZSBkZWxldGVkIGl...
        - key: ui_error_page_title
          value: RXJyb3I=
        - key: ui_create_import_total_failure_message_suffix
          value: VGhlIGltcG9ydCBmaWxlIG1heSBjb250YWluIGFkZGl0aW9uYWwgZXJyb3JzLCBidXQgdGhlIGltcG9ydCBvcGVyYXRpb24gZGl...
        - key: ui_approve_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_contact_sessioninfo_text
          value: VGhlIGZvbGxvd2luZyBpbmZvcm1hdGlvbiBtaWdodCBiZSB1c2VmdWwgdG8gdGhlIEhlbHAgRGVzayByZXByZXNlbnRhdGl2ZSB...
        - key: ui_column_creation_date_header
          value: Q3JlYXRpb24gRGF0ZQ==
        - key: ui_home_title_label
          value: U3BvbnNvciBQb3J0YWw=
        - key: ui_edit_accounts_content_label
          value: RWRpdCBBY2NvdW50
        - key: ui_date_picker_month_april
          value: QXByaWw=
        - key: ui_email_account_total_failure_message
          value: VW5hYmxlIHRvIHNlbmQgZW1haWwu
        - key: ui_notices_action_print_label
          value: Q3JlYXRlIFByaW50IEpvYg==
        - key: ui_column_last_name_header
          value: TGFzdCBOYW1l
        - key: ui_create_import_success_single_message
          value: QWNjb3VudCBpbXBvcnRlZCBzdWNjZXNzZnVsbHku
        - key: ui_create_import_async_message
          value: QWNjb3VudCBpbXBvcnRpbmcgd2lsbCBiZSBwcm9jZXNzZWQgaW4gdGhlIGJhY2tncm91bmQuIENoZWNrIE5vdGljZXMgZm9yIHN...
        - key: ui_extend_account_success_single_message
          value: QWNjb3VudCBleHRlbmRlZCBzdWNjZXNzZnVsbHku
        - key: ui_unit_minutes_symbol
          value: TQ==
        - key: ui_notify_sms_label
          value: U01T
        - key: ui_extend_account_cancel_button
          value: Q2FuY2Vs
        - key: ui_unit_days
          value: ZGF5cw==
        - key: ui_create_import_tab_label
          value: SW1wb3J0
        - key: ui_to_label
          value: VG86
        - key: ui_changepwd_currentpwd_label
          value: Q3VycmVudCBwYXNzd29yZDo=
        - key: ui_column_time_left_header
          value: VGltZSBMZWZ0
        - key: ui_account_action_approve_button
          value: QXBwcm92ZQ==
        - key: ui_create_known_instruction_message
          value: ''
        - key: ui_create_known_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGNyZWF0ZSB0aGlzIGFjY291bnQ/
        - key: ui_reinstate_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHJlaW5zdGF...
        - key: ui_date_picker_month_december
          value: RGVjZW1iZXI=
        - key: ui_notify_import_accounts_showing_label
          value: U2hvd2luZzog
        - key: ui_one_click_guest_link_invalid
          value: TGluayBpcyBpbnZhbGlkLiBQbGVhc2Ugc2lnbiBvbiB0byB0aGUgc3BvbnNvciBwb3J0YWwgdG8gYXBwcm92ZS9kZW55IGd1ZXN...
        - key: ui_date_picker_calendar_header_format
          value: JUIgJVk=
        - key: ui_resend_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHJlc2VudCB...
        - key: ui_field_email_error
          value: RW50ZXIgYSB2YWxpZCBlbWFpbCBhZGRyZXNzLg==
        - key: ui_suspend_account_reason_label
          value: UmVhc29uIGZvciBzdXNwZW5zaW9uOg==
        - key: ui_creation_date_label
          value: Q3JlYXRpb24gZGF0ZTo=
        - key: ui_field_date_range_limited_error
          value: VmFsaWQgZGF0ZXMgYXJlIHswfSB0byB7MX0=
        - key: ui_date_picker_short_day_tuesday
          value: VA==
        - key: ui_menu_switch_mobile_button
          value: U3dpdGNoIHRvIG1vYmlsZSBtb2Rl
        - key: ui_suspend_account_partial_failure_message
          value: TnVtYmVyIG9mIGVycm9yczo=
        - key: ui_deny_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIGRlbmllZCB...
        - key: ui_person_visited_label
          value: UGVyc29uIGJlaW5nIHZpc2l0ZWQgKGVtYWlsKTo=
        - key: ui_create_import_success_multi_message
          value: QWNjb3VudHMgaW1wb3J0ZWQgc3VjY2Vzc2Z1bGx5Lg==
        - key: ui_changepwd_newpwd_label
          value: TmV3IHBhc3N3b3JkOg==
        - key: ui_column_guest_location_header
          value: TG9jYXRpb24=
        - key: ui_field_digit_error
          value: RW50ZXIgYSB2YWxpZCBudW1iZXIu
        - key: ui_date_picker_short_day_sunday
          value: Uw==
        - key: ui_create_accounts_guest_info_content_label
          value: R3Vlc3QgSW5mb3JtYXRpb24=
        - key: ui_unit_minutes
          value: bWludXRlcw==
        - key: ui_account_action_extend_button
          value: RXh0ZW5k
        - key: ui_account_details_account_state_label
          value: U3RhdGU6
        - key: ui_from_label
          value: RnJvbQ==
        - key: ui_extend_account_instruction_message
          value: ''
        - key: ui_account_details_done_button
          value: RG9uZQ==
        - key: ui_unit_tuesday
          value: VHVlc2RheQ==
        - key: ui_notify_import_auto_notify_text
          value: R3Vlc3Qgbm90aWZpY2F0aW9ucyBhcmUgc2VudCBhdXRvbWF0aWNhbGx5
        - key: ui_company_label
          value: Q29tcGFueTo=
        - key: ui_date_picker_month_january
          value: SmFudWFyeQ==
        - key: ui_sms_account_total_failure_message
          value: VW5hYmxlIHRvIHNlbmQgdGV4dC4=
        - key: ui_delete_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGRlbGV0ZWQ6
        - key: ui_delete_account_ok_button
          value: T0s=
        - key: ui_notify_random_accounts_created_label
          value: QWNjb3VudHMgY3JlYXRlZDog
        - key: ui_notices_delete_button
          value: RGVsZXRlIE5vdGljZQ==
        - key: ui_create_known_tab_label
          value: S25vd24=
        - key: ui_extend_account_confirm_multi_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGV4dGVuZCB0aGUgc2VsZWN0ZWQgYWNjb3VudHM/
        - key: ui_create_accounts_access_info_to_date_label
          value: VG8gRGF0ZSAoeXl5eS1tbS1kZCk=
        - key: ui_time_picker_button
          value: U2V0IFRpbWU=
        - key: ui_post_access_continue_button
          value: Q29udGludWU=
        - key: ui_javascript_disabled_message
          value: WW91IG11c3QgdHVybiBvbiBKYXZhU2NyaXB0IHRvIHVzZSB0aGlzIHdlYiBzaXRlLg==
        - key: ui_field_date_ymd_error
          value: SW52YWxpZCBkYXRlIGZvcm1hdCAoeXl5eS1tbS1kZCku
        - key: ui_create_import_download_template_link
          value: RG93bmxvYWQgVGVtcGxhdGU=
        - key: ui_contact_policy_server_label
          value: UG9saWN5IHNlcnZlcjo=
        - key: ui_prefix_mismatch_policy_error
          value: UHJlZml4IGRpZCBub3QgbWF0Y2ggVXNlcm5hbWUgUG9saWN5
        - key: ui_column_company_header
          value: Q29tcGFueQ==
        - key: ui_notify_import_accounts_created_label
          value: QWNjb3VudHMgY3JlYXRlZDog
        - key: ui_date_picker_month_september
          value: U2VwdGVtYmVy
        - key: ui_reset_password_account_async_message
          value: QmVjYXVzZSBhIGxhcmdlIGFtb3VudCBvZiBhY2NvdW50cyB3ZXJlIHNlbGVjdGVkLCBhY2NvdW50cyB3aWxsIGJlIHBhc3N3b3J...
        - key: ui_delete_account_total_failure_message
          value: VW5hYmxlIHRvIGRlbGV0ZSBhY2NvdW50Lg==
        - key: ui_create_accounts_create_button
          value: Q3JlYXRl
        - key: ui_contact_helpdesk_title
          value: SGVscCBEZXNrIEluZm9ybWF0aW9u
        - key: ui_notify_known_done_button
          value: RG9uZQ==
        - key: ui_notices_done_button
          value: RG9uZQ==
        - key: ui_phone_number_label
          value: TW9iaWxlIG51bWJlcjo=
        - key: ui_column_email_address_header
          value: RW1haWwgQWRkcmVzcw==
        - key: ui_deny_account_total_failure_message
          value: VW5hYmxlIHRvIGRlbnkgYWNjb3VudC4=
        - key: ui_email_mismatch_policy_error
          value: RW1haWwgZGlkIG5vdCBtYXRjaCBVc2VybmFtZSBQb2xpY3k=
        - key: ui_aup_decline_button
          value: RGVjbGluZQ==
        - key: ui_changepwd_username_label
          value: VXNlcm5hbWU6
        - key: ui_notify_random_accounts_showing_label
          value: U2hvd2luZzog
        - key: ui_notices_content_label
          value: Tm90aWNlcw==
        - key: ui_account_action_deny_button
          value: RGVueQ==
        - key: ui_delete_account_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGRlbGV0ZSB0aGlzIGFjY291bnQ/
        - key: ui_field_max_error
          value: RmllbGQgdmFsdWUgY2Fubm90IGJlIGdyZWF0ZXIgdGhhbiB7MH0=
        - key: ui_contact_message
          value: Q29udGFjdCBJbmZvcm1hdGlvbg==
        - key: ui_approve_account_partial_success_message
          value: U29tZSBlcnJvcnMgb2NjdXJyZWQuIFRoZSBudW1iZXIgb2YgYWNjb3VudHMgc3VjY2Vzc2Z1bGx5IGFwcHJvdmVkOg==
        - key: ui_create_accounts_guest_type_content_label
          value: R3Vlc3QgdHlwZTo=
        - key: ui_unit_monday
          value: TW9uZGF5
        - key: ui_create_accounts_access_info_ssid_label
          value: U1NJRDo=
        - key: ui_invalid_input_error
          value: SW52YWxpZCBpbnB1dC4=
        - key: ui_banner_label
          value: U3BvbnNvciBQb3J0YWw=
        - key: ui_date_label
          value: RGF0ZTo=
        - key: ui_create_import_instruction_message
          value: Q2xpY2sgdG8gZG93bmxvYWQgdGhlIGltcG9ydCB0ZW1wbGF0ZSBmaWxlLg==
        - key: ui_create_random_confirm_single_message
          value: QXJlIHlvdSBzdXJlIHlvdSB3YW50IGNyZWF0ZSB0aGlzIHJhbmRvbSBhY2NvdW50Pw==
        - key: ui_firstname_mismatch_policy_error
          value: Rmlyc3ROYW1lIGRpZCBub3QgbWF0Y2ggVXNlcm5hbWUgUG9saWN5
        - key: ui_date_picker_short_day_saturday
          value: Uw==
      portalTheme:
        id: 9eb421c0-8c01-11e6-996c-525400b48521
        name: Default Blue theme
      portalTweakSettings: {}
    description: Default portal used by sponsors to create and manage accounts for authorized
      visitors to securely access the network
    id: bd48c1a1-9477-4746-8e40-e43d20c9f429
    name: Sponsor Portal (default)
    portalTestUrl: https://198.18.133.27:8445/sponsorportal/PortalSetup.action?portal=bd48c1a1-9477-4746-8e40-e43d20...
    portalType: SPONSOR
    settings:
      aupSettings:
        displayFrequency: FIRSTLOGIN
        includeAup: true
        requireScrolling: false
      loginPageSettings:
        includeAup: false
        maxFailedAttemptsBeforeRateLimit: 5
        requireAupScrolling: false
        socialConfigs: []
        timeBetweenLoginsDuringRateLimit: 2
      portalSettings:
        allowedInterfaces:
        - eth0
        - bond0
        authenticationMethod: 92faba60-8c01-11e6-996c-525400b48521
        availableSsids: []
        certificateGroupTag: Default Portal Certificate Group
        displayLang: USEBROWSERLOCALE
        fallbackLanguage: English
        httpsPort: 8445
        idleTimeout: 10
      postLoginBannerSettings:
        includePostAccessBanner: false
      sponsorChangePasswordSettings:
        allowSponsorToChangePwd: false
      supportInfoSettings:
        emptyFieldDisplay: HIDE
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: false

- name: Delete by id
  cisco.ise.sponsor_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
