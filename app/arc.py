import paramiko
from scp import SCPClient

paramiko.util.log_to_file('paramiko.log')

class Client:
    def __init__(self, url, user):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(url, username=user)

    def put_file(self, local_path, remote_path):
        scp = self._scp_client()
        scp.put(path, remove_path)

    def get_file(self, remote_path):
        scp = self._scp_client()
        scp.get(remote_path)

    def run(self, command):
        return self.client.exec_command(command)

    def close(self):
        self.client.close()

    def _scp_client(self):
        return SCPClient(self.client.get_transport())


def get_remote_path(job_id):
    return '$WORK/omningssimulator/{}'.format(job_id)