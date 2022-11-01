import pandas as pd
import random



def parseWithMoneyAndCount(dataframe, colName):
    result = []
    count = []
    gross = []
    for i, record in enumerate(dataframe[colName]):
        for x in record:
            # Lưu kết quả vào mảng tương ứng
            result.append(x)
            gross.append(dataframe['revenue'][i])
            count.append(1)
    # Tạo dataFrame
    t = pd.DataFrame({colName: result, 'Total': gross, 'Count': count})
    # Loại bỏ các giá trị trùng nhau và cộng các hàng tương ứng lại
    result1 = t.groupby(colName).sum()
    result1.reset_index(inplace=True)
    t2 = pd.DataFrame({colName: result, 'Mean': gross})
    result2 = t2.groupby(colName).mean()
    result2.reset_index(inplace=True)
    final = result1.merge(result2, on=colName, how='inner')
    t3 = pd.DataFrame({colName: result, 'Median': gross})
    result3 = t3.groupby(colName).median()
    result3.reset_index(inplace=True)
    final = final.merge(result3, on=colName, how='inner')
    return final


class BORFeatureExtractor:
    castRank = dict()
    crewRank = dict()
    countryRank = dict()
    keywordRank = dict()
    studioRank = []
    cast10Movies = []
    releases4crew = []
    studios10Larger = []

    def __init__(self):
        pass


    def fitCast(self, dataSource):
        cast = parseWithMoneyAndCount(dataSource, 'cast')
        cast.sort_values(by='Count', ascending=False, inplace=True)
        cast10Movies = cast[cast['Count'] > 5]
        cast10Movies.sort_values(by='Mean', ascending=False, inplace=True)
        cast10Movies.reset_index(drop=True, inplace=True)
        cast10Movies.sort_values(by='Mean', ascending=True, inplace=True)
        castRank = dict()
        for i, row in enumerate(cast10Movies['cast']):
            castRank[row] = i + 1
        self.castRank = castRank
        self.cast10Movies = cast10Movies

    def fitCrew(self, dataSource):
        crew = parseWithMoneyAndCount(dataSource, 'crew')
        releases4crew = crew[crew['Count'] > 4]
        crewRank = dict()
        releases4crew = releases4crew.sort_values(by='Mean').reset_index(drop=True)
        for i, row in enumerate(releases4crew['crew']):
            crewRank[row] = i + 1
        self.crewRank = crewRank
        self.releases4crew = releases4crew

    def fitStudio(self, dataSource):
        studio = parseWithMoneyAndCount(dataSource, 'production_companies')
        studios10Larger = studio[studio['Count'] > 5]
        studios10Larger.sort_values(by='Mean', ascending=True, inplace=True)
        studioRank = dict()
        for i, row in enumerate(studios10Larger['production_companies']):
            studioRank[row] = i + 1
        self.studioRank = studioRank
        self.studios10Larger = studios10Larger

    def fitCountry(self, dataSource):
        country = parseWithMoneyAndCount(dataSource, 'production_countries')
        release100Countries = country[country['Count'] >= 100]
        release100Countries = release100Countries.sort_values(by='Mean', ascending=True).reset_index(drop=True)
        countryRank = dict()
        for i, row in enumerate(release100Countries['production_countries']):
            countryRank[row] = i + 1  ## Plus 1 in order to release the 0 position for another film
        self.countryRank = countryRank

    def fitKeywords(self, dataSource):
        keyword = parseWithMoneyAndCount(dataSource, 'keywords')
        count50Keywords = keyword[keyword['Count'] > 20]
        count50Keywords = count50Keywords.sort_values(by='Mean', ascending=True).reset_index(drop=True)
        keywordRank = dict()
        for i, row in enumerate(count50Keywords['keywords']):
            keywordRank[row] = i + 1  ## Plus 1 in order to release the 0 position for another film
        self.keywordRank = keywordRank


    def fit(self, dataSource):
        # Cast
        self.fitCast(dataSource)
        # Crew
        self.fitCrew(dataSource)
        # Studio
        self.fitStudio(dataSource)
        # Country
        self.fitCountry(dataSource)
        # Keywords
        self.fitKeywords(dataSource)
        pass

    def extract(self, dataToExtract):
        # Cast
        def getCastsTeamRank(casts):
            total = 0
            for cast in casts:
                if cast not in self.castRank.keys():
                    total += random.randint(1, 200)
                    continue
                total += self.castRank[cast]
            return total

        dataToExtract['CastsRank'] = dataToExtract['cast'].apply(getCastsTeamRank)
        # NumLeadActor
        cast10Movies = self.cast10Movies
        cast10Movies.sort_values(by='Mean', ascending=False, inplace=True)
        top100Cast = list(cast10Movies['cast'][0:100])

        def getNumLeadActors(casts):
            total = 0
            for cast in casts:
                if cast in top100Cast:
                    total += 1
            return total

        dataToExtract['NumLeadActors'] = dataToExtract['cast'].apply(getNumLeadActors)
        # HasTop50Actors
        cast10Movies.sort_values(by='Mean', ascending=False, inplace=True)
        top50Cast = list(cast10Movies['cast'][0:50])

        def getHasTop30Actors(casts):
            for cast in casts:
                if cast in top50Cast:
                    return 1
            return 0

        dataToExtract['HasTop50Actors'] = dataToExtract['cast'].apply(getHasTop30Actors)
        # NumCrew
        dataToExtract['NumCrews'] = dataToExtract['crew'].apply(lambda x: len(x))

        # crewsTeamRank
        def getCrewsTeamRank(crews):
            total = 0
            for crew in crews:
                if crew not in self.crewRank.keys():
                    total += random.randint(1, 100)
                    continue
                total += self.crewRank[crew]
            return total

        dataToExtract['crewsTeamRank'] = dataToExtract['crew'].apply(getCrewsTeamRank)
        # NumTopCrew
        releases4crew = self.releases4crew
        releases4crew.sort_values(by='Mean', ascending=False, inplace=True)
        top150Crew = list(releases4crew['crew'][0:150])

        def getNumTopCrew(crews):
            total = 0
            for crew in crews:
                if crew in top150Crew:
                    total += 1
            return total

        dataToExtract['NumTopCrew'] = dataToExtract['crew'].apply(getNumTopCrew)
        # HasTopCrew
        releases4crew.sort_values(by='Mean', ascending=False, inplace=True)
        top50Crew = list(releases4crew['crew'][0:50])

        def getHasTopCrew(crews):
            for crew in crews:
                if crew in top50Crew:
                    return 1
            return 0

        dataToExtract['HasTopCrew'] = dataToExtract['crew'].apply(getHasTopCrew)
        # NumStudios
        dataToExtract['NumStudios'] = dataToExtract['production_companies'].apply(lambda x: len(x))

        # StudioRank
        def getStudioRank(studios):
            total = 0
            for studio in studios:
                if studio not in self.studioRank.keys():
                    total += random.randint(1, 200)
                    continue
                total += self.studioRank[studio]
            return total

        dataToExtract['StudioRank'] = dataToExtract['production_companies'].apply(getStudioRank)
        # NumTopStudios
        studios10Larger = self.studios10Larger
        studios10Larger.sort_values(by='Mean', ascending=False, inplace=True)
        top100Studios = list(studios10Larger['production_companies'][0:100])

        def getNumTopStudios(studios):
            total = 0
            for studio in studios:
                if studio in top100Studios:
                    total += 1
            return total

        dataToExtract['NumTopStudios'] = dataToExtract['production_companies'].apply(getNumTopStudios)
        # HasTopStudio
        studios10Larger.sort_values(by='Mean', ascending=False, inplace=True)
        top100Studios = list(studios10Larger['production_companies'][0:30])

        def getHasTopStudio(studios):
            for studio in studios:
                if studio in top100Studios:
                    return 1
            return 0

        dataToExtract['HasTopStudio'] = dataToExtract['production_companies'].apply(getHasTopStudio)

        # CountryRank
        def getCountryRank(countries):
            max = 0
            for country in countries:
                if country not in self.countryRank.keys():
                    continue
                if self.countryRank[country] > max:
                    max = self.countryRank[country]
            if max == 0:
                max = random.randint(1, 10)
            return max

        dataToExtract['CountryRank'] = dataToExtract['production_countries'].apply(getCountryRank)

        # keywordRank
        def getKeywordsRank(keywords):
            max = 0
            for keyword in keywords:
                if keyword not in self.keywordRank.keys():
                    continue
                if self.keywordRank[keyword] > max:
                    max = self.keywordRank[keyword]
            if max == 0:
                max = random.randint(1, 100)
            return max

        dataToExtract['keywordRank'] = dataToExtract['keywords'].apply(getKeywordsRank)



        # mlb = MultiLabelBinarizer()
        # onehot_genre = mlb.fit_transform(dataToExtract['genres'])
        # dataToExtract = dataToExtract.join(pd.DataFrame(onehot_genre,
        #                         columns=mlb.classes_,
        #                         index=dataToExtract.index))
        

        # dataToExtract.drop(['overview', 'title', 'production_companies','production_countries'\
        #     ,'cast', 'crew', 'keywords', 'original_language', 'genres'], axis = 1, inplace = True)

        # return dataToExtract
