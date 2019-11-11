import pdfkit
from plan_gen import PlanGenerator

class PDF_generator:

    """
    用于生成PDF
    """

    css = None
    options = None

    def __init__(self, css = "github.css", options = None):
        
        """
        css: string，css样式文件路径
        """

        self.css = css
        if options == None:
            self.options = {
                'page-size': 'A4',
                'margin-top': '0.3in',
                'margin-right': '0.3in',
                'margin-bottom': '0.3in',
                'margin-left': '0.3in',
                'encoding': "UTF-8",
            }

    def output_pdf(self, calendar, file_name):

        """
        输出PDF文件
        calendar: dic, 由Plan_generator生成的时间表dic
        file_name: string，输出文件名
        """

        # 计算需要的属性
        max_length = 0
        for (key, value) in calendar.items():
            if len(value) > max_length:
                max_length = len(value)
        print(max_length)

        # 生成HTML页面头部
        body_head = """
        <html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
            <head>
                <meta charset="utf-8" />
                <meta name="pdfkit-page-size" content="A4"/>
                <meta name="pdfkit-orientation" content="Portrait"/>
            </head>
            <body>
                <h2 class="title">背单词时间计划表</h2>
                <li>(注：带*表示之前没有背过的新list)</li>
                <hr>
        """

        # 生成表格头部
        table_head = """
        <table>
            <thead>
            <tr class="header">
                <th style="text-align: center;">日期</th>
                <th style="text-align: center;" colspan='%s'>list序号</th>
            </tr>
            </thead>
        """ % max_length

        # 生成表格内容
        table_content = ""
        for (key, value) in calendar.items():
            table_content += '<tr>'
            table_content += '<td style="text-align: left;">%s</td>' % key
            for section_number in value:
                table_content += '<td style="text-align: left;" width="50px";>%s</td>' % section_number
            table_content += '</tr>'

        # 生成表格尾部
        table_tail = """
        </table>
        """

        # 生成HTML页面尾部
        body_tail = """
            </body>
        </html>
        """
        
        output_body = body_head + table_head  + table_content + table_tail + body_tail
        pdfkit.from_string(output_body, file_name + ".pdf", css=self.css, options=self.options)

if __name__ == "__main__":
    pdf_gen = PDF_generator()
    plan_gen = PlanGenerator(31, 1, "20191111")
    calendar = plan_gen.generate_calendar()
    pdf_gen.output_pdf(calendar, "test")