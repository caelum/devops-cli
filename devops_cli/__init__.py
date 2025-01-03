import click
from .config import create_config
from .server import manage_server
from .deploy import deploy_app
from .logs import monitor_logs

@click.group()
def cli():
    pass

cli.add_command(create_config)
cli.add_command(manage_server)
cli.add_command(deploy_app)
cli.add_command(monitor_logs)