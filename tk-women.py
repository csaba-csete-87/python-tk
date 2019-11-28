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
brands["Banana Republic"] = set()
brands["Burberry"] = set()
brands["Calvin Klein"] = set()
brands["Chanel"] = set()
brands["Columbia"] = set()
brands["Cos"] = set()
brands["Dior"] = set()
brands["Each Other"] = set()
brands["Gucci"] = set()
brands["Jack Wolfskin"] = set()
brands["Levis"] = set()
brands["Lululemon"] = set()
brands["Louis Vuitton"] = set()
brands["Massimo Dutti"] = set()
brands["Michael Kors"] = set()
brands["Moon Boot"] = set()
brands["Nike"] = set()
brands["Prada"] = set()
brands["Ralph Lauren"] = set()
brands["Royal Speyside"] = set()
brands["Ted Baker"] = set()
brands["Tiffany"] = set()
brands["Tommy Hilfiger"] = set()
brands["Under Armour"] = set()
brands["Valentino"] = set()
brands["Volcom"] = set()

# Shoes
brands["Hunter"] = set()
brands["Ecco"] = set()
brands["EMU"] = set()
brands["Red Valentino"] = set()
brands["UGG"] = set()
brands["Jimmy Choo"] = set()
brands["LA BOTTINE SOURIANTE"] = set()
brands["Salomon"] = set()
brands["Timberland"] = set()


def add_brands_from_url(url):
    response = requests.get(url, headers=headers)
    results = response.json()['results']

    for item in results:
        brand = item['brandName']
        if brand in brands:
            brands[brand].add('    ' + item['label'] + ': ' + baseUrl + item['url'])


allItemsUrl = 'https://www.tkmaxx.com/uk/en/women/clothing/c/01020000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0001%252C0003%252CUK%2520Women%252CUK%25208%3Asize%3A0002%252C0004%252CUniversal%252CXS%3Asize%3A0001%252C0002%252CUK%2520Women%252CUK%25206&fetchAll=true&page=100'
newItemsUrl = 'https://www.tkmaxx.com/uk/en/women/new-in-womenswear/c/01010000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0001%252C0003%252CUK%2520Women%252CUK%25208%3Asize%3A0002%252C0004%252CUniversal%252CXS%3Asize%3A0001%252C0002%252CUK%2520Women%252CUK%25206&fetchAll=true&page=100'
clearanceUrl = 'https://www.tkmaxx.com/uk/en/clearance/women/c/05010000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0001%252C0003%252CUK%2520Women%252CUK%25208%3Asize%3A0002%252C0004%252CUniversal%252CXS%3Asize%3A0001%252C0002%252CUK%2520Women%252CUK%25206&fetchAll=true&page=100'
accessoriesUrl = 'https://www.tkmaxx.com/uk/en/women/accessories/c/01040000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock&fetchAll=true&page=100'
activeWearUrl = 'https://www.tkmaxx.com/uk/en/women/activewear/c/01030000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0001%252C0003%252CUK%2520Women%252CUK%25208%3Asize%3A0002%252C0004%252CUniversal%252CXS%3Asize%3A0001%252C0002%252CUK%2520Women%252CUK%25206&fetchAll=true&page=100'
shoesUrl = 'https://www.tkmaxx.com/uk/en/women/shoes/c/01050000/autoLoad?q=&sort=publishedDate-desc&facets=stockLevelStatus%3AinStock%3Asize%3A0007%252C0005%252CShoes%252C3%3Asize%3A0007%252C0004%252CShoes%252C2.5&fetchAll=true&page=100'

add_brands_from_url(allItemsUrl)
add_brands_from_url(newItemsUrl)
add_brands_from_url(clearanceUrl)
add_brands_from_url(accessoriesUrl)
add_brands_from_url(activeWearUrl)
add_brands_from_url(shoesUrl)

totalItems = 0
for brandName in brands:
    items = brands[brandName]
    if items:
        print(brandName + ' (' + str(len(items)) + ' items)')
        for item in items:
            totalItems += 1
            print(item)

print("Total items found: {}".format(totalItems))
