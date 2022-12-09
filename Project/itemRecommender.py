import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

#import film dan rating
df_ratings = pd.read_csv('ratings.csv')
df_movies = pd.read_csv('movies.csv')

#set table 
df_pred_item = df_ratings.pivot(index = 'movieId', columns = 'userId', values = 'rating')

df_pred_item.fillna(0, inplace = True)

no_user_voted = df_ratings.groupby('movieId')['rating'].agg('count')
no_movies_voted = df_ratings.groupby('userId')['rating'].agg('count')

df_pred_item = df_pred_item.loc[no_user_voted[no_user_voted > 10].index,:]
df_pred_item = df_pred_item.loc[:, no_movies_voted[no_movies_voted > 50].index]

csr_data = csr_matrix(df_pred_item.values)
df_pred_item.reset_index(inplace = True)

knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(csr_data)

def get_movie_recommendation_item_based(movie_name):
    movies_to_reccomend = 10
    movie_list = df_movies[df_movies['title'].str.contains(movie_name)]  
    if len(movie_list):        
        movie_idx= movie_list.iloc[0]['movieId']
        movie_idx = df_pred_item[df_pred_item['movieId'] == movie_idx].index[0]
        distances , indices = knn.kneighbors(csr_data[movie_idx], n_neighbors = movies_to_reccomend + 1)    
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key=lambda x: x[1])[:0:-1]
        recommend_frame = []
        for val in rec_movie_indices:
            movie_idx = df_pred_item.iloc[val[0]]['movieId']
            idx = df_movies[df_movies['movieId'] == movie_idx].index
            recommend_frame.append({'Title' : df_movies.iloc[idx]['title'].values[0], 'Distance':val[1]})
        df = pd.DataFrame(recommend_frame, index=range(1, movies_to_reccomend + 1))
        return df
    else:
        return "Film yang Anda masukkan tidak terdaftar dalam database. Coba film lain!"

# print(df_pred_item)
# print(no_user_voted)
# print(no_movies_voted)


# def get_genre(movie_name):
#     df_movies 