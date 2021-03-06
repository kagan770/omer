#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Yom import yom # creates just the "hayom...laomer" line

def weekandday(day):
    return day // 7, day % 7

def textforday(day, times=''):
    if day not in xrange(1,50):
        return u'''\
<html>
  <head>
    <title>Error</title>
  </head>
  <body>
    <div>
      Invalid input for day of Omer: %s
    </div>
  </body>
</html>
''' % day

    html = u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <title>Day %(day)s</title>
    <style type="text/css">
      @import url(/fonts/FrankRuhel/stylesheet.css);
      body
      {
        font-family:'frank_ruehl', vilna, "Times New Roman", Times, serif;
        font-size:18px;
        width:620px;
        float:right;
      }
      #bracha { %(bracha_style)s }
      #yom { font-size:22px; }
      .bold { font-weight:bold; }
      .bigbold 
      {
        font-weight:bold;
        font-size:19px;
      }
      #red
      {
        font-weight:bold;
        font-size:20px;
        color:red;
      }
      .center { text-align:center; }
      .left { text-align:left; }
      td { text-align:right; }
      table { %(twilight)s }
      #transparent { background:rgba(255, 255, 255, 0.3); }
      
    </style>
  </head>
  <body>
    <table border=0>
      <tr>
        <td>
          %(tzeit)s - %(zipcode)s
          <hr />
        </td>
      </tr>
      <tr>
        <td>
          <span id=bracha>%(bracha)s</span><br /><br />
          <span id=yom>%(yom)s</span><br /><br />
          %(harachaman)s<br /><br />
          %(lamnatzeach)s<br /><br />
        </td>
      </tr>
      <tr>
        <td>
          <table border=0 style="float:right;">
            %(anabechoach)s
            <tr>
              <td colspan=2 class=center>
                %(baruchshem)s
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td>
          <br />%(ribonoshelolam)s
        </td>
      </tr>
    </table>
    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script type="text/javascript" charset="utf-8">
      $(function() { $('body').hide().show(); });
    </script>
  </body>
