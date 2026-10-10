import pandas as pd

def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    def count_extreme(x):
        return sum(x != 3)
    
    df = reading_sessions.groupby(by='book_id').agg(
        lowest_rating = ('session_rating', 'min'),
        highest_rating = ('session_rating', 'max'),
        n_sessions = ('session_rating', 'size'),
        extreme_rating = ('session_rating', count_extreme)
    ).reset_index()

    df = df[(df.lowest_rating <= 2) & (df.highest_rating >= 4) & (df.n_sessions >= 5)]
    df['rating_spread'] = df['highest_rating'] - df['lowest_rating']
    df['polarization_score'] = (df['extreme_rating'] / df['n_sessions'] + 0.00001).round(2)
    df = df[df.polarization_score >= 0.6]

    df = df.merge(books, on='book_id', how='left')
    df = df[['book_id', 'title', 'author', 'genre', 'pages', 'rating_spread', 'polarization_score']]

    return df.sort_values(by=['polarization_score', 'title'], ascending=[False, False])