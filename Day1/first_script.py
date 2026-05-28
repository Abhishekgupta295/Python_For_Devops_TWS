import psutil

def check_cpu_threshold():
    cpu_threshold = int(input("Enter CPU usage threshold (in percentage): "))

    user_cpu_usage = psutil.cpu_percent(interval = 1)

    if user_cpu_usage > cpu_threshold:
        print(f"CPU usage is high: {user_cpu_usage}% Send Email Alert !!")
    else:
        print(f"Cpu is safe range , it is {user_cpu_usage}%")    

check_cpu_threshold()   