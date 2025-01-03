import click

@click.command()
@click.option('--log-file', default='app.log', help='Nome do arquivo de log')
def monitor_logs(log_file):
    """Monitora arquivos de log."""
    with open(log_file, 'r') as file:
        click.echo(file.read())