#!/usr/bin/env python              

import os
import sys
import json
import meraki

#Instantiate the client (API consumer class)
DASHBOARD = meraki.DashboardAPI(
            api_key=os.environ['MERAKI_API_KEY'],
            base_url='https://api.meraki.com/api/v1',
            print_console=False)

NETWORK = os.environ['NETWORK'] 


#Update the attributes of an SSID or create a new SSID - definition of values in config_ssid.py file
def update_ssid():
    
    print("Reading the configuration values from json file ...")

    # Reading config variables from JSON file, this info could come from external Database as well
    with open('config_ssid.json') as json_file:
        config_ssid = json.load(json_file)

    print("Updating Wireless SSID ...")

    try:
        resp = DASHBOARD.wireless.updateNetworkWirelessSsid(
            networkId=NETWORK,
            number=config_ssid['number'],
            name=config_ssid['name'],
            enabled=config_ssid['enabled'],
            authMode=config_ssid['authMode'],
            wpaEncryptionMode=config_ssid['wpaEncryptionMode'],
            radiusServers=config_ssid['radiusServers'],
            radiusAccountingEnabled=config_ssid['radiusAccountingEnabled'],
            radiusAccountingServers=config_ssid['radiusAccountingServers'],
            radiusEnabled=config_ssid['radiusEnabled'],
            radiusCoaEnabled=config_ssid['radiusCoaEnabled'],
            radiusAttributeForGroupPolicies=config_ssid['radiusAttributeForGroupPolicies'],
            ipAssignmentMode=config_ssid['ipAssignmentMode'],
            splashPage=config_ssid['splashPage'],
            walledGardenEnabled=config_ssid['walledGardenEnabled'],
            walledGardenRanges=config_ssid['walledGardenRanges'],
            minBitrate=config_ssid['minBitrate'],
            bandSelection=config_ssid['bandSelection'],
            perClientBandwidthLimitUp=config_ssid['perClientBandwidthLimitUp'],
            perClientBandwidthLimitDown=config_ssid['perClientBandwidthLimitDown'],
            visible=config_ssid['visible'],
            availableOnAllAps=config_ssid['availableOnAllAps'],
            availabilityTags=config_ssid['availabilityTags'],
            mandatoryDhcpEnabled=config_ssid['mandatoryDhcpEnabled'],
            useVlanTagging=config_ssid['useVlanTagging'],
            defaultVlanId=config_ssid['defaultVlanId'],
            lanIsolationEnabled=config_ssid['lanIsolationEnabled'])

        print("Executed update.")
    
    except meraki.APIError as e:
        sys.exit("Meraki API error: ", {e})
    except Exception as e:
        sys.exit("some other error: ", {e})


def main():

    update_ssid()

    
if __name__ == '__main__':                
    main()