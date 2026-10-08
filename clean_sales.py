import pandas as pd

INPUT = "sample_transactions.csv"
OUTPUT = "sales_clean_v2.csv"


def clean(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df[["id", "date", "amount"]]
        .dropna(subset=["amount"])
        .drop_duplicates(subset="id", keep="first")
    )


if __name__ == "__main__":
    clean(pd.read_csv(INPUT)).to_csv(OUTPUT, index=False)

# Self Written code
# input_file = 'sample_transactions.csv'
# output_file = 'sales_cleaned.csv'

# def clean_sales_date(input_file,output_file):
#     df = pd.read_csv(input_file)
#     df_select = df[['id','date','amount']]
#     df_select = df_select.dropna(subset= ['amount'])
#     df_cleaned = df_select.drop_duplicates(subset = ['id'])
#     df_cleaned.to_csv(output_file, index=False)


# clean_sales_date(input_file,output_file)