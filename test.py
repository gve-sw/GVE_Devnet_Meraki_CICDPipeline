#!/usr/bin/env python  

import os
import json
import meraki
import unittest

class Testing(unittest.TestCase):
    
    DASHBOARD = meraki.DashboardAPI(
            api_key = os.environ['MERAKI_API_KEY'],
            base_url='https://api.meraki.com/api/v1',
            print_console=False)
    
    NETWORK = os.environ['NETWORK']
    
    def test_name(self): 

        print("Reading configuration values from json file: config_ssid ")
        
        # Reading config variables from JSON file, this info could come from external Database as well
        with open('config_ssid.json') as json_file:
            config_ssid = json.load(json_file)

            print("Requesting current values for name from Meraki Dashboard API ... ")

            resp = self.DASHBOARD.wireless.getNetworkWirelessSsid(
                networkId=self.NETWORK,
                number=config_ssid["number"])
            
            expected_name = config_ssid["name"]
            actual_name = resp["name"]

            print("Current test - AssertEqual for SSID name: ")
            print("Expected Value: ", expected_name)
            print("Actual value", actual_name)

            self.assertEqual(expected_name, actual_name)

    def test_wpaEncryptionMode(self):

        print("Reading configuration values from json file: config_ssid ")     

        # Reading config variables from JSON file, this info could come from external Database as well
        with open('config_ssid.json') as json_file:
            config_ssid = json.load(json_file)

            print("Requesting current values for wpaEncryptionMode from Meraki Dashboard API ... ")


            resp = self.DASHBOARD.wireless.getNetworkWirelessSsid(
                networkId=self.NETWORK,
                number=config_ssid["number"])

            expected_wpaEncryptionMode= config_ssid["wpaEncryptionMode"]
            actual_wpaEncryptionMode = resp["wpaEncryptionMode"]

            print("Current test - AssertEqual for SSID wpa encryption mode: ")
            print("Expected Value: ", expected_wpaEncryptionMode)
            print("Actual value", actual_wpaEncryptionMode)

            self.assertEqual(expected_wpaEncryptionMode, actual_wpaEncryptionMode)

if __name__ == '__main__':

    print("Starting testing ... ")
    unittest.main()



