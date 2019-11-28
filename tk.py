import requests

baseUrl = 'https://www.tkmaxx.com/uk/en'

headers = {
    'Content-Type': 'application/json',
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a70fb012-6228-4a09-bc96-9add81e3f6da",
    'Host': "www.tkmaxx.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "_abck=B86753B83EF126E5BCF461C35CBC1260~-1~YAAQhWReaJAEShltAQAAUrxpgQI9YePk9II5eeG7TKpvZW4TTvHZuriWi4MLbJll9MBDuA1HE9hN1ieZzw+WQ5jBIHgoLLCCrcm2jB4+X8gF+XX+RX7aZNTJ6KyDQQ1/ONeSGrIzy45s+xzvwRtSpCorPE419THdlnKqs+z+jpVb1WaA9q/qQ8xm6QB8ZKkTaxr69vkwW9FuaDmigpfNG8eTa+I07+24o5X++iGsu9VQWIcb1CJ+TZ+rgsH1XvEvKI9yc8AnnGWUQSwS6V7T8JbeCgsW~-1~-1~-1; bm_sz=68C355B39B9152DE94B3F12D66DBC333~YAAQRDwQAkY7P4NtAQAAFFe6kAXHAP39PKYdNXMoN8k6QkksCTlYaS219IBgdcUFTiPP1FP4aEB2+E3LlMwiP3pwGtOGYbFhckx23v3aCigYRMRUnNa71BgG+JWkPVkN+edtb8KLRwuKCIf7+Xk+DgqUsB++s4CCKwl34TtxRnpIOtB5ECYsdL3BHdbVF/6Q; JSESSIONID=A5972C9C1ACD1723E817F493FD00189D; ROUTEID=.route5; minicartRefresh=false",
    'Connection': "keep-alive",

}

brands = dict()
brands["Adidas"] = set()
brands["Balenciaga"] = set()
brands["Banana Republic"] = set()
brands["Barbour"] = set()
brands["Billabong"] = set()
brands["Burberry"] = set()
brands["Buff"] = set()
brands["Burlington"] = set()
brands["Burton"] = set()
brands["Calvin Klein"] = set()
brands["Canada Goose"] = set()
brands["Champion"] = set()
brands["Christian Berg"] = set()
brands["Columbia"] = set()
brands["Diesel"] = set()
brands["Element"] = set()
brands["Gucci"] = set()
brands["Hackett"] = set()
brands["Herschel"] = set()
brands["Hugo Boss"] = set()
brands["Jack Wolfskin"] = set()
brands["Joop"] = set()
brands["Levis"] = set()
brands["Lululemon"] = set()
brands["Massimo Dutti"] = set()
brands["Mustang"] = set()
brands["Nautica"] = set()
brands["Nike"] = set()
brands["Original Penguin"] = set()
brands["Patagonia"] = set()
brands["Polo"] = set()
brands["Polo Ralph Lauren"] = set()
brands["Ralph Lauren"] = set()
brands["Salomon"] = set()
brands["Scotch & Soda"] = set()
brands["Skagen"] = set()
brands["SmartWool"] = set()
brands["Spyder"] = set()
brands["Starter"] = set()
brands["Ted Baker"] = set()
brands["The North Face"] = set()
brands["Tigha"] = set()
brands["Tommy Hilfiger"] = set()
brands["Turtle"] = set()
brands["Under Armour"] = set()
brands["US Polo Assn"] = set()
brands["Volcom"] = set()

# Materials
brands["Cashmere"] = set()


def add_brands_from_url(url):
    response = requests.get(url, headers=headers).json()
    if 'results' not in response:
        return
    results = response['results']

    for item in results:
        brand = item['brandName']
        if brand in brands:
            brands[brand].add('    ' + item['label'] + ': ' + baseUrl + item['url'])
        if is_cashmere(item) and is_not_scarf(item):
            brands["Cashmere"].add('    ' + item['brandName'] + ' ' + item['label'] + ': ' + baseUrl + item['url'])

def is_cashmere(item):
    return item['materialBadgeName'] == "Cashmere" or "Cashmere" in item['label']

def is_not_scarf(item):
    return "Scarf" not in item['label'] and "Gloves" not in item['label']

allItemsUrl = 'https://www.tkmaxx.com/uk/en/men/clothing/c/02020000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0002%252C0008%252CUniversal%252CM&fetchAll=true&page=50'
newItemsUrl = 'https://www.tkmaxx.com/uk/en/men/new-in-menswear/c/02010000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0002%252C0008%252CUniversal%252CM&fetchAll=true&page=50'
todayArrUrl = 'https://www.tkmaxx.com/uk/en/todays-arrivals/c/00000000/autoLoad?q=&sort=percentSaving-desc&facets=stockLevelStatus%3AinStock%3AdepartmentFacet%3A02000000&fetchAll=true&page=50'
clearanceUrl = 'https://www.tkmaxx.com/uk/en/clearance/men/c/05020000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0002%252C0008%252CUniversal%252CM&fetchAll=true&page=50'
activeWearUrl = 'https://www.tkmaxx.com/uk/en/men/activewear/c/02040000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0002%252C0008%252CUniversal%252CM&fetchAll=true&page=50'
accessoriesUrl = 'https://www.tkmaxx.com/uk/en/men/accessories/c/02030000/autoLoad?q=&sort=&facets=&fetchAll=true&page=50'
shoesUrl = 'https://www.tkmaxx.com/uk/en/men/shoes/c/02050000/autoLoad?q=&sort=publishedDate-desc&facets=size%3A0007%252C0022%252CShoes%252C8%3AstockLevelStatus%3AinStock&fetchAll=true&page=50'
savingsUrl = 'https://www.tkmaxx.com/uk/en/men/biggest-savings/c/02060000/autoLoad?q=&sort=price-asc&facets=allCategories%3A02000000%3ApriceValue%3A%255B20%2520TO%25201000%255D%3AstockLevelStatus%3AinStock%3Asize%3A0002%252C0008%252CUniversal%252CM%3Asize%3A0004%252C0011%252CChest%252C38%3Asize%3A0007%252C0022%252CShoes%252C8&fetchAll=true&page=50'
earlyAccessUrl = 'https://www.tkmaxx.com/uk/en/mens-early-access/c/88000201/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0002%252C0008%252CUniversal%252CM&fetchAll=false&page=50'

add_brands_from_url(todayArrUrl)
add_brands_from_url(allItemsUrl)
add_brands_from_url(newItemsUrl)
add_brands_from_url(clearanceUrl)
add_brands_from_url(activeWearUrl)
add_brands_from_url(accessoriesUrl)
add_brands_from_url(shoesUrl)
add_brands_from_url(savingsUrl)
add_brands_from_url(earlyAccessUrl)

totalItems = 0
for brandName in brands:
    items = brands[brandName]
    if items:
        print(brandName + ' (' + str(len(items)) + ' items)')
        for item in items:
            totalItems += 1
            print(item)

print("Total items found: {}".format(totalItems))
