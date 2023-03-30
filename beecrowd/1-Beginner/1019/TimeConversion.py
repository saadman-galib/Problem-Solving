seconds = int(input())

hour = seconds // 3600
seconds -= hour * 3600

minutes = seconds // 60
seconds -= minutes * 60

print(f"{hour}:{minutes}:{seconds}")