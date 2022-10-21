import requests
import random
import os

from tqdm import tqdm
from fake_useragent import UserAgent

from app import exporter

ports = {
    80 : "http://",
    443 : "https://",
}


def read_inputs():
    input_filename = 'all_registered_domains_ru.txt'
    input_filepath = os.path.join('input', input_filename)
    with open(input_filepath, 'r') as file:
        domains = [line.rstrip() for line in file]
    return domains


def run_scan(targets):
    for _ in tqdm(range(100)):
        target = random.choice(targets)
        request_header = {'User-Agent': UserAgent().chrome}
        for port in ports.keys():
            suffix = '/.git/HEAD'
            full_target = f'{ports[port]}{target}:{port}{suffix}'
            try:
                r = requests.get(full_target, headers=request_header)
                status = r.status_code
            except requests.exceptions.ConnectionError:
                status = 'Failed'
            exporter.export_scan_results(target, port, status, request_header)


if __name__ == "__main__":
    targets = read_inputs()
    run_scan(targets)
