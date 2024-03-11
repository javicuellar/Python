import psutil


print("CPU")
print(psutil.cpu_times())
for x in range(3):
    print(psutil.cpu_percent(interval=1))
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))
print(psutil.cpu_count())
print(psutil.cpu_stats())
print(psutil.cpu_freq())
print(psutil.getloadavg())  # also on Windows (emulated)

print("MEMORIA")
print(psutil.virtual_memory())
print(psutil.swap_memory())

print("PARTICIONES")
for i in psutil.disk_partitions():
    print(i)

print("DISCO")
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters(perdisk=False))

print("RED")
print(psutil.net_io_counters(pernic=True))
print(psutil.net_connections(kind='tcp'))
print(psutil.net_if_addrs())
print(psutil.net_if_stats())

print("OTROS")
print(psutil.users())
print(psutil.boot_time())

print("GESTIÓN PROCESOS")
print(psutil.pids())
p = psutil.Process(18888)
print("Nombre: ", p.name())
print("Ejecutable: ", p.exe())
# print("Directorio: ", p.cwd())
print("Línea de comando: ", p.cmdline())
print("Hijos: ", p.children(recursive=True))
print("Padres: ", p.parents())
print("Status: ", p.status())
print("Memoria: ", p.memory_info())
print("Conexiones: ", p.connections(kind='tcp'))

print("Test: ", psutil.test())

# Función que informa de los procesos terminados
def on_terminate(proc):
    print("process {} terminated".format(proc))

# waits for multiple processes to terminate
gone, alive = psutil.wait_procs(psutil.process_iter(), timeout=3, callback=on_terminate)
