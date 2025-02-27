temperatures = list(map(int, input("Enter temperature readings: ").split()))

def analyze_weather(temperatures):
  avg_temp = sum(temperatures) / len(temperatures)
  highest_temp = max(temperatures)
  lowest_temp = min(temperatures)

  return avg_temp, highest_temp, lowest_temp

avg_temp, highest_temp, lowest_temp = analyze_weather(temperatures)

print(f"Average Temperature: {avg_temp}")
print(f"Highest Temperature: {highest_temp}")
print(f"Lowest Temperature: {lowest_temp}")