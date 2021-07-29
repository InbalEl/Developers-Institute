import requests
import time

def timeResponse(url: str):
    print(url)
    start = time.perf_counter()
    response = requests.get(url)
    end = time.perf_counter()
    
    print(response.status_code)
    print(f'response elapsed field: {response.elapsed.total_seconds()}')
    print(f'delta, according to time lib: {(end - start)}')

print(timeResponse('https://www.ynet.co.il'))
print(timeResponse('https://www.ynet.co.il'))
print(timeResponse('https://www.youtube.com/'))
print(timeResponse('https://www.yellowheadinc.com/were-hiring/#career-opportunities'))

