import requests
from bs4 import BeautifulSoup

# List of URLs to check
urls = [
# page, rank
"https://www.auto.co.il/", # 500000
"https://meinungsplatz.de/", # 500000
"https://mingle.respondi.fr/", # 500000
"https://ebank.esunbank.com.tw/", # 500000
"https://www.yazuya.com/", # 500000
"https://www.maximiles.com/", # 500000
"https://www.maximiles.es/", # 500000
"https://wanggapc.com/", # 500000
"https://www.omypc.co.kr/", # 500000
"https://mingle.respondi.de/", # 500000
"https://www.mfac.or.kr/", # 1000000
"https://www.clubnuoveidee.it/", # 1000000
"https://www.co.becker.mn.us/", # 1000000
"https://www.maximiles.it/", # 1000000
"https://www.cut-hikari.com/", # 1000000
"https://mingle.respondi.it/", # 1000000
"https://www.ergonautas.upv.es/", # 1000000
"https://www.m3panel.dk/", # 1000000
"https://www.maximiles.gr/", # 1000000
"https://www.m3panel.fi/", # 1000000
"https://mingle.respondi.co.uk/", # 1000000
"https://www.maximiles.co.uk/", # 1000000
"https://www.luhacovice-lazne.com/", # 5000000
"https://www.tuemarkt.de/", # 5000000
"https://www.maximiles.nl/", # 5000000
"https://chamstudyland.com/", # 5000000
"https://www.koicd.kr/", # 5000000
"https://meinungsplatz.at/", # 5000000
"https://www.hlholdings.co.kr/", # 5000000
"https://sphere.gamexp.com/", # 5000000
"https://www.gomaths.ch/", # 5000000
"https://biztonsagabc.hu/", # 5000000
"https://www.constantine-hier-aujourdhui.fr/", # 5000000
"https://www.zipperenzo.nl/", # 5000000
"https://blessauto.kr/", # 5000000
"https://www.kupele-sklene-teplice.com/", # 5000000
"https://www.kupele-brusno.com/", # 5000000
"https://simef.minagri.gob.cl/", # 5000000
"https://old.municion.org/", # 5000000
"https://www.trencianske.sk/", # 5000000
"http://www.wolfcreekamphitheater.com/", # 5000000
"https://www.kingsing.com/", # 5000000
"https://www.maximiles.ie/", # 5000000
"https://www.rajecke.com/", # 5000000
"https://www.smartaccounts.eu/", # 5000000
"https://www.kupele-dudince.com/", # 5000000
"https://meinungsplatz.ch/", # 5000000
"https://www.m3panel.se/", # 5000000
"http://dkore.net/", # 5000000
"https://www.mcmcaribbeanrealty.com/", # 5000000
"https://www.turcianske.sk/", # 5000000
"https://www.sunflowers.sk/", # 5000000
"https://standardprice.kr/", # 5000000
"https://www.laflyer.in/", # 5000000
"https://www.kupele-na-slovensku.sk/", # 5000000
"http://www.djarena.ru/", # 5000000
"http://sisatotalnews.com/", # 5000000
"https://mingle.respondi.ch/", # 5000000
"https://mingle.respondi.at/", # 5000000
"https://www.sunflowers-agency.cz/", # 5000000
"http://www.beppuni.com/", # 5000000
"https://roomrentalsingapore.com.sg/", # 5000000
"https://www.m3panel.no/", # 5000000
"http://pgtour.co.kr/", # 5000000
"https://www.adnet-group.com/", # 5000000
"https://www.kupele-vysne-ruzbachy.com/", # 5000000
"https://www.zohar-israel.com/", # 5000000
"https://cointradestop.com/", # 5000000
"http://ff14.ffo.jp/", # 5000000
"https://nrpclassaction.com/", # 5000000
"https://vac.sjas.gov.si/", # 5000000
"https://www.cookingmama.com/", # 5000000
"https://www.bardejovske.sk/", # 5000000
"https://www.vizdiszkont.hu/", # 5000000
"http://www.jortek.com.br/", # 10000000
"https://www.webusable.com/", # 10000000
"https://www.ilfocolarecaminetti.it/", # 10000000
"http://shipscafe.net/", # 10000000
"https://www.stoffeerdersunie.nl/", # 10000000
"https://pro230407.prosell.kr/", # 10000000
"https://gomaths.ch/", # 10000000
"https://frenchbook.net/", # 10000000
"https://www.sangpae119.com/", # 10000000
"https://www.aquascape-cebu.com/", # 10000000
"https://colchester.mapxpress.net/", # 10000000
"http://tetuwo181.web.fc2.com/", # 10000000
"https://www.stoffeerdersunie.be/", # 10000000
"https://12v.org/", # 10000000
"https://www.adamscountygis.com/", # 10000000
"https://www.hotelhistrion.com/", # 10000000
"https://alkatreszplusz.hu/", # 10000000
"https://coventry.mapxpress.net/", # 10000000
"https://hostedftp.com/", # 10000000
"https://menkyo119.com/", # 10000000
"https://admin.tworldfriends.co.kr/", # 10000000
"https://www.julu.com/", # 10000000
"https://agrobio.elmedia.net/", # 10000000
"https://stroiteli.elmedia.net/", # 10000000
"https://charlestown.mapxpress.net/", # 10000000
"https://www.chicotrujillo.com/", # 10000000
"http://www.rajhlinky.wz.cz/", # 10000000
"https://aimcontrollers.com/", # 10000000
"https://otsegocountygis.mapxpress.net/", # 10000000
"https://www.sunflowers-agency.pl/", # 10000000
"https://hacona.com/", # 10000000
"https://www.arredamento-bologna-arredamenti.it/", # 10000000
"https://www.stoppingpoints.com/", # 10000000
"https://oneclickbusinesssolutions.com/", # 10000000
"https://sido.daegu.go.kr/", # 10000000
"https://www.oncugrup.com.tr/", # 10000000
"https://coffre.damaris.pro/", # 10000000
"https://brookfield.mapxpress.net/", # 10000000
"https://berlin.mapxpress.net/", # 10000000
"http://www.khrc.net/", # 10000000
"https://finterstellar.com/", # 10000000
"https://alev-trans.ru/", # 10000000
"https://westhaven.mapxpress.net/", # 50000000
"https://plymouth.mapxpress.net/", # 50000000
"https://www.goukei.com/", # 50000000
"https://www.unicampus.in/", # 50000000
"http://mackeyfi.somee.com/", # 50000000
"https://newington.mapxpress.net/", # 50000000
"https://doctor100.co.kr/", # 50000000
"https://www.a-tech-eng.com/", # 50000000
"http://www.atomica.co.uk/", # 50000000
"https://www.bluegrassrealty.com/", # 50000000
"https://pro230428.prosell.kr/", # 50000000
"https://isitdown.co.uk/", # 50000000
"https://www.inventum.hr/", # 50000000
"https://www.icon-media.com/", # 50000000
"https://woodbury.mapxpress.net/", # 50000000
"https://www.hotel-radium-palace.com/", # 50000000
"https://www.seniorske-pobyty.info/", # 50000000
"https://www.parallel-schallplatten.de/", # 50000000
"https://www.hotel-velka-fatra.com/", # 50000000
"https://backpacker.gr/", # 50000000
"https://www.pacificgroupbd.com/", # 50000000
"https://www.nidami.com/", # 50000000
"http://beppuni.com/", # 50000000
"http://e.pl/", # 50000000
"https://newhartford.mapxpress.net/", # 50000000
"https://shadowshroud.com/", # 50000000
"https://newbritain.mapxpress.net/", # 50000000
"https://milford.mapxpress.net/", # 50000000
"https://www.kusatsu.org/", # 50000000
"https://co.becker.mn.us/", # 50000000
"https://koicd.kr/", # 50000000
"https://shelton.mapxpress.net/", # 50000000
"http://shikokuhenro-tomonokai.jp/", # 50000000
"https://www.koizumi-koumonka.com/", # 50000000
"https://lillysoo29.prosell.kr/", # 50000000
"https://naugatuck.mapxpress.net/", # 50000000
"https://school.videogameaudio.com/", # 50000000
"https://hopkinton.mapxpress.net/", # 50000000
"http://www.danceworksmajesticsstudio.com/", # 50000000
"https://www.ellenfcasperphd.com/", # 50000000
"https://at-cinq.com/", # 50000000
"http://www.rallyetoulousesaintlouis.com/", # 50000000
"https://www.shamanicjourneys.com/", # 50000000
"https://suffield.mapxpress.net/", # 50000000
"http://sido.jeju.go.kr/", # 50000000
"http://www.sisatotalnews.com/", # 50000000
"https://www.hotel-aphrodite.com/", # 50000000
"https://woodbridge.mapxpress.net/", # 50000000
"https://cookingmama.com/", # 50000000
"https://oxford.mapxpress.net/", # 50000000
"https://www.artsandopinion.com/", # 50000000
"http://www.konishizokei.co.jp/", # 50000000
"https://bristol.mapxpress.net/", # 50000000
"https://atypical.gr/", # 50000000
"https://with.mando.com/", # 50000000
"https://www.vianocne-pobyty.info/", # 50000000
"https://crest-ihec.jp/", # 50000000
"https://chai-talk.artistchai.co.kr/", # 50000000
"https://shrujanlldc.org/", # 50000000
"https://www.hotel-polana-brusno.com/", # 50000000
"http://www.broadwaysalvage.com/", # 50000000
"https://www.pro-fusiononline.com/", # 50000000
"http://www.ssoc.chem.tohoku.ac.jp/", # 50000000
"https://www.centredetirgranby.ca/", # 50000000
"https://www.mettlerelectronics.com/", # 50000000
"https://stand.bg/", # 50000000
"https://southwindsor.mapxpress.net/", # 50000000
"https://rabbit.prosell.kr/", # 50000000
"https://www.shorelandmanagement.org/", # 50000000
"http://www.brookedanielsphotography.com/", # 50000000
"https://www.hotel-strand-vysne-ruzbachy.com/", # 50000000
"https://www.hotel-radin.com/", # 50000000
"https://southbury.mapxpress.net/", # 50000000
"https://seymour.mapxpress.net/", # 50000000
"https://gomumall.com/", # 50000000
"https://trans-servise.com/", # 50000000
"http://www.phildoylephoto.com/", # 50000000
"https://www.hacona.com/", # 50000000
"https://preston.mapxpress.net/", # 50000000
"https://webusable.com/", # 50000000
"https://www.sas-net.co.jp/", # 50000000
]

