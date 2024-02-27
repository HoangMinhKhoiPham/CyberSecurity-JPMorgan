import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    df = pd.read_csv(file)
    print(df)
    return df

def exercise_1(df):
    return list(df.columns)

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    return df['type'].unique()

def exercise_5(df):
    return df['newbalanceDest'].value_counts().head(10)

def exercise_6(df):
    return df[df['isFraud'] == 1]

def exercise_7(df):
    return df.groupby('oldbalanceDest')['newbalanceDest'].nunique().sort_values(ascending=False)

def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()

    def transaction_counts_split_by_fraud(df):
        return df.groupby(['type', 'isFraud']).size().unstack(fill_value=0)

    fig, axs = plt.subplots(2, figsize=(10, 12))
    transaction_counts(df).plot(ax=axs[0], kind='bar', color='skyblue')
    axs[0].set_title('Transaction Types Bar Chart')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar', stacked=True)
    axs[1].set_title('Transaction Types Split by Fraud Bar Chart')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    fig.suptitle('Transaction Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center',
                        xytext=(0, 10), textcoords='offset points')
    return 'The first graph shows the distribution of transaction types, providing insights into the frequency of each type. The second graph further breaks down the transaction types based on fraud detection, helping identify any patterns or anomalies.'


def visual_2(df):
    def query(df):
         return df[(df['type'] == 'CASH_OUT')][['oldbalanceDest', 'newbalanceDest']]

    plot = query(df).plot.scatter(x='oldbalanceDest', y='newbalanceDest', alpha=0.5)
    plot.set_title('Scatter Plot of Balance Delta')
    plot.set_xlabel('Origin Balance Delta')
    plot.set_ylabel('Destination Balance Delta')
    plot.set_xlim(left=-1e6, right=1e6)
    plot.set_ylim(bottom=-1e6, top=1e6)
    return 'The scatter plot visualizes the relationship between origin account balance delta and destination account balance delta for Cash Out transactions. It helps in understanding the distribution and any potential correlations between these two variables.'

def exercise_custom(df):
    return df.boxplot(column='amount', by='type', figsize=(10, 6))
    
def visual_custom(df):
    plot = exercise_custom(df)
    plot.set_title('Transaction Amount Distribution by Transaction Type')
    plot.set_xlabel('Transaction Type')
    plot.set_ylabel('Transaction Amount')
    plot.set_yscale('log')  # Set y-axis to logarithmic scale for better visualization of outliers
    return 'This boxplot visualizes the distribution of transaction amounts for different transaction types. Each box represents the interquartile range (IQR), with the median marked by the line inside the box. The whiskers extend to the most extreme data points within 1.5 times the IQR from the quartiles. Outliers beyond this range are plotted individually as points. The y-axis is scaled logarithmically for better visualization of the wide range of transaction amounts.'

