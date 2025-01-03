import click
import paramiko

@click.command()
@click.option('--host', prompt='Host', help='Endereço do servidor')
@click.option('--user', prompt='Usuário', help='Nome de usuário')
@click.option('--command', prompt='Comando', help='Comando a ser executado')
def manage_server(host, user, command):
    """Gerencia servidores remotos via SSH."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user)
    stdin, stdout, stderr = ssh.exec_command(command)
    click.echo(stdout.read().decode())
    ssh.close()