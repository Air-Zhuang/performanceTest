# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/6 18:41'
import unittest
import requests
from ddt import data

@data
class Test_Get(unittest.TestCase):
    @data("clannad")
    def test_get(self,value):
        # value="clannad"
        headers = {
            'Connection': 'keep - alive',
            'Accept': '* / *',
            'is_xhr': '1',
            'X - Requested - With': 'XMLHttpRequest',
            'is_referer': 'https: // www.baidu.com / s?wd = '+value+' & rsv_spt = 1 & rsv_iqid = 0xaa0fe2a7000432c2 & issp = 1 & f = 8 & rsv_bp = 1 & rsv_idx = 2 & ie = utf - 8 & rqlang = cn & tn = baiduhome_pg & rsv_enter = 0 & oq = '+value+' & rsv_t = ecf0nLG6DBeu6ifMjONb96FvQ4krT1D42gTCJUOQ8w6i1fSjgJ % 2F4 % 2FAtl2SGUQoqFaeiI & rsv_pq = b4a6f62d00044939 & bs = '+value,
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 64.0.3282.119Safari / 537.36',
            'is_pbs': value,
            'Referer': 'https://www.baidu.com/s?wd='+value+'&rsv_spt=1&rsv_iqid=0xaa0fe2a7000432c2&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq='+value+'&rsv_t=603epzdy3BrXuzHhPEgfmdQBbUVJm6xlqd3odO00zIjh4gA81IzvL9gEpqyMUPZu8Myz&rsv_pq=9a4c0e2100049f7b',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
        }

        cookies={
            'BIDUPSID':'48AD96B46794EA9927C40F0C5891566E',
            'BAIDUID':'503683A39460C340A96141902EF0A7C4:FG = 1',
            'PSTM' : '1523445624',
            'BD_UPN' : '12314753',
            'ispeed_lsm' : '2',
            'BDUSS' : 'kJGN0VzLWpOU1VURWt0dHlGckxXZllsTkc5MXB2NXQtZzV4eFZofmk2M0d0d3BiQVFBQUFBJCQAAAAAAAAAAAEAAAAZEBOvYmVjbGFubmFkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMYq41rGKuNaV',
            'BDORZ' : 'B490B5EBF6F3CD402E515D22BCDA1598',
            'H_PS_PSSID' : '1423_21100_26350_22073',
            'BD_CK_SAM':'1',
            'PSINO' : '1',
            'BDRCVFR[feWj1Vr5u3D]' : 'I67x6TjHwwYf0',
            'BD_HOME' : '1',
            'sugstore' : '0',
            'H_PS_645EC' : '603epzdy3BrXuzHhPEgfmdQBbUVJm6xlqd3odO00zIjh4gA81IzvL9gEpqyMUPZu8Myz',
            'BDSVRTM' : '164',
            'WWW_ST' : '1525601827415',
        }
        res=requests.get(url='https://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isbd=1&isid=9a4c0e2100049f7b&wd='+value+'&rsv_spt=1&rsv_iqid=0xaa0fe2a7000432c2&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq='+value+'&rsv_t=603epzdy3BrXuzHhPEgfmdQBbUVJm6xlqd3odO00zIjh4gA81IzvL9gEpqyMUPZu8Myz&rsv_pq=9a4c0e2100049f7b&bs='+value+'&rsv_sid=1423_21100_26350_22073&_ss=1&clist=&hsug=&f4s=1&csor=7&_cr1=30679',
                         headers=headers,cookies=cookies,verify=False)
        print "==============================="
        print res.text
        print res.status_code

if __name__ == '__main__':
    unittest.main()

    # mysuit=unittest.TestSuite()
    # mysuit.addTest(MyTestCase.test_get())
    # myrunner=unittest.TextTestRunner(verbosity=2) #verbosity=2感觉像是多了路径
    # myrunner.run(mysuit)


    # cases = unittest.TestLoader().loadTestsFromTestCase(Test_Get)
    # myrunner = unittest.TextTestRunner()  # verbosity=2感觉像是多了路径
    # myrunner.run(cases)
