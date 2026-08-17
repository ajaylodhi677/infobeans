time = int(input("Enter time in seconds: "))

# calculate hours
hours = time//3600

remainder = time%3600

# calculate minutes and seconds
minutes= remainder//60
seconds = remainder%60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")


