from dotenv import load_dotenv
import aiohttp
import json


load_dotenv()

async def fetch_data(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            data = await resp.text()
            data_dict = json.loads(data)
            return data_dict
        
async def get_pub_data(link, path):
    params = {
        "public_key": link,
        "path": path
    }
    url = "https://cloud-api.yandex.net/v1/disk/public/resources"
    response = await fetch_data(url, params)
    return response

async def get_download_link(link, path):
    params = {
        "public_key": link,
        "path": path
    }
    url = "https://cloud-api.yandex.net/v1/disk/public/resources/download"
    response = (await fetch_data(url, params))['href']
    return response
