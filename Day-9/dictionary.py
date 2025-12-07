# Dictionary

my_dic = {"name":"vm1", "size":"4GB", "type":"t2.micro"}

# Get values
print(my_dic["name"])

# Modifying and adding elements

my_dic["size"] = "8GB"

my_dic["id"] = "12345"

print(my_dic)

# Delete elements

del my_dic["id"]

print(my_dic)

# Checking Key existence in Dictionay

if "id" in my_dic:
    print("Size of the vm:", my_dic["size"])
else:
    print("Not found")

# Iterating through Keys and Values

for key, value in my_dic.items():
    print(key, value)
    

# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

def get_server_status(server_name):
    return server_config.get(server_name, {}).get("status", "server not found")

server_name = "server2"

status = get_server_status(server_name)

print(f"{server_name} status: {status}")