</html>
'''

    tzeit = u'צאת הכוכבים׃' + times[u'nightfall'].strftime(u'%H:%M %Y-%m-%d')
    twilight = u'background-color:#ddd;' if times['now'][0] < times[u'nightfall'] and times['now'][0] > times[u'sunset'] else u''
    bracha_style = u'color:#aaa;font-size:14px;' if times['now'][0] < times[u'sunset'] and times['now'][0] > times[u'dawn'] else u'font-size:21px;'
    bracha = u'בָּרוּךְ אַתָּה יְהוָה אֱלהֵינוּ מֶלֶךְ הָעוֹלָם, אֲשֶׁר קִדְּשָׁנוּ בְּמִצְוֹתָיו, וְצִוָּנוּ עַל סְפִירַת הָעוֹמֶר'
    harachaman = u'הָרַחֲמָן הוּא יַחֲזִיר לָנוּ עֲבוֹדַת בֵּית הַמִּקְדָּשׁ לִמְקוֹמָהּ, בִּמְהֵרָה בְיָמֵינוּ אָמֵן סֶלָה'
    baruchshem = u'בָּרוּךְ שֵׁם כְּבוֹד מַלְכוּתוֹ לְעוֹלָם וָעֶד'

    output = {
              u'day': day,
              u'twilight': twilight,
              u'zipcode': times['zipcode'],
              u'bracha_style': bracha_style,
              u'bracha': bracha+u'׃',
              u'yom': yom(day-1)+u'׃',
              u'harachaman': harachaman+u'׃',
              u'lamnatzeach': lamnatzeach(day),
              u'anabechoach': anabechoach(day-1),
              u'baruchshem': baruchshem+u'׃',
              u'ribonoshelolam': ribonoshelolam(day),
              u'tzeit': tzeit,
             }

    return html % output

def lamnatzeach(day):
    cday = day
    if day >= 16: cday = day + 1 # this is for dealing with
    if day >= 33: cday = day + 2 # the two commas in yismechu
    lamnatzeach = [ # double spacing so that we can easily parse <span id=red> as a single item
u'לַמְנַצֵּחַ  בִּנְגִינוֹת  מִזְמוֹר  שִׁיר׃  אֱלהִים  יְחָנֵּנוּ  וִיבָרְכֵנוּ,  יָאֵר  פָּנָיו  אִתָּנוּ  סֶלָה׃ ',
u' לָדַעַת  בָּאָרֶץ  דַּרְכֶּךָ,  בְּכָל  גּוֹיִם  יְשׁוּעָתֶךָ׃  יוֹדוּךָ  עַמִּים  ׀  אֱלהִים,  יוֹדוּךָ  עַמִּים  כֻּלָּם׃ ',
u' יִשְׂמְחוּ  וִירַנְּנוּ  לְאֻמִּים,  כִּי  תִשְׁפּוֹט  עַמִּים  מִישׁוֹר,  וּלְאֻמִּים  בָּאָרֶץ  תַּנְחֵם  סֶלָה׃  יוֹדוּךָ ',
u' עַמִּים  ׀  אֱלהִים,  יוֹדוּךָ  עַמִּים  כֻּלָּם׃  אֶרֶץ  נָתְנָה  יְבוּלָהּ,  יְבָרְכֵנוּ  אֱלהִים  אֱלהֵינוּ׃ ',
u' יְבָרְכֵנוּ  אֱלהִים,  וְיִירְאוּ  אוֹתוֹ  כָּל  אַפְסֵי  אָרֶץ׃']

    yismechu = lamnatzeach[2]
    numletters, i1, i2 = 0, None, None
    for c, char in enumerate(yismechu):
        if char in u'אבגדהוזחטיךכלםמןנסעףפץצקרשת':
            numletters += 1
        if numletters == day and not i1:
            i1 = c
        if numletters == day+1 and not i2:
            i2 = c
            while yismechu[i2-1] in u' ,׃':
                i2 -= 1

    lamnatzeach[2] = yismechu[:i1] + u'<span id=red>' + yismechu[i1:i2] + u'</span>' + yismechu[i2:]

    l = u''.join(lamnatzeach).split(u'  ')
    return u' '.join(l[:cday+3]) + u'\n<span class=bold>' + l[cday+3] + u'</span>\n' + u' '.join(l[cday+4:])

def anabechoach(day):
    anabechoach = [ # double spacing here for HTML as well as the roshei teivos sets at the end of the line
u'אָנָּא,  בְּכֹחַ  גְּדֻלַּת  יְמִינְךָ,  תַּתִּיר  צְרוּרָה  אב"ג ית"ץ',
u'קַבֵּל  רִנַּת  עַמְּךָ,  שַׂגְּבֵנוּ,  טַהֲרֵנוּ,  נוֹרָא  קר"ע שט"ן',
u'נָא  גִבּוֹר,  דּוֹרְשֵׁי  יִחוּדְךָ,  כְּבָבַת  שָׁמְרֵם  נג"ד יכ"ש',
u'בָּרְכֵם,  טַהֲרֵם,  רַחֲמֵי  צִדְקָתְךָ  תָּמִיד  גָּמְלֵם  בט"ר צת"ג',
u'חֲסִין  קָדוֹשׁ,  בְּרוֹב  טוּבְךָ  נַהֵל  עֲדָתֶךָ  חק"ב טנ"ע',
u'יָחִיד,  גֵּאֶה,  לְעַמְּךָ  פְּנֵה,  זוֹכְרֵי  קְדֻשָּׁתֶךָ  יג"ל פז"ק',
u'שַׁוְעָתֵנוּ  קַבֵּל,  וּשְׁמַע  צַעֲקָתֵנוּ,  יוֹדֵעַ  תַּעֲלוּמוֹת  שק"ו צי"ת']
    week, day = weekandday(day)
    out = []
    for num, row in enumerate(anabechoach):
        if num != week:
            out.append(u'\n<tr><td class=left>' + row.split(u'  ')[-1] +
                       u'</td><td>.' + u'  '.join(row.split(u'  ')[:-1]) + u'</td></tr>')
        else:
            a = row.split(u'  ')
            bolded_row = u'  '.join(a[:day]) + \
            u'  <span class=bigbold>' + a[day] + u'</span>  ' + \
            u'  '.join(a[day+1:])
            b = bolded_row.strip().split(u'  ')
            out.append(u'\n<tr><td class=left>' + b[-1] + u'</td><td>.' + u'  '.join(b[:-1]) + u'</td></tr>')
    return u''.join(out)

def ribonoshelolam(day):
    def sefiros(day):
        sefiros = u'חֶסֶד גְּבוּרָה תִּפְאֶרֶת נֶצַח הוֹד יְסוֹד מַלְכוּת'.split()
        week, day = weekandday(day-1)
        if week in (1, 5):
            s = u'י' + sefiros[week][2:] if week == 5 else sefiros[week]
            return u'<span class=bigbold>' + sefiros[day] + u' שֶׁבִּ' + s + u'</span>'
        else:
            s = u'ת' + sefiros[week][2:] if week == 2 else sefiros[week]
            return u'<span class=bigbold>' + sefiros[day] + u' שֶׁבְּ' + s + u'</span>'

    ribonoshelolam = [
u'רִבּוֹנוֹ שֶׁל עוֹלָם, אַתָּה צִוִּיתָנוּ עַל יְדֵי משֶׁה עַבְדֶּךָ לִסְפּוֹר סְפִירַת הָעוֹמֶר כְּדֵי לְטַהֲרֵנוּ מִקְלִפּוֹתֵינוּ וּמִטּוּמְאוֹתֵינוּ, כְּמוֹ שֶׁכָּתַבְתָּ בְּתוֹרָתֶךָ׃',
u'וּסְפַרְתֶּם לָכֶם מִמָּחֳרַת הַשַּׁבָּת מִיוֹם הֲבִיאֲכֶם אֶת עוֹמֶר הַתְּנוּפָה שֶׁבַע שַׁבָּתוֹת תְּמִימוֹת תִּהְיֶינָה, עַד מִמָּחֳרַת הַשַּׁבָּת הַשְּׁבִיעִית תִּסְפְּרוּ חֲמִשִּׁים יוֹם,',
u'כְּדֵי שֶׁיִּטָּהֲרוּ נַפְשׁוֹת עַמְּךָ יִשְׂרָאֵל מִזֻּהֲמָתָם, וּבְכֵן יְהִי רָצוֹן מִלְּפָנֶיךָ, יְהוָה אֱלהֵינוּ וֵאלהֵי אֲבוֹתֵינוּ,',
u'שֶׁבִּזְכוּת סְפִירַת הָעוֹמֶר שֶׁסָּפַרְתִּי הַיּוֹם יְתֻקַּן מַה שֶׁפָּגַמְתִּי בִּסְפִירָה',

u'וְאֶטָּהֵר וְאֶתְקַדֵּשׁ בִּקְדֻשָּׁה שֶׁל מַעְלָה,',
u'וְעַל יְדֵי זֶה יֻשְׁפַּע שֶׁפַע רַב בְּכָל הָעוֹלָמוֹת וּלְתַקֵּן אֶת נַפְשׁוֹתֵינוּ וְרוּחוֹתֵינוּ וְנִשְׁמוֹתֵינוּ מִכָּל סִיג וּפְגַם וּלְטַהֲרֵנוּ וּלְקַדְּשֵׁנוּ בִּקְדֻשָׁתְךָ הָעֶלְיוֹנָה, אָמֵן סֶלָה׃']

    return u' '.join(ribonoshelolam[:4] + [sefiros(day)] + ribonoshelolam[4:])

