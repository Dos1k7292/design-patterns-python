from report import Report


class TextReportBuilder:
    def __init__(self):
        self.report = Report()

    def set_header(self, header):
        self.report.header = header

    def set_content(self, content):
        self.report.content = content

    def set_footer(self, footer):
        self.report.footer = footer

    def get_report(self):
        return self.report


class HtmlReportBuilder:
    def __init__(self):
        self.report = Report()

    def set_header(self, header):
        self.report.header = f"<h1>{header}</h1>"

    def set_content(self, content):
        self.report.content = f"<p>{content}</p>"

    def set_footer(self, footer):
        self.report.footer = f"<footer>{footer}</footer>"

    def get_report(self):
        return self.report
