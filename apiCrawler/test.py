green = 92 # green
red = 91 # red
print(f"\033[{green}m")
print(f"\033[0m")

percentage = 20.4
cnt = int(percentage//2)
progress_bar = "━" * cnt
remain_bar = "━" * (50 - cnt)

print(f"{percentage:4.1f}%", end="")

print(f"\033[{green}m {progress_bar}", end="")
print(f"\033[{red}m{remain_bar}", end="")
