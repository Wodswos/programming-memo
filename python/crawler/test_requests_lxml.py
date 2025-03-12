import requests
# 导入所需的库
from lxml import etree

# 豆瓣读书 Top 250 页面 URL
url = 'https://book.douban.com/top250'

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # 发送 GET 请求获取页面内容
    response = requests.get(url, headers=headers)

    # 使用 lxml 解析 HTML
    html = etree.HTML(response.text)

    # 使用 xpath 提取书籍标题
    book_titles = html.xpath('//div[@class="pl2"]/a/@title')

    # 打印所有书籍标题
    for i, title in enumerate(book_titles, 1):
        print(f"{i}. {title}")

except requests.RequestException as e:
    print(f"请求失败: {e}")
except Exception as e:
    print(f"解析失败: {e}")
