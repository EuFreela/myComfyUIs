# YouTube Playlist Creator API

Esta API permite criar playlists no YouTube com base em palavras-chave. Você pode enviar uma lista de palavras-chave, e a API buscará vídeos relacionados no YouTube e criará uma playlist automaticamente no seu canal. Liat é configurada com a api.

## Requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- Python 3.7 ou superior
- Conta no Google Cloud com a API do YouTube Data habilitada
- Uma chave de API do YouTube Data

## Instalação

### 1. Clonar o Repositório

Clone este repositório em sua máquina local:

```bash
git clone https://github.com/seu_usuario/youtube-playlist-creator.git
cd youtube-playlist-creator
```

### 2. Criar um Ambiente Virtual

É recomendável criar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### 3. Instalar Dependências

Instale as dependências necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar a API Key do YouTube

Substitua `'SUA_API_KEY_AQUI'` pela sua chave de API do YouTube no arquivo `app.py`:

```python
API_KEY = 'SUA_API_KEY_AQUI'
```

## Como Usar

### 1. Executar a API

Execute o servidor Flask:

```bash
python app.py
```

O servidor será iniciado em `http://localhost:5000`.

### 2. Criar uma Playlist

Para criar uma playlist, envie uma requisição `POST` para o endpoint `/create_playlist` com um JSON contendo o nome da playlist, a descrição, as palavras-chave e o número máximo de vídeos a serem buscados por palavra-chave.

#### Exemplo de Requisição:

Você pode usar o **Postman**, **cURL**, ou qualquer cliente HTTP de sua escolha para enviar a requisição.

```json
POST http://localhost:5000/create_playlist
Content-Type: application/json

{
  "playlist_title": "Set List: Graf Hindenburg - LZ 129 (The Flight Of Songs)",
  "playlist_description": "https://agencylk7.wixsite.com/graf-hindenburg",
  "keywords": ["classic rock", "hard rock", "gold year 70"],
  "max_results": 5
}
```

#### Exemplo de Resposta:

A resposta da API incluirá o `playlist_id` da nova playlist criada e os vídeos adicionados:

```json
{
  "playlist_id": "ID_DA_PLAYLIST",
  "videos": [
    {"title": "Título do Vídeo 1", "video_id": "ID_DO_VIDEO_1"},
    {"title": "Título do Vídeo 2", "video_id": "ID_DO_VIDEO_2"},
    ...
  ]
}
```

## Estrutura do Projeto

```
/meu_projeto
    /app.py                # Código principal da API Flask
    /requirements.txt      # Lista de dependências
    /README.md             # Este arquivo README
```

## Personalização

Você pode personalizar o comportamento da API alterando os parâmetros padrão no código ou passando valores diferentes no corpo da requisição. Para mais detalhes, consulte a [documentação da API do YouTube Data](https://developers.google.com/youtube/v3).


## CRON

python cron_job.py
