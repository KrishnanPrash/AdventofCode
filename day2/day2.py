
# Data cleaning and data processing
data = None
with open("day2_input.txt", "r") as f:
    data = [[int(level) for level in line.split()] for line in f.readlines()]
diff_fn = lambda x,y: abs(x-y)

################# PART 1 #################
tracker1 = []
safeReportCount = 0
for report_idx, report in enumerate(data):
    if report[0] == report[1]:
        continue
    isIncreasing = report[0] < report[1]
    comp_fn = int.__lt__ if isIncreasing else int.__gt__
    i = 1
    while i < len(report):
        if comp_fn(report[i-1], report[i]) and (1 <= diff_fn(report[i-1], report[i]) <= 3):
            i += 1
        else:
            break
    if i == len(report): # Reached the end of the report traversal
        safeReportCount += 1
        tracker1.append(f"{report_idx}, {report}")

print(f"The safe report count is {safeReportCount}")

################# PART 2 #################
tracker2 = []

def is_increasing(nums):
    inc_cnt, dec_cnt = 0, 0
    idx = 1
    while idx < len(nums):
        diff = nums[idx] - nums[idx-1]
        if diff > 0: inc_cnt += 1
        elif diff < 0: dec_cnt += 1
        idx += 1
    return inc_cnt > dec_cnt

safeReportCount = 0
for report_idx, report in enumerate(data[:300]):
    comp_fn = int.__lt__ if is_increasing(report) else int.__gt__
    bad_level_seen = 0
    idx = 1
    log = ""
    while idx < len(report):
        if comp_fn(report[idx-1], report[idx]) and (1 <= diff_fn(report[idx-1], report[idx]) <= 3):
            idx += 1
        else:
            log += f"BAD LEVEL SEEN: {report[idx-1]=}, {report[idx]=}\n"
            bad_level_seen += 1
            report.pop(idx)
            # idx -= 1 
            
        if bad_level_seen > 1: 
            break
    
    if idx == len(report): # Reached the end of the report traversal
        safeReportCount += 1
        tracker2.append(f"{report_idx}, {report}")
    if f"{report_idx}, {report}" in tracker1:
        print(f"{report_idx}, {report} is supposed to be safe.")
        print(log)

print(f"The safe report count is {safeReportCount}")
