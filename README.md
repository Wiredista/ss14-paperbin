# 📄 Paperbin

Este é um gerador de documentos para uso no jogo [Space Station 14](https://spacestation14.com/). Ele permite a criação de documentos personalizados ou a partir de templates.

Uma versão online do gerador pode ser acessada [aqui](https://paperbin.kasparyan.tec.br/).

## Instalação

Baixe os arquivos do repositório e abra o arquivo `index.html` no seu navegador.

## Contribuindo

Se você deseja contribuir com o projeto, sinta-se livre para abrir uma issue ou um pull request.

### Adicionando templates

Para adicionar um novo template siga os passos abaixo:

1. Copie o arquivo `base-nanotrasen.txt` ou `base-syndicate.txt` e renomeie para o nome do novo template.
2. Substitua as tags `{{DOCUMENT.TITLE}}` e `{{DOCUMENT.BODY}}` pelo título e conteúdo do documento.
3. Adicione campos personalizados ao documento, se necessário, usando a tag `{{DOCUMENT.FIELD "Nome do campo"}}` ou `{{DOCUMENT.LIST "Nome do campo"}}` para campos de texto e listas, respectivamente.
4. Adicione o nome do novo template no arquivo `templates.json` seguindo o padrão dos outros templates.

Você também pode usar esse template abaixo como base: 
```
 [color=#1b487e]███░███░░░░██░░░░[/color]
 [color=#1b487e]░██░████░░░██░░░░[/color]      
 [color=#1b487e]░░█░██░██░░██░█░░[/color]               [head=3]NanoTrasen[/head]
 [color=#1b487e]░░░░██░░██░██░██░[/color] [bold]Estação {{STATION.SN}}[/bold]
 [color=#1b487e]░░░░██░░░████░███[/color]
=============================================
                SOLCITIAÇÃO DE EXEMPLO
=============================================
Tempo desde o início do turno e data: {{STATION.TIME}}
Redator do documento: {{AUTHOR.NAME}}
Posição do redator: {{AUTHOR.POSITION}}

Eu, {{AUTHOR.NAME}}, no cargo de {{AUTHOR.POSITION}}, solicito:
{{DOCUMENT.LIST "Lista de solicitações"}}

Razão para a solicitação: {{DOCUMENT.FIELD "Razão para a solicitação"}}

Motivo para a obtenção do equipamento: {{DOCUMENT.FIELD "Motivo para a obtenção do equipamento"}}

=============================================
                             [italic]Espaço para carimbos[/italic]
```
## Licença

Este projeto é licenciado sob a licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada (CC BY-SA 3.0) - veja o arquivo [LICENSE](LICENSE) para mais detalhes.