# CSS selector to search for
css_selector = """
img[name][id=domain],object[id=domain],[name=domain]:is(embed,form,iframe,img,object),
img[name][id=referrer],object[id=referrer],[name=referrer]:is(embed,form,iframe,img,object),
img[name][id=cookie],object[id=cookie],[name=cookie]:is(embed,form,iframe,img,object),
img[name][id=lastModified],object[id=lastModified],[name=lastModified]:is(embed,form,iframe,img,object),
img[name][id=readyState],object[id=readyState],[name=readyState]:is(embed,form,iframe,img,object),
img[name][id=title],object[id=title],[name=title]:is(embed,form,iframe,img,object),
img[name][id=dir],object[id=dir],[name=dir]:is(embed,form,iframe,img,object),
img[name][id=body],object[id=body],[name=body]:is(embed,form,iframe,img,object),
img[name][id=head],object[id=head],[name=head]:is(embed,form,iframe,img,object),
img[name][id=images],object[id=images],[name=images]:is(embed,form,iframe,img,object),
img[name][id=embeds],object[id=embeds],[name=embeds]:is(embed,form,iframe,img,object),
img[name][id=plugins],object[id=plugins],[name=plugins]:is(embed,form,iframe,img,object),
img[name][id=links],object[id=links],[name=links]:is(embed,form,iframe,img,object),
img[name][id=forms],object[id=forms],[name=forms]:is(embed,form,iframe,img,object),
img[name][id=scripts],object[id=scripts],[name=scripts]:is(embed,form,iframe,img,object),
img[name][id=getElementsByName],object[id=getElementsByName],[name=getElementsByName]:is(embed,form,iframe,img,object),
img[name][id=only],object[id=only],[name=only]:is(embed,form,iframe,img,object),
img[name][id=open],object[id=open],[name=open]:is(embed,form,iframe,img,object),
img[name][id=close],object[id=close],[name=close]:is(embed,form,iframe,img,object),
img[name][id=write],object[id=write],[name=write]:is(embed,form,iframe,img,object),
img[name][id=writeln],object[id=writeln],[name=writeln]:is(embed,form,iframe,img,object),
img[name][id=defaultView],object[id=defaultView],[name=defaultView]:is(embed,form,iframe,img,object),
img[name][id=hasFocus],object[id=hasFocus],[name=hasFocus]:is(embed,form,iframe,img,object),
img[name][id=designMode],object[id=designMode],[name=designMode]:is(embed,form,iframe,img,object),
img[name][id=execCommand],object[id=execCommand],[name=execCommand]:is(embed,form,iframe,img,object),
img[name][id=queryCommandEnabled],object[id=queryCommandEnabled],[name=queryCommandEnabled]:is(embed,form,iframe,img,object),
img[name][id=queryCommandIndeterm],object[id=queryCommandIndeterm],[name=queryCommandIndeterm]:is(embed,form,iframe,img,object),
img[name][id=queryCommandState],object[id=queryCommandState],[name=queryCommandState]:is(embed,form,iframe,img,object),
img[name][id=queryCommandSupported],object[id=queryCommandSupported],[name=queryCommandSupported]:is(embed,form,iframe,img,object),
img[name][id=queryCommandValue],object[id=queryCommandValue],[name=queryCommandValue]:is(embed,form,iframe,img,object),
img[name][id=hidden],object[id=hidden],[name=hidden]:is(embed,form,iframe,img,object),
img[name][id=visibilityState],object[id=visibilityState],[name=visibilityState]:is(embed,form,iframe,img,object),
img[name][id=onreadystatechange],object[id=onreadystatechange],[name=onreadystatechange]:is(embed,form,iframe,img,object),
img[name][id=onvisibilitychange],object[id=onvisibilitychange],[name=onvisibilitychange]:is(embed,form,iframe,img,object),
img[name][id=fgColor],object[id=fgColor],[name=fgColor]:is(embed,form,iframe,img,object),
img[name][id=linkColor],object[id=linkColor],[name=linkColor]:is(embed,form,iframe,img,object),
img[name][id=vlinkColor],object[id=vlinkColor],[name=vlinkColor]:is(embed,form,iframe,img,object),
img[name][id=alinkColor],object[id=alinkColor],[name=alinkColor]:is(embed,form,iframe,img,object),
img[name][id=bgColor],object[id=bgColor],[name=bgColor]:is(embed,form,iframe,img,object),
img[name][id=anchors],object[id=anchors],[name=anchors]:is(embed,form,iframe,img,object),
img[name][id=applets],object[id=applets],[name=applets]:is(embed,form,iframe,img,object),
img[name][id=clear],object[id=clear],[name=clear]:is(embed,form,iframe,img,object),
img[name][id=captureEvents],object[id=captureEvents],[name=captureEvents]:is(embed,form,iframe,img,object),
img[name][id=releaseEvents],object[id=releaseEvents],[name=releaseEvents]:is(embed,form,iframe,img,object),
img[name][id=all],object[id=all],[name=all]:is(embed,form,iframe,img,object),
img[name][id=onabort],object[id=onabort],[name=onabort]:is(embed,form,iframe,img,object),
img[name][id=onauxclick],object[id=onauxclick],[name=onauxclick]:is(embed,form,iframe,img,object),
img[name][id=onbeforeinput],object[id=onbeforeinput],[name=onbeforeinput]:is(embed,form,iframe,img,object),
img[name][id=onbeforematch],object[id=onbeforematch],[name=onbeforematch]:is(embed,form,iframe,img,object),
img[name][id=onbeforetoggle],object[id=onbeforetoggle],[name=onbeforetoggle]:is(embed,form,iframe,img,object),
img[name][id=onblur],object[id=onblur],[name=onblur]:is(embed,form,iframe,img,object),
img[name][id=oncancel],object[id=oncancel],[name=oncancel]:is(embed,form,iframe,img,object),
img[name][id=oncanplay],object[id=oncanplay],[name=oncanplay]:is(embed,form,iframe,img,object),
img[name][id=oncanplaythrough],object[id=oncanplaythrough],[name=oncanplaythrough]:is(embed,form,iframe,img,object),
img[name][id=onchange],object[id=onchange],[name=onchange]:is(embed,form,iframe,img,object),
img[name][id=onclick],object[id=onclick],[name=onclick]:is(embed,form,iframe,img,object),
img[name][id=onclose],object[id=onclose],[name=onclose]:is(embed,form,iframe,img,object),
img[name][id=oncontextlost],object[id=oncontextlost],[name=oncontextlost]:is(embed,form,iframe,img,object),
img[name][id=oncontextmenu],object[id=oncontextmenu],[name=oncontextmenu]:is(embed,form,iframe,img,object),
img[name][id=oncontextrestored],object[id=oncontextrestored],[name=oncontextrestored]:is(embed,form,iframe,img,object),
img[name][id=oncopy],object[id=oncopy],[name=oncopy]:is(embed,form,iframe,img,object),
img[name][id=oncuechange],object[id=oncuechange],[name=oncuechange]:is(embed,form,iframe,img,object),
img[name][id=oncut],object[id=oncut],[name=oncut]:is(embed,form,iframe,img,object),
img[name][id=ondblclick],object[id=ondblclick],[name=ondblclick]:is(embed,form,iframe,img,object),
img[name][id=ondrag],object[id=ondrag],[name=ondrag]:is(embed,form,iframe,img,object),
img[name][id=ondragend],object[id=ondragend],[name=ondragend]:is(embed,form,iframe,img,object),
img[name][id=ondragenter],object[id=ondragenter],[name=ondragenter]:is(embed,form,iframe,img,object),
img[name][id=ondragleave],object[id=ondragleave],[name=ondragleave]:is(embed,form,iframe,img,object),
img[name][id=ondragover],object[id=ondragover],[name=ondragover]:is(embed,form,iframe,img,object),
img[name][id=ondragstart],object[id=ondragstart],[name=ondragstart]:is(embed,form,iframe,img,object),
img[name][id=ondrop],object[id=ondrop],[name=ondrop]:is(embed,form,iframe,img,object),
img[name][id=ondurationchange],object[id=ondurationchange],[name=ondurationchange]:is(embed,form,iframe,img,object),
img[name][id=onemptied],object[id=onemptied],[name=onemptied]:is(embed,form,iframe,img,object),
img[name][id=onended],object[id=onended],[name=onended]:is(embed,form,iframe,img,object),
img[name][id=onerror],object[id=onerror],[name=onerror]:is(embed,form,iframe,img,object),
img[name][id=onfocus],object[id=onfocus],[name=onfocus]:is(embed,form,iframe,img,object),
img[name][id=onformdata],object[id=onformdata],[name=onformdata]:is(embed,form,iframe,img,object),
img[name][id=oninput],object[id=oninput],[name=oninput]:is(embed,form,iframe,img,object),
img[name][id=oninvalid],object[id=oninvalid],[name=oninvalid]:is(embed,form,iframe,img,object),
img[name][id=onkeydown],object[id=onkeydown],[name=onkeydown]:is(embed,form,iframe,img,object),
img[name][id=onkeypress],object[id=onkeypress],[name=onkeypress]:is(embed,form,iframe,img,object),
img[name][id=onkeyup],object[id=onkeyup],[name=onkeyup]:is(embed,form,iframe,img,object),
img[name][id=onload],object[id=onload],[name=onload]:is(embed,form,iframe,img,object),
img[name][id=onloadeddata],object[id=onloadeddata],[name=onloadeddata]:is(embed,form,iframe,img,object),
img[name][id=onloadedmetadata],object[id=onloadedmetadata],[name=onloadedmetadata]:is(embed,form,iframe,img,object),
img[name][id=onloadstart],object[id=onloadstart],[name=onloadstart]:is(embed,form,iframe,img,object),
img[name][id=onmousedown],object[id=onmousedown],[name=onmousedown]:is(embed,form,iframe,img,object),
img[name][id=onmouseenter],object[id=onmouseenter],[name=onmouseenter]:is(embed,form,iframe,img,object),
img[name][id=onmouseleave],object[id=onmouseleave],[name=onmouseleave]:is(embed,form,iframe,img,object),
img[name][id=onmousemove],object[id=onmousemove],[name=onmousemove]:is(embed,form,iframe,img,object),
img[name][id=onmouseout],object[id=onmouseout],[name=onmouseout]:is(embed,form,iframe,img,object),
img[name][id=onmouseover],object[id=onmouseover],[name=onmouseover]:is(embed,form,iframe,img,object),
img[name][id=onmouseup],object[id=onmouseup],[name=onmouseup]:is(embed,form,iframe,img,object),
img[name][id=onpaste],object[id=onpaste],[name=onpaste]:is(embed,form,iframe,img,object),
img[name][id=onpause],object[id=onpause],[name=onpause]:is(embed,form,iframe,img,object),
img[name][id=onplay],object[id=onplay],[name=onplay]:is(embed,form,iframe,img,object),
img[name][id=onplaying],object[id=onplaying],[name=onplaying]:is(embed,form,iframe,img,object),
img[name][id=onprogress],object[id=onprogress],[name=onprogress]:is(embed,form,iframe,img,object),
img[name][id=onratechange],object[id=onratechange],[name=onratechange]:is(embed,form,iframe,img,object),
img[name][id=onreset],object[id=onreset],[name=onreset]:is(embed,form,iframe,img,object),
img[name][id=onresize],object[id=onresize],[name=onresize]:is(embed,form,iframe,img,object),
img[name][id=onscroll],object[id=onscroll],[name=onscroll]:is(embed,form,iframe,img,object),
img[name][id=onscrollend],object[id=onscrollend],[name=onscrollend]:is(embed,form,iframe,img,object),
img[name][id=onsecuritypolicyviolation],object[id=onsecuritypolicyviolation],[name=onsecuritypolicyviolation]:is(embed,form,iframe,img,object),
img[name][id=onseeked],object[id=onseeked],[name=onseeked]:is(embed,form,iframe,img,object),
img[name][id=onseeking],object[id=onseeking],[name=onseeking]:is(embed,form,iframe,img,object),
img[name][id=onselect],object[id=onselect],[name=onselect]:is(embed,form,iframe,img,object),
img[name][id=onslotchange],object[id=onslotchange],[name=onslotchange]:is(embed,form,iframe,img,object),
img[name][id=onstalled],object[id=onstalled],[name=onstalled]:is(embed,form,iframe,img,object),
img[name][id=onsubmit],object[id=onsubmit],[name=onsubmit]:is(embed,form,iframe,img,object),
img[name][id=onsuspend],object[id=onsuspend],[name=onsuspend]:is(embed,form,iframe,img,object),
img[name][id=ontimeupdate],object[id=ontimeupdate],[name=ontimeupdate]:is(embed,form,iframe,img,object),
img[name][id=ontoggle],object[id=ontoggle],[name=ontoggle]:is(embed,form,iframe,img,object),
img[name][id=onvolumechange],object[id=onvolumechange],[name=onvolumechange]:is(embed,form,iframe,img,object),
img[name][id=onwaiting],object[id=onwaiting],[name=onwaiting]:is(embed,form,iframe,img,object),
img[name][id=onwebkitanimationend],object[id=onwebkitanimationend],[name=onwebkitanimationend]:is(embed,form,iframe,img,object),
img[name][id=onwebkitanimationiteration],object[id=onwebkitanimationiteration],[name=onwebkitanimationiteration]:is(embed,form,iframe,img,object),
img[name][id=onwebkitanimationstart],object[id=onwebkitanimationstart],[name=onwebkitanimationstart]:is(embed,form,iframe,img,object),
img[name][id=onwebkittransitionend],object[id=onwebkittransitionend],[name=onwebkittransitionend]:is(embed,form,iframe,img,object),
img[name][id=onwheel],object[id=onwheel],[name=onwheel]:is(embed,form,iframe,img,object),
img[name][id=implementation],object[id=implementation],[name=implementation]:is(embed,form,iframe,img,object),
img[name][id=URL],object[id=URL],[name=URL]:is(embed,form,iframe,img,object),
img[name][id=documentURI],object[id=documentURI],[name=documentURI]:is(embed,form,iframe,img,object),
img[name][id=compatMode],object[id=compatMode],[name=compatMode]:is(embed,form,iframe,img,object),
img[name][id=characterSet],object[id=characterSet],[name=characterSet]:is(embed,form,iframe,img,object),
img[name][id=contentType],object[id=contentType],[name=contentType]:is(embed,form,iframe,img,object),
img[name][id=doctype],object[id=doctype],[name=doctype]:is(embed,form,iframe,img,object),
img[name][id=documentElement],object[id=documentElement],[name=documentElement]:is(embed,form,iframe,img,object),
img[name][id=getElementsByTagName],object[id=getElementsByTagName],[name=getElementsByTagName]:is(embed,form,iframe,img,object),
img[name][id=getElementsByTagNameNS],object[id=getElementsByTagNameNS],[name=getElementsByTagNameNS]:is(embed,form,iframe,img,object),
img[name][id=getElementsByClassName],object[id=getElementsByClassName],[name=getElementsByClassName]:is(embed,form,iframe,img,object),
img[name][id=createElement],object[id=createElement],[name=createElement]:is(embed,form,iframe,img,object),
img[name][id=createElementNS],object[id=createElementNS],[name=createElementNS]:is(embed,form,iframe,img,object),
img[name][id=createDocumentFragment],object[id=createDocumentFragment],[name=createDocumentFragment]:is(embed,form,iframe,img,object),
img[name][id=createTextNode],object[id=createTextNode],[name=createTextNode]:is(embed,form,iframe,img,object),
img[name][id=createCDATASection],object[id=createCDATASection],[name=createCDATASection]:is(embed,form,iframe,img,object),
img[name][id=createComment],object[id=createComment],[name=createComment]:is(embed,form,iframe,img,object),
img[name][id=createProcessingInstruction],object[id=createProcessingInstruction],[name=createProcessingInstruction]:is(embed,form,iframe,img,object),
img[name][id=importNode],object[id=importNode],[name=importNode]:is(embed,form,iframe,img,object),
img[name][id=adoptNode],object[id=adoptNode],[name=adoptNode]:is(embed,form,iframe,img,object),
img[name][id=createAttribute],object[id=createAttribute],[name=createAttribute]:is(embed,form,iframe,img,object),
img[name][id=createAttributeNS],object[id=createAttributeNS],[name=createAttributeNS]:is(embed,form,iframe,img,object),
img[name][id=createEvent],object[id=createEvent],[name=createEvent]:is(embed,form,iframe,img,object),
img[name][id=createRange],object[id=createRange],[name=createRange]:is(embed,form,iframe,img,object),
img[name][id=createNodeIterator],object[id=createNodeIterator],[name=createNodeIterator]:is(embed,form,iframe,img,object),
img[name][id=createTreeWalker],object[id=createTreeWalker],[name=createTreeWalker]:is(embed,form,iframe,img,object),
img[name][id=activeElement],object[id=activeElement],[name=activeElement]:is(embed,form,iframe,img,object)
"""

# Output file to store the results
output_file = "results.txt"

def fetch_and_check_css(url, selector, file):
    try:
        # Fetch the page
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Parse the HTML using html5lib
        soup = BeautifulSoup(response.content, "html5lib")

        # Find elements matching the selector
        elements = soup.select(selector)
        if elements:
            file.write(f"Matches found on {url}:\n")
            for element in elements:
                # Get the localName, id attribute, and name attribute values
                local_name = element.name
                id_value = element.get('id', 'No id')
                name_value = element.get('name', 'No name')

                # Write the element details to the file
                file.write(f" - Element: {local_name}, id: {id_value}, name: {name_value}\n")
        else:
            file.write(f"No matches found on {url}\n")
    except requests.exceptions.RequestException as e:
        file.write(f"Error fetching {url}: {e}\n")

# Iterate over the URLs and check the selector
with open(output_file, "w") as file:
    # Iterate over the URLs and check the selector
    for url in urls:
        fetch_and_check_css(url, css_selector, file)

print(f"Results written to {output_file}")
