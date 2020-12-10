"""interactive script to gather list of subnets from meraki networks"""
#import required modules
import requests
import json

# Define static variables
# uncomment to set variable instead of having user input:
#API_KEY = 'key-value'
MERAKI_URL = 'https://api.meraki.com/api/v1/'
#ORG_KEY = 'org-id'
#headers = {'X-Cisco-Meraki-API-Key':API_KEY}

#welcome message for production value
print("##############################################################")
print("###                    LIST MERAKI SUBNETS                 ###")
print("##############################################################")
print("This script fetches you a list of subnets from your meraki org")
print("Please ensure you have permission to access your organisations")
print("dashboard API.")
print()
#prompt user for api key
print("Please enter your API Key:")
API_KEY = input()

print()

#prompt user for org id
print("Please enter your organisation ID:")
ORG_KEY = input()
headers = {'X-Cisco-Meraki-API-Key':API_KEY}

# Function to grab the list of the Networks for the Organisation
def get_net_id():
	net_list = requests.get(MERAKI_URL + 'organizations/' + ORG_KEY + '/networks', headers=headers)
	if net_list.status_code != 200:
       		print('Incorrect Network Query String: Error accessing:', MERAKI_URL + 'organizations/' + ORG_KEY + '/networks');
       		exit(1);
	else:
		json_list = json.loads(net_list.text)
		return json_list

# Function to grab the VLAN's in the Network, based on Network ID (passed)
def get_vlan_info(net_id):
	vlan_list = requests.get(MERAKI_URL + 'networks/' + net_id + '/appliance' + '/vlans', headers=headers)
	if vlan_list.status_code != 200:
       		print('Incorrect VLAN Query String: Error accessing:', MERAKI_URL + 'networks/' + net_id + '/appliance' + '/vlans');
        	exit(1);
	else:
		json_vlist = json.loads(vlan_list.text)
		return json_vlist

def main():
# Get list of networks and ID's
	print("starting main function and getting network ID's")
	net_data = get_net_id()
	for i in net_data:
		net_name = i["name"]
		net_id = i["id"]
# Ignore no VLAN networks by name
		if 'CORE' in net_name:
			continue
		if 'TW' in net_name:
			continue
		else:
# Use the ID to get a list of VLAN's per Network
			vlan_data = get_vlan_info(net_id)
			for v in vlan_data:
# Extract just the VLAN Name, and Subnet Range
				sub_net = v["subnet"]
				vlan_name = v["name"]
# Print Results in a CSV Friendly Format
				print(net_name + ', ' + vlan_name + ', ' + sub_net)
main()
