import os
import json


root_folder = 'venv'
stat_by_size = {}
m_size = 100
for root, _, files in os.walk(root_folder):
    for file in files:
        while os.stat(os.path.join(root, file)).st_size > m_size:
            m_size *= 10
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        stat_by_size.setdefault(m_size, (0, []))
        stat_by_size[m_size] = stat_by_size[m_size][0] + 1, stat_by_size[m_size][1]
        if ext not in stat_by_size[m_size][1]:
            stat_by_size[m_size][1].append(ext)
        m_size = 100
print(stat_by_size)
for_file = json.dumps(stat_by_size)
with open(root_folder + "_summary.json", 'w', encoding='utf=8') as sum_file:
    sum_file.write(for_file)
