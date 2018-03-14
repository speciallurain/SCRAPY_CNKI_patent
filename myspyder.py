# -*- coding: utf-8 -*-
#!/usr/bin/python
import re
import scrapy
from scrapy.http import Request
import urlparse
import requests
import hashlib
from scrapy.loader import ItemLoader
import time
import numpy
import math
from newSpider.items import InfoPipeline

class ItcastSpider(scrapy.Spider):
    name = 'itcast1'
    #allowd_domains=["http://www.shehui.pku.edu.cn/"]
     #f=open('D:\python1\mySpider_school\\newSpider\spiders\\test1.txt','r')
    #f=open('D:\python1\mySpider_school\\newSpider\spiders\\test2.txt', 'r')

    start_urls =["https://www.phil.pku.edu.cn/teacher.php ",
"http://econ.pku.edu.cn/quanzhi.php?cid=379",
"http://www.law.pku.edu.cn/sz/zzjs/ab/index.htm",
"http://www.law.pku.edu.cn/sz/zzjs/cd/index.htm",
"http://www.law.pku.edu.cn/sz/zzjs/eg/index.htm",
"http://www.law.pku.edu.cn/sz/zzjs/hl/index.htm",
"http://www.law.pku.edu.cn/sz/zzjs/mr/index.htm",
"http://www.law.pku.edu.cn/sz/zzjs/s/index.htm",
"http://www.law.pku.edu.cn/sz/zzjs/tz/index.htm",
"http://www.sg.pku.edu.cn/list/?17_1.html",
"http://www.sis.pku.edu.cn/cn/Teachers/do",
"http://marxism.pku.edu.cn/infoDataView.do?infoList=infoList&channelId=channel40",
"http://marxism.pku.edu.cn/infoDataView.do?infoList=infoList&channelId=channel41",
"http://marxism.pku.edu.cn/infoDataView.do?infoList=infoList&channelId=channel42",
"http://marxism.pku.edu.cn/infoDataView.do?infoList=infoList&channelId=channel43",
"http://marxism.pku.edu.cn/infoDataView.do?infoList=infoList&channelId=channel44",
"http://marxism.pku.edu.cn/infoDataView.do?infoList=infoList&channelId=channel45",
"http://marxism.pku.edu.cn/infoDataView.do?infoList=infoList&channelId=channel46",
"http://marxism.pku.edu.cn/infoDataView.do?infoList=infoList&channelId=channel47",
"https://www.psy.pku.edu.cn/c/faculty/",
"http://chinese.pku.edu.cn/teachingstaff/ancientliteratureresearchroom/",
"http://chinese.pku.edu.cn/teachingstaff/modernliteratureteachingroom/",
"http://chinese.pku.edu.cn/teachingstaff/contemporaryliteratureroom/",
"http://chinese.pku.edu.cn/teachingstaff/folkliteratureresearchroom/",
"http://chinese.pku.edu.cn/teachingstaff/literarytheoryresearchroom/",
"http://chinese.pku.edu.cn/teachingstaff/classicalliteratureteachingroom/",
"http://chinese.pku.edu.cn/teachingstaff/classicalchineseteachingroom/",
"http://chinese.pku.edu.cn/teachingstaff/modernchineseteachingroom/",
"http://chinese.pku.edu.cn/teachingstaff/languageteachingroom/",
"http://chinese.pku.edu.cn/teachingstaff/comparativeliteratureteacherroom/",
"http://chinese.pku.edu.cn/teachingstaff/linguisticlaboratory/",
"http://www.hist.pku.edu.cn/news/Article/ShowArticle.asp?ArticleID=104",
"http://archaeology.pku.edu.cn/Faculty/a//list.shtml",
"http://www.math.pku.edu.cn/static/quanzhijiaoyuan.html",
"http://www.phy.pku.edu.cn/personnel/faculty.xml",
"http://www.chem.pku.edu.cn/index.php?id=115",
"http://www.ues.pku.edu.cn/more_teacher.php?cid=31&istype=1",
"http://www.bio.pku.edu.cn/teacher.php?cid=146",
"http://web.mech.pku.edu.cn/subpage.asp?id=34",
"http://web.mech.pku.edu.cn/subpage.asp?id=35",
"http://www.coe.pku.edu.cn/faculty-list",
"http://auto.hust.edu.cn/szdw/xysz.htm",
"http://cese.pku.edu.cn/szdw/zzjs/index.htm",
"http://sbms.bjmu.edu.cn/jsdw/bssds/index.htm",
"http://sps.bjmu.edu.cn/szdw/sssds/index.htm",
"http://sps.bjmu.edu.cn/szdw/bssds/index.htm",
"http://nursing.bjmu.edu.cn/szdw/index.htm",
"http://www.art.pku.edu.cn/staff/faculty_directory/a/",
"http://www.gsm.pku.edu.cn/faculty_and_research/szdw/qzjs.htm",
"http://phi.ruc.edu.cn/index.php?s=/Index/news/cid/94.html",
"http://econ.ruc.edu.cn/more_js.php?cid=10769",
"http://www.law.ruc.edu.cn/sz/shizhi.asp",
"http://sis.ruc.edu.cn/html/1/258/index.html",
"http://sis.ruc.edu.cn/html/1/258/index.html",
"http://sis.ruc.edu.cn/html/1/258/index.html",
"http://sis.ruc.edu.cn/html/1/258/index.html",
"http://sis.ruc.edu.cn/html/1/258/index.html",
"http://ssps.ruc.edu.cn/index.php?s=/Index/teacher/cid/8.html",
"http://marx.ruc.edu.cn/tea_more.php?cid=21",
"http://jcr.ruc.edu.cn/yuangong/jiaoshi/",
"http://lishixueyuan.com/index.php?m=content&c=index&a=lists&catid=10",
"http://stat.ruc.edu.cn/teacher.php?cid=25",
"http://www.sard.ruc.edu.cn/faculty/index.jhtml",
"http://spap.ruc.edu.cn/jiaoshi.php?cid=22",
"http://www.irm.cn/teacher.php?cid=8",
"http://www.ase.buaa.edu.cn/san_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1079",
"http://yqgdxy.buaa.edu.cn/xyld.jsp?urltype=tree.TreeTempUrl&wbtreeid=1070",
"http://www.mse.buaa.edu.cn/szdw/jslb/index.htm",
"http://soft.buaa.edu.cn/szzs.htm",
"http://3y.nuc.edu.cn/szdw.htm",
"http://ac.bit.edu.cn/szdw/jsdw/index.htm",
"http://sae.bit.edu.cn/szdw/jsxx/index.htm",
"http://mse.ustb.edu.cn/shiziduiwu/shiziduiwu/",
"http://metall.ustb.edu.cn/jiansuo/2516.html",
"http://ces.ustb.edu.cn/a/shiziduiwu/xisuo/list_20_1.html",
"http://chem.buct.edu.cn/szdw/jsml/index.htm",
"http://sice.bupt.edu.cn/szll/xxlljsjyzx.htm",
"http://sice.bupt.edu.cn/szll/wxtxjyzx.htm",
"http://sice.bupt.edu.cn/szll/dmtjsjyzx.htm ",
"http://sice.bupt.edu.cn/szll/txwjsjyzx.htm ",
"http://sice.bupt.edu.cn/szll/fwwxjyzx.htm ",
"http://sice.bupt.edu.cn/szll/wlssjyzx.htm ",
"http://sice.bupt.edu.cn/szll/kdwljkjyzx.htm ",
"http://scs.bupt.edu.cn/cs_web/teacher/teacher_disp.aspx",
"http://cbs.cau.edu.cn/col/col9227/index.html ",
"http://cbs.cau.edu.cn/col/col9228/index.html",
"http://cbs.cau.edu.cn/col/col9229/index.html",
"http://cbs.cau.edu.cn/col/col9230/index.html",
"http://cbs.cau.edu.cn/col/col9231/index.html",
"http://cbs.cau.edu.cn/col/col9232/index.html",
"http://cbs.cau.edu.cn/col/col9247/index.html",
"http://cbs.cau.edu.cn/col/col9248/index.html",
"http://cbs.cau.edu.cn/col/col9249/index.html",
"http://cbs.cau.edu.cn/col/col9250/index.html",
"http://cbs.cau.edu.cn/col/col9251/index.html",
"http://cbs.cau.edu.cn/col/col9252/index.html",
"http://cbs.cau.edu.cn/col/col9253/index.html",
"http://coe.cau.edu.cn/col/col10747/index.html",
"http://coe.cau.edu.cn/col/col10748/index.html",
"http://spxy.cau.edu.cn/col/col22476/index.html",
"http://spxy.cau.edu.cn/col/col22477/index.html",
"http://nxy.cau.edu.cn/col/col27215/index.html",
"http://zihuan1.cau.edu.cn/col/col1534/index.html",
"http://zihuan1.cau.edu.cn/col/col4411/index.html",
"http://cpp.cau.edu.cn/col/col21988/index.html",
"http://cpp.cau.edu.cn/col/col21989/index.html",
"http://cvm.cau.edu.cn/col/col16968/index.html",
"http://cvm.cau.edu.cn/col/col16969/index.html",
"http://cvm.cau.edu.cn/col/col16970/index.html",
"http://cast1.cau.edu.cn/col/col19127/index.html",
"http://cast1.cau.edu.cn/col/col19148/index.html",
"http://lxy.bjfu.edu.cn/szdw/js/70251.html",
"http://lxy.bjfu.edu.cn/szdw/fjs/70259.html",
"http://fe.bnu.edu.cn/t002-t2-1-23.htm",
"http://psych.bnu.edu.cn/tabid/50/Default.aspx",
"http://wxy.bnu.edu.cn/szdw/gdhyyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/xdhyyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/wyxyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/gdwxyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/yyxyyyyyxyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/xddwxyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/msxyskfzyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/msxywhrlxyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/bjwxysjwxyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/ywjyyjs/index.html",
"http://wxy.bnu.edu.cn/szdw/wxczyjs/index.html",
"http://history.bnu.edu.cn/szdw/index.html",
"http://math.bnu.edu.cn/jzg/bmfl/index.html",
"http://geog.bnu.edu.cn/rydw/zrjs/index.html",
"http://sss.bnu.edu.cn/?team/tp/297.html",
"http://sss.bnu.edu.cn/?team/tp/298.html",
"http://cls.bnu.edu.cn/xuekejianshe/shiziduiwu/",
"http://env.bnu.edu.cn/szdw/js/",
"http://env.bnu.edu.cn/szdw/fjs/",
"http://www.art.bnu.edu.cn/College/index/id/729 ",
"http://www.art.bnu.edu.cn/College/index/id/745",
"http://www.art.bnu.edu.cn/College/index/id/746",
"http://www.art.bnu.edu.cn/College/index/id/747",
"http://www.art.bnu.edu.cn/College/index/id/748",
"http://www.art.bnu.edu.cn/College/index/id/749",
"http://www.art.bnu.edu.cn/College/index/id/750",
"http://math.cnu.edu.cn/szdw/qtjs/index.htm",
"http://sjc.cuc.edu.cn/teachers/",
"http://cctedu.cuc.edu.cn/",
"http://econ.cufe.edu.cn/sztd/jxms.htm",
"http://site.uibe.edu.cn/actionszdw/Index.aspx#",
"http://www.bsu.edu.cn/jyjx/msjs/index.htm",
"http://design.cafa.edu.cn/cn/faculty",
"http://mzx.muc.edu.cn/golist.action?catid=11",
"http://fxy.cupl.edu.cn/szdw/zzjs.htm",
"http://history.nankai.edu.cn/teacherzgsxk.action?zgsxk=1",
"http://sms.nankai.edu.cn/5534/list.htm",
"http://chem.nankai.edu.cn/ejym_wide.aspx?m=1.2&n=-1&t=3",
"http://mse.nankai.edu.cn/Show.asp?labelID=002001",
"http://chemeng.tju.edu.cn/cn/szdw;jsessionid=F8F2338FC041929E3C09D9DA14EC6E1B",
"http://come.tju.edu.cn/jxsz/xssz/gygcx/",
"http://fz.tjpu.edu.cn/1212/list.htm",
"http://zhongyao.tjutcm.edu.cn/szdw/ysfc.htm",
"http://electric.ncepu.edu.cn/szdw/jsdw/dlxtyjs/index.htm",
"http://ccet.tyut.edu.cn/newsList.asp?classID=6",
"http://smkxxy.imu.edu.cn/szdw/jbgc.htm",
"http://econ.lnu.edu.cn/szll/js.htm",
"http://chem.dlut.edu.cn/szdw1/azcpx.htm",
"http://www.ise.neu.edu.cn/jsml.html",
"http://gl.dlmu.edu.cn/html/szll/",
"http://wgyxy.ybu.edu.cn/szdw/yyx/szdw.htm",
"http://marx.nenu.edu.cn/szdw/azcpx.htm",
"http://202.198.133.34/Hsystem/bin/aspdu/list_jslbother.asp?sortindex=",
"http://202.198.133.35/huaxue/bin/aspdu/list_jslbother.asp?sortindex=%B8%DA%CE%BB",
"http://civil.hit.edu.cn/8458/list.htm",
"http://mse.hit.edu.cn/1720/list.htm",
"http://seie.hit.edu.cn/1812/list.htm",
"http://sme.hit.edu.cn/yjsds/list.htm",
"http://sec.hrbeu.edu.cn/238/list.htm",
"http://philosophy.fudan.edu.cn/p6981c6722/list.htm",
"http://history.fudan.edu.cn/7816/list.htm",
"http://www.chemistry.fudan.edu.cn/data/list/xsdtr",
"http://phys.fudan.edu.cn/7479/list.htm",
"http://math.fudan.edu.cn/MemberbySort.aspx?info_lb=565&flag=548",
"http://life.fudan.edu.cn/data/list/zc",
"http://medicine.fudan.edu.cn/TeacherList.aspx?info_lb=30&flag=2",
"http://mse.fudan.edu.cn/Data/List/szdw",
"http://environment.fudan.edu.cn/content.aspx?info_lb=98&flag=98",
"http://spfdu.fudan.edu.cn/Attr_Tutor_list.aspx?BID=3&SID=23",
"http://aa.fudan.edu.cn/Teacher.aspx?info_lb=606&flag=526",
"http://www.sirpa.fudan.edu.cn/?cat=5",
"http://structure.tongji.edu.cn/modules/teachers/allteachers.php?classid=261&col=4",
"http://geotec.tongji.edu.cn/ncontent.aspx?info_lb=98&flag=98",
"http://risedr.tongji.edu.cn/content.aspx?info_lb=162&flag=3",
"http://celiang.tongji.edu.cn/index.php?classid=5786",
"http://sese.tongji.edu.cn/3135/list.htm",
"http://landscape-caup.tongji.edu.cn/staff",
"http://archi-caup.tongji.edu.cn/Data/List/qzjs",
"http://tjdi.tongji.edu.cn/TeacherLogo.do?lang=",
"http://math.sjtu.edu.cn/faculty/",
"http://scce.sjtu.edu.cn/jiaoshi.php?c=3",
"http://life.sjtu.edu.cn/index.php?option=com_content&view=article&id=136&Itemid=184",
"http://life.sjtu.edu.cn/index.php?option=com_content&view=article&id=193&Itemid=184",
"http://life.sjtu.edu.cn/index.php?option=com_content&view=article&id=1430:2015-04-15-02-00-27&catid=46:2011-05-03-19-39-37&Itemid=184",
"http://life.sjtu.edu.cn/index.php?option=com_content&view=article&id=1429:2015-04-15-01-52-35&catid=46:2011-05-03-19-39-37&Itemid=184",
"http://life.sjtu.edu.cn/index.php?option=com_content&view=article&id=195&Itemid=184",
"http://life.sjtu.edu.cn/index.php?option=com_content&view=article&id=194&Itemid=184",
"http://me.sjtu.edu.cn/teacher_directory1.html",
"http://smse.sjtu.edu.cn/jiaogongminglu.asp",
"http://www.cs.sjtu.edu.cn/Faculty.aspx",
"http://naoce.sjtu.edu.cn/jsml.html",
"http://pharm.sjtu.edu.cn/home/teacher/index.html",
"http://www.acem.sjtu.edu.cn/faculty/index.html",
"http://hgxy.ecust.edu.cn/1180/list.htm",
"http://clxy.ecust.edu.cn/4640/list.htm",
"http://texcol.dhu.edu.cn/6535/list.htm",
"http://smxy.shou.edu.cn/2054/list.htm",
"http://smxy.shou.edu.cn/2056/list.htm",
"http://smxy.shou.edu.cn/2060/list.htm",
"http://smxy.shou.edu.cn/2062/list.htm",
"http://www.ed.ecnu.edu.cn/?teachercategory=onthejob",
"http://www.sees.ecnu.edu.cn/index.php?classid=7314 ",
"http://www.sees.ecnu.edu.cn/index.php?classid=7315",
"http://www.sees.ecnu.edu.cn/index.php?classid=7316",
"http://faculty.ecnu.edu.cn/search/teacherList.faces?siteId=10&pageId=0&nodeId=3555",
"http://ssm.shufe.edu.cn/Home/Index/tlist/id/25",
"http://www.shcmusic.edu.cn/list_22.aspx?cid=53&ppid=23&navindex=0",
"https://philo.nju.edu.cn/4712/list.htm",
"http://chin.nju.edu.cn/szdw5-1.html",
"https://physics.nju.edu.cn/ry/gk.htm",
"http://astronomy.nju.edu.cn/a/szdw/jsmc/",
"http://astronomy.nju.edu.cn/a/szdw/jsmc/#kongjian",
"http://chem.nju.edu.cn/staff/szlla.asp",
"http://as.nju.edu.cn/TeacherList.aspx",
"https://es.nju.edu.cn/zzry/list.htm",
"http://life.nju.edu.cn/?topi=1&fun=%bd%cc%ca%a6%c3%fb%c2%bc",
"https://eng.nju.edu.cn/5183/list.htm",
"https://eng.nju.edu.cn/5184/list.htm",
"http://im.nju.edu.cn/teachers.do?type=1&mid=4&mmid=41",
"http://im.nju.edu.cn/teachers.do?type=4&mid=4&mmid=5dcefb89-45a3-11e5-91a4-002454d0cc1b",
"http://im.nju.edu.cn/teachers.do?type=2&mid=4&mmid=7ddbacf0-2a46-11e5-8e21-002454d0cc1b",
"https://chemistry.suda.edu.cn/2119/list.htm",
"http://smse.seu.edu.cn/szry/list.htm",
"http://electronic.seu.edu.cn/11463/list.htm",
"http://electronic.seu.edu.cn/11465/list.htm",
"http://electronic.seu.edu.cn/11466/list.htm",
"http://electronic.seu.edu.cn/11467/list.htm",
"http://electronic.seu.edu.cn/11468/list.htm",
"http://electronic.seu.edu.cn/11469/list.htm",
"http://automation.seu.edu.cn/Depts.aspx?id=142",
"http://arch.seu.edu.cn/home/faculty.php?did=57&id=119",
"http://arch.seu.edu.cn/home/faculty.php?did=57&id=120",
"http://arch.seu.edu.cn/home/faculty.php?did=57&id=121",
"http://arch.seu.edu.cn/home/faculty.php?did=57&id=124",
"http://arch.seu.edu.cn/home/faculty.php?did=57&id=123",
"http://arch.seu.edu.cn/home/faculty.php?did=57&id=122",
"http://arch.seu.edu.cn/home/faculty.php?did=57&id=125",
"http://arch.seu.edu.cn/home/faculty.php?did=57&id=126",
"http://civil.seu.edu.cn/1089/list.htm",
"http://tc.seu.edu.cn/859/list.htm",
"http://bme.seu.edu.cn/499/list.htm",
"http://arts.seu.edu.cn/17122/list.htm",
"http://cepe.nuaa.edu.cn/index.php/Index/shiziindex/caid/129",
"http://web.ouc.edu.cn/hydq/szdw/list.htm",
"http://web.ouc.edu.cn/shuichan/5830/list.htm",
"http://pe.upc.edu.cn/s/79/t/182/07/fb/info67579.htm",
"http://geori.upc.edu.cn/s/57/t/394/p/1/c/5971/d/6442/list.htm",
"http://geori.upc.edu.cn/s/57/t/394/p/1/c/5971/d/6443/list.htm",
"http://www5.zzu.edu.cn/clgc/info/1022/1581.htm",
"http://www5.zzu.edu.cn/hxxy/szdw1.htm",
"http://bio.henu.edu.cn/szdw/js.htm",
"http://bio.henu.edu.cn/szdw/fjs.htm",
"http://ems.whu.edu.cn/szdw/qzjs/",
"http://fxy.whu.edu.cn/archive/category/10047",
"http://www.marx.whu.edu.cn/szll/",
"http://www.chem.whu.edu.cn/szdw.htm",
"http://sres.whu.edu.cn/szdw.asp",
"http://www.bio.whu.edu.cn/index.php/List/84.html",
"http://users.sgg.whu.edu.cn/",
"http://wsm70.whu.edu.cn/szdw/szdw.htm",
"http://sim.whu.edu.cn/sz/jsxq/",
"http://mse.hust.edu.cn/index.php/index/show/tid/20.html",
"http://oei.hust.edu.cn/szdw.htm",
"http://mat.hust.edu.cn/szll.htm",
"http://energy.hust.edu.cn/szdw/jsml.htm",
"http://seee.hust.edu.cn/szdw/qyjs.htm",
"http://cs.hust.edu.cn/szdw/szll.htm",
"http://jcyxy.tjmu.edu.cn/dsjj1.htm ",
"http://gwxy.tjmu.edu.cn/szdw/yxjs.htm",
"http://zyxy.cug.edu.cn/szdw/jszy/zykxygcx.htm",
"http://zyxy.cug.edu.cn/szdw/jszy/sydzx/jslb.htm",
"http://zyxy.cug.edu.cn/szdw/jszy/sygcx/jslb.htm",
"http://zyxy.cug.edu.cn/szdw/jszy/mjmcqgcx/jslb.htm",
"http://sescug.com/index.php?m=content&c=index&a=lists&catid=39",
"http://dxy.cug.edu.cn/info/1034/1295.htm ",
"http://smse.whut.edu.cn/yjspy/xsdw/ ",
"http://politics.ccnu.edu.cn/szll.htm",
"http://chinese.ccnu.edu.cn/szdw/zzls.htm",
"http://lst.hzau.edu.cn/sz/jsyg/",
"http://chfs.hzau.edu.cn/szdw/zzjs/",
"http://cpst.hzau.edu.cn/szdw/jsml/",
"http://emc.hzau.edu.cn/szdw/nyjjgl/",
"http://emc.hzau.edu.cn/szdw/scyx/",
"http://emc.hzau.edu.cn/szdw/qygl/",
"http://emc.hzau.edu.cn/szdw/kj/",
"http://emc.hzau.edu.cn/szdw/jjx/",
"http://my.hzau.edu.cn/szdw/",
"http://law.zuel.edu.cn/4086/list.htm",
"http://law.zuel.edu.cn/4087/list.htm",
"http://law.zuel.edu.cn/4088/list.htm",
"http://law.zuel.edu.cn/4089/list.htm",
"http://law.zuel.edu.cn/4090/list.htm",
"http://law.zuel.edu.cn/4091/list.htm",
"http://law.zuel.edu.cn/4092/list.htm",
"http://mse.csu.edu.cn/Content.aspx?moduleid=11cdfc02-3ae2-4cf7-bd24-67f0d4388499",
"http://smse.csu.edu.cn/Seconpage.aspx?strId=1ff7cf25-3c4a-426d-ba6f-aeb7d334fcfc",
"http://mpb.csu.edu.cn/mpb//pages/shi_list.jsp?parent_key=/team&fkey=/team/jzcx",
"http://math.csu.edu.cn/jsxx.jsp?urltype=tree.TreeTempUrl&wbtreeid=1005",
"http://cc.hnu.cn/index.php?option=com_content&task=category&sectionid=20&id=62&Itemid=228",
"http://cc.hnu.cn/index.php?option=com_content&task=category&sectionid=20&id=61&Itemid=229",
"http://fsc.hunnu.edu.cn/cmspack/index.php?controller=list&action=show&id=97&selectnav=2",
"http://fsc.hunnu.edu.cn/cmspack/index.php?controller=list&action=show&id=98&selectnav=2",
"http://cet.sysu.edu.cn/Teachers/Index.html",
"http://mse.sysu.edu.cn/teacher/teacher02/normal",
"http://gp.sysu.edu.cn/Teacher/Index.html",
"http://seit.sysu.edu.cn/teacher/teacher01",
"http://zssom.sysu.edu.cn/Info2ab7.html?level=1&typeid=0f296673-c1b3-4292-8e07-5925c1f9061d",
"http://sps.sysu.edu.cn/Faculty/Index.html",
"http://philosophy.sysu.edu.cn/sz/sz01/index.htm",
"http://phil-zh.sysu.edu.cn/Teachers/Index.html",
"http://math.sysu.edu.cn/Web/Teacher/TeacherAllList/21/42.html",
"http://cbe.xmu.edu.cn/11811/list.htm",
"http://cbe.xmu.edu.cn/11812/list.htm",
"http://cbe.xmu.edu.cn/11813/list.htm",
"http://cbe.xmu.edu.cn/11814/list.htm",
"http://cbe.xmu.edu.cn/11815/list.htm",
"http://cbe.xmu.edu.cn/11816/list.htm",
"http://chembio.xmu.edu.cn/teachers.asp",
"http://sklcsb.xmu.edu.cn/5350/list.htm",
"http://wel.xmu.edu.cn/ch/research/mid/5/catid/47",
"http://tdnp.xmu.edu.cn/4529/list.htm ",
"http://mbigc.xmu.edu.cn/ContentShow.aspx?Id=P2 ",
"http://ime.xmu.edu.cn/people.asp?id=2",
"http://dgo.xmu.edu.cn/people/chairman.html",
"http://mel.xmu.edu.cn/people_research.asp?id=12",
"http://coe.xmu.edu.cn/TeacherList.aspx?Id=T1",
"http://coe.xmu.edu.cn/TeacherList.aspx?Id=T2",
"http://coe.xmu.edu.cn/TeacherList.aspx?Id=T3",
"http://uac.xmu.edu.cn/index.php?m=content&c=index&a=show&catid=9&id=6",
"http://stats.xmu.edu.cn/teachers?Subject=Name",
"http://www.soe.xmu.edu.cn/faculty/faculty/#119 ",
"http://czx.xmu.edu.cn/user/jsfc.asp ",
"http://finance.xmu.edu.cn/teachers ",
"http://gjjmx.xmu.edu.cn/gjjmx/Teacher/ShowClass.asp?ClassID=13 ",
"http://safe.cumt.edu.cn/2834/list.htm",
"http://cese.cumt.edu.cn/jsdw/list.htm",
"http://eoe.njupt.edu.cn/9507/list.htm",
"http://sdxy.hhu.edu.cn/s/68/t/2863/p/1/c/2196/d/2198/list.htm",
"http://sdxy.hhu.edu.cn/s/68/t/2863/p/1/c/2196/d/2199/list.htm",
"http://sdxy.hhu.edu.cn/s/68/t/2863/p/1/c/2196/d/2200/list.htm",
"http://hjxy.hhu.edu.cn/s/35/t/2824/p/1/c/17077/d/17092/list.htm",
"http://biotech.jiangnan.edu.cn/szdw1/zg.htm",
"http://biotech.jiangnan.edu.cn/szdw1/fg.htm",
"http://foodsci.jiangnan.edu.cn/szdw/js.htm",
"http://foodsci.jiangnan.edu.cn/szdw/fjs.htm",
"http://linxue.njfu.edu.cn/info.php?cid=117",
"http://cas.nuist.edu.cn/TeacherList.aspx",
"http://yxy.njucm.edu.cn/s/43/t/24/p/1/c/402/d/680/list.htm",
"http://yxy.njucm.edu.cn/s/43/t/24/p/1/c/402/d/1120/list.htm",
"http://zyxy.cpu.edu.cn/752/list.htm",
"http://zyxy.cpu.edu.cn/753/list.htm",
"http://www.chem.zju.edu.cn/chinese/redir.php?catalog_id=471",
"http://www.cls.zju.edu.cn/cn/redir.php?catalog_id=125735",
"http://www.cers.zju.edu.cn/chinese/redir.php?catalog_id=18202",
"http://me.zju.edu.cn/mecn/6336/list.htm",
"http://opt.zju.edu.cn/redir.php?catalog_id=156603",
"http://mse.zju.edu.cn/chinese/redir.php?catalog_id=8994",
"http://mse.zju.edu.cn/chinese/redir.php?catalog_id=8995",
"http://ee.zju.edu.cn/chinese/redir.php?catalog_id=169606",
"http://www.cse.zju.edu.cn/chinese/redir.php?catalog_id=38181",
"http://www.cse.zju.edu.cn/chinese/redir.php?catalog_id=38182",
"http://www.cs.zju.edu.cn/chinese/redir.php?cust=jiaoshiml&id=256",
"http://www.caefs.zju.edu.cn/chinese/redir.php?catalog_id=1311",
"http://www.caefs.zju.edu.cn/chinese/redir.php?catalog_id=1312",
"http://www.cab.zju.edu.cn/chinese/11161/list.htm",
"http://bms.zju.edu.cn/redir.php?catalog_id=13489",
"http://www.cps.zju.edu.cn/index.php?c=index&a=jzyg&web=chinese",
"http://www.som.zju.edu.cn/jiaoshouyuyanjiu/jiaoshisousuo/",
"http://math.ustc.edu.cn/new/teachers.php",
"http://phys.ustc.edu.cn/?lan=&a=szdw",
"http://chem.ustc.edu.cn/szdw_16/jszb/201211/t20121106_143706.html",
"http://astro.ustc.edu.cn/staff/",
"http://ess.ustc.edu.cn/faculty",
"http://biox.ustc.edu.cn/684/list.htm",
"http://mse.ustc.edu.cn/2014/1020/c3334a30142/page.htm",
"http://www.snst.ustc.edu.cn/3958/list.htm",
"http://cs.ustc.edu.cn/szdw/ys/201006/t20100614_21994.html",
"http://safetyse.ustc.edu.cn/2010/0701/c4551a41554/page.htm",
"http://som.hfut.edu.cn/glxy/szdw/index.htm",
"http://chem.fzu.edu.cn/html/szdw/jsml/1.html",
"https://yx.jnu.edu.cn/teachers/list_41.aspx",
"https://yx.jnu.edu.cn/teachers/list_43.aspx",
"https://yx.jnu.edu.cn/teachers/list_45.aspx",
"https://yx.jnu.edu.cn/teachers/list_47.aspx",
"http://www.scut.edu.cn/ce/",
"http://www2.scut.edu.cn/material/2647/list.htm",
"http://www2.scut.edu.cn/material/2648/list.htm",
"http://www2.scut.edu.cn/material/2651/list.htm",
"http://www2.scut.edu.cn/material/2655/list.htm",
"http://www.scut.edu.cn/page/dept/bio/teacher.htm",
"http://cctm.gzucm.edu.cn/szdw/bssds.htm",
"http://cctm.gzucm.edu.cn/szdw/sssds.htm",
"http://www.hainu.edu.cn/STM/nonglin/SHTML_liebiao.asp@bbsid=6474.shtml",
"http://www.hainu.edu.cn/stm/nonglin/shtml_liebiao.asp@bbsid=6477.shtml",
"http://www.hainu.edu.cn/stm/nonglin/shtml_liebiao.asp@bbsid=6478.shtml",
"http://tmjz.gxu.edu.cn/szdw/jsdw.htm",
"http://math.scu.edu.cn/index.php?app=default&act=get_detail&cate_id=268",
"http://chem.scu.edu.cn/JSJJ",
"http://mse.scu.edu.cn/list1_50.aspx",
"http://mse.scu.edu.cn/list1_49.aspx",
"http://mse.scu.edu.cn/list1_51.aspx",
"http://jcfy.scu.edu.cn/News.aspx?NewsId=173",
"http://www.cme.cqu.edu.cn/szdw/jxjcx.htm",
"http://www.cme.cqu.edu.cn/szdw/jxsjzzx.htm",
"http://www.cme.cqu.edu.cn/szdw/jxdzgcx.htm",
"http://www.cme.cqu.edu.cn/szdw/gygcx.htm",
"http://www.cee.cqu.edu.cn/jsyd/jszy.htm",
"http://civil.cqu.edu.cn/2.jsp?urltype=tree.TreeTempUrl&wbtreeid=1004",
"http://ctt.swjtu.edu.cn/zh/teachers.jsp?m=19",
"http://www.ee.uestc.edu.cn/index/15/75/164",
"http://www.scie.uestc.edu.cn/main/teacher?page=1",
"http://www.scie.uestc.edu.cn/main/teacher?page=2",
"http://www.scie.uestc.edu.cn/main/teacher?page=3",
"http://www.scie.uestc.edu.cn/main/teacher?page=4",
"http://www.scie.uestc.edu.cn/main/teacher?page=5",
"http://www.scie.uestc.edu.cn/main/teacher?page=6",
"http://www.scie.uestc.edu.cn/main/teacher?page=7",
"http://www.scie.uestc.edu.cn/main/teacher?page=8",
"http://www.scie.uestc.edu.cn/main/teacher?page=9",
"http://www.scie.uestc.edu.cn/main/teacher?page=10",
"http://www.scie.uestc.edu.cn/main/teacher?page=11",
"http://www.scie.uestc.edu.cn/main/teacher?page=12",
"http://www.scie.uestc.edu.cn/main/teacher?page=13",
"http://www.scie.uestc.edu.cn/main/teacher?page=14",
"http://www.scie.uestc.edu.cn/main/teacher?page=15",
"http://www.scie.uestc.edu.cn/main/teacher?page=16",
"http://www.scie.uestc.edu.cn/main/teacher?page=17",
"http://www.scie.uestc.edu.cn/main/teacher?page=18",
"http://www.scie.uestc.edu.cn/main/teacher?page=19",
"http://www.scie.uestc.edu.cn/main/teacher?page=20",
"http://www.scie.uestc.edu.cn/main/teacher?page=21",
"http://www.scie.uestc.edu.cn/main/teacher?page=22",
"http://www.scie.uestc.edu.cn/main/teacher?page=23",
"http://www.scie.uestc.edu.cn/main/teacher?page=24",
"http://www.scie.uestc.edu.cn/main/teacher?page=25",
"http://www.scie.uestc.edu.cn/main/teacher?page=26",
"http://www.scie.uestc.edu.cn/main/teacher?page=27",
"http://www.scie.uestc.edu.cn/main/teacher?page=28",
"http://sgy.swpu.edu.cn/szdw/jsml/jsml1.htm",
"http://sgy.swpu.edu.cn/szdw/jsml/jsml3.htm",
"http://sgy.swpu.edu.cn/szdw/jsml/jsml5.htm",
"http://sgy.swpu.edu.cn/szdw/jsml/jsml7.htm",
"http://sgy.swpu.edu.cn/szdw/jsml/jsml2.htm",
"http://econ.swufe.edu.cn/html/szdw/zrjs/",
"http://geology.nwu.edu.cn/Article/lists/category/rcry.html",
"http://epe.xjtu.edu.cn/teachers.php?cat_id=60",
"http://mec.xjtu.edu.cn/index.php?m=content&c=index&a=lists&catid=159",
"http://mse.xjtu.edu.cn/",
"http://ee.xjtu.edu.cn/jzyg/jsxx/zmdh.htm",
"http://eie.xjtu.edu.cn/jglb.jsp?urltype=tree.TreeTempUrl&wbtreeid=1023",
"http://sppa.xjtu.edu.cn/szdw/jsxx.htm",
"http://jidian.nwpu.edu.cn/szdw.htm",
"http://cailiao.nwpu.edu.cn/2017/lingdao4.jsp?urltype=tree.TreeTempUrl&wbtreeid=1683",
"http://ste.xidian.edu.cn/html/yanjiushengpeiyang/tongyuandaoshi/http://cs.xidian.edu.cn/html/teacher/faculty/",
"http://nxy.nwsuaf.edu.cn/szdw/zjrc/index.htm",
"http://nxy.nwsuaf.edu.cn/szdw/jsyjy/index.htm",
"http://nxy.nwsuaf.edu.cn/szdw/fjsfyjy/index.htm",
"http://nxy.nwsuaf.edu.cn/szdw/zjzc/index.htm",
"http://www.lit.snnu.edu.cn/index.php?m=content&c=index&a=lists&catid=21",
"http://chem.lzu.edu.cn/lzupage/B20161110111849.html",
"http://chem.lzu.edu.cn/lzupage/B20161110113058.html",
"http://chem.lzu.edu.cn/lzupage/B20161110113115.html",
"http://chem.lzu.edu.cn/lzupage/B20161110113136.html",
"http://chem.lzu.edu.cn/lzupage/B20161110113159.html",
"http://chem.lzu.edu.cn/lzupage/B20161110113216.html",
"http://chem.lzu.edu.cn/lzupage/B20161110113232.html",
"http://chem.lzu.edu.cn/lzupage/B20161110113253.html",
"http://chem.lzu.edu.cn/lzupage/B20161230092452.html",
"http://atmos.lzu.edu.cn/lzupage/B20101203093722.html",
"http://lifesc.lzu.edu.cn/category-9.html",
"http://caoye.lzu.edu.cn/lzupage/B20091123102856.html",
"http://stxy.qhu.edu.cn/szdw/jgml/index.htm",
"http://chem.nxu.edu.cn/szdw/jsdw.htm",
"http://hgxy.xju.edu.cn/info/1178/2082.htm",
"http://hgxy.shzu.edu.cn/3338/list.htm",
"http://hgxy.shzu.edu.cn/3339/list.htm",
"http://zyxy.cumtb.edu.cn/szdw/szgk/index.html",
"http://www.cup.edu.cn/oil/jsdw/yqjgcx/index.htm",
"http://www.cup.edu.cn/oil/jsdw/yqtkfgcx/index.htm",
"http://www.cup.edu.cn/oil/jsdw/hyyqgcx/index.htm",
"http://www.cup.edu.cn/oil/jsdw/gclxx/index.htm",
"http://www.cup.edu.cn/oil/jsdw/yqgchwyjs/index.htm",
"http://www.cup.edu.cn/geosci/szdw/jiaoshou/index.htm",
"http://www.cup.edu.cn/geosci/szdw/fujiaoshou/index.htm",
"http://www.cup.edu.cn/geosci/szdw/jiangshi/index.htm",
"http://www.sesr.cugb.edu.cn/sysjs/zxjj/szdw/ysfc/",
"http://www.cugb.edu.cn/schoolTeacher.action?deptCode=30100&level=1",
"http://eng.nbu.edu.cn/szdw1/jgxx/zgjzc.htm",
"http://eng.nbu.edu.cn/szdw1/jgxx/fgjzc.htm",
"http://eng.nbu.edu.cn/szdw1/jgxx/zjzc.htm",
"http://eng.nbu.edu.cn/szdw1/jgxx/xzry.htm",
"http://www.ic.cas.cn/yjdw/ys/",
"http://www.ic.cas.cn/yjdw/brjh/",
"http://www.ic.cas.cn/yjdw/jcqn/",
"http://www.ic.cas.cn/yjdw/zgjgwry/",
"http://mse.xhu.edu.cn/812/list.htm",
"http://mse.xhu.edu.cn/815/list.htm",
"http://mse.xhu.edu.cn/816/list.htm",
"http://mse.xhu.edu.cn/817/list.htm",
"http://mse.xhu.edu.cn/818/list.htm"]#f.readline()#f.read()#["http://www.law.pku.edu.cn/sz/zzjs/ab/index.htm","https://www.phil.pku.edu.cn/teacher.php"]
    teacherItem= []

    def parse(self, response):
        # tt = response.xpath("//body [@id='top']")
        node_list = response.xpath('//body//a')

        for node in node_list:
            name = node.xpath(".//text()").extract_first("")

            t=name.encode("utf8")
            f=open('D:\python1\mySpider_school\\newSpider\spiders\\test1.txt','r')
            #print f
            Dictionary=f.read()#
            f.close()
            #print Dictionary#.encode("utf8")
            # "师资力量离退休人员教研室研究机构系行政系党委系学术委员会系学位委员会科研学术系图书馆北京大学哲学系 宗教学系Department of Philosophy, and of Religious Studies, Peking University网站地图机构人员师资力量离退休人员教研室研究机构系行政系党委系学术委员会系学位委员会机构人员师资力量学院概况新闻中心师资招生教学科研学生事务合作交流高端培训图书馆校友中心发展建设组织机构北京大学 校图书馆 管理登录 系信箱登录 English友情链接： 北京大学 | 北大招生网 | 中外法学 | 香港大学法学院 | 北京大学诊所式法律实验教学中心 | 北大法律信息网 | 百年院庆首页 | English | 学院邮箱 | 本站地图 | 内部管理 | 联系我们 | 旧版主页首页在职教师 在职教师在职教师退休教师行政教辅客座教授访问教授兼职教授讲席教授兼职导师博士后永远怀念学院概况新闻中心师资招生教学科研学生事务合作交流高端培训图书馆校友中心发展建设组织机构主页 历史概况 新闻报道 机构人员 科研学术 招生信息 教学工作 系图书馆 学术期刊 继续教育 学生工作"
            #print  type(Dictionary)
            post_url=[]
            if  not t in Dictionary:
                #print t
                post_url .append( node.xpath("./@href").extract()[0])
                info_1 = ""
                info_1 += "".join(post_url)
                a=response.url
                b=info_1.encode("utf-8")
                #c=a+b
                c=b.strip()
                d=urlparse.urljoin(response.url, c)
               # print d,"66666666666666666666666666666666666666666666666666"
                #print c
                #if a[:4]==b[:4]:

                yield Request(url=d, meta={"name": name}, callback=self.parse_detail)
                #else:
                    #yield Request(url=d, meta={"name": name}, callback=self.parse_detail)
                    #yield Request(url=response.url+'/'+post_url, meta={"name": name}, callback=self.parse_detail)
    #
    def parse_detail(self, response):
        name = response.meta.get("name")
        name.strip()
        #print name,
        info_list = response.xpath('//body//text()').extract()
        info = ""
        info += "".join(info_list)
        person_part_1=info.encode("utf-8")

        #print name
        #print person_part_1



        #print person_part_1
        # #
        # #img_list = response.xpath('//body//img/@src').extract()
        url_list_1 = response.xpath('//body//a')
        #
        pic_path = []
        pic_url_list = response.xpath('//body//img/@src').extract()
        pic_url=[]
        for url in pic_url_list:
            print url, '444444444444444444444444444'
            print response.url, '33333333333333333333333333333'
            pic_url.append(urlparse.urljoin(response.url, url))
        #     print pic_url, '555555555555555555555555555555555555555555555555555555555'
        #     try:
        #         req = requests.get(pic_url)
        #         pic_md5 = hashlib.md5(pic_url.encode('utf-8')).hexdigest()
        #         pic_path.append(pic_md5)
        #         fq = open("E:/img//%s.jpg" % (pic_md5), 'wb')
        #         fq.write(req.content)
        #         fq.close()
        #     except requests.exceptions.ConnectionError:
        #         print('cannot reach the website-------------')
        # print name
        # for nod_1 in url_list_1:
        #     url_list_2=nod_1.xpath('./@href').extract()
        #     name_1 = nod_1.xpath(".//text()").extract_first("")
        #     t = name_1.encode("utf8")
        #
        #
        #     info_2 = ""
        #     info_2 += "".join(url_list_2)
        #     print t
            #print person_part_1

        # #
        #     Dictionary = "主页 历史概况 新闻报道 机构人员 科研学术 招生信息 教学工作 系图书馆 学术期刊 继续教育 学生工作北京大学哲学系 宗教学系Department of Philosophy, and of Religious Studies, Peking University网站地图机构人员师资力量离退休人员教研室研究机构系行政系党委系学术委员会系学位委员会机构人员师资力量学院概况新闻中心师资招生教学科研学生事务合作交流高端培训图书馆校友中心发展建设组织机构北京大学 校图书馆 管理登录 系信箱登录 English友情链接： 北京大学 | 北大招生网 | 中外法学 | 香港大学法学院 | 北京大学诊所式法律实验教学中心 | 北大法律信息网 | 百年院庆首页 | English | 学院邮箱 | 本站地图 | 内部管理 | 联系我们 | 旧版主页首页在职教师 在职教师在职教师退休教师行政教辅客座教授访问教授兼职教授讲席教授兼职导师博士后永远怀念学院概况新闻中心师资招生教学科研学生事务合作交流高端培训图书馆校友中心发展建设组织机构"
        #
        # #     ap=0
        #     if not t in Dictionary:
        #         #ap=ap+1
        #
        #         #print t,'after'
        #
        #         a = response.url
        #         b = info_2.encode("utf-8")
        #         url_2 = a + b
        #         d = urlparse.urljoin(response.url, b)
        #         name = response.meta.get("name")
        #         name.strip()
        #         print name
        #         print
        #         if not ".jpg" in d:
        #             print d,"2222222222222"


                #if a[:4] == b[:4]:
                    #if not '@'in b:
                    # yield Request(url=d, meta={"name": name,"name_1":name_1,"person_part_1":person_part_1,"pic_url":pic_url_list}, callback=self.parse_detail_1)
                #else:
                    #if not '@' in url_2:
                        #yield Request(url=d, meta={"name": name, "person_part_1": person_part_1,"pic_url":pic_path},callback=self.parse_detail_1)
            # if ap==0:
        teacherItem = []
        item = InfoPipeline()
        item["name"] = name
        item["pic_url"] ="1"
        item["person_part_1"] = person_part_1
        item["person_part_2"] = pic_url
        teacherItem.append(item)
        return teacherItem


    # def parse_detail_1(self,response1):
    #     info_list = response1.xpath('//body//text()').extract()
    #     info = ""
    #     info += "".join(info_list)
    #     name = response1.meta.get("name", "")
    #     name_1 = response1.meta.get("name_1", "")
    #     person_part_1=response1.meta.get("person_part_1")
    #     person_part_2 = info.encode("utf-8")
    #     print name_1
    #     print name,",,,,,,,"
        #print person_part_1
        #print person_part_2
        # teacherItem = []
        #
        # name = response.meta.get("name", "")
        # pic_path = response.meta.get("pic_url", "")

        #
        # item = InfoPipeline()
        # item["name"] = name
        # item["pic_url"] = pic_path
        # item["person_part_1"] = person_part_1
        # item["person_part_2"] = person_part_2
        # teacherItem.append(item)
        # return teacherItem

