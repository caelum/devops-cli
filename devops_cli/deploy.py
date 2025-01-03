import click
import subprocess

@click.command()
@click.option('--repo', prompt='Repositório', help='URL do repositório Git')
@click.option('--branch', default='main', help='Branch a ser deployada')
def deploy_app(repo, branch):
    """Deploy de aplicações a partir de um repositório Git."""
    subprocess.run(['git', 'clone', '-b', branch, repo])
    click.echo(f"Aplicação deployada a partir do branch '{branch}' do repositório '{repo}'")