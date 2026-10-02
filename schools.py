# Import library
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# best maths schools
best_math_schools = (
    schools
    .loc[schools['average_math'] >= 800*0.8, ['school_name','average_math']]
    .sort_values(by='average_math', ascending=False)
)
best_math_schools

# top 10 schools
schools['total_SAT'] = schools['average_math']+schools['average_reading']+schools['average_writing']

top_10_schools = (
    schools
    .loc[:,['school_name','total_SAT']]
    .sort_values(by='total_SAT', ascending=False)
    .head(10)
)
top_10_schools

# largest deviation in SAT score
largest_std_dev = (
    schools
    .groupby('borough')
    .agg(
        num_schools=('school_name','count'),
        average_SAT=('total_SAT','mean'),
        std_SAT=('total_SAT','std')
        )
    .round(2)
)

largest_std_dev
