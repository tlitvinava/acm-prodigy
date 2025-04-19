
# import asyncio, aiohttp 
# import requests
# import json
# from aiohttp import BasicAuth

# async def parse_ndjson_stream(url: str, username: str, password: str) -> dict:
#     """
#     Асинхронно парсит NDJSON-поток с HTTP Basic Auth
#     Возвращает асинхронный генератор словарей (JSON-объектов)
    
#     Параметры:
#         url: URL NDJSON-потока
#         username: логин для аутентификации
#         password: пароль для аутентификации
    
#     Использование:
#         async for data in parse_ndjson_stream(url, "user", "pass"):
#             print(data)
#     """
#     auth = BasicAuth(username, password)
    
#     async with aiohttp.ClientSession(auth=auth) as session:
#         async with session.get(url) as response:
#             buffer = ""
            
#             async for chunk in response.content.iter_any():
#                 buffer += chunk.decode('utf-8')
                
#                 while "\n" in buffer:
#                     line, buffer = buffer.split("\n", 1)
#                     line = line.strip()
                    
#                     if not line:
#                         continue
                        
#                     try:
#                         yield json.loads(line)
#                     except json.JSONDecodeError as e:
#                         raise ValueError(f"Invalid JSON: {line}") from e

# async def process_data():
#     base_url = "https://solve.bsuir.by/api/"
#     endpoint = "ccs/contests/22/event-feed"
#     login = "denvilk"
#     password = "Prodigy@Netw0rk"
#     auth = BasicAuth(login, password)
    
#     async with aiohttp.ClientSession(auth=BasicAuth(login, password)) as session:
#         async for data in parse_ndjson_stream(base_url + endpoint, login, password):
#             try:
#                 if data.get("data", {}).get("judgement_type_id") == 'AC':
#                     solution_id = data["id"]
#                     solution_url = f"{base_url}v0/solutions/{solution_id}"
                    
#                     #async with session.get(solution_url) as resp:
#                     async with session.get(
#                         solution_url,
#                         auth=auth,  
#                         headers={
#                             "Referer": f"{base_url}contest/22",
#                             "X-Requested-With": "XMLHttpRequest"
#                         }
#                     ) as resp:
#                         if resp.status == 200:
#                             solution_data = await resp.json()
#                             print(solution_data)
#                         else:
#                             print(f"Error fetching solution {solution_id}: {resp.status}")
#             except KeyError as e:
#                 print(f"Missing key in data: {e}")
#             except Exception as e:
#                 print(f"Unexpected error: {e}")

# asyncio.run(process_data())

import asyncio
import aiohttp
import json
from aiohttp import BasicAuth
import sys

async def parse_ndjson_stream(url: str, session: aiohttp.ClientSession) -> dict:
    """Асинхронный парсер NDJSON потока"""
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            buffer = ""
            async for chunk in response.content.iter_any():
                buffer += chunk.decode('utf-8')
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    if line.strip():
                        try:
                            yield json.loads(line)
                        except json.JSONDecodeError:
                            continue
    except Exception as e:
        print(f"Stream error: {str(e)}")
        raise

async def process_data():
    base_url = "https://solve.bsuir.by/api/"
    endpoint = "ccs/contests/22/event-feed"
    login = "denvilk"
    password = "Prodigy@Netw0rk"
    
    # Настройки подключения
    connector = aiohttp.TCPConnector(
        limit=30,
        force_close=True,
        enable_cleanup_closed=True,
        ssl=False  # Попробуйте True, если сервер использует SSL
    )
    
    timeout = aiohttp.ClientTimeout(total=300, connect=60)
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Connection": "keep-alive"
    }

    async with aiohttp.ClientSession(
        auth=BasicAuth(login, password),
        connector=connector,
        timeout=timeout,
        headers=headers
    ) as session:
        
        try:
            async for data in parse_ndjson_stream(
                f"{base_url}{endpoint}", 
                session
            ):
                try:
                    if data.get("data", {}).get("judgement_type_id") == 'AC':
                        solution_id = data["id"]
                        solution_url = f"{base_url}v0/solutions/{solution_id}"
                        
                        async with session.get(
                            solution_url,
                            headers={
                                "Referer": f"{base_url}contest/22",
                                "X-Requested-With": "XMLHttpRequest"
                            }
                        ) as resp:
                            if resp.status == 200:
                                print(await resp.json())
                            else:
                                print(f"Error {resp.status}: {await resp.text()}")
                except KeyError as e:
                    print(f"Missing key: {e}")
                except Exception as e:
                    print(f"Processing error: {str(e)}")
                    
        except aiohttp.ClientError as e:
            print(f"Connection error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    # Настройка event loop для Windows
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    try:
        asyncio.run(process_data())
    except KeyboardInterrupt:
        print("Interrupted by user")