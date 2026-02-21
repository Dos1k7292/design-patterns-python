from builders import TextReportBuilder, HtmlReportBuilder
from director import ReportDirector


director = ReportDirector()

print("TEXT REPORT")
text_builder = TextReportBuilder()
director.construct(text_builder)
text_report = text_builder.get_report()
text_report.show()

print("\nHTML REPORT")
html_builder = HtmlReportBuilder()
director.construct(html_builder)
html_report = html_builder.get_report()
html_report.show()
