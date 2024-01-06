import multiprocessing
_ = multiprocessing.cpu_count()
workers = (4 if _ > 4 else _) * 2 + 1
bind = '0.0.0.0:5000'
timeout = 0