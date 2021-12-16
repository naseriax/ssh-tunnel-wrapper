import sshtunnel
from paramiko import SSHClient
import paramiko

def cliExec(cmd):
    output = ""
    stdout = ssh.exec_command(cmd)[1]
    while True:
        line = stdout.readline()
        if not line:
            break
        output += line
    return output

if __name__ == "__main__":

    #First Jump Server===========================================================
    jumpServer1 = '1.1.1.1'
    FromClientandJumpServer1 = 22
    js1User = "root"
    js1Pass = "password"

    #Second Jump Server==========================================================
    jumpServer2 = '2.2.2.2'
    FromJumpServer1andJumpServer2 = 22
    js2User = "root"
    js2Pass = "password.(0V"

    #Target======================================================================
    target = '10.10.10.10'
    FromJumpServer2andtarget = 22
    targetUser = "root"
    targetPassword="password"
    cmd = 'uname -a'
    #============================================================================


    with sshtunnel.open_tunnel(
        ssh_address_or_host=(jumpServer1, FromClientandJumpServer1),
        remote_bind_address=(jumpServer2, FromJumpServer1andJumpServer2),
        ssh_username=js1User,
        ssh_password=js1Pass,
    ) as tunnel1:
        print(f'Connection to tunnel1 {jumpServer1}:{FromClientandJumpServer1} OK...')
        with sshtunnel.open_tunnel(
            ssh_address_or_host=('localhost', tunnel1.local_bind_port),
            remote_bind_address=(target, FromJumpServer2andtarget),   
            ssh_username=js2User,
            ssh_password=js2Pass,
        ) as tunnel2:
            print(f'Connection to tunnel2 {jumpServer2}:{FromJumpServer1andJumpServer2} OK...')
            with SSHClient() as ssh:
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('localhost',
                    port=tunnel2.local_bind_port,
                    username=targetUser,
                    password=targetPassword,
                )
                print(f'Connection to Target {target}:{FromJumpServer2andtarget} OK...')
                print(cliExec(cmd))