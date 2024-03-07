# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class DatasourcePipeline:
    def process_item(self, item, spider):
        return item

class SaveToMongoDBMPacketStorm:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://mongo:1qazse4%40W%23@194.233.95.254:27017/?authSource=admin'),
            mongo_db=crawler.settings.get('MONGO_DB', 'MPacketStorm')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        data = {
            'categories' : 'Malware Packet Storm',
            'title': adapter.get('title'),
            'source': adapter.get('source'),
            'postedDate': adapter.get('postedDate'),
            'url': adapter.get('url'),
            'author': adapter.get('author'),
            'articleText': adapter.get('articleText'),
            
        }
        self.db.malwarespider.insert_one(data)
        return item
    
class SaveToMongoDBRPacketStorm:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://mongo:1qazse4%40W%23@194.233.95.254:27017/?authSource=admin'),
            mongo_db=crawler.settings.get('MONGO_DB', 'RPacketStore')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        data = {
            'categories' : 'Ransom Packet Storm',
            'title': adapter.get('title'),
            'postedDate': adapter.get('postedDate'),
            'url': adapter.get('url'),
            'author': adapter.get('author'),
            'articleText': adapter.get('articleText'),
            
        }
        self.db.ransomspider.insert_one(data)
        return item
class ScmagazinePipeline:
    def process_item(self, item, spider):
        from itemadapter import ItemAdapter

        adapter = ItemAdapter(item)
        article_text = adapter.get('articleText')
        if article_text:
            stripped_text = ' '.join(article_text.split())
            adapter['articleText'] = stripped_text
        return item
    
class SaveToMongoDBScmagazine:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://mongo:1qazse4%40W%23@194.233.95.254:27017/?authSource=admin'),
            mongo_db=crawler.settings.get('MONGO_DB', 'scmagazine')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        data = {
            'categories' : 'Malware Scmagazine',
            'title': adapter.get('title'),
            'postedDate': adapter.get('postedDate'),
            'url': adapter.get('url'),
            'author': adapter.get('author'),
            'articleText': adapter.get('articleText'),
            
        }
        self.db.malwarescmagazine.insert_one(data)
        return item
    
class SaveToMongoDBMTheregister:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://mongo:1qazse4%40W%23@194.233.95.254:27017/?authSource=admin'),
            mongo_db=crawler.settings.get('MONGO_DB', 'mtheregister')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        data = {
            'categories' : 'Malware The Register',
            'title': adapter.get('title'),
            'postedDate': adapter.get('postedDate'),
            'url': adapter.get('url'),
            'author': adapter.get('author'),
            'articleText': adapter.get('articleText'),
            
        }
        self.db.malwaretheregister.insert_one(data)
        return item
    
class SaveToMongoDBRTheregister:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://mongo:1qazse4%40W%23@194.233.95.254:27017/?authSource=admin'),
            mongo_db=crawler.settings.get('MONGO_DB', 'rtheregister')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        data = {
            'categories' : 'Ransomware The Register',
            'title': adapter.get('title'),
            'postedDate': adapter.get('postedDate'),
            'url': adapter.get('url'),
            'author': adapter.get('author'),
            'articleText': adapter.get('articleText'),
            
        }
        self.db.ransomtheregister.insert_one(data)
        return item
    
class SaveToMongoDBMTripwire:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://mongo:1qazse4%40W%23@194.233.95.254:27017/?authSource=admin'),
            mongo_db=crawler.settings.get('MONGO_DB', 'mtripwire')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        data = {
            'categories' : 'Ransomware The Register',
            'title': adapter.get('title'),
            'postedDate': adapter.get('postedDate'),
            'url': adapter.get('url'),
            'author': adapter.get('author'),
            'articleText': adapter.get('articleText'),
            
        }
        self.db.malwaretripwire.insert_one(data)
        return item

