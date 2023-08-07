def check_health_label(label):
    red_count = label.count('R')
    yellow_count = label.count('Y')

    if red_count >= 3 or (red_count >= 2 and yellow_count >= 2) or (red_count + yellow_count == 5):
        print("nakhor lite")
    else:
        print("rahat baash")


health_label = input().strip().upper()
check_health_label(health_label)
