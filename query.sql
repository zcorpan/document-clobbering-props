SELECT
  page,
  rank
FROM `httparchive.all.pages`,
UNNEST (features) AS features
WHERE date = '2024-09-01'
  AND client = 'desktop'
  AND is_root_page
  AND features.feature = "DOMClobberedShadowedDocumentPropertyAccessed"
ORDER BY rank
