
from langchain.tools import BaseTool
import pandas as pd

# creation of Custom Tool for Sales Data Analysis

desc = (
    " use this tool when you are asked to analyze the csv sales data "
    " It will return a list of data analysis results"
    "using pandas dataframe"
)


class DataAnalyzer(BaseTool):
    name = "DataAnalyzer"
    description = desc
    
    def _run(self, csv_path:str):
        df = pd.read_csv(csv_path)
        # Top-selling menu items by quantity
        total_sales = df['TotalAmount'].sum()
                # Top-selling menu items by quantity
        top_items_quantity = df.groupby('MenuItem')['Quantity'].sum().nlargest(5)
                # Top-selling menu items by revenue
        top_items_revenue = df.groupby('MenuItem')['TotalAmount'].sum().nlargest(5)
        # Sales trends over time
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])
        df['Month'] = df['OrderDate'].dt.month
        monthly_sales = df.groupby('Month')['TotalAmount'].sum()
        # Revenue Analysis by day
        daily_revenue = df.groupby('OrderDate')['TotalAmount'].sum()
        
        return {
            'total_sales': total_sales,
            'top_items_quantity': top_items_quantity,
            'top_items_revenue': top_items_revenue,
            'monthly_sales': monthly_sales,
            'daily_revenue': daily_revenue,}
        
    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")        
        