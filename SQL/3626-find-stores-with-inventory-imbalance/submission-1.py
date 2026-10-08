import pandas as pd

def find_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    inventory = (
        inventory.sort_values(by=['price', 'quantity'], ascending=[False, False])
        .reset_index(drop=True)
        )

    df = inventory.groupby(by='store_id').agg(
            most_exp_idx = ('price', 'idxmax'),
            most_cheap_idx = ('price', 'idxmin'),
            n_products = ('product_name', 'nunique')
        )

    df = df[df.n_products.ge(3)]

    df1 = (
        inventory.loc[df.most_exp_idx.values]
        .rename(columns={'product_name': 'most_exp_product', 'quantity': 'quantity_exp'})
        .loc[:, ['store_id', 'most_exp_product', 'quantity_exp']]
    )
    df2 = (
        inventory.loc[df.most_cheap_idx.values]
        .rename(columns={'product_name': 'cheapest_product', 'quantity': 'quantity_cheap'})
        .loc[:, ['store_id', 'cheapest_product', 'quantity_cheap']]
    )

    df = df1.merge(df2, on='store_id', how='inner')
    df = df[df['quantity_cheap'] > df['quantity_exp']]
    df['imbalance_ratio'] = (df['quantity_cheap'] / df['quantity_exp']).round(2)
    df = df.merge(stores, on='store_id', how='left')

    return (
        df.loc[:, ['store_id', 'store_name', 'location', 'most_exp_product', 'cheapest_product', 'imbalance_ratio']]
        .sort_values(by=['imbalance_ratio', 'store_name'], ascending=[False, True])
    )