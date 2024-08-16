###############################################
# Fonksiyonlara Özellik Ekleme VE Docstring Ekleme
###############################################

###############################################
# GÖREV 1: Fonksiyonlara Özellik Ekleme
###############################################
# cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argumanla biçimlendirilebilir olsun.
# Var olan özelliği de argumandan kontrol edilebilir hale getirebilirsiniz.

# ÖNCESİ
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


# SONRASI
def check_df(dataframe, head=5, tail=5, quan=False):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(tail))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    if quan:
        print("##################### Quantiles #####################")
        print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


import pandas as pd
df = pd.read_csv("datasets/titanic.csv")
check_df(df, head=3, tail=3, quan=True)

###############################################
# cat_summary() için ratio özelliği argumana verilmiştir.
###############################################

import seaborn as sns
import matplotlib.pyplot as plt

# ÖNCESİ
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()

cat_summary(df, "Sex")


# SONRASI
def cat_summary(dataframe, col_name, plot=False, ratio=True):
    if ratio:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts()}))
        print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()


cat_summary(df, "Sex", plot=False, ratio=False)