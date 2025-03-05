from DrissionPage import ChromiumPage
import time
import json


class DoubanBooksCrawlerWeb:
    """豆瓣图书Top250爬虫类 - WebPage版本"""

    def __init__(self, save_path='douban-books.json'):
        """初始化爬虫"""
        self.page = ChromiumPage()
        self.base_url = 'https://book.douban.com/top250'
        self.books = []
        self.save_path = save_path

    def crawl_page(self, page_num=0):
        """爬取指定页码的数据"""
        url = self.base_url
        if page_num > 0:
            url = f"{self.base_url}?start={page_num * 25}"

        try:
            print(f"正在爬取第 {page_num + 1} 页...")
            self.page.get(url)

            # 获取所有图书项
            for link in self.page.eles('css:td div a'):
                href = link.attr('href')
                if href:  # 确保链接存在
                    book_detail = self.get_book_detail(href)
                    if book_detail:  # 如果成功获取到详情，添加到books列表中
                        self.books.append(book_detail)

            return True

        except Exception as e:
            print(f"爬取第 {page_num + 1} 页时出错: {e}")
            return False

    def get_book_detail(self, url):
        """获取图书详细信息"""
        try:
            # 创建新的标签页访问详情页
            new_page = self.page.new_tab(url)

            # xpath version:
            # title_h1 = new_page.ele('xpath://*[@id="wrapper"]/h1/span')
            # css selector version:
            title_h1 = new_page.ele('css:#wrapper > h1 > span')

            # 一般 css selector 为 #link-report > div > div
            # 简介比较长的会有一个「展开全部」，其 css selector 为 #link-report > span.all.hidden > div > div
            intro_div = new_page.ele("css:#link-report div > div")
            # div element 有一系列 p element，所有 p element 中内容需要合并起来是简介内容
            # 合并所有p元素的文本内容
            intro = ''
            for p in intro_div.eles('css:p'):
                intro += p.text + '\n'
            
            # 去除多余空白
            intro = intro.strip()
            print(f"Title: {title_h1.text}")

            # 获取详细信息
            detail = {
                'title': title_h1.text,
                'intro': intro
            }
            # 关闭标签页
            new_page.close()
            return detail

        except Exception as e:
            print(f"获取详情页信息失败: {e}")
            return {}
    
    def crawl_all_pages(self, max_pages=10):
        """爬取所有页面的数据"""
        for page_num in range(max_pages):
            success = self.crawl_page(page_num)
            if not success:
                print(f"爬取终止于第 {page_num + 1} 页")
                break
                
            # 随机延迟，避免请求过于频繁
            delay = 3 + (page_num % 3)
            print(f"等待 {delay} 秒后继续...")
            time.sleep(delay)
        self.save_data()

    def save_data(self):
        """保存爬取的数据到文件"""
        if not self.books:
            print("没有数据可保存")
            return
        try:
            with open(self.save_path, 'w', encoding='utf-8') as f:
                json.dump(self.books, f, ensure_ascii=False, indent=2)
            print(f"数据已保存到: {self.save_path}")
            print(f"共爬取 {len(self.books)} 本图书信息")
        except Exception as e:
            print(f"保存数据时出错: {e}")
    
    def run(self, max_pages=10):
        """运行爬虫"""
        start_time = time.time()
        print(f"开始爬取豆瓣图书Top250...")

        try:
            self.crawl_all_pages(max_pages)
            self.save_data()
        finally:
            # 确保浏览器正确关闭
            self.page.quit()
        
        end_time = time.time()
        print(f"爬取完成，耗时: {end_time - start_time:.2f} 秒")


if __name__ == '__main__':
    # 创建爬虫实例并运行
    crawler = DoubanBooksCrawlerWeb()
    crawler.run(max_pages=2)  # 测试爬取前2页
