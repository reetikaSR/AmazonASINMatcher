import AmazonASINMatcher

# s = "https://www.amazon.in/Vivo-V9-19-FullView-Sapphire/dp/B07D167YND/ref=br_msw_pdt-1?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=D34C7Q06RK4YAXM3DXZZ&pf_rd_t=36701&pf_rd_p=90db5b1f-b752-4136-91d6-e8b8af0dbb14&pf_rd_i=desktop"
# s = "https://www.amazon.co.jp/%E3%80%8C%E6%B5%B7%E5%A4%96%E7%99%BA%E9%80%81%E5%AF%BE%E5%BF%9C%E3%80%8D%E4%BC%9D%E7%B5%B1%E7%9A%84%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3-%E5%8D%97%E9%83%A8%E9%89%84%E5%99%A8-%E9%89%84%E7%93%B6-%E8%A6%B3%E6%9C%88-%E3%83%9B%E3%83%BC%E3%83%AD%E3%83%BC%E3%81%AA%E3%81%97-TBC005/dp/B01MXOY3UH/ref=sr_1_1_sspa?s=home&ie=UTF8&qid=1527788367&sr=1-1-spons&keywords=%E5%8D%97%E9%83%A8%E9%89%84%E5%99%A8+%E9%89%84%E7%93%B6&psc=1"
# s = "https://www.amazon.com.mx/Rich-Dad-Poor-Teach-Middle/dp/1612680194/ref=sr_1_1?s=books&ie=UTF8&qid=1527788593&sr=1-1&keywords=rich+dad+poor+dad"
# s = "https://www.amazon.com.mx/Rich-Dad-Poor-Teach-Middle/d/1612680194/ref=sr_1_1?s=books&ie=UTF8&qid=1527788593&sr=1-1&keywords=rich+dad+poor+dad"

# s = "www.google.com/Rich-Dad-Poor-Teach-Middle/dp/16126804/ref=sr_1_1?s=books&ie=UTF8&qid=1527788593&sr=1-1&keywords=rich+dad+poor+dad"
# s = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Delectronics&field-keywords=dp&rh=n%3A976419031%2Ck%3Adp"
s = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Delectronics&field-keywords=dp%2Ftiynt%2Fgd&rh=n%3A976419031%2Ck%3Adp%2Ftiynt%2Fgd"



obj = AmazonASINMatcher.url_matcher(s)
print(obj)

# mention its a python project in readme
# remove link string
# change region to market place
# pip3
# dont expose your object
# check license
# AmazonASinMAtcher