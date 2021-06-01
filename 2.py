import os
import re
from requests import get


def download_file_log(url_log, local_filename="nginx_logs.txt"):
    """ function to download log file
    :param url_log: source URL
    :param local_filename: output file
    """
    with get(url_log, stream=True) as row:
        row.raise_for_status()  # проверка работы URL
        with open(local_filename, 'wb') as file:
            for chunk in row.iter_content(chunk_size=8192):
                file.write(chunk)
    return local_filename


url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
nginx_log_file = "nginx_logs.txt"
"""
r'((?:\d{1,3}\.){3}(?:\d{1,3}){1})' regex for IP
r'(?:\[)(.*)(?:])' regex for date
r'\s"{1}([A-Z]+)' regex for request type
r'(?:\/(.*))' regex for url
r'(?:\/(?:.*)"\s)(\d+)(?:\s)(\d+)' regex for response
"""
reg = r'((?:\d{1,3}\.){3}(?:\d{1,3}){1})' \
      r'(?:\s-){2}\s' \
      r'(?:\[)(.*)(?:])' \
      r'\s"{1}([A-Z]+)' \
      r'\s{1}' \
      r'(?:\/(.*))' \
      r'(?:\s[A-Z]{4})' \
      r'(?:\/(?:.*)"\s)(\d+)(?:\s)(\d+)'
BIG_REGEX = re.compile(reg)
result = []
if not os.path.exists(nginx_log_file):
    nginx_log_file = download_file_log(url, nginx_log_file)
with open(nginx_log_file, 'r', encoding='utf-8') as log_file:
    for line in log_file:
        result.append(BIG_REGEX.findall(line.strip()))
print(result)
