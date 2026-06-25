SELECT company_name,
COUNT(*) AS total_jobs
FROM jobs
GROUP BY company_name
ORDER BY total_jobs DESC;

SELECT job_title, company_name, average_salary
FROM jobs
ORDER BY average_salary DESC;


SELECT city,
COUNT(*) AS jobs
FROM jobs
GROUP BY city
ORDER BY jobs DESC;

SELECT work_mode,
COUNT(*) AS jobs
FROM jobs
GROUP BY work_mode;

SELECT
AVG(average_salary)
FROM jobs;


SELECT category,
COUNT(*)
FROM jobs
GROUP BY category
ORDER BY COUNT(*) DESC;

SELECT category,
AVG(average_salary)
FROM jobs
GROUP BY category;