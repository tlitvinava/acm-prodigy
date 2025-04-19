import asyncio
import aiohttp
import json
import time
from aiohttp import BasicAuth

async def parse_accepted_solutions():
    # Конфигурационные параметры
    SOLVE_URL = "https://solve.bsuir.by/"
    login = "denvilk"
    password = "Prodigy@Netw0rk"
    CONTEST_ID = 23  # ID соревнования
    begin_time = int(time.time())
    # Создаем сессию с общими настройками
    async with aiohttp.ClientSession() as session:
        try:
            # 1. Аутентификация в системе
            auth_url = f"{SOLVE_URL}/api/v0/login/"
            async with session.post(auth_url, json={
            'login': login,
            'password': password
        }
        ) as auth_resp:
                if auth_resp.status != 201:
                    error = await auth_resp.text()
                    print(f"Ошибка авторизации: {auth_resp.status} - {error}")
                    return
                
                print("Успешная авторизация в системе")
                cookies = auth_resp.cookies
            
            # 2. Получаем поток событий
            event_feed_url = f"{SOLVE_URL}api/ccs/contests/{CONTEST_ID}/event-feed"
            async with session.get(event_feed_url, auth = BasicAuth(login, password)) as response:
                if response.status != 200:
                    print(f"Ошибка получения event-feed: {response.status}")
                    return
                
                print("Подключено к event-feed. Обработка данных...")
                buffer = ""
                
                async for chunk in response.content.iter_any():
                    buffer += chunk.decode('utf-8')
                    
                    # Обрабатываем построчно
                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        line = line.strip()
                        
                        if not line:
                            continue
                            

                        event = json.loads(line)
                        if is_accepted_solution(event):
                            await fetch_solution_details(session, cookies, SOLVE_URL, event, begin_time)
        
        except aiohttp.ClientError as e:
            print(f"Сетевая ошибка: {e}")
        except Exception as e:
            print(f"Критическая ошибка: {e}")

def is_accepted_solution(event):
    """Проверяем, является ли событие Accepted решением"""
    return (
        event.get("type") == "judgements" and 
        event.get("data", {}).get("judgement_type_id") == "AC"
    )

async def fetch_solution_details(session, cookies, base_url, event, begin_time):
    """Получаем детали решения"""
    solution_id = event.get("data", {}).get("submission_id")
    if not solution_id:
        print("Отсутствует ID решения в событии")
        return
    
    solution_url = f"{base_url}api/v0/solutions/{solution_id}"
    async with session.get(solution_url, cookies=cookies, headers={'X-Solve-Sync': 'true'}) as resp:
        if resp.status == 200:
            solution_data = await resp.json()
            print("\n" + "="*50)
            print(f"Найдено Accepted решение (ID: {solution_id}):")
            print(begin_time)
            #if solution_data['create_time'] > begin_time:
            print(solution_data["problem"]["id"], solution_data["problem"]["statement"]["title"], solution_data["scope_user"]["title"])
            
            # Здесь можно добавить обработку данных решения
            # Например, сохранение в файл или базу данных
            
        else:
            print(f"Не удалось получить решение {solution_id}: {resp.status}")

asyncio.run(parse_accepted_solutions())

