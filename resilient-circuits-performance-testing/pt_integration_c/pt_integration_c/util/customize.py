# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for pt_integration_c"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the pt_integration_c package"""
    reload_params = {"package": u"pt_integration_c",
                    "incident_fields": [u"pt_int_c_delay", u"pt_int_c_num_artifacts", u"pt_int_c_num_runs", u"pt_int_c_sample_data"], 
                    "action_fields": [u"delay", u"num_artifacts", u"num_runs", u"sample_data"], 
                    "function_params": [u"pt_int_artifact_description", u"pt_int_artifact_id", u"pt_int_artifact_value", u"pt_int_delay", u"pt_int_num_artifacts", u"pt_int_num_runs", u"pt_int_sample_data"], 
                    "datatables": [], 
                    "message_destinations": [u"pt_integration_c"], 
                    "functions": [u"pt_integration_c_process_added_artifact", u"pt_integration_c_run"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [u"PT Integration C: Set Custom Fields"], 
                    "workflows": [u"pt_integration_c_process_added_artifact", u"pt_integration_c_run"], 
                    "actions": [u"PT Integration C: Process Artifact", u"PT Integration C: Run", u"PT Integration C: Start"], 
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Incident fields:
    #     pt_int_c_delay
    #     pt_int_c_num_artifacts
    #     pt_int_c_num_runs
    #     pt_int_c_sample_data
    #   Action fields:
    #     delay
    #     num_artifacts
    #     num_runs
    #     sample_data
    #   Function inputs:
    #     pt_int_artifact_description
    #     pt_int_artifact_id
    #     pt_int_artifact_value
    #     pt_int_delay
    #     pt_int_num_artifacts
    #     pt_int_num_runs
    #     pt_int_sample_data
    #   Message Destinations:
    #     pt_integration_c
    #   Functions:
    #     pt_integration_c_process_added_artifact
    #     pt_integration_c_run
    #   Scripts:
    #     PT Integration C: Set Custom Fields
    #   Workflows:
    #     pt_integration_c_process_added_artifact
    #     pt_integration_c_run
    #   Rules:
    #     PT Integration C: Process Artifact
    #     PT Integration C: Run
    #     PT Integration C: Start


    yield ImportDefinition(u"""
eyJncm91cHMiOiBudWxsLCAibG9jYWxlIjogbnVsbCwgIndvcmtmbG93cyI6IFt7ImRlc2NyaXB0
aW9uIjogIiIsICJ3b3JrZmxvd19pZCI6IDM3LCAidGFncyI6IFtdLCAib2JqZWN0X3R5cGUiOiAi
aW5jaWRlbnQiLCAiZXhwb3J0X2tleSI6ICJwdF9pbnRlZ3JhdGlvbl9jX3J1biIsICJ1dWlkIjog
ImIyOGRjNjMwLTYyM2ItNDczMS1hYWM0LWM4YmY0ZDFiNGE2MiIsICJhY3Rpb25zIjogW10sICJj
b250ZW50IjogeyJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThc
Ij8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEw
MDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4v
MjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIw
MTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEw
MDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1u
XCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4
c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5h
bWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwicHRf
aW50ZWdyYXRpb25fY19ydW5cIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIlBUIEludGVn
cmF0aW9uIEM6IFJ1blwiPjxkb2N1bWVudGF0aW9uLz48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZl
bnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMTUzc2hoYjwvb3V0Z29pbmc+PC9z
dGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzAzdDRoamdcIiBuYW1lPVwi
UFQgSW50ZWdyYXRpb24gQzogUnVuXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRl
bnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI5ODFkZWQ5Yi01NmQ0LTQ5
MmMtODAxOS02OTZlZGY5ZmE3YTBcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19z
Y3JpcHRcIjpcIlxcbnJlc3VsdHNfY29udGVudCA9IHJlc3VsdHMuY29udGVudFxcblxcbiMgQWRk
IGFsbCBBcnRpZmFjdHNcXG5mb3IgYSBpbiByZXN1bHRzX2NvbnRlbnQuYXJ0aWZhY3RzX3RvX2Ny
ZWF0ZTpcXG4gIFxcbiAgYXJ0aWZhY3RfZGVzY3JpcHRpb24gPSB1XFxcInswfVxcXFxuXFxcXG57
MX1cXFxcblxcXFxuezJ9XFxcIi5mb3JtYXQoXFxcIiUlX19QVF9JTlRfQ19fJSVcXFwiLCBhLmRl
c2NyaXB0aW9uLCByZXN1bHRzX2NvbnRlbnQuc2FtcGxlX2RhdGEpXFxuICBcXG4gIGluY2lkZW50
LmFkZEFydGlmYWN0KFxcXCJTdHJpbmdcXFwiLCBhLnZhbHVlLCBhcnRpZmFjdF9kZXNjcmlwdGlv
bilcXG4gIFxcbiMgVXBkYXRlIG51bV9ydW5zXFxuaW5jaWRlbnQucHJvcGVydGllcy5wdF9pbnRf
Y19udW1fcnVucyA9IHJlc3VsdHNfY29udGVudC5yZW1haW5pbmdfcnVuc1wiLFwicHJlX3Byb2Nl
c3Npbmdfc2NyaXB0XCI6XCJcXG5pbnB1dHMucHRfaW50X251bV9hcnRpZmFjdHMgPSBpbmNpZGVu
dC5wcm9wZXJ0aWVzLnB0X2ludF9jX251bV9hcnRpZmFjdHNcXG5pbnB1dHMucHRfaW50X251bV9y
dW5zID0gaW5jaWRlbnQucHJvcGVydGllcy5wdF9pbnRfY19udW1fcnVuc1xcbmlucHV0cy5wdF9p
bnRfZGVsYXkgPSBpbmNpZGVudC5wcm9wZXJ0aWVzLnB0X2ludF9jX2RlbGF5XFxuaW5wdXRzLnB0
X2ludF9zYW1wbGVfZGF0YSA9IGluY2lkZW50LnByb3BlcnRpZXMucHRfaW50X2Nfc2FtcGxlX2Rh
dGEuY29udGVudFwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGlu
Y29taW5nPlNlcXVlbmNlRmxvd18wMDd6bmhtPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VG
bG93XzFpdTA0NHc8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PGVuZEV2ZW50IGlkPVwiRW5kRXZl
bnRfMGxxcDhnMFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMWl1MDQ0dzwvaW5jb21pbmc+PGlu
Y29taW5nPlNlcXVlbmNlRmxvd18xcHlzZm80PC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5j
ZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMWl1MDQ0d1wiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNr
XzAzdDRoamdcIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8wbHFwOGcwXCIvPjxzZXF1ZW5jZUZsb3cg
aWQ9XCJTZXF1ZW5jZUZsb3dfMTUzc2hoYlwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4
bVwiIHRhcmdldFJlZj1cIkV4Y2x1c2l2ZUdhdGV3YXlfMXVyYnR3bFwiLz48ZXhjbHVzaXZlR2F0
ZXdheSBpZD1cIkV4Y2x1c2l2ZUdhdGV3YXlfMXVyYnR3bFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZs
b3dfMTUzc2hoYjwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wMDd6bmhtPC9vdXRn
b2luZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzFweXNmbzQ8L291dGdvaW5nPjwvZXhjbHVzaXZl
R2F0ZXdheT48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzAwN3puaG1cIiBuYW1lPVwi
aWYgbnVtX3J1bnMgICZndDsgMFwiIHNvdXJjZVJlZj1cIkV4Y2x1c2l2ZUdhdGV3YXlfMXVyYnR3
bFwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzAzdDRoamdcIj48Y29uZGl0aW9uRXhwcmVzc2lv
biBsYW5ndWFnZT1cInJlc2lsaWVudC1jb25kaXRpb25zXCIgeHNpOnR5cGU9XCJ0Rm9ybWFsRXhw
cmVzc2lvblwiPjwhW0NEQVRBW3tcImNvbmRpdGlvbnNcIjpbe1wiZXZhbHVhdGlvbl9pZFwiOjEs
XCJmaWVsZF9uYW1lXCI6XCJpbmNpZGVudC5wcm9wZXJ0aWVzLnB0X2ludF9jX251bV9ydW5zXCIs
XCJtZXRob2RcIjpcImd0XCIsXCJ0eXBlXCI6bnVsbCxcInZhbHVlXCI6MH1dLFwiY3VzdG9tX2Nv
bmRpdGlvblwiOlwiXCIsXCJsb2dpY190eXBlXCI6XCJhbGxcIn1dXT48L2NvbmRpdGlvbkV4cHJl
c3Npb24+PC9zZXF1ZW5jZUZsb3c+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xcHlz
Zm80XCIgc291cmNlUmVmPVwiRXhjbHVzaXZlR2F0ZXdheV8xdXJidHdsXCIgdGFyZ2V0UmVmPVwi
RW5kRXZlbnRfMGxxcDhnMFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQ
TU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwi
IGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0
RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5k
cyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMzkxXCIgeT1cIjE4OFwiLz48YnBtbmRp
OkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjM4
NlwiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBt
bmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzAzdDRoamdcIiBpZD1cIlNl
cnZpY2VUYXNrXzAzdDRoamdfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9
XCIxMDBcIiB4PVwiNjQ1XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpC
UE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8wbHFwOGcwXCIgaWQ9XCJFbmRFdmVudF8w
bHFwOGcwX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwi
ODU3XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjEzXCIgd2lkdGg9XCIwXCIgeD1cIjg3NVwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVs
PjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVu
Y2VGbG93XzFpdTA0NHdcIiBpZD1cIlNlcXVlbmNlRmxvd18xaXUwNDR3X2RpXCI+PG9tZ2RpOndh
eXBvaW50IHg9XCI3NDVcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21n
ZGk6d2F5cG9pbnQgeD1cIjg1N1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIv
PjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBc
IiB4PVwiODAxXCIgeT1cIjE4NC41XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1O
RWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzE1M3NoaGJc
IiBpZD1cIlNlcXVlbmNlRmxvd18xNTNzaGhiX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0Mjdc
IiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1c
IjQ5NFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxh
YmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNDYwLjVcIiB5
PVwiMTg0LjVcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6
QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRXhjbHVzaXZlR2F0ZXdheV8xdXJidHdsXCIgaWQ9XCJF
eGNsdXNpdmVHYXRld2F5XzF1cmJ0d2xfZGlcIiBpc01hcmtlclZpc2libGU9XCJ0cnVlXCI+PG9t
Z2RjOkJvdW5kcyBoZWlnaHQ9XCI1MFwiIHdpZHRoPVwiNTBcIiB4PVwiNDk0XCIgeT1cIjE4MVwi
Lz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIw
XCIgeD1cIjUxOVwiIHk9XCIyMzRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5T
aGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzAwN3puaG1c
IiBpZD1cIlNlcXVlbmNlRmxvd18wMDd6bmhtX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI1NDRc
IiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1c
IjY0NVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxh
YmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjc5XCIgeD1cIjU1NVwiIHk9
XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBN
TkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMXB5c2ZvNFwiIGlkPVwiU2VxdWVuY2VG
bG93XzFweXNmbzRfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjUxOVwiIHhzaTp0eXBlPVwib21n
ZGM6UG9pbnRcIiB5PVwiMjMxXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTE5XCIgeHNpOnR5cGU9
XCJvbWdkYzpQb2ludFwiIHk9XCIyOTVcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI4NzVcIiB4c2k6
dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI5NVwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjg3NVwi
IHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjI0XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxv
bWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNjk3XCIgeT1cIjI3My41
XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxh
bmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4iLCAid29ya2Zsb3dfaWQiOiAi
cHRfaW50ZWdyYXRpb25fY19ydW4iLCAidmVyc2lvbiI6IDN9LCAiY3JlYXRvcl9pZCI6ICJhZG1p
bkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX2J5IjogImFkbWluQGV4YW1wbGUuY29tIiwg
Imxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NzYxNTMxMzkwMDMsICJjb250ZW50X3ZlcnNpb24iOiAz
LCAicHJvZ3JhbW1hdGljX25hbWUiOiAicHRfaW50ZWdyYXRpb25fY19ydW4iLCAibmFtZSI6ICJQ
VCBJbnRlZ3JhdGlvbiBDOiBSdW4ifSwgeyJkZXNjcmlwdGlvbiI6ICIiLCAid29ya2Zsb3dfaWQi
OiAzOCwgInRhZ3MiOiBbXSwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgImV4cG9ydF9rZXki
OiAicHRfaW50ZWdyYXRpb25fY19wcm9jZXNzX2FkZGVkX2FydGlmYWN0IiwgInV1aWQiOiAiMjRl
YjdiNzctM2ZjYy00Y2FlLWFmODMtZmIyMGRiNTA3YTViIiwgImFjdGlvbnMiOiBbXSwgImNvbnRl
bnQiOiB7InhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48
ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0
L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEw
MDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1
MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0
L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4
bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1c
Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNw
YWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJwdF9pbnRl
Z3JhdGlvbl9jX3Byb2Nlc3NfYWRkZWRfYXJ0aWZhY3RcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIg
bmFtZT1cIlBUIEludGVncmF0aW9uIEM6IFByb2Nlc3MgQWRkZWQgQXJ0aWZhY3RcIj48ZG9jdW1l
bnRhdGlvbi8+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+
U2VxdWVuY2VGbG93XzB3OW10c2g8L291dGdvaW5nPjwvc3RhcnRFdmVudD48ZW5kRXZlbnQgaWQ9
XCJFbmRFdmVudF8xNTFsOGpsXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18xb2Fwa3JjPC9pbmNv
bWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMHc5bXRzaFwi
IHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNr
XzBqN2k3ZTBcIi8+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMGo3aTdlMFwiIG5hbWU9
XCJQVCBJbnRlZ3JhdGlvbiBDOiBQcm9jZXNzIEFkZGVkIEEuLi5cIiByZXNpbGllbnQ6dHlwZT1c
ImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1c
IjI3MjVhMzZjLWI3YmUtNDc5NC05YTM1LWU4NjEwNjk4N2M2YVwiPntcImlucHV0c1wiOnt9LFwi
cHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJpbnB1dHMucHRfaW50X2FydGlmYWN0X2lkID0gYXJ0
aWZhY3QuaWRcXG5pbnB1dHMucHRfaW50X2FydGlmYWN0X2Rlc2NyaXB0aW9uID0gYXJ0aWZhY3Qu
ZGVzY3JpcHRpb24uY29udGVudFxcbmlucHV0cy5wdF9pbnRfYXJ0aWZhY3RfdmFsdWUgPSBhcnRp
ZmFjdC52YWx1ZVwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGlu
Y29taW5nPlNlcXVlbmNlRmxvd18wdzltdHNoPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VG
bG93XzFvYXBrcmM8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNl
cXVlbmNlRmxvd18xb2Fwa3JjXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMGo3aTdlMFwiIHRh
cmdldFJlZj1cIkVuZEV2ZW50XzE1MWw4amxcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdy
YW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1
bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1l
bnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxv
bWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjM2NVwiIHk9XCIxNjlc
Ii8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5
MFwiIHg9XCIzNjBcIiB5PVwiMjA0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1O
U2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8xNTFsOGpsXCIg
aWQ9XCJFbmRFdmVudF8xNTFsOGpsX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdp
ZHRoPVwiMzZcIiB4PVwiOTc4XCIgeT1cIjE2OVwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6
Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjk5NlwiIHk9XCIyMDhcIi8+PC9i
cG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5F
bGVtZW50PVwiU2VxdWVuY2VGbG93XzB3OW10c2hcIiBpZD1cIlNlcXVlbmNlRmxvd18wdzltdHNo
X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MDFcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIg
eT1cIjE4N1wiLz48b21nZGk6d2F5cG9pbnQgeD1cIjYyN1wiIHhzaTp0eXBlPVwib21nZGM6UG9p
bnRcIiB5PVwiMTg3XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwi
MTNcIiB3aWR0aD1cIjBcIiB4PVwiNTE0XCIgeT1cIjE2NS41XCIvPjwvYnBtbmRpOkJQTU5MYWJl
bD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZp
Y2VUYXNrXzBqN2k3ZTBcIiBpZD1cIlNlcnZpY2VUYXNrXzBqN2k3ZTBfZGlcIj48b21nZGM6Qm91
bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiNjI3XCIgeT1cIjE0N1wiLz48L2Jw
bW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxv
d18xb2Fwa3JjXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMW9hcGtyY19kaVwiPjxvbWdkaTp3YXlwb2lu
dCB4PVwiNzI3XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxODdcIi8+PG9tZ2RpOndh
eXBvaW50IHg9XCI5NzhcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjE4N1wiLz48YnBt
bmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1c
Ijg1Mi41XCIgeT1cIjE2NVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+
PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+Iiwg
IndvcmtmbG93X2lkIjogInB0X2ludGVncmF0aW9uX2NfcHJvY2Vzc19hZGRlZF9hcnRpZmFjdCIs
ICJ2ZXJzaW9uIjogMn0sICJjcmVhdG9yX2lkIjogImFkbWluQGV4YW1wbGUuY29tIiwgImxhc3Rf
bW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjog
MTU3NjE1MzAxNjI4MywgImNvbnRlbnRfdmVyc2lvbiI6IDIsICJwcm9ncmFtbWF0aWNfbmFtZSI6
ICJwdF9pbnRlZ3JhdGlvbl9jX3Byb2Nlc3NfYWRkZWRfYXJ0aWZhY3QiLCAibmFtZSI6ICJQVCBJ
bnRlZ3JhdGlvbiBDOiBQcm9jZXNzIEFkZGVkIEFydGlmYWN0In1dLCAiYWN0aW9ucyI6IFt7InRp
bWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAidHlwZSI6
IDAsICJuYW1lIjogIlBUIEludGVncmF0aW9uIEM6IFByb2Nlc3MgQXJ0aWZhY3QiLCAidGFncyI6
IFtdLCAidmlld19pdGVtcyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJ3b3JrZmxvd3MiOiBbInB0
X2ludGVncmF0aW9uX2NfcHJvY2Vzc19hZGRlZF9hcnRpZmFjdCJdLCAibG9naWNfdHlwZSI6ICJh
bGwiLCAiZXhwb3J0X2tleSI6ICJQVCBJbnRlZ3JhdGlvbiBDOiBQcm9jZXNzIEFydGlmYWN0Iiwg
InV1aWQiOiAiZTcyZmZlNDYtMmJjNC00MWMxLThkOGQtZjViODUxZjhjZmEyIiwgImF1dG9tYXRp
b25zIjogW10sICJjb25kaXRpb25zIjogW3sidHlwZSI6IG51bGwsICJldmFsdWF0aW9uX2lkIjog
bnVsbCwgImZpZWxkX25hbWUiOiAiYXJ0aWZhY3QuZGVzY3JpcHRpb24iLCAibWV0aG9kIjogImNv
bnRhaW5zIiwgInZhbHVlIjogIiUlX19QVF9JTlRfQ19fJSUifSwgeyJ0eXBlIjogbnVsbCwgImV2
YWx1YXRpb25faWQiOiBudWxsLCAiZmllbGRfbmFtZSI6IG51bGwsICJtZXRob2QiOiAib2JqZWN0
X2FkZGVkIiwgInZhbHVlIjogbnVsbH1dLCAiaWQiOiA1MywgIm1lc3NhZ2VfZGVzdGluYXRpb25z
IjogW119LCB7InRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRl
bnQiLCAidHlwZSI6IDAsICJuYW1lIjogIlBUIEludGVncmF0aW9uIEM6IFJ1biIsICJ0YWdzIjog
W10sICJ2aWV3X2l0ZW1zIjogW10sICJlbmFibGVkIjogdHJ1ZSwgIndvcmtmbG93cyI6IFsicHRf
aW50ZWdyYXRpb25fY19ydW4iXSwgImxvZ2ljX3R5cGUiOiAiYWxsIiwgImV4cG9ydF9rZXkiOiAi
UFQgSW50ZWdyYXRpb24gQzogUnVuIiwgInV1aWQiOiAiMTFmNjE0ODgtYmQ1Yi00Y2QyLTkxM2Mt
OGIyODU5ZDhmYmRiIiwgImF1dG9tYXRpb25zIjogW10sICJjb25kaXRpb25zIjogW3sidHlwZSI6
IG51bGwsICJldmFsdWF0aW9uX2lkIjogbnVsbCwgImZpZWxkX25hbWUiOiAiaW5jaWRlbnQucHJv
cGVydGllcy5wdF9pbnRfY19udW1fcnVucyIsICJtZXRob2QiOiAiY2hhbmdlZCIsICJ2YWx1ZSI6
IG51bGx9XSwgImlkIjogNTIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdfSwgeyJ0aW1lb3V0
X3NlY29uZHMiOiA4NjQwMCwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInR5cGUiOiAxLCAi
bmFtZSI6ICJQVCBJbnRlZ3JhdGlvbiBDOiBTdGFydCIsICJ0YWdzIjogW10sICJ2aWV3X2l0ZW1z
IjogW3sic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAi
c2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRl
bnQiOiAiMjYyNTJkYTQtNjM1NC00MjU1LTliYmMtMjQ2NjFiMjAxODhjIiwgInN0ZXBfbGFiZWwi
OiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlv
biIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAi
Y29udGVudCI6ICJiMTczYTM5Yi04MzM4LTQ2NjAtYTJmNS0zMjMxMjkzYjNkOTEiLCAic3RlcF9s
YWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZv
Y2F0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVp
ZCIsICJjb250ZW50IjogIjg2YWI5M2NkLWJiYjUtNDI4ZS1iNmY2LTFiOTUzOTlhMThiYyIsICJz
dGVwX2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogImFjdGlv
bmludm9jYXRpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVs
ZF91dWlkIiwgImNvbnRlbnQiOiAiNzllYzBmOTQtYjYwMi00MDQ2LTg5NDctZGYzMDRmMjNmMWMw
IiwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJlbmFibGVkIjogdHJ1ZSwgIndvcmtmbG93cyI6IFtd
LCAibG9naWNfdHlwZSI6ICJhbGwiLCAiZXhwb3J0X2tleSI6ICJQVCBJbnRlZ3JhdGlvbiBDOiBT
dGFydCIsICJ1dWlkIjogIjUzNDZjZjE1LWFmYWEtNDM0MS1iNjM1LTUxM2U3N2RlZDIzNCIsICJh
dXRvbWF0aW9ucyI6IFt7InR5cGUiOiAicnVuX3NjcmlwdCIsICJzY3JpcHRzX3RvX3J1biI6ICJQ
VCBJbnRlZ3JhdGlvbiBDOiBTZXQgQ3VzdG9tIEZpZWxkcyIsICJ2YWx1ZSI6IG51bGx9XSwgImNv
bmRpdGlvbnMiOiBbXSwgImlkIjogNTEsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdfV0sICJs
YXlvdXRzIjogW10sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAyLCAiaWQiOiAzLCAiaW5kdXN0
cmllcyI6IG51bGwsICJmdW5jdGlvbnMiOiBbeyJkaXNwbGF5X25hbWUiOiAiUFQgSW50ZWdyYXRp
b24gQzogUHJvY2VzcyBBZGRlZCBBcnRpZmFjdCIsICJkZXNjcmlwdGlvbiI6IHsiY29udGVudCI6
ICJQcm9jZXNzZXMgdGhlIEFydGlmYWN0IGFkZGVkLiBKdXN0IHJldHVybnMgYSBzdWNjZXNzID0g
VHJ1ZSIsICJmb3JtYXQiOiAidGV4dCJ9LCAiY3JlYXRvciI6IHsidHlwZSI6ICJ1c2VyIiwgImRp
c3BsYXlfbmFtZSI6ICJBZG1pbiBVc2VyIiwgImlkIjogNzEsICJuYW1lIjogImFkbWluQGV4YW1w
bGUuY29tIn0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjog
Il9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVs
ZF91dWlkIiwgImNvbnRlbnQiOiAiNjlhNDlmOTMtZDIxZC00ZjVhLTllODYtNGI0YTgxMDk2YjIx
IiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAi
X19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxk
X3V1aWQiLCAiY29udGVudCI6ICI2NzNjOTFiOC1lZTliLTQ5YzMtOGFhMy1iYTM3N2ZiNDBiOTEi
LCAic3RlcF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJf
X2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRf
dXVpZCIsICJjb250ZW50IjogImJiOTExNjE3LWQwODItNGFkNS04MjE4LTRlOTBhZWNkMGZhMCIs
ICJzdGVwX2xhYmVsIjogbnVsbH1dLCAidGFncyI6IFtdLCAiZXhwb3J0X2tleSI6ICJwdF9pbnRl
Z3JhdGlvbl9jX3Byb2Nlc3NfYWRkZWRfYXJ0aWZhY3QiLCAidXVpZCI6ICIyNzI1YTM2Yy1iN2Jl
LTQ3OTQtOWEzNS1lODYxMDY5ODdjNmEiLCAibGFzdF9tb2RpZmllZF9ieSI6IHsidHlwZSI6ICJ1
c2VyIiwgImRpc3BsYXlfbmFtZSI6ICJBZG1pbiBVc2VyIiwgImlkIjogNzEsICJuYW1lIjogImFk
bWluQGV4YW1wbGUuY29tIn0sICJ2ZXJzaW9uIjogMSwgIndvcmtmbG93cyI6IFt7InByb2dyYW1t
YXRpY19uYW1lIjogInB0X2ludGVncmF0aW9uX2NfcHJvY2Vzc19hZGRlZF9hcnRpZmFjdCIsICJ0
YWdzIjogW10sICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJ1dWlkIjogbnVsbCwgImFjdGlv
bnMiOiBbXSwgIm5hbWUiOiAiUFQgSW50ZWdyYXRpb24gQzogUHJvY2VzcyBBZGRlZCBBcnRpZmFj
dCIsICJ3b3JrZmxvd19pZCI6IDM4LCAiZGVzY3JpcHRpb24iOiBudWxsfV0sICJsYXN0X21vZGlm
aWVkX3RpbWUiOiAxNTc2MTUyNzczODgzLCAiZGVzdGluYXRpb25faGFuZGxlIjogInB0X2ludGVn
cmF0aW9uX2MiLCAiaWQiOiA3MSwgIm5hbWUiOiAicHRfaW50ZWdyYXRpb25fY19wcm9jZXNzX2Fk
ZGVkX2FydGlmYWN0In0sIHsiZGlzcGxheV9uYW1lIjogIlBUIEludGVncmF0aW9uIEM6IFJ1biIs
ICJkZXNjcmlwdGlvbiI6IHsiY29udGVudCI6ICJGdW5jdGlvbiB0aGF0OiBcbi0gU2xlZXBzIGZv
ciBkZWxheSBcbi0gR2VuZXJhdGVzIGxpc3Qgb2YgbnVtX2FydGlmYWN0cyBcbi0gUmV0dXJucyBs
aXN0IG9mIEFydGlmYWN0cyB0byBhZGQsIHJlbWFpbmluZyBudW1iZXIgb2YgcnVucyBhbmQgc2Ft
cGxlIGRhdGEiLCAiZm9ybWF0IjogInRleHQifSwgImNyZWF0b3IiOiB7InR5cGUiOiAidXNlciIs
ICJkaXNwbGF5X25hbWUiOiAiQWRtaW4gVXNlciIsICJpZCI6IDcxLCAibmFtZSI6ICJhZG1pbkBl
eGFtcGxlLmNvbSJ9LCAidmlld19pdGVtcyI6IFt7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlw
ZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAi
ZmllbGRfdXVpZCIsICJjb250ZW50IjogImU3NmIwMjM4LTU4NDctNDU5NC1hOWM4LTg0NDZmOWVm
YmYzNyIsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBl
IjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJm
aWVsZF91dWlkIiwgImNvbnRlbnQiOiAiYTIxMjE1ZTAtMWI3NC00ZDk0LWExNzItM2MwZjU5OTI5
MzhlIiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUi
OiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZp
ZWxkX3V1aWQiLCAiY29udGVudCI6ICIyMTI4Y2E1Zi0xMjI0LTQ0MWUtODg2Yi0zMGI5NDI3Y2I1
MTEiLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6
ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmll
bGRfdXVpZCIsICJjb250ZW50IjogImExMGFhNGUxLTEwZTItNDY3Yy05ZTE4LWRkZGEyNzg2ZDlm
NSIsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAidGFncyI6IFtdLCAiZXhwb3J0X2tleSI6ICJwdF9p
bnRlZ3JhdGlvbl9jX3J1biIsICJ1dWlkIjogIjk4MWRlZDliLTU2ZDQtNDkyYy04MDE5LTY5NmVk
ZjlmYTdhMCIsICJsYXN0X21vZGlmaWVkX2J5IjogeyJ0eXBlIjogInVzZXIiLCAiZGlzcGxheV9u
YW1lIjogIkFkbWluIFVzZXIiLCAiaWQiOiA3MSwgIm5hbWUiOiAiYWRtaW5AZXhhbXBsZS5jb20i
fSwgInZlcnNpb24iOiAxLCAid29ya2Zsb3dzIjogW3sicHJvZ3JhbW1hdGljX25hbWUiOiAicHRf
aW50ZWdyYXRpb25fY19ydW4iLCAidGFncyI6IFtdLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQi
LCAidXVpZCI6IG51bGwsICJhY3Rpb25zIjogW10sICJuYW1lIjogIlBUIEludGVncmF0aW9uIEM6
IFJ1biIsICJ3b3JrZmxvd19pZCI6IDM3LCAiZGVzY3JpcHRpb24iOiBudWxsfV0sICJsYXN0X21v
ZGlmaWVkX3RpbWUiOiAxNTc2MTUyNzM5MDc1LCAiZGVzdGluYXRpb25faGFuZGxlIjogInB0X2lu
dGVncmF0aW9uX2MiLCAiaWQiOiA3MCwgIm5hbWUiOiAicHRfaW50ZWdyYXRpb25fY19ydW4ifV0s
ICJhY3Rpb25fb3JkZXIiOiBbXSwgImdlb3MiOiBudWxsLCAidGFncyI6IFtdLCAidGFza19vcmRl
ciI6IFtdLCAidHlwZXMiOiBbXSwgInRpbWVmcmFtZXMiOiBudWxsLCAid29ya3NwYWNlcyI6IFtd
LCAiaW5ib3VuZF9tYWlsYm94ZXMiOiBudWxsLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJwaGFz
ZXMiOiBbXSwgIm5vdGlmaWNhdGlvbnMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJpbmNp
ZGVudF90eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTU3NjE1NDI0MjI1MiwgImRlc2NyaXB0aW9u
IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1
c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjogIkN1c3Rv
bWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1NzYxNTQyNDIy
NTIsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJlbmFi
bGVkIjogZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4i
OiBmYWxzZX1dLCAic2NyaXB0cyI6IFt7ImRlc2NyaXB0aW9uIjogIlNldHMgdGhlIGZpZWxkczpc
bi0gcHRfaW50X2NfbnVtX2FydGlmYWN0c1xuLSBwdF9pbnRfY19udW1fcnVuc1xuLSBwdF9pbnRf
Y19kZWxheVxuLSBwdF9pbnRfY19zYW1wbGVfZGF0YSIsICJsYW5ndWFnZSI6ICJweXRob24iLCAi
dGFncyI6IFtdLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAiZXhwb3J0X2tleSI6ICJQVCBJ
bnRlZ3JhdGlvbiBDOiBTZXQgQ3VzdG9tIEZpZWxkcyIsICJ1dWlkIjogIjQ1NGVlYTU2LTZlZDgt
NGExYy1iMzY5LTg1N2QwZDYwMjc4ZiIsICJhY3Rpb25zIjogW10sICJjcmVhdG9yX2lkIjogImFk
bWluQGV4YW1wbGUuY29tIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20i
LCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU3NjE1MjYwMjU0NSwgInNjcmlwdF90ZXh0IjogIlxu
IyBTZXQgZmllbGRzXG5cbmluY2lkZW50LnByb3BlcnRpZXMucHRfaW50X2NfbnVtX2FydGlmYWN0
cyA9IHJ1bGUucHJvcGVydGllcy5udW1fYXJ0aWZhY3RzXG5pbmNpZGVudC5wcm9wZXJ0aWVzLnB0
X2ludF9jX251bV9ydW5zID0gcnVsZS5wcm9wZXJ0aWVzLm51bV9ydW5zXG5pbmNpZGVudC5wcm9w
ZXJ0aWVzLnB0X2ludF9jX2RlbGF5ID0gcnVsZS5wcm9wZXJ0aWVzLmRlbGF5XG5pbmNpZGVudC5w
cm9wZXJ0aWVzLnB0X2ludF9jX3NhbXBsZV9kYXRhID0gcnVsZS5wcm9wZXJ0aWVzLnNhbXBsZV9k
YXRhLmNvbnRlbnQiLCAiaWQiOiAzNSwgIm5hbWUiOiAiUFQgSW50ZWdyYXRpb24gQzogU2V0IEN1
c3RvbSBGaWVsZHMifV0sICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzNCwgInZlcnNpb24i
OiAiMzQuMi40NyIsICJidWlsZF9udW1iZXIiOiA0NywgIm1pbm9yIjogMn0sICJtZXNzYWdlX2Rl
c3RpbmF0aW9ucyI6IFt7InByb2dyYW1tYXRpY19uYW1lIjogInB0X2ludGVncmF0aW9uX2MiLCAi
dGFncyI6IFtdLCAiZXhwb3J0X2tleSI6ICJwdF9pbnRlZ3JhdGlvbl9jIiwgInV1aWQiOiAiYjJk
ZWViZmYtNmE5OS00ZDNhLWFhNDQtYTkxMDI2NjQ1NWIyIiwgImV4cGVjdF9hY2siOiB0cnVlLCAi
ZGVzdGluYXRpb25fdHlwZSI6IDAsICJ1c2VycyI6IFsiaW50ZWdyYXRpb25zQGV4YW1wbGUuY29t
Il0sICJhcGlfa2V5cyI6IFtdLCAibmFtZSI6ICJwdF9pbnRlZ3JhdGlvbl9jIn1dLCAiaW5jaWRl
bnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMiOiBbeyJvcGVyYXRp
b25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAi
cHRfaW50X3NhbXBsZV9kYXRhIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVs
bCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyNjcsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1
aWQiOiAiYTEwYWE0ZTEtMTBlMi00NjdjLTllMTgtZGRkYTI3ODZkOWY1IiwgImNob3NlbiI6IGZh
bHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiT3B0aW9uYWwgc2FtcGxlIGRh
dGEgdG8gcmV0dXJuIHRvIG1ha2UgdGhlIG1lc3NhZ2UgbGFyZ2VyIiwgImludGVybmFsIjogZmFs
c2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAidGFncyI6IFtdLCAiYWxs
b3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3B0X2lu
dF9zYW1wbGVfZGF0YSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIi
OiAiIiwgIm5hbWUiOiAicHRfaW50X3NhbXBsZV9kYXRhIiwgImRlcHJlY2F0ZWQiOiBmYWxzZSwg
ImNhbGN1bGF0ZWQiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2Vy
dmVyIjogZmFsc2V9LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlv
bl9wZXJtcyI6IHt9LCAidGV4dCI6ICJwdF9pbnRfbnVtX3J1bnMiLCAiYmxhbmtfb3B0aW9uIjog
ZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDI2NiwgInJl
YWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICJhMjEyMTVlMC0xYjc0LTRkOTQtYTE3Mi0zYzBmNTk5
MjkzOGUiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogIm51bWJlciIsICJ0b29sdGlw
IjogIlRoZSBudW1iZXIgb2YgcnVucyByZW1haW5pbmciLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJp
Y2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJ0YWdzIjogW10sICJhbGxvd19kZWZh
dWx0X3ZhbHVlIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vcHRfaW50X251bV9y
dW5zIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFt
ZSI6ICJwdF9pbnRfbnVtX3J1bnMiLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6
IGZhbHNlLCAidmFsdWVzIjogW10sICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZX0s
IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30s
ICJ0ZXh0IjogInB0X2ludF9hcnRpZmFjdF9kZXNjcmlwdGlvbiIsICJibGFua19vcHRpb24iOiBm
YWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjcxLCAicmVh
ZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjY3M2M5MWI4LWVlOWItNDljMy04YWEzLWJhMzc3ZmI0
MGI5MSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjog
IkRlc2NyaXB0aW9uIG9mIHRoZSBBcnRpZmFjdCIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90
ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgInRhZ3MiOiBbXSwgImFsbG93X2RlZmF1bHRf
dmFsdWUiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9wdF9pbnRfYXJ0aWZhY3Rf
ZGVzY3JpcHRpb24iLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjog
IiIsICJuYW1lIjogInB0X2ludF9hcnRpZmFjdF9kZXNjcmlwdGlvbiIsICJkZXByZWNhdGVkIjog
ZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJ2YWx1ZXMiOiBbXSwgImRlZmF1bHRfY2hvc2Vu
X2J5X3NlcnZlciI6IGZhbHNlfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJv
cGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAicHRfaW50X251bV9hcnRpZmFjdHMiLCAiYmxh
bmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJp
ZCI6IDI3MCwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICJlNzZiMDIzOC01ODQ3LTQ1OTQt
YTljOC04NDQ2ZjllZmJmMzciLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogIm51bWJl
ciIsICJ0b29sdGlwIjogIk51bWJlciBvZiBBcnRpZmFjdHMgdG8gR2VuZXJhdGUiLCAiaW50ZXJu
YWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJ0YWdzIjog
W10sICJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rp
b24vcHRfaW50X251bV9hcnRpZmFjdHMiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBs
YWNlaG9sZGVyIjogIiIsICJuYW1lIjogInB0X2ludF9udW1fYXJ0aWZhY3RzIiwgImRlcHJlY2F0
ZWQiOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAiZGVmYXVsdF9j
aG9zZW5fYnlfc2VydmVyIjogZmFsc2V9LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAx
MSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJwdF9pbnRfZGVsYXkiLCAiYmxhbmtf
b3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6
IDI2OCwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICIyMTI4Y2E1Zi0xMjI0LTQ0MWUtODg2
Yi0zMGI5NDI3Y2I1MTEiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogIm51bWJlciIs
ICJ0b29sdGlwIjogIlRoZSB0aW1lIGluIG1zIHRvIHNsZWVwIGJlZm9yZSByZXR1cm5pbmciLCAi
aW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJ0
YWdzIjogW10sICJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9f
ZnVuY3Rpb24vcHRfaW50X2RlbGF5IiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFj
ZWhvbGRlciI6ICIiLCAibmFtZSI6ICJwdF9pbnRfZGVsYXkiLCAiZGVwcmVjYXRlZCI6IGZhbHNl
LCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAidmFsdWVzIjogW10sICJkZWZhdWx0X2Nob3Nlbl9ieV9z
ZXJ2ZXIiOiBmYWxzZX0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0
aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogInB0X2ludF9hcnRpZmFjdF9pZCIsICJibGFua19vcHRp
b24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjY5
LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjY5YTQ5ZjkzLWQyMWQtNGY1YS05ZTg2LTRi
NGE4MTA5NmIyMSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgInRv
b2x0aXAiOiAiSUQgb2YgdGhlIEFydGlmYWN0IiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3Rl
eHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAidGFncyI6IFtdLCAiYWxsb3dfZGVmYXVsdF92
YWx1ZSI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3B0X2ludF9hcnRpZmFjdF9p
ZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUi
OiAicHRfaW50X2FydGlmYWN0X2lkIiwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImNhbGN1bGF0ZWQi
OiBmYWxzZSwgInZhbHVlcyI6IFtdLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2V9
LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9
LCAidGV4dCI6ICJwdF9pbnRfYXJ0aWZhY3RfdmFsdWUiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2Us
ICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDI3MiwgInJlYWRfb25s
eSI6IGZhbHNlLCAidXVpZCI6ICJiYjkxMTYxNy1kMDgyLTRhZDUtODIxOC00ZTkwYWVjZDBmYTAi
LCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICJBcnRp
ZmFjdCdzIFZhbHVlIiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRl
bXBsYXRlcyI6IFtdLCAidGFncyI6IFtdLCAiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAi
ZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3B0X2ludF9hcnRpZmFjdF92YWx1ZSIsICJoaWRlX25v
dGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAicHRfaW50X2Fy
dGlmYWN0X3ZhbHVlIiwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwg
InZhbHVlcyI6IFtdLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2V9LCB7Im9wZXJh
dGlvbnMiOiBbXSwgInR5cGVfaWQiOiA2LCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0Ijog
IlNhbXBsZSBEYXRhIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogInByb3BlcnRp
ZXMiLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDI2NSwgInJlYWRfb25seSI6IGZhbHNlLCAi
dXVpZCI6ICI3OWVjMGY5NC1iNjAyLTQwNDYtODk0Ny1kZjMwNGYyM2YxYzAiLCAiY2hvc2VuIjog
ZmFsc2UsICJpbnB1dF90eXBlIjogInRleHRhcmVhIiwgInRvb2x0aXAiOiAiU2FtcGxlIHRleHQg
dGhhdCBjYW4gYmUgcGFzdGVkIGluIHRvIGluY3JlYXNlIHRoZSBzaXplIG9mIHRoZSBtZXNzYWdl
IGFkZGVkIHRvIHRoZSBtZXNzYWdlIGRlc3RpbmF0aW9uIiwgImludGVybmFsIjogZmFsc2UsICJy
aWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAidGFncyI6IFtdLCAiYWxsb3dfZGVm
YXVsdF92YWx1ZSI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3NhbXBs
ZV9kYXRhIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAi
bmFtZSI6ICJzYW1wbGVfZGF0YSIsICJkZXByZWNhdGVkIjogZmFsc2UsICJjYWxjdWxhdGVkIjog
ZmFsc2UsICJ2YWx1ZXMiOiBbXSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlfSwg
eyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogNiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAi
dGV4dCI6ICJOdW1iZXIgb2YgQXJ0aWZhY3RzIHRvIEFkZCIsICJibGFua19vcHRpb24iOiBmYWxz
ZSwgInByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyNjMs
ICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiMjYyNTJkYTQtNjM1NC00MjU1LTliYmMtMjQ2
NjFiMjAxODhjIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAidG9v
bHRpcCI6ICIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxh
dGVzIjogW10sICJ0YWdzIjogW10sICJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJleHBv
cnRfa2V5IjogImFjdGlvbmludm9jYXRpb24vbnVtX2FydGlmYWN0cyIsICJoaWRlX25vdGlmaWNh
dGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAibnVtX2FydGlmYWN0cyIs
ICJkZXByZWNhdGVkIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJyZXF1aXJlZCI6ICJh
bHdheXMiLCAidmFsdWVzIjogW10sICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZX0s
IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDYsICJvcGVyYXRpb25fcGVybXMiOiB7fSwg
InRleHQiOiAiTnVtYmVyIG9mIFJ1bnMiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgi
OiAicHJvcGVydGllcyIsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjYyLCAicmVhZF9vbmx5
IjogZmFsc2UsICJ1dWlkIjogImIxNzNhMzliLTgzMzgtNDY2MC1hMmY1LTMyMzEyOTNiM2Q5MSIs
ICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgInRvb2x0aXAiOiAiTnVt
YmVyIG9mIHRpbWVzIHRvIEFkZCB0aGUgQXJ0aWZhY3RzIiwgImludGVybmFsIjogZmFsc2UsICJy
aWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAidGFncyI6IFtdLCAiYWxsb3dfZGVm
YXVsdF92YWx1ZSI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL251bV9y
dW5zIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFt
ZSI6ICJudW1fcnVucyIsICJkZXByZWNhdGVkIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2Us
ICJyZXF1aXJlZCI6ICJhbHdheXMiLCAidmFsdWVzIjogW10sICJkZWZhdWx0X2Nob3Nlbl9ieV9z
ZXJ2ZXIiOiBmYWxzZX0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDYsICJvcGVyYXRp
b25fcGVybXMiOiB7fSwgInRleHQiOiAiRGVsYXkgaW4gbXMgYmV0d2VlbiBydW5zIiwgImJsYW5r
X29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogInByb3BlcnRpZXMiLCAiY2hhbmdlYWJsZSI6IHRy
dWUsICJpZCI6IDI2NCwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICI4NmFiOTNjZC1iYmI1
LTQyOGUtYjZmNi0xYjk1Mzk5YTE4YmMiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjog
Im51bWJlciIsICJ0b29sdGlwIjogIklmIG51bV9ydW5zID4gMSwgdGhlIGRlbGF5IGluIG1zIGJl
dHdlZW4gdGhlIG51bWJlciBvZiBydW5zIiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQi
OiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAidGFncyI6IFtdLCAiYWxsb3dfZGVmYXVsdF92YWx1
ZSI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL2RlbGF5IiwgImhpZGVf
bm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJkZWxheSIs
ICJkZXByZWNhdGVkIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJyZXF1aXJlZCI6ICJh
bHdheXMiLCAidmFsdWVzIjogW10sICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZX0s
IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDAsICJvcGVyYXRpb25fcGVybXMiOiB7fSwg
InRleHQiOiAicHRfaW50X2NfbnVtX2FydGlmYWN0cyIsICJibGFua19vcHRpb24iOiBmYWxzZSwg
InByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyOTEsICJy
ZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiNjc3NDIyMmItN2Q0OS00NGIzLThjZjItNWI2MWFj
NTMxMjdkIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAidG9vbHRp
cCI6ICIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVz
IjogW10sICJ0YWdzIjogW10sICJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJleHBvcnRf
a2V5IjogImluY2lkZW50L3B0X2ludF9jX251bV9hcnRpZmFjdHMiLCAiaGlkZV9ub3RpZmljYXRp
b24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogInB0X2ludF9jX251bV9hcnRp
ZmFjdHMiLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAidmFsdWVz
IjogW10sICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZX0sIHsib3BlcmF0aW9ucyI6
IFtdLCAidHlwZV9pZCI6IDAsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAicHRfaW50
X2Nfc2FtcGxlX2RhdGEiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiAicHJvcGVy
dGllcyIsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjk0LCAicmVhZF9vbmx5IjogZmFsc2Us
ICJ1dWlkIjogIjk2NDZhMDNmLWI3NDQtNDA1OS1iNzQxLTgzZGY3ZWUzOWQ1ZCIsICJjaG9zZW4i
OiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dGFyZWEiLCAidG9vbHRpcCI6ICIiLCAiaW50ZXJu
YWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJ0YWdzIjog
W10sICJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lkZW50
L3B0X2ludF9jX3NhbXBsZV9kYXRhIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFj
ZWhvbGRlciI6ICIiLCAibmFtZSI6ICJwdF9pbnRfY19zYW1wbGVfZGF0YSIsICJkZXByZWNhdGVk
IjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJ2YWx1ZXMiOiBbXSwgImRlZmF1bHRfY2hv
c2VuX2J5X3NlcnZlciI6IGZhbHNlfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMCwg
Im9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJwdF9pbnRfY19udW1fcnVucyIsICJibGFu
a19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgImNoYW5nZWFibGUiOiB0
cnVlLCAiaWQiOiAyOTIsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiNTRlMTQ1ZmYtMjFm
OS00YjNmLWIzNWEtMDJmMTkwMjA3MDQ5IiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6
ICJudW1iZXIiLCAidG9vbHRpcCI6ICIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6
IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJ0YWdzIjogW10sICJhbGxvd19kZWZhdWx0X3ZhbHVl
IjogZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lkZW50L3B0X2ludF9jX251bV9ydW5zIiwgImhp
ZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJwdF9p
bnRfY19udW1fcnVucyIsICJkZXByZWNhdGVkIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2Us
ICJ2YWx1ZXMiOiBbXSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlfSwgeyJvcGVy
YXRpb25zIjogW10sICJ0eXBlX2lkIjogMCwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6
ICJwdF9pbnRfY19kZWxheSIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6ICJwcm9w
ZXJ0aWVzIiwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyOTMsICJyZWFkX29ubHkiOiBmYWxz
ZSwgInV1aWQiOiAiNTJlZTgzM2ItNjI3Ni00MmQzLTk1YmYtMGEwZmNjYjQwZGZlIiwgImNob3Nl
biI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAidG9vbHRpcCI6ICIiLCAiaW50ZXJu
YWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJ0YWdzIjog
W10sICJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lkZW50
L3B0X2ludF9jX2RlbGF5IiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRl
ciI6ICIiLCAibmFtZSI6ICJwdF9pbnRfY19kZWxheSIsICJkZXByZWNhdGVkIjogZmFsc2UsICJj
YWxjdWxhdGVkIjogZmFsc2UsICJ2YWx1ZXMiOiBbXSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZl
ciI6IGZhbHNlfV0sICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTU3NjE1NDI0MDgy
NH0=
"""
    )