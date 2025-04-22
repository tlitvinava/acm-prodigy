import requests
import json
import logging
from main.utils import Configuration

def parse_accepted_solutions():
    # Конфигурационные параметры
    login = Configuration('configuration.solve.login')
    password = Configuration('configuration.solve.password')
    solve_url = Configuration('configuration.solve.url')
    CONTEST_ID = 23  # ID соревнования
    # Авторизация
    login_resp = requests.post(
            f'{solve_url}/api/v0/login/',
            json={
                'login': login,
                'password': password
            }
        )
    if login_resp.status_code != 200:
        logging.error(f"Не удалось войти в систему Solve\n{login_resp.json()}")
        return
    cookies = login_resp.cookies

    # Парсинг потока 
    event_feed_url = Configuration('configuration.solve.login').replace('{contest_id}', str(CONTEST_ID))
    response = requests.get(event_feed_url, cookies=cookies)

    if response.status != 200:
        logging.error(f"Ошибка получения event-feed: {response.status}")
        return
                
    logging.debug("Подключено к event-feed. Обработка данных...")
    try:
        for line in response.iter_lines():
            if line:  # игнорируем пустые keep-alive строки
                try:
                    event = json.loads(line.decode('utf-8'))
                    if is_accepted_solution(event):
                        fetch_solution_details(solve_url, cookies, event)
                except json.JSONDecodeError as e:
                    logging.error(f"Ошибка парсинга JSON: {e}")
    finally:
        response.close()

def is_accepted_solution(event):
    return (
        event.get("type") == "judgements" and 
        event.get("data", {}).get("judgement_type_id") == "AC"
    )

def fetch_solution_details(base_url, cookies, event):
    solution_id = event.get("data", {}).get("submission_id")
    
    solution_url = f"{base_url}api/v0/solutions/{solution_id}"
    resp = requests.get(solution_url, headers={'X-Solve-Sync': 'true'}, cookies=cookies)

    if resp.status == 200:
        solution_data = resp.json()
        logging.info(f"Новое принятое решение (ID: {solution_id}):", solution_data["problem"]["id"], solution_data["problem"]["statement"]["title"], solution_data["scope_user"]["title"])
    else:
        logging.error(f"Не удалось получить решение {solution_id}: {resp.status}")

parse_accepted_solutions()