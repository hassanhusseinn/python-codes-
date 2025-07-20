

logs = [
      {"username": "alice", "ip": "192.168.1.1", "status": "Success"},
      {"username": "bob", "ip": "192.168.1.2", "status": "Failure"},
      {"username": "alice", "ip": "192.168.1.3", "status": "Failure"},
      {"username": "carol", "ip": "192.168.1.4", "status": "Success"},
      {"username": "bob", "ip": "192.168.1.2", "status": "Failure"},
      {"username": "alice", "ip": "192.168.1.1", "status": "Failure"},
      {"username": "dave", "ip": "192.168.1.5", "status": "Failure"},
      {"username": "bob", "ip": "192.168.1.2", "status": "Failure"}
  ]


for log in logs:
  if log["ip"] == "192.168.1.4":
      print(log)

#we chose sets bcuz sets do not allow duplicate items so it will only take the unique ones hehe :) 


unique_ips = {log["ip"] for log in logs}
print("Unique IP Addresses:", unique_ips)



















