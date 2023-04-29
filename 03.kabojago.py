import requests
from bs4 import BeautifulSoup

print("[제주도]")
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%A0%9C%EC%A3%BC%EB%8F%84+%EB%AA%85%EC%86%8C&oquery=%EC%A0%9C%EC%A3%BC%EB%8F%84+%EA%B4%80%EA%B4%91%EC%A7%80&tqi=iZzt9lp0J14ssd8jf7ossssstlh-436676"
res = requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text, "lxml")
jeju_list = soup.find("ul", attrs={"class":"zPw6U"}).find_all("li",attrs={"class":"S0Ns3 DyAcu"}, limit=6)
for index, jeju in enumerate(jeju_list):
    title = jeju.find("span", attrs={"class":"xBZDS"}).get_text()
    second = jeju.find("div", attrs={"class":"qVZk1"}).get_text()
    link = jeju.find("a")["href"]
    print("{}. {} ({})".format(index+1, title, second))
    print(" (링크 : {})".format(link))
print()