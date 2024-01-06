import multiprocessing
_ = multiprocessing.cpu_count()
workers = (4 if _ > 4 else _) * 2 + 1
bind = '0.0.0.0:12345'
timeout = 0
preload_app = True