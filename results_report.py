import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv

df = pd.read_csv("results.csv")

# profile = ProfileReport(df, title="Football Results")

# profile.to_file('results_report.html')

my_report = sv.analyze(df)
my_report.show_html()