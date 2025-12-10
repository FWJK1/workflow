import seaborn as sns
import matplotlib.pyplot as plt

from src.wrangling.data_clean import clean_process_data


def chart_gender():
    df = clean_process_data()
    gender_count = df.groupby('gender')['count'].sum().reset_index()
    sns.barplot(data=gender_count, x='gender', y='count')
    plt.title("Livi's Gender Plot")
    plt.xticks(rotation=45)
    plt.savefig("latex/figures/gender_bar.png")


if __name__ == "__main__":
    chart_gender()