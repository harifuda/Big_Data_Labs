ratingsDF = ses.read.csv("ratings.csv", header=True, inferSchema=True)
moviesDF = ses.read.csv('movies.csv', header=True, inferSchema=True)
moviesDF.show(truncate=False)

ratingsCountDF = ratingsDF.groupBy('movieId').count()
ratingsCountDF.show(truncate=False)

joinedDF = moviesDF.join(ratingsCountDF, "movieId")
joinedDF.select(col('movieId'), col('title'), col('count')).orderBy(col('movieId')).show(truncate=False)
joinedDF.select('movieId', 'title', 'count').where(col('movieId') == 6).show(truncate=False)
joinedDF.select('movieId', 'title', 'count').where(col('title') == 'Usual Suspects, The (1995)').show(truncate=False)