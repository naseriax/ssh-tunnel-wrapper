# ssh-tunnel-wrapper
SSH Tunnel wrapper!

Topology:
```
Client =====Tunnel1(22)===> JumpServer1 ==== Tunnel2(22) ====> JumpServer2 =====> Target
```
 - Client is the machine where we execute the script and have access to the IP address of JumpServer1 (Port 22).
 - JumpServer1 is the server with access to JumpServer2 and Client IP addresses (Port22).
 - JumpServer2 is the server with access to JumpServer1 and Target IP addresses (Port22).
 - Target is the device we need to reach from Client (Indirectly).

For each jumpserver, make sure below configuration change is applied before executing the script:
```
#vi /etc/ssh/sshd_config
Chnage "#AllowTcpForwarding yes" to "AllowTcpForwarding yes" (Uncommenting the field to allow SSH Session forwarding)
```
