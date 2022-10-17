#############################################
# PROJE GÖREVLERİ
#############################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv("C:\Users\\Merve.Elmas\Desktop\datasets\persona.csv")
df.head()

   PRICE   SOURCE   SEX COUNTRY  AGE
0     39  android  male     bra   17
1     39  android  male     bra   17
2     49  android  male     bra   17
3     29  android  male     tur   17
4     49  android  male     tur   17

df.info()

 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   PRICE    5000 non-null   int64 
 1   SOURCE   5000 non-null   object
 2   SEX      5000 non-null   object
 3   COUNTRY  5000 non-null   object
 4   AGE      5000 non-null   int64 
dtypes: int64(2), object(3)
  
df.shape

(5000, 5)

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()

android    2974
ios        2026
Name: SOURCE, dtype: int64

# Soru 3: Kaç unique PRICE vardır?

df["PRICE"].nunique()

6

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

29    1305
39    1260
49    1031
19     992
59     212
9      200
Name: PRICE, dtype: int64

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

#1. yol
df["COUNTRY"].value_counts()

#2.yol
df.groupby("COUNTRY").count()

usa    2065
bra    1496
deu     455
tur     451
fra     303
can     230
Name: COUNTRY, dtype: int64

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

#1.yol
df.groupby("COUNTRY")["PRICE"].sum()

#2.yol
df.groupby("COUNTRY").agg({"PRICE": ["sum"]})

COUNTRY
bra    51354
can     7730
deu    15485
fra    10177
tur    15689
usa    70225
Name: PRICE, dtype: int64

# Soru 7: SOURCE türlerine göre satış sayıları nedir?

#1.yol
df["SOURCE"].value_counts()

#2.yol
df.groupby("SOURCE")["PRICE"].count()

android    2974
ios        2026
Name: SOURCE, dtype: int64

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

#1.yol
df.groupby("COUNTRY")["PRICE"].mean()

#2.yol
df.groupby("COUNTRY").agg({"PRICE": ["mean"]})

COUNTRY
bra    34.327540
can    33.608696
deu    34.032967
fra    33.587459
tur    34.787140
usa    34.007264
Name: PRICE, dtype: float64

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE")["PRICE"].mean()

SOURCE
android    34.174849
ios        34.069102
Name: PRICE, dtype: float64

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE": ["mean"]})

                    PRICE
                      mean
COUNTRY SOURCE            
bra     android  34.387029
        ios      34.222222
can     android  33.330709
        ios      33.951456
deu     android  33.869888
        ios      34.268817
fra     android  34.312500
        ios      32.776224
tur     android  36.229437
        ios      33.272727
usa     android  33.760357
        ios      34.371703


#############################################
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE" : "mean"}).head()

                                PRICE
COUNTRY SOURCE  SEX    AGE           
bra     android female 15   38.714286
                       16   35.944444
                       17   35.666667
                       18   32.255814
                       19   35.206897


#############################################
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE" : "mean"}).sort_values("PRICE", ascending=False)

                            PRICE
COUNTRY SOURCE  SEX    AGE       
bra     android male   46    59.0
usa     android male   36    59.0
fra     android female 24    59.0
usa     ios     male   32    54.0
deu     android female 36    49.0
                           ...
usa     ios     female 38    19.0
                       30    19.0
can     android female 27    19.0
fra     android male   18    19.0
deu     android male   26     9.0


# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
# agg_df.reset_index(inplace=True)

agg_df = agg_df.reset_index()
agg_df.head()

  COUNTRY   SOURCE     SEX  AGE  PRICE
0     bra  android    male   46   59.0
1     usa  android    male   36   59.0
2     fra  android  female   24   59.0
3     usa      ios    male   32   54.0
4     deu  android  female   36   49.0
#############################################
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0, 18, 23, 30, 40, 70], labels=["0_18", "19_23", "24_30", "31_40", "41_70"])
agg_df.head()
agg_df.columns

  COUNTRY   SOURCE     SEX  AGE  PRICE AGE_CAT
0     bra  android    male   46   59.0   41_70
1     usa  android    male   36   59.0   31_40
2     fra  android  female   24   59.0   24_30
3     usa      ios    male   32   54.0   31_40
4     deu  android  female   36   49.0   31_40

##########################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

agg_df = pd.DataFrame([{"customers_level_based": str(i[0]+"_"+i[1]+"_"+i[2]+"_"+i[5]).upper(),
                        "PRICE": i[4]} for i in agg_df.values])

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

                              PRICE
customers_level_based              
BRA_ANDROID_FEMALE_0_18   35.645303
BRA_ANDROID_FEMALE_19_23  34.077340
BRA_ANDROID_FEMALE_24_30  33.863946
BRA_ANDROID_FEMALE_31_40  34.898326
BRA_ANDROID_FEMALE_41_70  36.737179
                             ...
USA_IOS_MALE_0_18         33.983495
USA_IOS_MALE_19_23        34.901872
USA_IOS_MALE_24_30        34.838143
USA_IOS_MALE_31_40        36.206324
USA_IOS_MALE_41_70        35.750000

#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])

agg_df = agg_df.reset_index()

agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max","sum"]})


             PRICE                        
              mean        max          sum
SEGMENT                                   
D        29.206780  32.333333   817.789833
C        33.509674  34.077340   904.761209
B        34.999645  36.000000   944.990411
A        38.691234  45.428571  1044.663328

#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user = "TUR_ANDROID_FEMALE_31_40"

agg_df[agg_df["customers_level_based"] == new_user]

   customers_level_based      PRICE      SEGMENT
 TUR_ANDROID_FEMALE_31_40  41.833333       A

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?

new_user = "FRA_IOS_FEMALE_31_40"

agg_df[agg_df["customers_level_based"] == new_user]

customers_level_based      PRICE SEGMENT
FRA_IOS_FEMALE_31_40  32.818182       C
