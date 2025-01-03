import click

@click.command()
@click.option('--config-file', default='config.yaml', help='Nome do arquivo de configuração')
@click.option('--key', prompt='Chave', help='Chave de configuração')
@click.option('--value', prompt='Valor', help='Valor de configuração')
def create_config(config_file, key, value):
    """Cria um arquivo de configuração com a chave e valor especificados."""
    config_content = f"{key}: {value}\n"
    with open(config_file, 'w') as file:
        file.write(config_content)
    click.echo(f"Arquivo de configuração '{config_file}' criado com sucesso!")