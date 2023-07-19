import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec
import seaborn.objects as so
import scipy as sp
from sklearn import preprocessing

def highest_subscribe(df):
  top10_channelsub = df[['creator_name', 'creator_gender','total_channel_subscriber']].groupby('creator_name').max().\
                        sort_values(by = 'total_channel_subscriber',ascending = False).head(10)
  top10_channelsub.reset_index(drop = False, inplace = True)
  gender_palette =  {'Male': '#bbdefb', 'Female': '#42a5f5', 'Company': '#0d47a1'}
  plt.figure(figsize = (9,4))
  sns.barplot(x = 'creator_name',y = 'total_channel_subscriber', palette = gender_palette, hue = "creator_gender", data = top10_channelsub )
  plt.xticks(rotation = 45)
  plt.title('Top 10 Channels subscriber wise', color = 'black')
  plt.xlabel('Creator Name')
  plt.ylabel('Total Channel Subscriber')
  plt.legend(loc = 1)

def highest_views(df):
  top10_channelview = df[['creator_name','total_channel_views', 'creator_gender']].groupby('creator_name').max().\
                        sort_values(by = 'total_channel_views',ascending = False).head(10)
  top10_channelview.reset_index(drop = False, inplace = True)
  gender_palette = {'Male': '#bbdefb', 'Female': '#42a5f5', 'Company': '#0d47a1'}
  plt.figure(figsize = (9,4))
  g = sns.barplot(x = 'creator_name',y = 'total_channel_views', hue = 'creator_gender', palette = gender_palette, data =     top10_channelview )
  g.set_yscale("log")
  g.set_yticks([10 ** n for n in range(10, 12)])
  plt.xticks(rotation = 45)
  plt.title('Top 10 Channels views wise', color = 'black')
  plt.xlabel('Creator Name')
  plt.ylabel('Total Channel with highest views')
  plt.legend(loc = 1)

def numberOfLike_byGen(df):
  gender_palette =  {'Male': '#bbdefb', 'Female': '#42a5f5', 'Company': '#0d47a1'}
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 6), sharey=True)
  sns.barplot(x="creator_gender", y="no_of_likes", palette = gender_palette, data=df, errorbar = None, ax = ax1)
  ax1.set_xlabel("")
  ax1.set_ylabel("No of Likes")
  fig.suptitle('Gender Vs Likes')
  ax1.ticklabel_format(style='plain', axis='y')

  sns.barplot(x="creator_gender", y="no_of_likes", palette = gender_palette, data=df, ax = ax2)
  ax2.set_xlabel("")
  ax2.set_ylabel("No of Likes")
  ax2.ticklabel_format(style='plain', axis='y')
  fig.legend(loc = 1, handles=ax2.get_children()[0:3], labels=gender_palette.keys())
    
def numberofLike_by_min(df) :
  cata_palette =  {'Supershort': '#8aacc8', 'Short': '#5d99c6', 'Medium': '#2286c3', 'Long':'#0077c2', 'SuperLong': '#0069c0'}
  plt.figure(figsize = (7,4))
  sns.barplot(x ="length_catagories", y = 'no_of_likes', data = df, errorbar = None, palette = cata_palette )
  plt.title('Average likes per Video Category', fontsize = 10)
  plt.xlabel('Video Cateogory')
  plt.ylabel('No of likes')
  plt.yticks([200000 * n for n in range(6)])
  plt.legend(('Supershort', 'Short', 'Meduim', 'Long', 'SuperLong'),
           loc= 1, shadow=True)

def video_quality_Like(df):
    
  palette = sns.color_palette('Blues')[0:6]
  fig, ax1 = plt.subplots(1, figsize=(9, 6), sharey=True)
  sns.barplot(x="maximum_quality_of_the_video", y="no_of_likes", palette = palette, data=df, errorbar = None, ax = ax1)
  ax1.set_xlabel("quality_video")
  ax1.set_ylabel("No of Likes")
  fig.suptitle('Likes Vs Video Quality')
  ax1.ticklabel_format(style='plain', axis='y')

