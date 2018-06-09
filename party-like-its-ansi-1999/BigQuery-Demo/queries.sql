
-- name: python_question_views
SELECT
  CONCAT(
    'stackoverflow.com/questions/',
    CAST(id as STRING)) as url,
  title,
  view_count
FROM `bigquery-public-data.stackoverflow.posts_questions`
WHERE tags like '%python%'
ORDER BY view_count DESC
LIMIT 10