import requests
from parsel import Selector

def get_products_from_aliexpress():

    r = requests.get('https://www.aliexpress.com/gcp/300000455/nkxMfXZYsW?spm=a2g0o.home.brazilchannel.1.31c81c91lFXAlt&disableNav=YES&pha_manifest=ssr&_immersiveMode=true', 
                    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'})
    sel = Selector(text=r.text)

    with open('webscraping/aliexpress/html/ali.html', 'w', encoding='utf-8') as f:
        f.write(r.text)

    results = list()

    blocks = sel.xpath('//a[@class="productContainer"]')

    for block in blocks:
        price = ''.join(block.xpath('.//div[contains(@id,"info_container")]/div[1]/div//text()').getall())
        title = block.xpath('.//div[contains(@id,"titleContainer")]//text()').get()
        results.append({title:price})

    return results

print(get_products_from_aliexpress())