from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()

headers["authority"] = "statusinvest.com.br"
headers["accept"] = "*/*"
headers["accept-language"] = "en-US,en;q=0.8"
headers["content-type"] = "application/x-www-form-urlencoded; charset=UTF-8"
headers["origin"] = "https://statusinvest.com.br"
headers["sec-ch-ua"] = '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = '"Windows"'
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "same-origin"
headers["sec-gpc"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
