import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import KNNImputer
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# ****************************STEP 1: Load the dataset****************************
df = pd.read_csv(r"netflix_titles.csv")

# print(df.head(10))
# print(df.shape)
# print(df.dtypes)
# print(df.isnull().sum())
# print(df.isnull().sum().sum())

# ****************************STEP 2: Duplicate Handling****************************

# print(df.duplicated().sum())
a_data = df.head(5)
new_df = pd.concat([df, a_data], ignore_index=True)
# # print(new_df.shape)
df_clean = new_df.drop_duplicates()
# # print(df_clean.shape)

# ****************************Step 3: Missing Values****************************

# df_missing = df_clean.copy()

# null_data = df_missing.sample(50, random_state=42).index
# df_missing.loc[null_data, 'release_year'] = np.nan

# df_movies = df_missing[df_missing['type'] == 'Movie'].copy()
# df_movies['duration_num'] = df_movies['duration'].str.extract(r'(\d+)').astype(float)
# df_movies['duration_num'] = df_movies['duration_num'].fillna(df_movies['duration_num'].mean())

# df_movies['duration_num'] = df_movies['duration_num'].fillna(df_movies['duration_num'].median())

# df_tv_shows = df_missing[df_missing['type'] == 'TV Show'].copy()
# df_tv_shows['duration_num'] = df_tv_shows['duration'].str.extract(r'(\d+)').astype(float)
# print(df_tv_shows['duration_num'].isnull().sum())

# df_missing['release_year']=df_missing['release_year'].fillna(df_missing['release_year'].mean())

# df_missing['release_year'] = df_missing['release_year'].fillna(df_missing['release_year'].median())

# print(df_movies['duration_num'].max())
# print(df_movies.loc[df_movies['duration_num'].idxmax()])

# print(df_missing['rating'].value_counts(dropna=False))

# df_mode = df_missing['rating'].mode()[0]
# df_missing['rating'] = df_missing['rating'].fillna(df_mode)

# print(df_missing['rating'].value_counts())
# print(df_missing['release_year'].isnull().sum())
# df_missing['release_year'] = df_missing['release_year'].ffill()
# print(df_missing['release_year'].isnull().sum())

# KNNImputer:

# df_movies = df_missing[df_missing['type'] == 'Movie'].copy()
# df_movies['duration_num'] = df_movies['duration'].str.extract(r'(\d+)').astype(float)

# df_tv_shows = df_missing[df_missing['type'] == 'TV Show'].copy()
# df_tv_shows['duration_num'] = df_tv_shows['duration'].str.extract(r'(\d+)').astype(float)

# # print(df_movies['duration_num'].isnull().sum())
# # print()
# null = df_movies[df_movies['duration_num'].isnull()].index
# # print(df_movies.loc[null, 'duration_num'])

# imputer = KNNImputer(n_neighbors=10)

# num_col = ['release_year', 'duration_num']
# if not df_movies.empty and df_movies[num_col].isnull().any(axis=None):
#     df_movies[num_col] = imputer.fit_transform(df_movies[num_col])

# if not df_tv_shows.empty and df_tv_shows[num_col].isnull().any(axis=None):
#     df_tv_shows[num_col] = imputer.fit_transform(df_tv_shows[num_col])

# df_movies['duration'] = df_movies['duration_num'].astype(str) + ' min'
# df_tv_shows['duration'] = df_tv_shows['duration_num'].apply(
#     lambda x: f"{int(x)} Seasons" if int(x)==1 else f"{int(x)} Seasons"
# )

# df_combined_clean = pd.concat([df_movies, df_tv_shows], axis=0).sort_index()
# print(df_combined_clean.columns)
# df_missing['duration'] = df_combined_clean['duration'].copy()
# df_missing['release_year'] = df_combined_clean['release_year'].copy()




# ****************************Step 4 — Outlier Detection****************************

# year_column = df_missing['release_year']
# fig, axes = plt.subplots(2, 2, figsize=(12, 5))

# sns.boxplot(x=year_column, ax=axes[0, 0])
# axes[0, 0].set_title('Original Data')


# Q1 = year_column.quantile(0.25)
# Q3 = year_column.quantile(0.75)

# IQR = Q3 - Q1

# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")

# outliers = df_missing[(year_column < lower_bound) | (year_column > upper_bound)]
# print("number of outliers rows: ", len(outliers))

# df_removed_outliers = df_missing[(df_missing['release_year'] >= lower_bound) & (df_missing['release_year'] <= upper_bound)]

# sns.boxplot(x=df_removed_outliers['release_year'], ax=axes[0, 1])
# axes[0, 1].set_title('Outliers Removed')


# df_clipped = df_missing.copy()
# df_clipped['release_year'] = df_clipped['release_year'].clip(lower=lower_bound, upper=upper_bound)

