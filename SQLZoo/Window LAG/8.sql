SELECT B.NAME,
       Date_format(B.whn, '%Y-%m-%d'),
       ( B.confirmed - B.lag_confirmed ) AS peakNewCases,
       B.confirmed
FROM   (SELECT A.NAME,
               A.whn,
               A.nc,
               A.confirmed,
               A.lag_confirmed,
               ( Rank()
                   OVER (
                     partition BY A.NAME
                     ORDER BY A.nc DESC) ) AS r
        FROM   (SELECT NAME,
                       whn,
                       confirmed - Lag(confirmed, 1)
                                     OVER (
                                       partition BY NAME
                                       ORDER BY whn) AS nc,
                       confirmed,
                       Lag(confirmed, 1)
                         OVER (
                           partition BY NAME
                           ORDER BY whn)             AS lag_confirmed
                FROM   covid
                ORDER  BY whn) A
        WHERE  A.nc >= 1000) B
WHERE  B.r = 1 
