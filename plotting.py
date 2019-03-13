from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

f=figure(height=500,width=1000,x_axis_type="datetime",title="Motion Graph")
f.yaxis.minor_tick_line_color=None
f.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@start_string"),("End","@end_string")])
f.add_tools(hover)

output_file("graph.html")

f.quad(left="Start",right="End",top=1,bottom=0,color="green",source=cds)

show(f)
