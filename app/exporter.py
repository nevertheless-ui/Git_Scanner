import os
from datetime import datetime



def export_scan_results(host, port, request_code, header):
    filename = os.path.join(f'output/{request_code}.txt')
    with open(filename, 'a', encoding='utf8') as export_file:
        line = f'{datetime.now()} | {host} | {port} | {header}\n'
        export_file.write(line)
