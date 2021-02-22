import calendar
from datetime import datetime

class ModCalender(calendar.LocaleHTMLCalendar):

    def __init__(self):
        calendar.LocaleHTMLCalendar.__init__(self, firstweekday=6,locale='ja_jp')

    #オーバーライド
    def formatmonth(self, theyear, themonth, withyear=True):
        v = []
        a = v.append
        a('<table class="table table-bordered" style="table-layout: fixed;">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        # 見た目調整　※もっと良い方法があると思います。
        week_count = len(self.monthdays2calendar(theyear, themonth))
        if week_count == 6:
            a('<br /><br />') 
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, theyear, themonth, week_count))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    #オーバーライド
    def formatweek(self, theweek, theyear, themonth, week_count):
        s = ''.join(self.formatday(d, theyear, themonth) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    #オーバーライド
    def formatday(self, day, theyear, themonth):
        html = [];
        if day == 0:
            return '<td style="background-color: #eeeeee">&nbsp;</td>'
        else:
            html = '<td class="text-center {highlight}"><a href="{url}" style="color:{text}">{day}</a></td>'
            text = 'blue'
            highlight = ''

        date = datetime(year=theyear, month=themonth, day=day)
        return html.format(
                        url='/todo/{}/{}/{}'.format(theyear, themonth, day),
                        text=text,
                        day=day,
                        highlight=highlight
        )