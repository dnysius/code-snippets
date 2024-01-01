/*4*/
SELECT company, num, COUNT(*)
FROM route WHERE stop=149 OR stop=53
GROUP BY company, num
HAVING num IN ('4','45')

/*5*/
SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop=53 AND b.stop='149'

/*6*/
SELECT a.company, a.num, stopa.name, stopb.name
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE (stopa.name='Craiglockhart' AND stopb.name='London Road')

/*7*/
SELECT  a.company, a.num
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE (a.stop='115' and b.stop ='137') OR (b.stop='115' and a.stop ='137')
GROUP BY a.num, a.company
/*8*/
SELECT a.company, a.num
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
JOIN stops stopa ON (a.stop=stopa.id)
JOIN stops stopb ON (b.stop=stopb.id)
WHERE (stopa.name='Craiglockhart' and stopb.name='Tollcross') OR (stopb.name='Craiglockhart' and stopa.name='Tollcross')
GROUP BY a.num, a.company
/*9* */
SELECT stopb.name, a.company, a.num
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
JOIN stops stopa ON (a.stop=stopa.id)
JOIN stops stopb ON (b.stop=stopb.id)
WHERE a.company='LRT' AND (stopa.name='Craiglockhart' OR stopb.name='Craiglockhart')
GROUP BY a.num, a.company, stopb.name
/*10*/
SELECT B.Bnum, B.Bcompany, stops.name AS transfer, A.Anum, A.Acompany FROM
(SELECT route.num AS Anum, route.company AS Acompany, route.stop FROM route JOIN (SELECT company, num FROM route WHERE stop='147') aroute ON (route.num=aroute.num AND route.company=aroute.company)) A
JOIN
(SELECT route.num AS Bnum, route.company AS Bcompany, route.stop FROM route JOIN (SELECT company, num FROM route WHERE stop='53') droute ON (route.num=droute.num AND route.company=droute.company)) B
ON A.stop=B.stop
JOIN stops ON A.stop=stops.id