def video_quality_view(df):
    
  palette = sns.color_palette('Blues')[0:6]
  fig, ax1 = plt.subplots(1, figsize=(9, 6), sharey=True)
  sns.barplot(x="maximum_quality_of_the_video", y="vid_view", palette = palette, data=df, errorbar = None, ax = ax1)
  ax1.set_xlabel("Quality Video")
  ax1.set_ylabel("Video View")
  fig.suptitle('Video View Vs Video Quality')
  ax1.ticklabel_format(style='plain', axis='y')
    
def video_view_year(df): 
  palette = sns.color_palette('Blues')[0:7]
  top_year = df[ (df['upload_year'].astype(int) >= 2013 )  & (df["upload_year"].astype(int) <= 2022)].sort_values( by = 'upload_year', ascending = False)
  fig, ax1= plt.subplots(1, figsize=(9, 6), sharey=True)
  sns.barplot(x="upload_year", y="vid_view", data= top_year, errorbar = None, ax = ax1, palette = palette)
  ax1.set_xlabel("Video Upload Year")
  ax1.set_ylabel("Video View")
  fig.suptitle("Upload Year Vs Video View", fontsize = 10)
  ax1.ticklabel_format(style='plain', axis='y')
  #fig.legend(loc = 1, handles=ax1.get_children()[0:8], labels=quality_palette.keys())

def video_view_month(df): 
  data = df[['vid_view', 'upload_month']].groupby('upload_month').mean().sort_values('vid_view', ascending = False).reset_index()
  palette = sns.color_palette('Blues')[0:11]
  fig, ax1= plt.subplots(figsize=(16, 9), sharey=True)
  sns.barplot( x = "upload_month", y= "vid_view", data = data, palette = palette, ax = ax1, errorbar = None)
  ax1.set_xlabel("Video View")
  ax1.set_ylabel("upload_month")
  fig.suptitle("Video View Vs Upload Month")
             
def video_view_week(df): 
  data = df[['vid_view', 'upload_weekday']].groupby('upload_weekday').mean().sort_values('vid_view', ascending = False).reset_index()
  palette = sns.color_palette('Blues')[0:7]
  fig, ax1= plt.subplots(1, figsize=(10, 7), sharey=True)
  sns.barplot(x="upload_weekday", y="vid_view", data= data, errorbar = None, ax = ax1, palette = palette )
  ax1.set_xlabel("Video Upload Day")
  ax1.set_ylabel("Video View")
  fig.suptitle("Upload Day Vs Video View", fontsize = 13)
  ax1.ticklabel_format(style='plain', axis='y')

def language_of_video(df): 
  palette = sns.color_palette('Blues')[0:11]
  data = df[(df['language_of_the_video'] == "English") | (df['language_of_the_video'] == "Hindi") | (df['language_of_the_video'] == "Italian") | (df['language_of_the_video'] == "Tamil") | (df['language_of_the_video'] == "Telugu") | (df['language_of_the_video'] == "Malayalam") | (df['language_of_the_video'] == "Japenese")]
  fig, ax1= plt.subplots(1, figsize=(10, 7), sharey=True)
  sns.barplot(x="language_of_the_video", y="no_of_likes", data= data, errorbar = None, ax = ax1, palette = palette )
  ax1.set_xlabel("language_of_the_video")
  ax1.set_ylabel("no_of_likes")
  fig.suptitle("language vs Like", fontsize = 13)
  ax1.ticklabel_format(style='plain', axis='y')

def pairplot_relevancy_video_view(df):
  x_vars = ["creator_gender", "duration_in_seconds", "date_of_video_upload", "no_of_likes", "no_of_comments", "language_of_the_video", "subtitle", "video_description", "hashtags", "maximum_quality_of_the_video", "premiered_or_not", "com_en_per_week"]
  y_vars = ["vid_view"]
    
  x_var_iter = iter(x_vars)
  def ret_label():
    return next(x_var_iter)

  def generate_r_stats(i):
    return i + get_r_stats(i)

