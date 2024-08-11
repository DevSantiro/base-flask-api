import os
import importlib

def register_routes(app):
    # Diretório base onde as versões da API estão localizadas
    base_dir = os.path.join(os.path.dirname(__file__))

    # Itera sobre cada versão de API dentro do diretório 'routes'
    for version in os.listdir(base_dir):
        # Caminho completo da versão
        version_path = os.path.join(base_dir, version)
        
        # Verifica se é um diretório para poder prosseguir (irá ignorar arquivos)
        if os.path.isdir(version_path):
            # Itera sobre os arquivos dentro da pasta da versão (controllers, etc.)
            for filename in os.listdir(version_path):
                # Verifica se o arquivo termina com '.py' e não é '__init__.py'
                if filename.endswith('.py') and filename != '__init__.py':
                    # Cria o nome do módulo com base na estrutura de diretórios
                    module_name = f'routes.{version}.{filename[:-3]}'

                    # Faz o import do módulo
                    module = importlib.import_module(module_name)

                    # Verifica se o módulo possui um 'bp' (Blueprint) e registra na aplicação
                    if hasattr(module, 'bp'):
                        # Extrai o número da versão para usar no prefixo da URL
                        version_number = version.split('_')[-1]
                        app.register_blueprint(module.bp, url_prefix=f'/{version_number}')

