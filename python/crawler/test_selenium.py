import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# 添加用户代理
# options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

driver_path = ChromeDriverManager().install()
print(f'>> Driver installed in: {driver_path}')
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# driver.get("https://www.zhihu.com/hot")
driver.get("https://movie.douban.com/top250")

print(f'>> website title: {driver.title}')

def get_movies(driver):
    # 豆瓣电影 top250
    # #content > div > div.article > ol > li > div
    # movies = driver.find_elements(By.CSS_SELECTOR, '#content > div > div.article > ol > li > div')
    # #content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a
    a_elements = driver.find_elements(By.CSS_SELECTOR, '#content > div > div.article > ol > li > div > div.info > div.hd > a')
    # 尝试爬取知乎热榜失败
    # 登陆报错「请求参数异常，请更新客户端后重试」
    # #TopstoryContent > div > div.Topstory-hot.HotList.css-1x36n8t > div.HotList-list > section:nth-child(1)
    # topics = driver.find_elements(By.CSS_SELECTOR, '#TopstoryContent > div > div.Topstory-hot.HotList.css-1x36n8t > div.HotList-list > section')

    movies_info = []
    for a_element in a_elements:
        url = a_element.get_attribute("href")
        comments = get_comments(url)
        movies_info.append({
            'name': a_element.text,
            'url': a_element.get_attribute("href"),
            'comments': comments
        })
    return movies_info

def get_comments(url):
    main_window = driver.current_window_handle
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get(url)
    comments = []
    for i in range(5):
        # #hot-comments > div:nth-child(1) > div > p > span
        elem = driver.find_element(By.CSS_SELECTOR, f'#hot-comments > div:nth-child({i+1}) > div > p > span')
        # print(elem.text)
        comments.append(elem.text)

    driver.close()
    driver.switch_to.window(main_window)
    return comments

movie_comments = get_movies(driver)
# 使用 indent=2 让 JSON 文件更易读
# 使用 ensure_ascii=False 确保中文字符正确显示
with open('movie_comments.json', 'w', encoding='utf-8') as f:
    json.dump(movie_comments, f, ensure_ascii=False, indent=2)

driver.quit()