#Find correlation value 
  def get_r_stats(label):
    x_type = df[label].dtype
    if x_type == "object" and len(df[label].value_counts()) == 2:
        r, p = sp.stats.pointbiserialr(df[label].apply(lambda x: int(x)), df["vid_view"])
    elif x_type == "object":
        x_le = preprocessing.LabelEncoder()
        x_le.fit(df[label])
        x_series = x_le.transform(df[label])
        r, p = sp.stats.pearsonr(x_series, df["vid_view"])
    elif x_type == "datetime64[ns]":
        r, p = -2, 0
    else:
        r, p = sp.stats.pearsonr(df[label], df["vid_view"])
    
    return f"\nr = {r:.2f} --- p = {p:.2g}"

  gen_keys = {}
  
  for i in range(len(x_vars)):
    gen_keys[f"x{i}"] = generate_r_stats

  p = (
      so.Plot(df, y="vid_view")
      .layout(size=(10, 20))
      .scale(y="log")
      .pair(x=x_vars, wrap=3)
      .add(so.Dots())
#       .add(so.Dots(color="#ffff00"), so.Agg())
      .add(so.Path(color="#ffff00"), so.PolyFit(order=2))
      .label(**gen_keys)
  )

  return p


def pairplot_relevancy_num_likes(df):
  x_vars = ["creator_gender", "duration_in_seconds", "date_of_video_upload", "language_of_the_video", "subtitle", "video_description", "hashtags", "maximum_quality_of_the_video", "premiered_or_not", "com_en_per_week"]
  y_vars = ["no_of_likes"]
    
  x_var_iter = iter(x_vars)
    
  def ret_label():
    return next(x_var_iter)

  def generate_r_stats(i):
    return i + get_r_stats(i)

#Find correlation value 
  def get_r_stats(label):
    x_type = df[label].dtype
    if x_type == "object" and len(df[label].value_counts()) == 2:
        r, p = sp.stats.pointbiserialr(df[label].apply(lambda x: int(x)), df["no_of_likes"])
    elif x_type == "object":
        x_le = preprocessing.LabelEncoder()
        x_le.fit(df[label])
        x_series = x_le.transform(df[label])
        r, p = sp.stats.spearmanr(x_series, df["no_of_likes"])
    elif x_type == "datetime64[ns]":
        r, p = -2, 0
    else:
        r, p = sp.stats.spearmanr(df[label], df["no_of_likes"])
    
    return f"\nr = {r:.2f} --- p = {p:.2g}"

  gen_keys = {}
  
  for i in range(len(x_vars)):
    gen_keys[f"x{i}"] = generate_r_stats

  p = (
      so.Plot(df, y="no_of_likes")
      .layout(size=(10, 20))
      .scale(y="log")
      .pair(x=x_vars, wrap=3)
      .add(so.Dots())
#       .add(so.Dots(color="#ffff00"), so.Agg())
      .add(so.Paths(color="#ffff00"), so.PolyFit(order=2))
      .label( **gen_keys)
  )

  return p

def video_view_language(df) :
  df1 = df[["language_of_the_video", "vid_view"]].groupby("language_of_the_video").mean().sort_values("vid_view",ascending=False).reset_index()
  top3 = df1.head(3)
  palette = []
  for i in df1["language_of_the_video"]:
    i = int(i)
    if i == top3.loc[0]["language_of_the_video"]:
       palette.append((i, "#0277bd"))
    elif i == top3.loc[1]["language_of_the_video"]:
       palette.append((i, "#0277bd"))
    elif i == top3.loc[2]["language_of_the_video"]:
       palette.append((i, "#0277bd"))
    else:
       palette.append((i, "#dddddd"))
  palette_dict = dict(palette)
  fig, ax1= plt.subplots(1, figsize=(12, 7), sharey=True)
  sns.barplot(x="language_of_the_video", y="vid_view", data=df1, palette=palette_dict, errorbar = None, ax = ax1)
  ax1.set_xlabel("Language of video")
  ax1.set_ylabel("Video View")
  fig.suptitle("Language Vs Video View", fontsize = 13)
  ax1.ticklabel_format(style='plain', axis='y')





