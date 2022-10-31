import paramiko


def paramiko_ssh(host, port=22, username='darius', password='Cisc0123', cmd='ls'):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        return x
    except Exception as e:
        print(f'{host} 连接失败！{e}')


if __name__ == '__main__':
    print(paramiko_ssh('192.168.50.217'))
