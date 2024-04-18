import urllib.request as req

def getTitlesAndLinks(url): # 返回([[标题, 连结]]， 下一页连结)
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    # 抓取文章连接，生成列表
    titles = root.find_all("div", class_="title")
    article_link_lst = []
    for title in titles:
        if title.a != None:
            article_title = title.a.string
            article_link = "https://www.ptt.cc" + title.a.get("href")
            article_link_lst.append([article_title, article_link])
    # 抓取下一页的连结
    nextLink = "https://www.ptt.cc" + root.find("a", string="‹ 上頁").get("href")
    print(nextLink)
    return (article_link_lst, nextLink)

def getArticleInfo(url):
    print(url)
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    # 获取 Like/DislikeCount
    count_like = 0
    count_dislike = 0
    push_lst = root.find_all("div", class_="push")
    for push in push_lst:
        if push.span.string == "推 ":
            count_like += 1
        elif push.span.string == "噓 ":
            count_dislike += 1
    # 获取 PublishTime
    spans = root.find_all("span", class_="article-meta-value")
    if len(spans) < 4:
        publish_time = ""
    else:
        publish_time = spans[3].string
    return [str(count_like), str(count_dislike), publish_time]

contents_page_url = "https://www.ptt.cc/bbs/Lottery/index.html"
# 抓取3个页面的data
count = 0
while count < 3:
    art_titl_links = getTitlesAndLinks(contents_page_url)
    for art in art_titl_links[0]:
        article_link = art[1]
        article_info = getArticleInfo(article_link)
        with open("article.csv", "a+", encoding="utf-8") as f:
            f.write(art[0] + ',')
            line = ','.join(article_info)
            f.write(line + '\n')
    contents_page_url = art_titl_links[1]
    count += 1
    print("抓完一页, ", contents_page_url)