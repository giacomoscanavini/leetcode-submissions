import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    df = product_purchases.merge(product_info, on='product_id', how='left')
    df = df[['user_id', 'category']]
    df = df.merge(df, how='cross', suffixes=['1', '2'])
    df = df[(df.user_id1 == df.user_id2) & (df.category1 < df.category2)]

    df = df.groupby(by=['category1', 'category2']).agg(
        customer_count = ('user_id1', 'nunique')
    ).reset_index()
    
    df = df[df.customer_count >= 3]
    return df[['category1', 'category2', 'customer_count']].sort_values(by=['customer_count', 'category1', 'category2'], ascending=[False, True, True])