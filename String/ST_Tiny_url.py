"""
inyURL is a URL shortening service where you enter a URL
such as https://leetcode.com/problems/design-tinyurl
and it returns a short URL such as http://tinyurl.com/4e9iAk.
Design a class to encode a URL and decode a tiny URL
"""
class Codec:

    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)


    def decode(self, shortUrl):
        return self.urls[int(shortUrl.split('/')[-1])]

codec = Codec()
longUrl = "https://leetcode.com/problems/design-tinyurl"
shortUrl = codec.encode(longUrl)
print(shortUrl)

decoded_url = codec.decode(shortUrl)
print(decoded_url)
