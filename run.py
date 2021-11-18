#%%
from user_agents import parse
user_agent = "Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2889 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/1696 MicroMessenger/8.0.15.2001(0x28000F41) Process/to"
ua = parse(user_agent)

print(ua.browser)
print(ua.os)



# %%
import csv
from user_agents import parse
reader = csv.reader(open('uaList.csv', 'r',encoding='UTF-8',errors='ignore'))
writer = csv.writer(open('uaOutput.csv', 'w'))

headers = next(reader)
headers.append("Browser")
headers.append("OperatingSystem")
writer.writerow(headers)
for row in reader:
    temp = parse(row[0])
    row.append(str(temp.browser))
    row.append(str(temp.os))
    writer.writerow(row)

# os = next(next(reader))
# os.append("OperatingSystem")
# writer.writerow(os)
# for row in reader:
#     temp = parse(row[0])
#     row.append(str(temp.os))
#     writer.writerows(row)
#     print(row)
 # %%
