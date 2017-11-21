import billboard as bb
import xlwt

def main():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Billboard Chart')
    chart = bb.ChartData('hot-100')

    col_date = 0
    
    while(True):
        date = chart.date
        if date >= '2014-09-06':
            ws.write(col_date, 0, date)
            for i in range(len(chart)):
                ws.write(col_date, 1, chart[i].weeks)
                ws.write(col_date, 2, chart[i].rank)
                ws.write(col_date, 3, chart[i].title)
                ws.write(col_date, 4, chart[i].artist)
                ws.write(col_date, 5, chart[i].peakPos)
                ws.write(col_date, 6, chart[i].lastPos)
                col_date += 1
            chart = bb.ChartData('hot-100', chart.previousDate)
            print(date)
        else :
            break
    
    wb.save('billboard-top-100.xls')

main()
