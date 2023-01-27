import requests
import datetime

# Endpoint para listar repositórios
url = "http://localhost:8081/service/rest/v1/repositories"

# Fazer requisição GET
response = requests.get(url)
print(response)

# Iterar sobre cada repositório
# for repo in response.json():
#     last_downloaded = repo["lastDownloaded"]
#     if last_downloaded:
#         last_downloaded = datetime.datetime.fromisoformat(last_downloaded)
#         if (datetime.datetime.now() - last_downloaded).days > 15:
#             # Endpoint para deletar repositório
#             delete_url = f"http://nexus-url/service/rest/v1/repositories/{repo['name']}"
#             # Fazer requisição DELETE
#             requests.delete(delete_url)