# sns.boxplot(x=df_clipped['release_year'], ax=axes[1, 0])
# axes[1, 0].set_title('Outliers Clipped')

# plt.tight_layout()
# plt.show()

# dbscan = DBSCAN(eps=1.5, min_samples=15)
# x_outliers = df_movies[['release_year', 'duration_num']]
# predictions = dbscan.fit_predict(x_outliers)

# x_outliers['cluster_id'] = predictions

# sns.scatterplot(
#     data = x_outliers,
#     x= 'release_year',
#     y = 'duration_num',
#     hue = 'cluster_id',
#     palette = 'Set1'
# )

# plt.title('DBSCAN')
# # plt.show()

# print(x_outliers['cluster_id'].value_counts())

# ****************************Step 5 — Encoding****************************

# df_encoded = df_missing[['type','rating']].dropna().copy()

# label_encoder = LabelEncoder()
# df_encoded['type_label'] = label_encoder.fit_transform(df_encoded['type'])
# df_encoded['rating_label'] = label_encoder.fit_transform(df_encoded['rating'])

# print(df_encoded['type'].value_counts())
# print("--"*20)
# print(df_encoded['rating'].value_counts())
# print("----Label Encoding----")
# print(df_encoded['type_label'].value_counts())
# print("--"*20)
# print(df_encoded['rating_label'].value_counts())



# one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first')
# encoded_array = one_hot_encoder.fit_transform(df_encoded[['type']])
# encoded_rating = one_hot_encoder.fit_transform(df_encoded[['rating']])

# df_ohe_check = pd.DataFrame(
#     encoded_array, 
#     columns=one_hot_encoder.get_feature_names_out(['type'])
# )

# print("--- One Hot Encoding(type) ---")
# print(df_ohe_check.head(10))

# ****************************Step 6 — Feature Scaling****************************

# df_missing = df_clean.copy()

# null_data = df_missing.sample(50, random_state=42).index
# df_missing.loc[null_data, 'release_year'] = np.nan

# df_movies = df_missing[df_missing['type'] == 'Movie'].copy()
# df_movies['duration_num'] = df_movies['duration'].str.extract(r'(\d+)').astype(float)

# df_tv_shows = df_missing[df_missing['type'] == 'TV Show'].copy()
# df_tv_shows['duration_num'] = df_tv_shows['duration'].str.extract(r'(\d+)').astype(float)

# null = df_movies[df_movies['duration_num'].isnull()].index


# imputer = KNNImputer(n_neighbors=10)

# num_col = ['release_year', 'duration_num']
# if not df_movies.empty and df_movies[num_col].isnull().any(axis=None):
#     df_movies[num_col] = imputer.fit_transform(df_movies[num_col])

# if not df_tv_shows.empty and df_tv_shows[num_col].isnull().any(axis=None):
#     df_tv_shows[num_col] = imputer.fit_transform(df_tv_shows[num_col])

# df_movies['duration'] = df_movies['duration_num'].astype(str) + ' min'
# df_tv_shows['duration'] = df_tv_shows['duration_num'].apply(
#     lambda x: f"{int(x)} Seasons" if int(x)==1 else f"{int(x)} Seasons"
# )

# df_combined_clean = pd.concat([df_movies, df_tv_shows], axis=0).sort_index()

# df_missing['duration'] = df_combined_clean['duration'].copy()
# df_missing['release_year'] = df_combined_clean['release_year'].copy()


# year_column = df_missing['release_year']

# Q1 = year_column.quantile(0.25)
# Q3 = year_column.quantile(0.75)

# IQR = Q3 - Q1

# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# df_clean_outliers=df_missing.copy()

# df_clean_outliers['release_year'] = df_clean_outliers['release_year'].clip(lower_bound, upper_bound)

# df_scaling = df_clean_outliers.dropna().copy()

# # MinMaxScaler
# minmax_scaler = MinMaxScaler()
# df_scaling['MinMax_Scaled_Year'] = minmax_scaler.fit_transform(df_scaling[['release_year']])

# # StandardScaler
# standard_scaler = StandardScaler()
# df_scaling['Standard_Scaled_Year'] = standard_scaler.fit_transform(df_scaling[['release_year']])

# # print(df_scaling.head())

# # ****************************Step 7 — Final ML Preparation****************************

# x =df_scaling[['MinMax_Scaled_Year']]

# y = df_clean_outliers.loc[df_scaling.index, 'type']

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# print(f"""
#     x_train.shape : {x_train.shape}
#     x_test.shape  : {x_test.shape}
#     y_train.shape : {y_train.shape}
#     y_test.shape  : {y_test.shape}
# """)

# print("\nDataset preprocessing completed successfully.")









