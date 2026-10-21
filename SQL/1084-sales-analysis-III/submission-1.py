import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on='product_id', how='left')
    df = df.groupby(by=['product_id', 'product_name']).agg(
        min_sale_date = ('sale_date', 'min'),
        max_sale_date = ('sale_date', 'max')
    ).reset_index()

    return df[(df.min_sale_date >= '2019-01-01') & (df.max_sale_date <= '2019-03-31')][['product_id', 'product_name']]