import requests;
from bs4 import BeautifulSoup;
import jianshu_saver;

class JianshuCrawler:
    def __init__(self):
        self.saver = jianshu_saver.Saver();

    def crawl(self, rootURL):
        httpConn = requests.get(rootURL);
        if(httpConn.status_code == 200):
            soup = BeautifulSoup(httpConn.text, 'html.parser', from_encoding='utf-8');
            titles = soup.find_all("a", class_="title");
            abstracts = soup.find_all("p", class_="abstract");
            times = soup.find_all("span", class_="time");
            for index in range(len(titles)):
                self.saver.save(titles[index].get_text(),abstracts[index].get_text(),times[index]["data-shared-at"].split("T")[0]);
                #print titles[index].get_text();
                #print abstracts[index].get_text();
                #print times[index]["data-shared-at"].split("T")[0];
        else:
            print(httpConn.status_code);

if __name__ == "__main__":
    rootURL = "http://www.jianshu.com/u/93539be96624";
    obj_crawler = JianshuCrawler();
    obj_crawler.crawl(rootURL);
