def predict_usage(usage_values):
    diff = usage_values[-1] - usage_values[0]
    slope = diff / (len(usage_values) - 1)
    return usage_values[-1] + slope
# Historical data: hours of usage in the past 4 weeks
usage_values = [50, 60, 70, 80]
next_week_usage = predict_usage(usage_values)

print(f"Predicted ChatGPT usage for next week: {next_week_usage}")
