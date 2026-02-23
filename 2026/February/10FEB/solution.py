from datetime import datetime

def get_relative_results(results):
    results.sort()
    origin = results[0]
    ans = []
    for item in results:
        if origin == item:
            ans.append("0")
        else:
            t1 = datetime.strptime(origin, "%H:%M:%S")
            t2 = datetime.strptime(item, "%H:%M:%S")
            diff = (t2 - t1).total_seconds()
            m, s = divmod(int(diff), 60)
            item = f"+{m}:{s:02d}"
            ans.append(item)
    print(ans)
    return ans
