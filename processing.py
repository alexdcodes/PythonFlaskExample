import paramiko


def do_calculation(number1, number2):
    return number1 + number2


def ssh_connection(ip1, username, password):
    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip1, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

    ssh_conn = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn.recv(99535)
    return ip1, username, password, banner_output
