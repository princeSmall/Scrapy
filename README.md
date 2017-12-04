#### 创建项目

1、scrapy startproject tutorial （你的项目名称）
    
   1. spider 爬虫目录，用于创建文件，编写爬虫代码
   2. settings 配置文件
   3. items 设置数据存储
   4. pipelines 数据处理和存储

#### 编写爬虫代码

1、定义一个类princesmall，导入scrapy

2、必须定义name、allowed_domains、start_urls

  1. name：爬虫的名字
  2. allowed_domains：爬取的范围
  3. start_urls 爬取得开始网页

  
         name = "lezhi"
         allowed_domains = ["lezhi.com"]
         start_urls = [
        "http://www.lezhi.com/Resume/hefei?perpage/10/companyname_type/1/keywords/%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6/degreem/0/page/1=",
         ]

3、def parse （self，response）
  
     scrapy 返回response的默认方法

  1. css解析，直接定位到目录

        allfill = response.css(".right.fll").xpath("label/div[1]/text()").extract()
    
  2. XPath解析，层层下拨

        name = response.xpath('//a/div/label/div[1]/text()').extract()
        
        
#### 保存爬取数据

1. settings.py 文件

        ROBOTSTXT_OBEY = False
        
        ITEM_PIPELINES = {
        'tutorial.pipelines.TutorialPipeline': 300,
        }
        
2. items.py 文件

        class TutorialItem(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        company = scrapy.Field()
        name = scrapy.Field()
        info = scrapy.Field()
        pass
 
3. pipelines.py 文件

        import json
        import codecs

        class TutorialPipeline(object):
               def __init__(self):
                   self.file = codecs.open('small.json','wb',encoding='utf-8')

               def process_item(self, item, spider):
                   line = json.dumps(dict(item)) + '\n'
                   print line, '>>>>>'
                   self.file.write(line.decode("unicode_escape"))
                   return item
               
                   
好吧，简单的数据爬取，完美收关

#### 项目中遇到的问题总结

下载scrapy及使用问题

* Permission denied 

        权限问题：加sudo，输入密码

* TLSVersion.TLSv1_1: SSL.OP_NO_TLSv1_1 

        版本问题： pip install scrapy 需要 pyopenssl  twisted ==13.1.0

* spider加载item类中方法，找不到

        目录问题：from ..items import DmozItem（第一个点表示当前目录，第二个点表示上层目录）
