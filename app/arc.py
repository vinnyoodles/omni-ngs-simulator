import paramiko
from scp import SCPClient

ARC_USER = 'vincentl'
ARC_DIR = '/groups/ngsproj/generated_data'
QSUB_DIR = '/groups/ngsproj/omni-ngs-simulator/arc'

paramiko.util.log_to_file('paramiko.log')

class Client:
    def __init__(self, url, user):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(url, username=user)

    def put_file(self, local_path, remote_path):
        scp = self._scp_client()
        scp.put(local_path, remote_path)

    def get_file(self, local_path, remote_path):
        scp = self._scp_client()
        scp.get(remote_path, local_path=local_path)

    def run(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return ' '.join(stdout)

    def close(self):
        self.client.close()

    def _scp_client(self):
        return SCPClient(self.client.get_transport())


def get_remote_path(job_id):
    return '{}/{}'.format(ARC_DIR, job_id)
